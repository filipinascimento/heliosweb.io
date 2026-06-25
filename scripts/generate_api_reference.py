#!/usr/bin/env python3
from __future__ import annotations

import ast
import html
import json
import os
import re
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path


DOCS_SITE = Path(__file__).resolve().parents[1]
ROOT = Path(os.environ.get("HELIOS_MONOREPO_ROOT", DOCS_SITE.parent)).resolve()
DOCS = DOCS_SITE / "docs"


@dataclass(frozen=True)
class Symbol:
    name: str
    kind: str
    source: Path
    line: int
    summary: str = ""
    signature: str = ""
    params: tuple[str, ...] = ()
    returns: str = ""
    remarks: str = ""
    examples: tuple[str, ...] = ()
    category: str = "Reference"
    methods: tuple["Symbol", ...] = ()


class ApiExtractionError(RuntimeError):
    pass


def empty_doc() -> dict:
    return {
        "summary": "",
        "params": (),
        "returns": "",
        "remarks": "",
        "examples": (),
        "apiSection": "",
        "apiSubsection": "",
    }


def rel(path: Path) -> str:
    path = path.resolve()
    for package_root in (ROOT / "helios-web-next", ROOT / "helios-network-v2", ROOT / "helios-xnet"):
        try:
            return path.relative_to(package_root).as_posix()
        except ValueError:
            continue
    return path.relative_to(ROOT).as_posix()


def line_link(symbol: Symbol) -> str:
    return f"`{rel(symbol.source)}:{symbol.line}`"


def slug(name: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_.-]+", "-", name).strip("-")
    return cleaned or "symbol"


def link_for(symbol: Symbol) -> str:
    return f"{slug(symbol.name)}.md"


def link_label(symbol: Symbol) -> str:
    return f"[`{symbol.name}`]({link_for(symbol)})"


def read_json(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        return json.load(handle)


def git_revision() -> str:
    try:
        return subprocess.check_output(
            ["git", "-C", str(ROOT / "helios-network-v2"), "rev-parse", "--short", "HEAD"],
            text=True,
            stderr=subprocess.DEVNULL,
        ).strip()
    except Exception:
        return "current-checkout"


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def clean_generated_api_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)
    for child in path.iterdir():
        if child.name == "index.md":
            continue
        if child.is_dir():
            shutil.rmtree(child)
        elif child.suffix == ".md":
            child.unlink()


def jsdoc_before(lines: list[str], index: int) -> str:
    return parse_jsdoc_before(lines, index).get("summary", "")


def parse_jsdoc_before(lines: list[str], index: int) -> dict:
    cursor = index - 1
    while cursor >= 0 and not lines[cursor].strip():
        cursor -= 1
    if cursor < 0 or "*/" not in lines[cursor]:
        return empty_doc()
    block: list[str] = []
    while cursor >= 0:
        block.append(lines[cursor])
        if "/**" in lines[cursor]:
            break
        cursor -= 1
    if not block or "/**" not in block[-1]:
        return empty_doc()
    cleaned: list[str] = []
    for raw in reversed(block):
        line = raw.rstrip()
        line = re.sub(r"^\s*/\*\*\s?", "", line)
        line = re.sub(r"\s*\*/\s*$", "", line)
        line = re.sub(r"^\s*\*\s?", "", line)
        if not line.strip():
            continue
        cleaned.append(line.rstrip())

    summary: list[str] = []
    tags: dict[str, list[str]] = {
        "param": [],
        "returns": [],
        "remarks": [],
        "example": [],
        "apiSection": [],
        "apiSubsection": [],
    }
    current: str | None = None
    for line in cleaned:
        stripped = line.strip()
        if stripped.startswith("@"):
            tag, _, rest = stripped[1:].partition(" ")
            tag = "returns" if tag == "return" else tag
            if tag not in tags:
                current = None
                continue
            current = tag
            if rest.strip():
                tags[tag].append(rest.strip())
            continue
        if current:
            value = line if current == "example" else stripped
            if tags[current]:
                tags[current][-1] += "\n" + value
            else:
                tags[current].append(value)
        elif not tags["param"] and not tags["returns"] and not tags["remarks"] and not tags["example"]:
            summary.append(stripped)

    return {
        "summary": " ".join(summary).strip(),
        "params": tuple(tags["param"]),
        "returns": " ".join(tags["returns"]).strip(),
        "remarks": " ".join(tags["remarks"]).strip(),
        "examples": tuple(tags["example"]),
        "apiSection": " ".join(tags["apiSection"]).strip(),
        "apiSubsection": " ".join(tags["apiSubsection"]).strip(),
    }


def parse_js_exports(entry: Path) -> list[str]:
    text = entry.read_text(encoding="utf-8")
    names: list[str] = []
    for match in re.finditer(r"export\s*\{(?P<body>.*?)\}\s*from", text, re.S):
        for part in match.group("body").split(","):
            name = part.strip()
            if not name:
                continue
            if " as " in name:
                name = name.split(" as ", 1)[1].strip()
            names.append(name)
    for match in re.finditer(r"export\s+(?:class|function|const|let|var)\s+([A-Za-z_$][\w$]*)", text):
        names.append(match.group(1))
    return sorted(dict.fromkeys(names))


def resolve_js_module(base: Path, specifier: str) -> Path:
    path = (base.parent / specifier).resolve()
    if path.suffix:
        return path
    return path.with_suffix(".js")


def parse_js_imports(module: Path) -> dict[str, tuple[str, Path]]:
    text = module.read_text(encoding="utf-8")
    imports: dict[str, tuple[str, Path]] = {}
    for match in re.finditer(r"import\s*\{(?P<body>.*?)\}\s*from\s*['\"](?P<path>[^'\"]+)['\"]", text, re.S):
        target = resolve_js_module(module, match.group("path"))
        for part in match.group("body").split(","):
            name = part.strip()
            if not name:
                continue
            imported = name
            local = name
            if " as " in name:
                imported, local = [item.strip() for item in name.split(" as ", 1)]
            imports[local] = (imported, target)
    for match in re.finditer(r"import\s+(?P<local>[A-Za-z_$][\w$]*)\s+from\s*['\"](?P<path>[^'\"]+)['\"]", text):
        imports[match.group("local")] = ("default", resolve_js_module(module, match.group("path")))
    return imports


def parse_js_export_sources(module: Path, seen: set[Path] | None = None) -> dict[str, Path]:
    module = module.resolve()
    seen = seen or set()
    if module in seen:
        return {}
    seen.add(module)
    text = module.read_text(encoding="utf-8")
    exports: dict[str, Path] = {}

    for match in re.finditer(r"export\s+(?:class|function|const|let|var)\s+([A-Za-z_$][\w$]*)", text):
        exports[match.group(1)] = module
    for match in re.finditer(r"export\s+default\s+([A-Za-z_$][\w$]*)", text):
        exports["default"] = module

    imports = parse_js_imports(module)

    reexport_pattern = r"export\s*\{(?P<body>.*?)\}\s*from\s*['\"](?P<path>[^'\"]+)['\"]\s*;?"
    for match in re.finditer(reexport_pattern, text, re.S):
        target = resolve_js_module(module, match.group("path"))
        target_exports = parse_js_export_sources(target, seen)
        for part in match.group("body").split(","):
            raw = part.strip()
            if not raw:
                continue
            imported = raw
            exported = raw
            if " as " in raw:
                imported, exported = [item.strip() for item in raw.split(" as ", 1)]
            exports[exported] = target_exports.get(imported, target)

    local_export_text = re.sub(reexport_pattern, "", text, flags=re.S)
    for match in re.finditer(r"export\s*\{(?P<body>.*?)\}\s*;?", local_export_text, re.S):
        for part in match.group("body").split(","):
            raw = part.strip()
            if not raw:
                continue
            local = raw
            exported = raw
            if " as " in raw:
                local, exported = [item.strip() for item in raw.split(" as ", 1)]
            if local in imports:
                imported, target = imports[local]
                target_exports = parse_js_export_sources(target, seen)
                exports[exported] = target_exports.get(imported, target)
            else:
                exports[exported] = module
    return exports


def parse_js_source_symbols(path: Path, names: set[str]) -> list[Symbol]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    aliases: dict[str, str] = {}
    for match in re.finditer(r"export\s*\{(?P<body>.*?)\}\s*;?", text, re.S):
        for part in match.group("body").split(","):
            raw = part.strip()
            if not raw:
                continue
            local = raw
            exported = raw
            if " as " in raw:
                local, exported = [item.strip() for item in raw.split(" as ", 1)]
            if exported in names:
                aliases[local] = exported
    symbols: list[Symbol] = []
    for index, line in enumerate(lines, start=1):
        export_alias_match = re.match(r"^\s*export\s*\{(?P<body>.*?)\}\s*;?", line)
        if export_alias_match:
            for part in export_alias_match.group("body").split(","):
                raw = part.strip()
                if not raw:
                    continue
                exported = raw.split(" as ", 1)[1].strip() if " as " in raw else raw
                if exported not in names:
                    continue
                doc = parse_jsdoc_before(lines, index - 1)
                symbols.append(Symbol(
                    exported,
                    "symbol",
                    path,
                    index,
                    doc["summary"],
                    line.strip(),
                    doc["params"],
                    doc["returns"],
                    doc["remarks"],
                    doc["examples"],
                    doc["apiSection"] or "Reference",
                ))
            continue
        match = re.match(r"^\s*export\s+(?P<kind>class|function|const|let|var)\s+(?P<name>[A-Za-z_$][\w$]*)", line)
        if match and match.group("name") in names:
            doc = parse_jsdoc_before(lines, index - 1)
            kind = "symbol" if match.group("kind") in {"const", "let", "var"} else match.group("kind")
            symbols.append(Symbol(
                match.group("name"),
                kind,
                path,
                index,
                doc["summary"],
                line.strip(),
                doc["params"],
                doc["returns"],
                doc["remarks"],
                doc["examples"],
                doc["apiSection"] or "Reference",
            ))
            continue
        alias_match = re.match(r"^\s*(?:const|let|var|class|function)\s+(?P<name>[A-Za-z_$][\w$]*)", line)
        if alias_match and alias_match.group("name") in aliases:
            doc = parse_jsdoc_before(lines, index - 1)
            symbols.append(Symbol(
                aliases[alias_match.group("name")],
                "symbol" if not line.lstrip().startswith(("class ", "function ")) else ("class" if line.lstrip().startswith("class ") else "function"),
                path,
                index,
                doc["summary"],
                line.strip(),
                doc["params"],
                doc["returns"],
                doc["remarks"],
                doc["examples"],
                doc["apiSection"] or "Reference",
            ))
    return symbols


