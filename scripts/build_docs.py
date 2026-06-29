#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import subprocess
import sys
import json
import os
from pathlib import Path


DOCS_SITE = Path(__file__).resolve().parents[1]
ROOT = Path(os.environ.get("HELIOS_MONOREPO_ROOT", DOCS_SITE.parent)).resolve()
VENDOR_DIR = DOCS_SITE / "docs" / "assets" / "vendor" / "helios"


def run(command: list[str]) -> None:
    subprocess.run(command, cwd=DOCS_SITE, check=True)


def copy_tree(source: Path, target: Path) -> None:
    if not source.exists():
        return
    if target.exists():
        shutil.rmtree(target)
    shutil.copytree(source, target)


def copy_file(source: Path, target: Path) -> None:
    if not source.exists():
        raise FileNotFoundError(f"Required docs example asset is missing: {source}")
    target.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(source, target)


def resolve_dist(package_name: str) -> Path:
    candidate = DOCS_SITE / "node_modules" / package_name / "dist"
    if candidate.exists():
        return candidate
    raise FileNotFoundError(
        f"Could not locate {package_name} dist assets in node_modules. "
        f"Install {package_name} with npm, or register a local npm link and run `npm run link:local`."
    )


def describe_staged_package(package_name: str) -> None:
    package_root = DOCS_SITE / "node_modules" / package_name
    package_json = package_root / "package.json"
    version = "unknown version"
    if package_json.exists():
        try:
            version = json.loads(package_json.read_text(encoding="utf-8")).get("version") or version
        except json.JSONDecodeError:
            pass
    source = "npm-linked local package" if package_root.is_symlink() else "npm-installed package"
    print(f"Staging {package_name} runtime bundle from {source} ({version})")


def copy_optional_bundle_helpers(source_dir: Path, target_dir: Path, bundle_source: str) -> None:
    """Copy Vite helper chunks referenced by the staged ESM bundle."""
    helper_names = sorted(set(re.findall(r"__vite-browser-external-[A-Za-z0-9_-]+\.js", bundle_source)))
    for helper_name in helper_names:
        copy_file(source_dir / helper_name, target_dir / helper_name)
        helper_map = source_dir / f"{helper_name}.map"
        if helper_map.exists():
            copy_file(helper_map, target_dir / f"{helper_name}.map")


def stage_example_assets() -> None:
    """Stage local ESM bundles used by interactive examples.

    Release docs prefer installed package bundles from node_modules. Local
    checkout builds are accepted as a fallback while preparing the release.
    """
    try:
        network_dist = resolve_dist("helios-network")
        web_dist = resolve_dist("helios-web")
    except FileNotFoundError:
        if (VENDOR_DIR / "helios-network.js").exists() and (VENDOR_DIR / "helios-web.es.js").exists():
            print("Using committed Helios vendor bundles; released packages were not installed yet.")
            return
        raise

    describe_staged_package("helios-network")
    describe_staged_package("helios-web")

    if VENDOR_DIR.exists():
        shutil.rmtree(VENDOR_DIR)
    VENDOR_DIR.mkdir(parents=True, exist_ok=True)

    network_source = (network_dist / "helios-network.js").read_text(encoding="utf-8")
    copy_file(network_dist / "helios-network.js", VENDOR_DIR / "helios-network.js")
    copy_file(network_dist / "helios-network.js.map", VENDOR_DIR / "helios-network.js.map")
    copy_optional_bundle_helpers(network_dist, VENDOR_DIR, network_source)
    copy_tree(network_dist / "compiled", VENDOR_DIR / "compiled")
    copy_tree(network_dist / "workers", VENDOR_DIR / "workers")

    copy_tree(web_dist / "assets", VENDOR_DIR / "assets")
    web_source = (web_dist / "helios-web.es.js").read_text(encoding="utf-8")
    web_source = web_source.replace('from "helios-network"', 'from "./helios-network.js"')
    web_source = web_source.replace('import("helios-network")', 'import("./helios-network.js")')
    web_source = web_source.replace('"/assets/', '"./assets/')
    (VENDOR_DIR / "helios-web.es.js").write_text(web_source, encoding="utf-8")
    copy_file(web_dist / "helios-web.es.js.map", VENDOR_DIR / "helios-web.es.js.map")


