#!/usr/bin/env python3
from __future__ import annotations

import re
import shutil
import subprocess
import sys
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


def resolve_dist(env_name: str, package_name: str, sibling_name: str) -> Path:
    candidates: list[Path] = []
    explicit = os.environ.get(env_name)
    if explicit:
        candidates.append(Path(explicit).expanduser().resolve())
    candidates.append(DOCS_SITE / "node_modules" / package_name / "dist")
    candidates.append(ROOT / sibling_name / "dist")
    for candidate in candidates:
        if candidate.exists():
            return candidate
    searched = "\n".join(f"- {candidate}" for candidate in candidates)
    raise FileNotFoundError(
        f"Could not locate {package_name} dist assets. Searched:\n{searched}\n"
        f"Install {package_name}@0.10.0 or set {env_name}."
    )


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
    network_dist = resolve_dist("HELIOS_NETWORK_DIST", "helios-network", "helios-network-v2")
    web_dist = resolve_dist("HELIOS_WEB_DIST", "helios-web", "helios-web-next")

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


def write_root_homepage() -> None:
    site_dir = DOCS_SITE / "site"
    site_dir.mkdir(parents=True, exist_ok=True)
    (site_dir / "index.html").write_text("""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Helios</title>
  <style>
    :root { color-scheme: light dark; font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    body { margin: 0; min-height: 100vh; display: grid; place-items: center; background: #f7f9fb; color: #17212b; }
    main { width: min(920px, calc(100vw - 40px)); }
    img { width: min(360px, 72vw); height: auto; display: block; margin-bottom: 34px; }
    h1 { font-size: clamp(2.3rem, 8vw, 5.8rem); line-height: 0.94; margin: 0 0 24px; letter-spacing: 0; }
    p { max-width: 680px; font-size: 1.15rem; line-height: 1.65; margin: 0 0 32px; color: #435160; }
    .actions { display: flex; flex-wrap: wrap; gap: 12px; }
    a { border: 1px solid #17212b; color: #17212b; text-decoration: none; padding: 12px 16px; border-radius: 6px; font-weight: 650; }
    a.primary { background: #17212b; color: white; }
    @media (prefers-color-scheme: dark) {
      body { background: #0d1117; color: #eef4fa; }
      p { color: #b6c2cf; }
      a { border-color: #eef4fa; color: #eef4fa; }
      a.primary { background: #eef4fa; color: #0d1117; }
    }
  </style>
</head>
<body>
  <main>
    <img src="/docs/assets/helios-web-logo.svg" alt="Helios">
    <h1>Interactive network visualization.</h1>
    <p>Helios pairs a WebGPU/WebGL renderer with a WebAssembly graph store, plus CLI, notebook, and desktop hosts for real workflows.</p>
    <div class="actions">
      <a class="primary" href="/app/">Launch app</a>
      <a href="/docs/">Read docs</a>
      <a href="https://github.com/filipinascimento/heliosweb.io">Source</a>
    </div>
  </main>
</body>
</html>
""", encoding="utf-8")
    (site_dir / "CNAME").write_text("heliosweb.io\n", encoding="utf-8")


def write_app_route() -> None:
    app_dir = DOCS_SITE / "site" / "app"
    app_dir.mkdir(parents=True, exist_ok=True)
    (app_dir / "index.html").write_text("""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Helios App</title>
  <style>
    html, body, #app { margin: 0; width: 100%; height: 100%; overflow: hidden; background: #070a0f; }
    #status { position: fixed; left: 16px; bottom: 14px; z-index: 2; color: white; font: 13px/1.4 ui-sans-serif, system-ui, sans-serif; background: rgba(7, 10, 15, 0.72); padding: 8px 10px; border-radius: 6px; }
  </style>
</head>
<body>
  <div id="app"></div>
  <div id="status">Loading 10k Watts-Strogatz network...</div>
  <script type="module" src="./main.js"></script>
</body>
</html>
""", encoding="utf-8")
    (app_dir / "main.js").write_text("""import HeliosNetwork from '../docs/assets/vendor/helios/helios-network.js';
import { Helios } from '../docs/assets/vendor/helios/helios-web.es.js';

const params = new URLSearchParams(window.location.search);
const nodeCount = Math.max(1, Math.floor(Number(params.get('nodes') || params.get('nodeCount') || 10000)));
const dataset = String(params.get('dataset') || 'small-world').toLowerCase();
const status = document.querySelector('#status');

async function generateGrid3D(count) {
  const side = Math.max(2, Math.round(Math.cbrt(count)));
  const nodeCount = Math.min(count, side ** 3);
  const network = await HeliosNetwork.create({ directed: false, initialNodes: nodeCount, initialEdges: nodeCount * 3 });
  const edges = new Uint32Array(nodeCount * 6);
  let offset = 0;
  const indexAt = (x, y, z) => z * side * side + y * side + x;
  const push = (from, x, y, z) => {
    if (x >= side || y >= side || z >= side) return;
    const to = indexAt(x, y, z);
    if (to >= nodeCount) return;
    edges[offset++] = from;
    edges[offset++] = to;
  };
  for (let z = 0; z < side; z += 1) {
    for (let y = 0; y < side; y += 1) {
      for (let x = 0; x < side; x += 1) {
        const from = indexAt(x, y, z);
        if (from >= nodeCount) break;
        push(from, x + 1, y, z);
        push(from, x, y + 1, z);
        push(from, x, y, z + 1);
      }
    }
  }
  if (offset > 0) network.addEdges(edges.subarray(0, offset));
  return network;
}

function chooseNetwork() {
  if (dataset === 'grid' || dataset === 'grid2d') {
    const side = Math.max(2, Math.round(Math.sqrt(nodeCount)));
    return HeliosNetwork.generateLattice2D({ rows: side, columns: side, periodic: true });
  }
  if (dataset === 'grid3d') {
    return generateGrid3D(nodeCount);
  }
  return HeliosNetwork.generateWattsStrogatz({
    nodeCount,
    neighborLevel: Number(params.get('neighborLevel') || 8),
    rewiringProbability: Number(params.get('rewiringProbability') || 0.08),
    directed: false,
    seed: Number(params.get('seed') || 13),
  });
}

const network = await chooseNetwork();
const helios = new Helios(network, {
  container: document.querySelector('#app'),
  renderer: params.get('renderer') || undefined,
});

await helios.ready;
helios.frameNetwork({ animate: false });
status.textContent = `${network.nodeCount?.() ?? nodeCount} nodes - ${dataset === 'small-world' ? 'Watts-Strogatz' : dataset}`;
setTimeout(() => status.remove(), 3200);
window.helios = helios;
window.network = network;
""", encoding="utf-8")


def main() -> int:
    stage_example_assets()
    run([sys.executable, "scripts/generate_api_reference.py"])
    run([sys.executable, "-m", "mkdocs", "build", "-f", "mkdocs.yml", "--strict"])
    write_root_homepage()
    write_app_route()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