def parse_js_methods(path: Path, names: set[str]) -> list[Symbol]:
    lines = path.read_text(encoding="utf-8").splitlines()
    symbols: list[Symbol] = []
    pattern = re.compile(r"^\s+(?P<async>async\s+)?(?P<name>[A-Za-z_$][\w$]*)\s*\(")
    for index, line in enumerate(lines, start=1):
        match = pattern.match(line)
        if not match or match.group("name") not in names:
            continue
        doc = parse_jsdoc_before(lines, index - 1)
        symbols.append(Symbol(
            match.group("name"),
            "method",
            path,
            index,
            doc["summary"],
            line.strip(),
            doc["params"],
            doc["returns"],
            doc["remarks"],
            doc["examples"],
            doc["apiSection"] or "Reference",
        ))
    return symbols


def parse_js_class_methods(path: Path, class_names: set[str]) -> dict[str, tuple[Symbol, ...]]:
    lines = path.read_text(encoding="utf-8").splitlines()
    methods_by_class: dict[str, tuple[Symbol, ...]] = {}
    class_pattern = re.compile(r"^\s*(?:export\s+)?class\s+(?P<name>[A-Za-z_$][\w$]*)\b")
    method_pattern = re.compile(r"^\s{2}(?P<async>async\s+)?(?P<name>[A-Za-z_$][\w$]*)\s*\((?P<args>[^)]*)\)")
    static_property_pattern = re.compile(r"^\s{2}static\s+(?P<name>[A-Za-z_$][\w$]*)\s*=")
    getter_pattern = re.compile(r"^\s{2}get\s+(?P<name>[A-Za-z_$][\w$]*)\s*\(")

    index = 0
    while index < len(lines):
        class_match = class_pattern.match(lines[index])
        if not class_match or class_match.group("name") not in class_names:
            index += 1
            continue

        class_name = class_match.group("name")
        brace_depth = lines[index].count("{") - lines[index].count("}")
        cursor = index + 1
        methods: list[Symbol] = []
        while cursor < len(lines) and brace_depth > 0:
            line = lines[cursor]
            if brace_depth == 1:
                static_property_match = static_property_pattern.match(line)
                if static_property_match:
                    doc = parse_jsdoc_before(lines, cursor)
                    methods.append(Symbol(
                        static_property_match.group("name"),
                        "property",
                        path,
                        cursor + 1,
                        doc["summary"],
                        line.strip(),
                        doc["params"],
                        doc["returns"],
                        doc["remarks"],
                        doc["examples"],
                        doc["apiSection"] or "Reference",
                    ))
                    brace_depth += line.count("{") - line.count("}")
                    cursor += 1
                    continue
                getter_match = getter_pattern.match(line)
                if getter_match and not getter_match.group("name").startswith("_"):
                    doc = parse_jsdoc_before(lines, cursor)
                    methods.append(Symbol(
                        getter_match.group("name"),
                        "property",
                        path,
                        cursor + 1,
                        doc["summary"],
                        line.strip(),
                        doc["params"],
                        doc["returns"],
                        doc["remarks"],
                        doc["examples"],
                        doc["apiSection"] or "Reference",
                    ))
                method_match = method_pattern.match(line)
                if method_match:
                    method_name = method_match.group("name")
                    if not method_name.startswith("_"):
                        doc = parse_jsdoc_before(lines, cursor)
                        signature = line.strip()
                        kind = "constructor" if method_name == "constructor" else "method"
                        methods.append(Symbol(
                            method_name,
                            kind,
                            path,
                            cursor + 1,
                            doc["summary"],
                            signature,
                            doc["params"],
                            doc["returns"],
                            doc["remarks"],
                            doc["examples"],
                            doc["apiSection"] or "Reference",
                        ))
            brace_depth += line.count("{") - line.count("}")
            cursor += 1
        methods_by_class[class_name] = tuple(methods)
        index = cursor
    return methods_by_class


def attach_methods(symbols: list[Symbol], method_sources: dict[str, tuple[Symbol, ...]]) -> list[Symbol]:
    attached: list[Symbol] = []
    for symbol in symbols:
        methods = tuple(
            with_category(method, infer_member_section(symbol.name, method))
            for method in method_sources.get(symbol.name, ())
        )
        attached.append(Symbol(
            symbol.name,
            symbol.kind,
            symbol.source,
            symbol.line,
            symbol.summary,
            symbol.signature,
            symbol.params,
            symbol.returns,
            symbol.remarks,
            symbol.examples,
            symbol.category,
            methods,
        ))
    return attached


def parse_ts_declarations(path: Path) -> list[Symbol]:
    symbols: list[Symbol] = []
    lines = path.read_text(encoding="utf-8").splitlines()
    pattern = re.compile(r"^export\s+(?P<kind>class|interface|type|function|const|declare class)\s+(?P<name>[A-Za-z_$][\w$]*)")
    for index, line in enumerate(lines, start=1):
        match = pattern.match(line)
        if not match:
            continue
        signature = line.strip()
        symbols.append(Symbol(
            match.group("name"),
            match.group("kind").replace("declare ", ""),
            path,
            index,
            summary=jsdoc_before(lines, index - 1),
            signature=signature,
        ))
    return symbols


def parse_public_js_symbols(path: Path, exported_names: set[str]) -> list[Symbol]:
    lines = path.read_text(encoding="utf-8").splitlines()
    symbols: list[Symbol] = []
    pattern = re.compile(r"^(?:export\s+)?(?:class|function|const|let|var)\s+([A-Za-z_$][\w$]*)")
    for index, line in enumerate(lines, start=1):
        match = pattern.match(line)
        if match and match.group(1) in exported_names:
            kind = "class" if "class " in line else "symbol"
            symbols.append(Symbol(match.group(1), kind, path, index, jsdoc_before(lines, index - 1), line.strip()))
    return symbols


def parse_python_public_api(package: Path) -> list[Symbol]:
    init_path = package / "__init__.py"
    module = ast.parse(init_path.read_text(encoding="utf-8"))
    all_names: set[str] = set()
    for node in module.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "__all__" and isinstance(node.value, ast.List):
                    all_names.update(item.value for item in node.value.elts if isinstance(item, ast.Constant) and isinstance(item.value, str))

    symbols: list[Symbol] = []
    files = [init_path, *(path for path in package.glob("*.py") if path.name != "__init__.py")]
    for source in files:
        tree = ast.parse(source.read_text(encoding="utf-8"))
        for node in tree.body:
            if isinstance(node, (ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)) and node.name in all_names:
                kind = "class" if isinstance(node, ast.ClassDef) else "function"
                summary = ast.get_docstring(node) or ""
                symbols.append(Symbol(node.name, kind, source, node.lineno, summary.split("\n\n", 1)[0]))
    return sorted(symbols, key=lambda item: (item.source.as_posix(), item.line, item.name))


def parse_c_headers(include_dir: Path) -> tuple[list[Symbol], list[str]]:
    public_headers = [
        path for path in sorted(include_dir.glob("*.h"))
        if not path.name.startswith("ut") and path.name != "CXSortTest.h"
    ]
    symbols: list[Symbol] = []
    missing: list[str] = []
    comment = ""
    for header in public_headers:
        lines = header.read_text(encoding="utf-8", errors="replace").splitlines()
        for index, line in enumerate(lines, start=1):
            stripped = line.strip()
            if stripped.startswith("/**"):
                block = [stripped]
                cursor = index
                while "*/" not in block[-1] and cursor < len(lines):
                    block.append(lines[cursor].strip())
                    cursor += 1
                cleaned = []
                for raw in block:
                    item = raw.removeprefix("/**").removesuffix("*/").strip()
                    item = item.removeprefix("*").strip()
                    if item:
                        cleaned.append(item)
                comment = " ".join(cleaned)
                continue
            if not stripped.startswith("CX_EXTERN "):
                continue
            signature = stripped
            while not signature.endswith(";") and index < len(lines):
                index += 1
                signature += " " + lines[index - 1].strip()
            match = re.search(r"\b(CX[A-Za-z0-9_]+)\s*\(", signature)
            if not match:
                continue
            name = match.group(1)
            if not comment:
                missing.append(f"{header.name}:{index} `{name}`")
            symbols.append(Symbol(name, "function", header, index, comment, signature))
            comment = ""
    return symbols, missing


def markdown_table(symbols: list[Symbol]) -> str:
    if not symbols:
        return "_No public symbols were found._\n"
    rows = ["| Symbol | Kind | Source | Summary |", "| --- | --- | --- | --- |"]
    for symbol in symbols:
        summary = symbol.summary.replace("\n", " ").replace("|", "\\|")
        rows.append(f"| {link_label(symbol)} | {symbol.kind} | {line_link(symbol)} | {summary} |")
    return "\n".join(rows) + "\n"