def resolve_main_app_dir() -> Path:
    for candidate in (
        DOCS_SITE / "node_modules" / "helios-web" / "docs" / "app",
        ROOT / "helios-web" / "docs" / "app",
    ):
        if (candidate / "main.js").exists():
            return candidate
    raise FileNotFoundError("Could not locate Helios Web main app source. Run `npm install` or set HELIOS_MONOREPO_ROOT.")


def rewrite_main_app_source(source: str) -> str:
    source = source.replace(
        "import HeliosNetwork, { AttributeType } from 'helios-network';",
        "import HeliosNetwork, { AttributeType } from '../docs/assets/vendor/helios/helios-network.js';",
    )
    source = source.replace(
        "import { Helios, EVENTS, HeliosUI } from '../../src/index.js';",
        "import { Helios, EVENTS, HeliosUI } from '../docs/assets/vendor/helios/helios-web.es.js';",
    )
    return source.replace("'/assets/umap/", "'/docs/assets/vendor/helios/assets/umap/")


def write_root_homepage() -> None:
    site_dir = DOCS_SITE / "site"
    site_dir.mkdir(parents=True, exist_ok=True)
    (site_dir / "index.html").write_text("""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Helios</title>
  <link rel="icon" href="/docs/assets/helios-mark.svg" type="image/svg+xml">
  <style>
    :root {
      color-scheme: light dark;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #f7f9fb;
      color: #17212b;
    }
    * { box-sizing: border-box; }
    body { margin: 0; min-height: 100vh; background: #f7f9fb; color: #17212b; }
    a { color: inherit; }
    .shell { width: min(1260px, calc(100vw - 40px)); margin: 0 auto; }
    header { min-height: min(760px, 100vh); display: flex; flex-direction: column; }
    nav { position: relative; z-index: 5; display: flex; justify-content: flex-end; align-items: center; gap: 24px; padding: 22px 0 6px; }
    .tabs { display: flex; align-items: center; gap: 4px; border: 1px solid #cbd5df; border-radius: 8px; padding: 4px; background: #ffffff; }
    .tabs a { text-decoration: none; font-weight: 650; font-size: 0.95rem; line-height: 1; padding: 10px 13px; border-radius: 6px; white-space: nowrap; }
    .tabs a:hover, .tabs a.primary { background: #17212b; color: #ffffff; }
    .hero { flex: 1; display: grid; grid-template-columns: minmax(0, 0.95fr) minmax(420px, 560px); align-items: center; gap: clamp(28px, 5vw, 64px); margin-top: -50pt; padding: 8px 0 60px; }
    .logo { width: min(390px, 76vw); height: auto; display: block; margin: 0 0 28px; }
    h1 { font-size: clamp(2.35rem, 6vw, 5.4rem); line-height: 0.96; margin: 0 0 24px; letter-spacing: 0; max-width: 760px; }
    .lead { max-width: 700px; font-size: 1.13rem; line-height: 1.68; margin: 0 0 30px; color: #435160; }
    .actions { display: flex; flex-wrap: wrap; gap: 10px; margin-bottom: 34px; }
    .button { border: 1px solid #17212b; color: #17212b; text-decoration: none; padding: 11px 13px; border-radius: 6px; font-weight: 700; }
    .button.primary { background: #17212b; color: white; }
    .button.disabled { color: #83909e; border-color: #b9c4cf; background: #edf2f6; cursor: not-allowed; position: relative; }
    .button.disabled::after { content: attr(data-tooltip); position: absolute; left: 50%; bottom: calc(100% + 10px); transform: translateX(-50%); padding: 6px 8px; border-radius: 5px; background: #17212b; color: #ffffff; font-size: 0.78rem; line-height: 1; white-space: nowrap; opacity: 0; pointer-events: none; transition: opacity 120ms ease; }
    .button.disabled:hover::after, .button.disabled:focus-visible::after { opacity: 1; }
    .facts { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; max-width: 760px; }
    .fact { border-top: 2px solid #2f7d79; padding-top: 10px; font-size: 0.92rem; line-height: 1.45; color: #435160; }
    .fact strong { display: block; color: #17212b; margin-bottom: 4px; }
    .preview { aspect-ratio: 1; min-height: 430px; border: 1px solid #cbd5df; border-radius: 8px; overflow: hidden; background: #ffffff; position: relative; }
    #network-preview { position: absolute; inset: 0; }
    .preview-label { position: absolute; left: 14px; bottom: 12px; z-index: 2; color: #17212b; font-size: 0.78rem; letter-spacing: 0; background: rgba(255, 255, 255, 0.76); padding: 7px 9px; border-radius: 5px; }
    .below { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1px; border-top: 1px solid #d8e0e8; background: #d8e0e8; }
    .below section { background: #ffffff; padding: 28px; min-height: 190px; }
    .below h2 { font-size: 1.05rem; margin: 0 0 10px; letter-spacing: 0; }
    .below p { margin: 0 0 18px; line-height: 1.6; color: #536170; }
    .below a { font-weight: 700; text-decoration-thickness: 1px; text-underline-offset: 3px; }
    @media (max-width: 860px) {
      header { min-height: auto; }
      nav { align-items: flex-start; flex-direction: column; }
      .tabs { width: 100%; overflow-x: auto; }
      .hero { grid-template-columns: 1fr; margin-top: 0; padding-top: 28px; }
      .preview { min-height: min(86vw, 420px); }
      .facts, .below { grid-template-columns: 1fr; }
    }
    @media (prefers-color-scheme: dark) {
      :root, body { background: #0d1117; color: #eef4fa; }
      .tabs, .below section { background: #111922; border-color: #2a3541; }
      .tabs { border-color: #2a3541; }
      .tabs a:hover, .tabs a.primary, .button.primary { background: #eef4fa; color: #0d1117; }
      .lead, .fact, .below p { color: #b6c2cf; }
      .fact strong { color: #eef4fa; }
      .button { border-color: #eef4fa; color: #eef4fa; }
      .button.disabled { color: #737f8d; border-color: #43505f; background: #17202a; }
      .button.disabled::after { background: #eef4fa; color: #0d1117; }
      .below { border-color: #2a3541; background: #2a3541; }
      .preview { border-color: #2a3541; background: #071018; }
      .preview-label { color: #dce8f2; background: rgba(7, 16, 24, 0.72); }
    }
  </style>
</head>
<body>
  <header class="shell">
    <nav aria-label="Primary">
      <div class="tabs">
        <a class="primary" href="/app/">App</a>
        <a href="/docs/">Docs</a>
        <a href="/docs/examples/">Examples</a>
        <a href="https://github.com/filipinascimento/helios-web">GitHub</a>
      </div>
    </nav>
    <div class="hero">
      <main>
        <img class="logo" src="/docs/assets/helios-logo.svg" alt="Helios">
        <h1>Interactive network visualization</h1>
        <p class="lead">Helios pairs a WebGPU/WebGL renderer with a WebAssembly graph store for graph visualization, embeddings, and real workflows. It is built for 1M+ nodes with real-time GPU-based layout in 2D and 3D, plus CLI, notebook, desktop, and agentic skill integrations.</p>
        <div class="actions">
          <a class="button primary" href="/app/">Launch app</a>
          <a class="button" href="/docs/">Read docs</a>
          <a class="button" href="/docs/getting-started/">Quickstart</a>
          <a class="button" href="/docs/apps/helios-cli/#agentic-skill">CLI & Skills</a>
          <span class="button disabled" role="button" aria-disabled="true" tabindex="0" data-tooltip="Coming soon...">Desktop</span>
        </div>
        <div class="facts">
          <div class="fact"><strong>Renderer</strong> WebGPU first, WebGL2 fallback.</div>
          <div class="fact"><strong>Network core</strong> WASM-backed graph storage, formats, and embeddings.</div>
          <div class="fact"><strong>Integrations</strong> Browser, CLI, notebooks, desktop, and agentic skills.</div>
        </div>
      </main>
      <aside class="preview" aria-label="3D Watts-Strogatz preview">
        <div id="network-preview"></div>
        <div class="preview-label">3D Watts-Strogatz preview</div>
      </aside>
    </div>
  </header>
  <div class="below">
    <section>
      <h2>Open The App</h2>
      <p>Load the main Helios Web app with the standard panels and the 10k-node Watts-Strogatz default.</p>
      <a href="/app/">Go to /app/</a>
    </section>
    <section>
      <h2>Build With Helios</h2>
      <p>Install `helios-network` and `helios-web`, then compose the renderer into your own application.</p>
      <a href="/docs/getting-started/">Start the quickstart</a>
    </section>
    <section>
      <h2>Use Other Hosts</h2>
      <p>Run Helios through the CLI, notebooks, or desktop package while keeping the same network formats.</p>
      <a href="/docs/apps/helios-cli/">See app integrations</a>
    </section>
  </div>
  <script type="module">
    import HeliosNetwork from '/docs/assets/vendor/helios/helios-network.js';
    import { Helios } from '/docs/assets/vendor/helios/helios-web.es.js';

    const container = document.querySelector('#network-preview');
    const label = document.querySelector('.preview-label');

    try {
      const network = await HeliosNetwork.generateWattsStrogatz({
        nodeCount: 2000,
        neighborLevel: 2,
        rewiringProbability: 0.006,
        directed: false,
        seed: 17,
      });
      const helios = new Helios(network, {
        container,
        mode: '3d',
        projection: 'perspective',
        ui: {
          panels: ['data', 'mappers', 'layout', 'camera'],
          allowDrag: true,
        },
        debug: false,
        storage: false,
        session: false,
        startup: {
          hideCanvasUntilFirstFrame: false,
          layoutIterations: 0,
          layoutDurationMs: 0,
          initialCameraFit: false,
        },
        warnOnUnsavedSessionChanges: false,
        legends: { enabled: false },
        behaviors: { legends: false },
      });
      await helios.ready;
      helios.layout?.()?.setSettings?.({ linkDistance: 6 }, { reheat: true, reason: 'landing-preview' });
      helios.nodeSizeScale(2);
      helios.edgeWidthScale(3);
      helios.legends(false);
      helios.setCameraPose?.({ distance: 1000, target: [0, 0, 0] }, { applyState: false });
      helios.cameraControls?.({
        autoFit: true,
        autoFitPaddingRatio: 0.04,
        animation: true,
        orbit: true,
        orbitSpeed: 0.04,
        orbitAngle: 16,
        orbitAxis: [0.83, 0.75, 0],
      });
      label.textContent = '2,000 nodes - 3D Watts-Strogatz';
      window.__heliosLandingPreview = helios;
    } catch (error) {
      console.warn('Helios landing preview failed to start', error);
      label.textContent = 'Preview unavailable';
    }
  </script>
</body>
</html>
""", encoding="utf-8")
    (site_dir / "CNAME").write_text("heliosweb.io\n", encoding="utf-8")


def write_app_route() -> None:
    app_dir = DOCS_SITE / "site" / "app"
    app_dir.mkdir(parents=True, exist_ok=True)
    source_dir = resolve_main_app_dir()
    (app_dir / "index.html").write_text("""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Helios App</title>
  <link rel="icon" href="/docs/assets/helios-mark.svg" type="image/svg+xml">
  <style>
    html, body, #app { margin: 0; width: 100%; height: 100%; overflow: hidden; background: #f7f9fb; }
    @media (prefers-color-scheme: dark) {
      html, body, #app { background: #070a0f; }
    }
  </style>
</head>
<body>
  <div id="app"></div>
  <script type="module" src="./main.js"></script>
</body>
</html>
""", encoding="utf-8")
    app_source = rewrite_main_app_source((source_dir / "main.js").read_text(encoding="utf-8"))
    (app_dir / "main.js").write_text(app_source, encoding="utf-8")


def main() -> int:
    stage_example_assets()
    run([sys.executable, "scripts/generate_api_reference.py"])
    run([sys.executable, "-m", "mkdocs", "build", "-f", "mkdocs.yml", "--strict"])
    write_root_homepage()
    write_app_route()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