def definition_rows(items: list[tuple[str, str]]) -> str:
    rows = ['<dl class="helios-api-definition-list">']
    for label, value in items:
        if not value:
            continue
        rows.extend([
            f"<dt>{html.escape(label)}</dt>",
            f"<dd>{html.escape(value)}</dd>",
        ])
    rows.append("</dl>")
    return "\n".join(rows)


def inline_html(text: str) -> str:
    text = " ".join((text or "").split())
    if not text:
        return ""
    parts: list[str] = []
    cursor = 0
    for match in re.finditer(r"`([^`]+)`", text):
        parts.append(html.escape(text[cursor:match.start()]))
        parts.append(f"<code>{html.escape(match.group(1))}</code>")
        cursor = match.end()
    parts.append(html.escape(text[cursor:]))
    return "".join(parts)


TYPE_LINKS = {
    "Helios": "/docs/api/helios-web/Helios/",
    "HeliosFilter": "/docs/api/helios-web/HeliosFilter/",
    "HeliosNetwork": "/docs/api/helios-network-js-wasm/HeliosNetwork/",
    "Mapper": "/docs/api/helios-web/Mapper/",
    "MapperCollection": "/docs/api/helios-web/MapperCollection/",
    "Behavior": "/docs/api/helios-web/Behavior/",
    "BehaviorManager": "/docs/api/helios-web/BehaviorManager/",
    "BehaviorRegistry": "/docs/api/helios-web/BehaviorRegistry/",
    "FilterBehavior": "/docs/api/helios-web/FilterBehavior/",
    "MappersBehavior": "/docs/api/helios-web/MappersBehavior/",
}


def normalize_type_text(type_hint: str) -> str:
    text = (type_hint or "").strip()
    replacements = {
        "import('helios-network').default": "HeliosNetwork",
        "import(\"helios-network\").default": "HeliosNetwork",
        "object": "Object",
        "boolean": "boolean",
        "number": "number",
        "string": "string",
    }
    for source, target in replacements.items():
        text = text.replace(source, target)
    text = text.replace("Array<object>", "Array.<Object>")
    text = text.replace("Array<Object>", "Array.<Object>")
    return text


def type_html(type_hint: str) -> str:
    text = normalize_type_text(type_hint)
    if not text:
        return ""
    pattern = re.compile(r"\b[A-Za-z_$][\w$]*\b")
    parts: list[str] = []
    cursor = 0
    for match in pattern.finditer(text):
        token = match.group(0)
        parts.append(html.escape(text[cursor:match.start()]))
        if token in TYPE_LINKS:
            parts.append(f'<a href="{TYPE_LINKS[token]}"><code>{html.escape(token)}</code></a>')
        else:
            parts.append(f"<code>{html.escape(token)}</code>")
        cursor = match.end()
    parts.append(html.escape(text[cursor:]))
    return "".join(parts)


def split_jsdoc_type(text: str) -> tuple[str, str]:
    text = text.strip()
    if not text.startswith("{"):
        return "", text
    depth = 0
    for index, char in enumerate(text):
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                return text[1:index].strip(), text[index + 1:].strip()
    return "", text


def parse_param_doc(param: str) -> dict[str, str]:
    match = re.match(r"(?s)^(.*?)\s+-\s*(.*)$", param)
    if match:
        left = match.group(1).strip()
        right = match.group(2).strip()
    else:
        left = param.strip()
        right = ""
    type_hint, name = split_jsdoc_type(left)
    if not type_hint:
        name = left
    if not right and "\n" in name:
        name, right = name.split("\n", 1)
    optional = name.startswith("[") and name.endswith("]")
    default = ""
    if optional:
        name = name[1:-1]
        if "=" in name:
            name, default = [item.strip() for item in name.split("=", 1)]
    return {
        "name": name.strip(),
        "type": type_hint,
        "attributes": "optional" if optional else "",
        "default": default,
        "description": (right or "").strip(),
    }


def extract_signature_args(signature: str) -> list[str]:
    if not signature or not signature.splitlines():
        return []
    first = signature.splitlines()[0].strip()
    match = re.search(r"\((?P<args>[^)]*)\)", first)
    if not match:
        return []
    args = match.group("args").strip()
    if not args:
        return []
    return [arg.strip() for arg in args.split(",") if arg.strip()]


def inferred_param_description(name: str, member_name: str = "") -> str:
    clean = name.strip("{}[] ").split("=", 1)[0].strip()
    readable = humanize_name(clean)
    if clean in {"behaviorCtor"}:
        return "Behavior constructor or factory to register."
    if clean in {"behaviorOrOptions"}:
        return "Behavior instance or options for the named behavior."
    if clean in {"network"}:
        return "Network instance to read from or mutate."
    if clean in {"path", "filePath"}:
        return "Filesystem path to read from or write to."
    if clean in {"query"}:
        return "Query expression to parse and evaluate."
    if clean in {"selector"}:
        return "Selector that receives the matching indices."
    if clean in {"nodeSelector"}:
        return "Node selector that receives or provides node indices."
    if clean in {"edgeSelector"}:
        return "Edge selector that receives or provides edge indices."
    if clean in {"dst", "target", "outIndices"}:
        return "Caller-provided destination buffer."
    if clean in {"sourceNodes", "nodeIndices", "edgeIndices", "indices", "ids"}:
        return "Node or edge indices used by the operation."
    if clean in {"count", "nodeCount", "edgeCount", "capacity", "nodeCapacity", "edgeCapacity"}:
        return "Number of entries or available output slots."
    if clean in {"index", "node", "edge"}:
        return "Node, edge, or attribute index."
    if clean in {"name", "sourceName", "edgeName", "attributeName"}:
        return "Attribute or API identifier."
    if clean in {"scope"}:
        return "Attribute scope: node, edge, or network."
    if clean in {"type", "attrType", "attributeType"}:
        return "Attribute value type."
    if clean in {"dimension", "componentsPerNode", "componentSizeBytes", "stride", "nodeStrideBytes", "edgeStrideBytes"}:
        return "Element width or memory-stride setting."
    if clean in {"direction"}:
        return "Traversal direction for directed graphs."
    if clean in {"includeSourceNodes"}:
        return "Whether the source nodes may appear in the result."
    if clean in {"includeEdges"}:
        return "Whether traversed edge ids should be included."
    if clean in {"level", "maxLevel"}:
        return "Concentric hop distance."
    if clean in {"compressionLevel"}:
        return "Compression level for compressed output formats."
    if clean in {"fmt"}:
        return "Format string."
    if clean in {"probabilities", "blockSizes", "degreeSequence"}:
        return "Generator input data."
    if clean in {"detail"}:
        return "Event payload passed to listeners."
    if clean in {"filter"}:
        return "Filter instance or filter options to activate."
    if clean in {"options", "maybeOptions", "previewOptions"}:
        return "Options object for this operation."
    readable_member = humanize_name(member_name).strip()
    if clean == "value":
        return f"New {readable_member} value. Omit this argument to read the current value." if readable_member else "New value. Omit this argument when the method supports readback."
    if clean in {"color", "style"}:
        return f"New {readable_member} value. Omit this argument to read the current value." if readable_member else "New style value."
    if clean in {"nodeId", "nodeIds", "nodeIndices", "edgeIds", "indices"}:
        return "Node or edge identifiers/indices used by the operation."
    if clean in {"slot", "mask"}:
        return "State bit slot or mask value."
    if clean in {"mode", "type", "name", "format", "channel", "scope", "reason"}:
        return f"{readable.capitalize()} for this operation."
    if clean in {"handler"}:
        return "Callback invoked for the registered event."
    if clean in {"source", "network", "nextNetwork"}:
        return "Network or input source used by the operation."
    if clean in {"pose", "fromPose", "toPose"}:
        return "Camera pose fields to apply."
    if clean in {"nodeIndices", "indices"}:
        return "Node or edge indices affected by the operation."
    if member_name.startswith("CX"):
        return f"{readable.capitalize()} argument."
    return f"Value passed to `{member_name}`." if member_name else "Value passed to this API."


def inferred_param_type(name: str, member_name: str = "") -> str:
    clean = name.strip("{}[] ").split("=", 1)[0].strip()
    method = member_name or ""
    if clean in {"options", "maybeOptions", "previewOptions"}:
        return "Object"
    if clean in {"handler", "behaviorCtor", "initializer"}:
        return "Function"
    if clean in {"filter"}:
        return "HeliosFilter"
    if clean in {"network", "nextNetwork"}:
        return "HeliosNetwork"
    if clean in {"source"}:
        return "Blob|ArrayBuffer|string|File"
    if clean in {"nodeIndices", "indices", "nodeIds"}:
        return "Array<number>|TypedArray"
    if clean in {"clientX", "clientY", "count", "slot", "mask", "index"}:
        return "number"
    if clean in {"type", "typeWithNamespace", "name", "format", "mode", "reason", "channel", "attributeName"}:
        return "string"
    if clean in {"color"} or method.lower().endswith("color") or "background" in method.lower():
        return "string|Array<number>"
    if clean == "style":
        return "Object"
    if clean == "value":
        lowered = method.lower()
        if any(term in lowered for term in ("enabled", "nodes", "edges", "topographic", "normalize", "fastduring", "depthwrite", "fast")):
            return "boolean"
        if any(term in lowered for term in ("scale", "base", "width", "opacity", "size", "radius", "strength", "bias", "threshold", "interval", "duration", "factor", "chars", "rows", "visible", "bandwidth", "weight", "shininess", "supersampling")):
            return "number"
        if any(term in lowered for term in ("mode", "source", "property", "family", "colormap", "quality")):
            return "string"
    return ""


def parameter_table(params: tuple[str, ...], signature: str = "", infer_missing: bool = True) -> str:
    rows_data = [parse_param_doc(param) for param in params]
    documented_names = {row["name"].split(".", 1)[0].strip("{}[] ") for row in rows_data}
    if infer_missing:
        for arg in extract_signature_args(signature):
            name = arg.split("=", 1)[0].strip()
            clean_name = name.strip("{}[] ")
            if not clean_name or clean_name.startswith("...") or clean_name in documented_names:
                continue
            rows_data.append({
                "name": clean_name,
                "type": inferred_param_type(clean_name, signature.split("(", 1)[0].replace("async ", "").strip()),
                "attributes": "optional" if "=" in arg else "",
                "default": arg.split("=", 1)[1].strip() if "=" in arg else "",
                "description": inferred_param_description(clean_name, signature.split("(", 1)[0].replace("async ", "").strip()),
            })
    if not rows_data:
        return ""
    rows = [
        '<table class="helios-api-params">',
        "<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>",
        "<tbody>",
    ]
    for row in rows_data:
        type_cell = type_html(row["type"]) if row["type"] else ""
        name = row["name"]
        if "." in name:
            parent, child = name.rsplit(".", 1)
            name_cell = (
                f'<span class="helios-api-param-nested" title="{html.escape(name)}">'
                f'<span aria-hidden="true">|</span><code>{html.escape(child)}</code>'
                "</span>"
            )
        else:
            name_cell = f'<code>{html.escape(name)}</code>'
        attributes_cell = html.escape(row["attributes"])
        default_cell = f"<code>{html.escape(row['default'])}</code>" if row["default"] else ""
        rows.append(
            "<tr>"
            f'<td class="helios-api-param-name">{name_cell}</td>'
            f'<td class="helios-api-param-type">{type_cell}</td>'
            f'<td class="helios-api-param-attributes">{attributes_cell}</td>'
            f'<td class="helios-api-param-default">{default_cell}</td>'
            f'<td class="helios-api-param-description">{inline_html(row["description"])}</td>'
            "</tr>"
        )
    rows.extend(["</tbody>", "</table>"])
    return "\n".join(rows)


def returns_markup(returns: str) -> str:
    if not returns:
        return ""
    text = returns.strip()
    type_hint, remainder = split_jsdoc_type(text)
    if type_hint:
        text = remainder
    elif text and not re.search(r"\s", text):
        type_hint = text
        text = ""
    type_markup = f'<span class="helios-api-return-type"><strong>Type</strong> {type_html(type_hint)}</span>' if type_hint else ""
    desc_html = f"<p>{inline_html(text)}</p>" if text else ""
    return f'<div class="helios-api-return">{desc_html}{type_markup}</div>'


def returns_type_text(returns: str) -> str:
    if not returns:
        return ""
    text = returns.strip()
    type_hint, _ = split_jsdoc_type(text)
    if type_hint:
        return normalize_type_text(type_hint)
    if text and not re.search(r"\s", text):
        return normalize_type_text(text)
    return ""


def humanize_name(name: str) -> str:
    words = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", name).replace("_", " ").replace("-", " ")
    return words.lower()


def inferred_method_summary(method: Symbol) -> str:
    name = method.name
    readable = humanize_name(name)
    if method.params or extract_signature_args(method.signature):
        args = extract_signature_args(method.signature)
        if len(args) == 1:
            arg_name = args[0].split("=", 1)[0].strip("{}[] ")
            if arg_name in {"value", "color", "style", "options", "mode", "insets"}:
                return f"Read or set the {readable} setting."
        if name.startswith("set"):
            return f"Set the {humanize_name(re.sub(r'^set', '', name) or name)} setting."
    if name.startswith(("get", "is", "has")):
        subject = humanize_name(re.sub(r"^(get|is|has)", "", name) or name)
        return f"Returns the current {subject} value or state."
    if name.startswith(("set", "replace", "restore", "apply", "activate", "clear", "reset", "toggle")):
        subject = humanize_name(re.sub(r"^(set|replace|restore|apply|activate|clear|reset|toggle)", "", name) or name)
        return f"Updates the {subject} state on the current instance."
    if name.startswith(("add", "remove", "register", "use", "detach", "destroy")):
        subject = humanize_name(re.sub(r"^(add|remove|register|use|detach|destroy)", "", name) or name)
        return f"Manages {subject} for the current instance."
    if name.startswith(("load", "save", "serialize", "export", "import", "parse")):
        subject = humanize_name(re.sub(r"^(load|save|serialize|export|import|parse)", "", name) or name)
        return f"Handles {subject} for the current graph or visualization state."
    return f"Configures or reads {readable}."


def inferred_return_type(method: Symbol) -> str:
    name = method.name
    args = extract_signature_args(method.signature)
    if method.kind == "property":
        return ""
    if len(args) == 1:
        arg_name = args[0].split("=", 1)[0].strip("{}[] ")
        value_type = inferred_param_type(arg_name, name)
        if arg_name in {"value", "color", "style", "mode", "options", "insets"}:
            return f"{value_type or 'Object'}|this"
    if name.startswith(("set", "clear", "reset", "activate", "restore", "register", "request", "enable", "disable", "notify", "use", "add")):
        return "this"
    if name.startswith(("get", "is", "has")):
        return ""
    return ""


def inferred_return_description(method: Symbol) -> str:
    type_text = inferred_return_type(method)
    if not type_text:
        return ""
    if "|" in type_text and "this" in type_text:
        readable = humanize_name(method.name)
        return f"Current {readable} value when called without arguments; otherwise this instance for chaining."
    return "This instance."


def member_return_type(member: Symbol) -> str:
    return returns_type_text(member.returns) or inferred_return_type(member)


def member_returns_markup(member: Symbol) -> str:
    if member.returns:
        return returns_markup(member.returns)
    return_type = inferred_return_type(member)
    description = inferred_return_description(member)
    if not return_type and not description:
        return ""
    type_markup = f'<span class="helios-api-return-type"><strong>Type</strong> {type_html(return_type)}</span>' if return_type else ""
    desc_html = f"<p>{inline_html(description)}</p>" if description else ""
    return f'<div class="helios-api-return">{desc_html}{type_markup}</div>'


SECTION_DESCRIPTIONS = {
    "Static Properties": "Constants and metadata exposed directly on the class.",
    "Lifecycle": "Creation, initialization, prewarming, cleanup, and renderer lifetime.",
    "Behaviors": 'Behavior registration and state. Built-in behavior implementations are documented under <a href="section-behaviors.md">Behaviors</a>.',
    "Filtering And State": 'Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.',
    "Network And Persistence": 'Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.',
    "Figure Export": 'High-resolution figure capture and download. <a href="ExporterBehavior.md">ExporterBehavior</a> provides the built-in export interface.',
    "Events": "Event subscription helpers and emitted interaction events.",
    "Camera And View": 'Camera framing, target following, dimensional mode, and transitions. <a href="InterfaceBehavior.md">InterfaceBehavior</a> can expose these controls.',
    "Layout And Positions": 'Layout selection, position sources, interpolation, and position snapshots. <a href="LayoutBehavior.md">LayoutBehavior</a> handles the built-in layout UI.',
    "Mappers": 'Mapper configuration for node and edge visual channels. <a href="MappersBehavior.md">MappersBehavior</a> handles mapper UI state.',
    "Appearance": 'Visual rendering settings for nodes, edges, labels, legends, density, shading, and background. <a href="AppearanceBehavior.md">AppearanceBehavior</a>, <a href="LabelsBehavior.md">LabelsBehavior</a>, and <a href="LegendsBehavior.md">LegendsBehavior</a> cover the built-in controls.',
    "Rendering And Picking": 'Render requests, picking, framebuffer inspection, and attribute tracking. <a href="HoverBehavior.md">HoverBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> use these lower-level hooks.',
    "Configuration": "General configuration setters and compatibility helpers.",
    "Utilities": "Additional public helpers that do not belong to a narrower API area.",
}


def infer_member_section(class_name: str, member: Symbol) -> str:
    if member.category and member.category != "Reference":
        return member.category
    name = member.name
    if member.kind == "property":
        if name.startswith("static ") or name.isupper() or name in {"STATES", "STATE_BITS", "UI_BINDINGS"}:
            return "Static Properties"
        return "Instance Properties"
    if name == "constructor":
        return "Construction"
    if name in {"initialize", "ready", "prewarm", "destroy", "replaceNetwork"}:
        return "Lifecycle"
    if "Behavior" in name or name in {"behavior", "behaviors", "hasBehavior", "getBehavior", "registerBehavior", "useBehavior", "serializeBehaviorState", "restoreBehaviorState"}:
        return "Behaviors"
    if "Filter" in name or "State" in name or name in {"nodeState", "edgeState", "resetStateStyles"}:
        return "Filtering And State"
    if "Network" in name or "VisualizationState" in name or "Portable" in name or name.startswith(("load", "save", "serialize", "restore", "import", "exportVisualization", "attach", "clearAttached")):
        return "Network And Persistence"
    if "Figure" in name or "Export" in name:
        return "Figure Export"
    if name in {"on", "listen", "off", "onAny", "emit"}:
        return "Events"
    if "Camera" in name or name in {"frameNetwork", "mode", "setMode"}:
        return "Camera And View"
    if "Layout" in name or "Position" in name or name in {"layout", "positions", "interpolation", "startLayout", "stopLayout"}:
        return "Layout And Positions"
    if "Mapper" in name or name == "mappers":
        return "Mappers"
    if any(term in name for term in ("Color", "Opacity", "Size", "Width", "Blend", "Depth", "Shaded", "AmbientOcclusion", "Density", "Label", "Legend", "supersampling")):
        return "Appearance"
    if any(term in name for term in ("Render", "Picking", "Framebuffer", "AttributeTracking")):
        return "Rendering And Picking"
    if name.startswith(("set", "get", "clear", "reset", "toggle")):
        return "Configuration"
    return "Utilities"


def member_summary(member: Symbol) -> str:
    if member.summary:
        return member.summary
    if member.kind == "property":
        return f"{humanize_name(member.name).capitalize()} exposed by the class."
    return inferred_method_summary(member)


def method_anchor(method: Symbol) -> str:
    return f"{method.kind}-{slug(method.name).lower()}"


def section_anchor(section: str) -> str:
    return f"api-{slug(section).lower()}"


def clean_symbol_signature(symbol: Symbol) -> str:
    signature = symbol.signature.strip()
    if symbol.kind in {"method", "constructor"}:
        args_match = re.search(r"\((?P<args>[^)]*)\)", signature)
        prefix = "async " if signature.startswith("async ") else ""
        return f"{prefix}{symbol.name}({args_match.group('args') if args_match else ''})"
    return signature


def inferred_example(member: Symbol) -> str:
    if member.examples:
        return ""
    if member.kind != "method":
        return ""
    args = extract_signature_args(member.signature)
    if not args:
        if member.name.startswith(("get", "is", "has")):
            return f"const value = helios.{member.name}();"
        return ""
    first = args[0].split("=", 1)[0].strip("{}[] ")
    if first in {"handler"}:
        return f"const stop = helios.{member.name}(EVENTS.NODE_CLICK, (event) => {{\n  console.log(event.detail);\n}});"
    if first in {"color"} or member.name.lower().endswith("color") or "background" in member.name.lower():
        return f"helios.{member.name}('#4aa3ff');"
    if first in {"mode"}:
        return f"await helios.{member.name}('2d');" if member.signature.strip().startswith("async ") else f"helios.{member.name}('2d');"
    if first in {"options", "maybeOptions", "previewOptions"}:
        return f"helios.{member.name}({{\n  enabled: true,\n}});"
    if first in {"value"}:
        value_type = inferred_param_type(first, member.name)
        value = "true" if value_type == "boolean" else ("'auto'" if value_type == "string" else "1")
        return f"helios.{member.name}({value});"
    if first in {"nodeIndices", "nodeIds", "indices"}:
        return f"helios.{member.name}([0, 1, 2]);"
    return ""


def group_members(members: tuple[Symbol, ...]) -> list[tuple[str, list[Symbol]]]:
    order = [
        "Construction",
        "Static Properties",
        "Instance Properties",
        "Lifecycle",
        "Behaviors",
        "Filtering And State",
        "Network And Persistence",
        "Figure Export",
        "Events",
        "Camera And View",
        "Layout And Positions",
        "Mappers",
        "Appearance",
        "Rendering And Picking",
        "Configuration",
        "Utilities",
    ]
    grouped_members: dict[str, list[Symbol]] = {}
    for member in members:
        if member.kind == "constructor":
            continue
        grouped_members.setdefault(member.category or "Utilities", []).append(member)
    result = []
    for section in order + sorted(section for section in grouped_members if section not in order):
        items = grouped_members.get(section, [])
        if items:
            result.append((section, items))
    return result


def member_detail(member: Symbol) -> str:
    summary = member_summary(member)
    signature = member.signature.strip()
    params = parameter_table(member.params, signature)
    returns = member_returns_markup(member)
    args_match = re.search(r"\((?P<args>[^)]*)\)", signature)
    call = f"{member.name}({args_match.group('args') if args_match else ''})" if member.kind == "method" else member.name
    return_type = member_return_type(member)
    return_suffix = f" &rarr; &#123;{html.escape(return_type)}&#125;" if return_type else ""
    heading_level = "###"
    parts = [
        f'<a id="{method_anchor(member)}" class="helios-api-member-anchor"></a>',
        "",
        f"{heading_level} `{call}`{return_suffix}",
        "",
        '<div class="helios-api-member-detail">',
        "",
    ]
    parts.append(f'<p class="helios-api-source">Source: <code>{html.escape(rel(member.source))}:{member.line}</code></p>')
    if summary:
        parts.append(f"<p>{inline_html(summary)}</p>")
    if params:
        parts.extend(["<h4>Parameters</h4>", params])
    if returns:
        parts.extend(["<h4>Returns</h4>", returns])
    if member.remarks:
        parts.extend(["<h4>Notes</h4>", f"<p>{inline_html(member.remarks)}</p>"])
    for example in member.examples:
        parts.extend([
            "<h4>Example</h4>",
            '<pre class="helios-api-example"><code>',
            html.escape(example.strip()),
            "</code></pre>",
        ])
    generated_example = inferred_example(member)
    if generated_example:
        parts.extend([
            "<h4>Example</h4>",
            '<pre class="helios-api-example"><code>',
            html.escape(generated_example),
            "</code></pre>",
        ])
    parts.append("</div>")
    return "\n".join(parts)


def member_sections(members: tuple[Symbol, ...]) -> str:
    groups = [(section, [item for item in items if item.kind in {"method", "property"}]) for section, items in group_members(members)]
    groups = [(section, items) for section, items in groups if items]
    if not groups:
        return ""
    chunks: list[str] = []
    for section, items in groups:
        chunks.extend([
            f"## {section} {{ #{section_anchor(section)} .helios-api-section-title }}",
            "",
        ])
        description = SECTION_DESCRIPTIONS.get(section, "")
        if description:
            chunks.extend([f'<p class="helios-api-section-description">{description}</p>', ""])
        for member in items:
            chunks.extend([member_detail(member), ""])
    return "\n".join(chunks)


def symbol_detail_markdown(symbol: Symbol, package_title: str) -> str:
    constructor = next((method for method in symbol.methods if method.kind == "constructor"), None)
    parts = [
        f"# {symbol.name}",
        "",
        f'<div class="helios-api-kind">{html.escape(symbol.kind)}</div>',
        "",
        f'<p class="helios-api-back"><a href="index.md">Back to {html.escape(package_title)}</a></p>',
        "",
        definition_rows([
            ("Kind", symbol.kind),
            ("Source", f"{rel(symbol.source)}:{symbol.line}"),
        ]),
    ]
    if symbol.summary:
        parts.extend(["", "## Description", "", '<div markdown="1" class="helios-api-template-section">', symbol.summary, "</div>"])
    if symbol.signature:
        parts.extend(["", "## Signature", "", '<div markdown="1" class="helios-api-template-section">', "", "```text", symbol.signature.strip(), "```", "", "</div>"])
    constructor_params = constructor.params if constructor else ()
    if symbol.params or constructor_params:
        parts.extend([
            "",
            "## Parameters",
            "",
            '<div class="helios-api-template-section">',
            parameter_table(symbol.params or constructor_params, constructor.signature if constructor else symbol.signature),
            "</div>",
        ])
    if symbol.returns:
        parts.extend(["", "## Returns", "", '<div class="helios-api-template-section">', returns_markup(symbol.returns), "</div>"])
    if symbol.remarks:
        parts.extend(["", "## Notes", "", '<div markdown="1" class="helios-api-template-section">', symbol.remarks, "</div>"])
    members_markup = member_sections(symbol.methods)
    if members_markup:
        parts.extend(["", members_markup])
    for example in symbol.examples:
        parts.extend(["", "## Example", "", '<div markdown="1" class="helios-api-template-section">', "", "```js", example.strip(), "```", "", "</div>"])
    return "\n".join(parts)


def symbol_directory(symbols: list[Symbol], link_prefix: str = "") -> str:
    if not symbols:
        return "_No annotated symbols were found._\n"
    rows = ['<div class="helios-api-directory">']
    for symbol in symbols:
        summary = symbol.summary.replace("\n", " ") or "Add source documentation to expand this reference entry."
        rows.extend([
            f'<a class="helios-api-directory-item" href="{link_prefix}{slug(symbol.name)}/">',
            f"<span>{html.escape(symbol.kind)}</span>",
            f"<strong>{html.escape(symbol.name)}</strong>",
            f"<em>{html.escape(summary)}</em>",
            "</a>",
        ])
    rows.append("</div>")
    return "\n".join(rows) + "\n"


def sectioned_directory(groups: list[tuple[str, str, list[Symbol]]], link_prefix: str = "") -> str:
    sections: list[str] = []
    for title, description, symbols in groups:
        if not symbols:
            continue
        sections.extend([
            f"## {title}",
            "",
            f'<p class="helios-api-group-description">{html.escape(description)}</p>' if description else "",
            symbol_directory(symbols, link_prefix=link_prefix),
            "",
        ])
    return "\n".join(sections)


def behavior_directory(symbols: list[Symbol], link_prefix: str = "") -> str:
    core_names = {
        "Behavior",
        "BehaviorManager",
        "BehaviorRegistry",
    }
    auxiliary_names = {
        "BEHAVIOR_IDS",
        "createDefaultBehaviorRegistry",
    }
    groups = [
        (
            "Core",
            "Base behavior contracts, registry helpers, and runtime managers shared by every behavior.",
            [symbol for symbol in symbols if symbol.name in core_names],
        ),
        (
            "Behavior Implementations",
            "Built-in behavior classes that attach interaction, layout, mapper, filter, labels, legends, interface, and export workflows to a Helios instance.",
            [symbol for symbol in symbols if symbol.name.endswith("Behavior") and symbol.name not in core_names],
        ),
        (
            "Auxiliary",
            "Supporting exports used to configure or compose behavior integrations.",
            [
                symbol
                for symbol in symbols
                if symbol.name in auxiliary_names or (symbol.name not in core_names and not symbol.name.endswith("Behavior"))
            ],
        ),
    ]
    return sectioned_directory(groups, link_prefix=link_prefix)


SECTION_DETAILS = {
    ("Helios Web API", "Core"): """
Use this section when wiring a visualization into an application. `Helios` owns
the renderer, behavior registry, camera, mapper collections, layout controller,
filter state, persistence state, and figure export entry points. The common
runtime path is to create or load a `HeliosNetwork`, instantiate `Helios` with a
DOM container, wait for readiness, then configure behaviors and mappers.

The core page is also the best place to check lifecycle details: initialization
promises, frame requests, renderer fallback behavior, and methods that bridge
application state to the visual scene.
""",
    ("Helios Web API", "Behaviors"): """
Behaviors are the user-facing modules that keep Helios composable. Each behavior
owns one workflow, such as labels, legends, filters, mappers, layout controls,
selection, hover inspection, interface controls, persistence, or export. The
behavior manager creates the default set, and applications can register custom
behavior classes when they need different UI or state synchronization.

Read the base `Behavior` contract first if you are adding a new behavior. Use
the implementation pages when you want to configure an existing workflow.
""",
    ("Helios Web API", "Layouts"): """
Layouts are responsible for producing node positions, not for drawing nodes.
Static layouts consume existing coordinates; worker-backed and GPU-backed
layouts update positions over time. Position delegates expose the buffer bridge
between layout algorithms and renderable node positions.

Choose the layout page based on where work should run: static data, JavaScript
worker force simulation, or GPU force simulation.
""",
    ("Helios Web API", "Mappers"): """
Mappers translate graph attributes into visual channels. A mapper can connect
node or edge attributes to color, size, width, opacity, labels, outlines, or
other renderer inputs. Mapper collections keep related mapper state grouped so
behaviors and UI panels can read and update it consistently.

Use mapper APIs when the visualization should react to data values rather than
constant style settings.
""",
    ("Helios Web API", "Filters"): """
Filters describe which graph elements should remain visible and, depending on
configuration, which elements should continue participating in layout. They are
usually created from attribute predicates or query-like state and then attached
through the filter behavior.

Use filters for reversible visual exploration. Use Helios Network selectors
when you need a graph-data operation or a persistent subset.
""",
    ("Helios Web API", "Persistence"): """
Persistence APIs save visualization state, preferences, sessions, and storage
envelopes. The state manager captures runtime settings such as active mappers,
panels, layouts, and behavior state. Storage managers decide where those
snapshots live: browser storage, remote storage, dummy storage, or a host
application bridge.

Use these APIs when an application needs autosave, named sessions, portable
state files, or host-specific save/restore integration.
""",
    ("Helios Web API", "Export"): """
Export APIs capture figures and previews from the renderer. Presets describe
common output sizes and settings, while export helpers coordinate render
settling, background choices, and format-specific capture.

Use these APIs for screenshots, publication figures, thumbnail generation, and
host applications that need deterministic preview images.
""",
    ("Helios Network JS/WASM API", "Methods"): """
The JavaScript/WASM methods are split between ergonomic helpers and low-level
buffer access. Attribute helpers are the right default for application code.
Direct buffer methods are for performance-sensitive integrations that need to
operate on WASM-backed typed arrays.

When using direct buffers, allocate first and view second. Avoid holding a typed
array view across calls that can grow WASM memory; use `withBufferAccess(...)`
where available.
""",
    ("Helios Network Native C API", "Serialization"): """
Serialization functions are the source of truth for file-format support in the
native graph core. Higher-level JavaScript, Python, CLI, widget, and desktop
surfaces delegate to these readers and writers when possible.

Use the data-format guides for file structure explanations and language-level
load/save examples. Use this reference for exact native function signatures.
""",
}


def section_details(package_title: str, title: str) -> str:
    return SECTION_DETAILS.get((package_title, title), "").strip()


def write_symbol_pages(package_dir: Path, package_title: str, symbols: list[Symbol]) -> None:
    seen: set[str] = set()
    for symbol in symbols:
        page = package_dir / link_for(symbol)
        if page.name in seen:
            page = package_dir / f"{slug(symbol.name)}-{symbol.line}.md"
        seen.add(page.name)
        write(page, symbol_detail_markdown(symbol, package_title))


def write_group_pages(package_dir: Path, package_title: str, groups: list[tuple[str, str, list[Symbol]]]) -> None:
    for title, description, symbols in groups:
        directory = behavior_directory(symbols, link_prefix="../") if package_title == "Helios Web API" and title == "Behaviors" else symbol_directory(symbols, link_prefix="../")
        details = section_details(package_title, title)
        text = f"""
# {title}

<p class="helios-api-back"><a href="index.md">Back to {html.escape(package_title)}</a></p>

{description}

{details}

{directory}
"""
        write(package_dir / f"section-{slug(title).lower()}.md", text)


def typed_parameters(symbol: Symbol) -> list[dict[str, str]]:
    rows = [parse_param_doc(param) for param in symbol.params]
    documented_names = {row["name"].split(".", 1)[0].strip("{}[] ") for row in rows}
    for arg in extract_signature_args(symbol.signature):
        name = arg.split("=", 1)[0].strip()
        clean_name = name.strip("{}[] ")
        if not clean_name or clean_name.startswith("...") or clean_name in documented_names:
            continue
        rows.append({
            "name": clean_name,
            "type": inferred_param_type(clean_name, symbol.name),
            "attributes": "optional" if "=" in arg else "",
            "default": arg.split("=", 1)[1].strip() if "=" in arg else "",
            "description": inferred_param_description(clean_name, symbol.name),
        })
    return [
        {
            "name": row["name"],
            "type": normalize_type_text(row["type"]),
            "attributes": row["attributes"],
            "default": row["default"],
            "description": row["description"],
        }
        for row in rows
    ]


def typed_returns(returns: str) -> dict[str, str]:
    type_hint, description = split_jsdoc_type(returns.strip()) if returns else ("", "")
    if returns and not type_hint and returns.strip() and not re.search(r"\s", returns.strip()):
        type_hint = returns.strip()
        description = ""
    return {
        "type": normalize_type_text(type_hint),
        "description": description,
    }


def typed_symbol(symbol: Symbol) -> dict:
    returns = typed_returns(symbol.returns)
    return {
        "name": symbol.name,
        "kind": symbol.kind,
        "source": {"path": rel(symbol.source), "line": symbol.line},
        "summary": member_summary(symbol) if symbol.kind in {"method", "property"} else symbol.summary,
        "signature": clean_symbol_signature(symbol),
        "parameters": typed_parameters(symbol),
        "returns": returns,
        "remarks": symbol.remarks,
        "examples": list(symbol.examples),
        "category": symbol.category,
        "methods": [typed_symbol(method) for method in symbol.methods],
    }


API_REFERENCE: dict[str, dict] = {
    "schemaVersion": "1.0.0",
    "description": "Typed Helios API documentation reference generated from public package boundaries and source annotations.",
    "packages": {},
}


def record_package_reference(package_id: str, package_title: str, version: str, symbols: list[Symbol], notes: dict | None = None) -> None:
    API_REFERENCE["packages"][package_id] = {
        "title": package_title,
        "version": version,
        "symbols": [typed_symbol(symbol) for symbol in symbols],
        "notes": notes or {},
    }


def missing_summary_list(symbols: list[Symbol]) -> list[Symbol]:
    return [symbol for symbol in symbols if not symbol.summary.strip()]


BEHAVIOR_EXTENSION_CLASSES = {
    "Behavior",
    "BehaviorManager",
    "BehaviorRegistry",
    "AppearanceBehavior",
    "ExporterBehavior",
    "FilterBehavior",
    "HoverBehavior",
    "InterfaceBehavior",
    "LabelsBehavior",
    "LayoutBehavior",
    "LegendsBehavior",
    "MappersBehavior",
    "SelectionBehavior",
}


PRIMARY_MEMBER_COVERAGE_CLASSES = {
    "Helios",
    "HeliosFilter",
    "HeliosUI",
}


def is_member_coverage_optional(symbol: Symbol, member: Symbol) -> bool:
    if symbol.name not in PRIMARY_MEMBER_COVERAGE_CLASSES:
        return True
    if member.name == "constructor":
        return True
    if symbol.name in BEHAVIOR_EXTENSION_CLASSES:
        return True
    return False


def missing_member_summary_list(symbols: list[Symbol]) -> list[tuple[Symbol, Symbol]]:
    missing: list[tuple[Symbol, Symbol]] = []
    for symbol in symbols:
        for member in symbol.methods:
            if is_member_coverage_optional(symbol, member):
                continue
            if member.kind in {"method", "property"} and not member.summary.strip():
                missing.append((symbol, member))
    return missing


def annotated_symbols(symbols: list[Symbol]) -> list[Symbol]:
    return [symbol for symbol in symbols if symbol.summary.strip()]


def unique_symbols(symbols: list[Symbol]) -> list[Symbol]:
    seen: set[str] = set()
    unique: list[Symbol] = []
    for symbol in symbols:
        if symbol.name in seen:
            continue
        seen.add(symbol.name)
        unique.append(symbol)
    return unique


def with_category(symbol: Symbol, category: str) -> Symbol:
    return Symbol(
        symbol.name,
        symbol.kind,
        symbol.source,
        symbol.line,
        symbol.summary,
        symbol.signature,
        symbol.params,
        symbol.returns,
        symbol.remarks,
        symbol.examples,
        category,
        symbol.methods,
    )


def categorize_helios_web(symbol: Symbol) -> str:
    name = symbol.name
    source = rel(symbol.source)
    if name in {"EVENTS", "FIGURE_EXPORT_PRESETS"}:
        return "Constants"
    if name in {"Helios"}:
        return "Core"
    if name in {"createDefaultMappers"}:
        return "Internal"
    if name in {"BEHAVIOR_IDS", "createDefaultBehaviorRegistry"}:
        return "Behaviors"
    if "behaviors/" in source or name.endswith("Behavior") or name in {"Behavior", "BehaviorManager", "BehaviorRegistry"}:
        return "Behaviors"
    if "layouts/" in source or name.endswith("Layout") or name in {"GpuForcePositionDelegate", "PositionDelegate"}:
        return "Layouts"
    if "pipeline/" in source or name in {"Mapper", "MapperCollection", "VisualAttributes"}:
        return "Mappers"
    if "filters/" in source or name.endswith("Filter"):
        return "Filters"
    if "export/" in source or "Export" in name or name.startswith("exportFigure") or name.startswith("getFigureExport"):
        return "Export"
    if (
        "persistence/" in source
        or "/storage/" in source
        or "/state/" in source
        or "Persistence" in name
        or "Storage" in name
        or name.startswith("createDefault")
        or name.startswith("serialize")
        or name.startswith("parse")
        or name.startswith("migrate")
    ):
        return "Persistence"
    if name.startswith(("createMemory", "LocalStorage", "IndexedDB", "SessionStore", "State")):
        return "Persistence"
    return "Internal"


def categorize_network_js(symbol: Symbol) -> str:
    if symbol.kind == "class":
        return "Classes"
    if symbol.kind == "method":
        return "Methods"
    return "Enums And Constants"


def categorize_python(symbol: Symbol) -> str:
    if symbol.name.startswith(("read_", "to_", "from_")):
        return "Import And Conversion"
    if symbol.name in {"Network"}:
        return "Network"
    if "UMAP" in symbol.name or symbol.name == "NetworkExportResult":
        return "UMAP"
    return "Enums And Models"


def categorize_c(symbol: Symbol) -> str:
    name = symbol.name
    if "Selector" in name:
        return "Selectors"
    if "Session" in name:
        return "Measurement Sessions"
    if any(term in name for term in ("Measure", "Leiden", "ConnectedComponents", "Coreness")):
        return "Measurements"
    if any(term in name for term in ("Read", "Write", "Serialization")):
        return "Serialization"
    if "Query" in name or "Select" in name:
        return "Queries"
    if "Attribute" in name or "Category" in name:
        return "Attributes"
    if "Buffer" in name or "Active" in name or "Version" in name:
        return "Buffers And Versions"
    if any(term in name for term in ("Add", "Remove", "Neighbor", "Edge", "Node", "Topology", "Compact")):
        return "Topology"
    return "Network Lifecycle"


def apply_categories(symbols: list[Symbol], categorizer) -> list[Symbol]:
    return [with_category(symbol, categorizer(symbol)) for symbol in symbols]


def grouped(symbols: list[Symbol], descriptions: dict[str, str], order: list[str]) -> list[tuple[str, str, list[Symbol]]]:
    by_category: dict[str, list[Symbol]] = {}
    for symbol in symbols:
        by_category.setdefault(symbol.category, []).append(symbol)
    result: list[tuple[str, str, list[Symbol]]] = []
    for category in order + sorted(category for category in by_category if category not in order):
        items = by_category.get(category, [])
        if items:
            result.append((category, descriptions.get(category, ""), sorted(items, key=lambda item: item.name.lower())))
    return result


def require_summaries(symbols: list[Symbol], names: set[str], label: str) -> None:
    missing = sorted(
        name
        for name in names
        if not any(symbol.name == name and symbol.summary.strip() for symbol in symbols)
    )
    if missing:
        raise ApiExtractionError(f"{label} is missing source annotation summaries for: {', '.join(missing)}")


def emit_helios_web() -> None:
    package_dir = DOCS / "api" / "helios-web"
    clean_generated_api_dir(package_dir)
    package = read_json(ROOT / "helios-web-next" / "package.json")
    entry = ROOT / "helios-web-next" / "src" / "index.js"
    exports = parse_js_exports(entry)
    export_sources = parse_js_export_sources(entry)
    symbols: list[Symbol] = []
    for source in sorted(set(export_sources.values())):
        names = {name for name, path in export_sources.items() if path == source}
        symbols.extend(parse_js_source_symbols(source, names))
    class_method_sources: dict[str, tuple[Symbol, ...]] = {}
    for source in sorted(set(export_sources.values())):
        class_names = {symbol.name for symbol in symbols if symbol.kind == "class" and symbol.source == source}
        class_method_sources.update(parse_js_class_methods(source, class_names))
    symbols = attach_methods(symbols, class_method_sources)
    method_symbols = parse_js_methods(ROOT / "helios-web-next" / "src" / "Helios.js", {
        "getFigureExportCapabilities",
        "exportFigureBlob",
        "exportFigurePreviewBlob",
        "exportFigure",
    })
    method_symbols.extend(parse_js_methods(ROOT / "helios-web-next" / "src" / "behaviors" / "MappersBehavior.js", {
        "setChannelConfig",
        "getSerializedChannelConfig",
    }))
    method_symbols.extend(parse_js_methods(ROOT / "helios-web-next" / "src" / "behaviors" / "FilterBehavior.js", {
        "replaceRules",
        "clear",
    }))
    required = {
        "Helios",
        "Behavior",
        "BehaviorManager",
        "BehaviorRegistry",
        "SelectionBehavior",
        "HoverBehavior",
        "LabelsBehavior",
        "LegendsBehavior",
        "LayoutBehavior",
        "AppearanceBehavior",
        "MappersBehavior",
        "FilterBehavior",
        "ExporterBehavior",
        "InterfaceBehavior",
        "HeliosStorageManager",
        "BrowserStorageManager",
        "RemoteStorageManager",
        "DummyStorageManager",
        "HeliosStateManager",
        "HeliosFilter",
        "Mapper",
        "MapperCollection",
        "FIGURE_EXPORT_PRESETS",
        "createDefaultBehaviorRegistry",
        "createHeliosStorageManager",
        "createPersistenceEnvelope",
        "parsePersistenceEnvelope",
        "serializePersistenceEnvelope",
    }
    require_summaries(symbols + method_symbols, required, "Helios Web API")
    undocumented = [
        Symbol(name, "export", export_sources.get(name, entry), 1)
        for name in exports
        if name != "default" and not any(symbol.name == name and symbol.summary.strip() for symbol in symbols)
    ]
    member_gaps = missing_member_summary_list(symbols)
    # Helios Web method docs are rendered on their owning class pages. Keeping
    # them as standalone package cards mixes member APIs with class/module APIs
    # and makes sections such as Behaviors look like an unstructured symbol dump.
    all_documented = apply_categories(annotated_symbols(symbols), categorize_helios_web)
    web_groups = grouped(all_documented, {
        "Core": "The main visualization controller and primary user-facing entry points.",
        "Constants": "Named event ids, figure presets, and other exported constant surfaces.",
        "Behaviors": "Composable behavior modules for interaction, labels, legends, mappers, filters, interface state, and export controls.",
        "Layouts": "Layout controllers and position delegates for static, worker, D3 force, and GPU force layouts.",
        "Mappers": "Visual attribute mapping primitives used to bind graph data to colors, sizes, opacity, and related channels.",
        "Filters": "Filter builders and behavior APIs for render-only or render-and-layout graph filtering.",
        "Export": "Figure export presets, capability checks, PNG/SVG capture, and preview helpers.",
        "Persistence": "State manager, storage manager, session, preference, and envelope APIs for saving and restoring visualization state.",
        "Internal": "Advanced exported utilities that are usually consumed by Helios Web itself or custom integrations.",
    }, ["Core", "Constants", "Behaviors", "Layouts", "Mappers", "Filters", "Export", "Persistence", "Internal"])
    write_symbol_pages(package_dir, "Helios Web API", all_documented)
    write_group_pages(package_dir, "Helios Web API", web_groups)
    if not any(title == "Internal" for title, _, _ in web_groups):
        write(package_dir / "internal.md", """
# Internal

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

No advanced internal exports are documented in this build. When an exported helper is intended for advanced extension rather than everyday use, categorize it here in `scripts/generate_api_reference.py`.
""")
    record_package_reference(
        "helios-web",
        "Helios Web",
        package.get("version", "unknown"),
        all_documented,
        {"sourceEntry": rel(entry), "exportedSymbols": len(exports)},
    )
    text = f"""
# Helios Web API

<img class="helios-api-logo" src="../../assets/helios-web-logo.svg" alt="Helios Web logo">

<p class="helios-api-version">Version {package.get("version", "unknown")}</p>

Helios Web is the browser visualization layer: renderer selection, camera and interaction state, behaviors, mappers, filters, layouts, persistence, and export. The reference below is grouped by the way users usually extend or configure a visualization.

{sectioned_directory(web_groups)}

## Typed Reference

The docs build emits a structured typed reference at [`../reference.json`](../reference.json) from source exports and code annotations. TypeScript declaration files are downstream artifacts and are not used as an API documentation source.

## Annotation Coverage Notes

Top-level public exports without source summaries:

{chr(10).join(f"- `{symbol.name}` from {line_link(symbol)}" for symbol in undocumented[:120]) if undocumented else "- No unannotated public exports detected."}

Primary public class members currently using generated fallback descriptions:

{chr(10).join(f"- `{owner.name}.{member.name}` from {line_link(member)}" for owner, member in member_gaps[:160]) if member_gaps else "- No generated member-summary fallbacks detected."}
"""
    write(DOCS / "api" / "helios-web" / "index.md", text)


def emit_network_js() -> None:
    package_dir = DOCS / "api" / "helios-network-js-wasm"
    clean_generated_api_dir(package_dir)
    package = read_json(ROOT / "helios-network-v2" / "package.json")
    entry = ROOT / "helios-network-v2" / "src" / "helios-network.js"
    impl = ROOT / "helios-network-v2" / "src" / "js" / "HeliosNetwork.js"
    exports = parse_js_exports(entry)
    implementation_names = set(exports)
    if "default" in implementation_names:
        implementation_names.add("HeliosNetwork")
    symbols = parse_public_js_symbols(impl, implementation_names)
    symbols = attach_methods(symbols, parse_js_class_methods(impl, {symbol.name for symbol in symbols if symbol.kind == "class"}))
    require_summaries(symbols, {symbol.name for symbol in symbols}, "Helios Network JS/WASM API")
    method_names = {
        "nodeAttribute",
        "edgeAttribute",
        "nodeAttributes",
        "edgeAttributes",
        "networkAttribute",
        "networkAttributes",
        "defineNodeAttribute",
        "defineEdgeAttribute",
        "defineNetworkAttribute",
        "withBufferAccess",
        "getNodeAttributeBuffer",
        "getEdgeAttributeBuffer",
        "getNetworkAttributeBuffer",
    }
    method_symbols = parse_js_methods(impl, method_names)
    require_summaries(method_symbols, method_names, "Helios Network JS/WASM public methods")
    documented_symbols = apply_categories(annotated_symbols(symbols), categorize_network_js)
    documented_methods = apply_categories(annotated_symbols(method_symbols), categorize_network_js)
    all_documented = documented_symbols + documented_methods
    network_groups = grouped(all_documented, {
        "Classes": "Network and selector classes exposed by the JavaScript/WASM package.",
        "Methods": "High-level chainable attribute helpers and low-level buffer access methods.",
        "Enums And Constants": "Constants mirrored from the WASM/native core for attributes, traversal, measurements, and execution modes.",
    }, ["Classes", "Methods", "Enums And Constants"])
    write_symbol_pages(package_dir, "Helios Network JS/WASM API", all_documented)
    write_group_pages(package_dir, "Helios Network JS/WASM API", network_groups)
    record_package_reference(
        "helios-network-js-wasm",
        "Helios Network JS/WASM",
        package.get("version", "unknown"),
        all_documented,
        {"entry": rel(entry), "implementation": rel(impl), "exportedSymbols": len(exports)},
    )
    text = f"""
# Helios Network JS/WASM API

<p class="helios-api-version">Version {package.get("version", "unknown")}</p>

The JavaScript/WASM package wraps the WebAssembly graph store with selectors, attribute APIs, serialization helpers, and direct typed-buffer access. Use the chainable attribute helpers for everyday code; the direct buffer methods remain documented as the low-level performance path when performance requires operating on WASM-backed views directly.

{sectioned_directory(network_groups)}

## Coverage Notes

The current JavaScript/WASM package does not publish TypeScript declarations. Until declarations are added, this extractor uses the public package entry plus implementation JSDoc and refuses to document deep modules. The structured reference is available at [`../reference.json`](../reference.json).
"""
    write(DOCS / "api" / "helios-network-js-wasm" / "index.md", text)


def emit_network_python() -> None:
    docs_package_dir = DOCS / "api" / "helios-network-python"
    clean_generated_api_dir(docs_package_dir)
    package = read_json(ROOT / "helios-network-v2" / "python" / "pyproject.toml") if False else {}
    pyproject = (ROOT / "helios-network-v2" / "python" / "pyproject.toml").read_text(encoding="utf-8")
    version_match = re.search(r'^version\s*=\s*"([^"]+)"', pyproject, re.M)
    source_package_dir = ROOT / "helios-network-v2" / "python" / "src" / "helios_network"
    symbols = apply_categories(unique_symbols(parse_python_public_api(source_package_dir)), categorize_python)
    missing_docstrings = [symbol for symbol in symbols if not symbol.summary]
    if missing_docstrings:
        raise ApiExtractionError(
            "Helios Network Python API is missing public docstrings for: "
            + ", ".join(symbol.name for symbol in missing_docstrings)
        )
    python_groups = grouped(symbols, {
        "Network": "The main Python wrapper around the native graph core.",
        "Import And Conversion": "Readers and conversion helpers for BXNet, ZXNet, XNet, GML, node-link JSON, NetworkX, and igraph.",
        "UMAP": "UMAP integration helpers that export fuzzy and nearest-neighbor graphs as Helios networks.",
        "Enums And Models": "Enums and small model classes shared with the native core.",
    }, ["Network", "Import And Conversion", "UMAP", "Enums And Models"])
    write_symbol_pages(docs_package_dir, "Helios Network Python API", symbols)
    write_group_pages(docs_package_dir, "Helios Network Python API", python_groups)
    record_package_reference(
        "helios-network-python",
        "Helios Network Python",
        version_match.group(1) if version_match else "unknown",
        symbols,
        {"publicPackage": rel(source_package_dir)},
    )
    text = f"""
# Helios Network Python API

<p class="helios-api-version">Version {version_match.group(1) if version_match else "unknown"}</p>

The Python API provides a convenient wrapper for the native graph core plus file readers and conversion utilities for common graph ecosystems.

{sectioned_directory(python_groups)}

## Coverage Notes

The structured reference is available at [`../reference.json`](../reference.json).

{chr(10).join(f"- `{symbol.name}` from {line_link(symbol)}" for symbol in missing_docstrings) if missing_docstrings else "- No missing docstring summaries detected for extracted public Python symbols."}
"""
    write(DOCS / "api" / "helios-network-python" / "index.md", text)


def emit_network_c() -> None:
    package_dir = DOCS / "api" / "helios-network-native-c"
    clean_generated_api_dir(package_dir)
    include_dir = ROOT / "helios-network-v2" / "src" / "native" / "include" / "helios"
    symbols, missing = parse_c_headers(include_dir)
    if missing:
        raise ApiExtractionError(
            "Helios Network Native C API is missing Doxygen comments for: "
            + ", ".join(missing[:20])
        )
    symbols = apply_categories(symbols, categorize_c)
    c_groups = grouped(symbols, {
        "Network Lifecycle": "Allocation, destruction, version, and graph-wide metadata helpers.",
        "Topology": "Node, edge, neighbor, compaction, and topology mutation APIs.",
        "Attributes": "Attribute definition, lookup, categorization, and multi-category APIs.",
        "Buffers And Versions": "Direct buffer access and version counters used by high-performance integrations.",
        "Selectors": "Node and edge selector containers used for filtering and set operations.",
        "Queries": "Query parser and selector APIs.",
        "Serialization": "Readers and writers for BXNet, ZXNet, XNet, GML, and node-link JSON.",
        "Measurements": "One-shot graph measurements such as degree, strength, clustering, dimension, and centrality.",
        "Measurement Sessions": "Steppable native measurement sessions for long-running algorithms.",
    }, ["Network Lifecycle", "Topology", "Attributes", "Buffers And Versions", "Selectors", "Queries", "Serialization", "Measurements", "Measurement Sessions"])
    write_symbol_pages(package_dir, "Helios Network Native C API", symbols)
    write_group_pages(package_dir, "Helios Network Native C API", c_groups)
    record_package_reference(
        "helios-network-native-c",
        "Helios Network Native C",
        "native",
        symbols,
        {"includeDir": rel(include_dir), "exportedFunctions": len(symbols)},
    )
    text = f"""
# Helios Network Native C API

<p class="helios-api-version">Native core reference</p>

The C API is the native surface behind the WASM and Python bindings. Functions are grouped by lifecycle, topology, attributes, selectors, serialization, and measurements.

{sectioned_directory(c_groups)}

## Coverage Notes

The extractor reads `CX_EXTERN` declarations and the nearest preceding Doxygen-style block comment. Internal bundled headers and uthash/utarray compatibility headers are intentionally excluded. For more precise grouping later, add a section annotation to the Doxygen block and wire it into `scripts/generate_api_reference.py`.

{chr(10).join(f"- {item}" for item in missing[:80]) if missing else "- No missing C comment summaries detected for extracted declarations."}
"""
    write(DOCS / "api" / "helios-network-native-c" / "index.md", text)


def main() -> int:
    API_REFERENCE["packages"] = {}
    emit_helios_web()
    emit_network_js()
    emit_network_python()
    emit_network_c()
    write(DOCS / "api" / "reference.json", json.dumps(API_REFERENCE, indent=2, sort_keys=True))
    status = f"""
# API Reference

<p class="helios-api-version">Preview reference generated from revision {git_revision()}</p>

The API reference is generated from package boundaries and source annotations. Each package has a landing page, section pages through the navigation, and per-symbol pages for classes, functions, methods, constants, and native C functions.

<div class="helios-api-search" data-api-search>
  <label for="helios-api-search-input">Search API reference</label>
  <input id="helios-api-search-input" type="search" placeholder="Search classes, methods, functions, and constants" autocomplete="off">
  <div class="helios-api-search-results" data-api-search-results></div>
</div>

<div class="helios-api-directory">
  <a class="helios-api-directory-item" href="helios-web/"><span>browser visualization</span><strong>Helios Web</strong><em>Renderer, camera, behaviors, mappers, filters, layouts, persistence, and export.</em></a>
  <a class="helios-api-directory-item" href="helios-network-js-wasm/"><span>javascript / wasm</span><strong>Helios Network JS/WASM</strong><em>WASM graph store wrapper, selectors, attributes, serialization, and direct buffers.</em></a>
  <a class="helios-api-directory-item" href="helios-network-python/"><span>python</span><strong>Helios Network Python</strong><em>Python wrapper, file readers, conversion helpers, and UMAP graph export.</em></a>
  <a class="helios-api-directory-item" href="helios-network-native-c/"><span>native c</span><strong>Helios Network Native C</strong><em>Native graph lifecycle, topology, attributes, selectors, serialization, and measurements.</em></a>
</div>

The structured typed reference for tooling is available at [`reference.json`](reference.json). Do not hand-edit generated API pages; update the source annotations and rerun the generator.
"""
    write(DOCS / "api" / "index.md", status)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
