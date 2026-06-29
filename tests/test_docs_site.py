from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml


DOCS_SITE = Path(__file__).resolve().parents[1]
ROOT = DOCS_SITE.parent


def run(command: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(command, cwd=DOCS_SITE, text=True, capture_output=True, check=True)


def test_mkdocs_material_and_sidecode_are_configured():
    config = yaml.safe_load((DOCS_SITE / "mkdocs.yml").read_text(encoding="utf-8"))
    assert config["theme"]["name"] == "material"
    assert config["theme"]["logo"] == "assets/helios-logo.svg"
    assert config["theme"]["favicon"] == "assets/helios-mark.svg"
    mark = (DOCS_SITE / "docs/assets/helios-mark.svg").read_text(encoding="utf-8")
    assert "viewBox=\"0 0 221.462 221.462\"" in mark
    assert "<rect width=\"64\" height=\"64\"" not in mark
    sidecode_config = next(item["sidecode"] for item in config["plugins"] if isinstance(item, dict) and "sidecode" in item)
    assert sidecode_config["import_map"]["helios-web"].endswith("helios-web.es.js")
    assert config["site_url"].endswith("/docs/")
    assert "assets/stylesheets/helios.css" in config["extra_css"]
    assert "assets/javascripts/api-search.js" in config["extra_javascript"]
    assert config["extra"]["homepage"] == "https://heliosweb.io/"
    assert config["extra"]["version"]["default"] == "0.10.9"
    assert any("Examples" in item for item in config["nav"])
    assert any("Apps And Integrations" in item for item in config["nav"])
    requirements = (DOCS_SITE / "requirements.txt").read_text(encoding="utf-8")
    assert "mkdocs-sidecode==0.1.7" in requirements
    assert "./vendor/mkdocs-sidecode" not in requirements
    build_script = (DOCS_SITE / "scripts/build_docs.py").read_text(encoding="utf-8")
    assert "vendor\" / \"mkdocs-sidecode\"" not in build_script
    assert "PYTHONPATH" not in build_script


def test_api_generator_emits_public_reference_pages():
    run([sys.executable, "scripts/generate_api_reference.py"])
    expected = [
        DOCS_SITE / "docs/api/helios-web/index.md",
        DOCS_SITE / "docs/api/helios-network-js-wasm/index.md",
        DOCS_SITE / "docs/api/helios-network-python/index.md",
        DOCS_SITE / "docs/api/helios-network-native-c/index.md",
    ]
    for path in expected:
        assert path.exists(), path
        text = path.read_text(encoding="utf-8")
        assert "helios-api-directory" in text
        assert "helios-network-v2/" not in text
        assert "helios-web-next/" not in text
    reference = json.loads((DOCS_SITE / "docs/api/reference.json").read_text(encoding="utf-8"))
    assert reference["schemaVersion"] == "1.0.0"
    assert "helios-web" in reference["packages"]
    assert any(symbol["name"] == "Helios" for symbol in reference["packages"]["helios-web"]["symbols"])
    assert (DOCS_SITE / "docs/api/helios-web/Helios.md").exists()
    assert (DOCS_SITE / "docs/api/helios-web/section-constants.md").exists()
    assert (DOCS_SITE / "docs/api/helios-web/section-behaviors.md").exists()
    assert (DOCS_SITE / "docs/api/helios-web/section-layouts.md").exists()
    assert (DOCS_SITE / "docs/api/helios-web/section-persistence.md").exists()
    assert (DOCS_SITE / "docs/api/helios-web/HeliosStorageManager.md").exists()
    assert (DOCS_SITE / "docs/api/helios-web/HeliosStateManager.md").exists()
    assert (DOCS_SITE / "docs/api/helios-web/SessionStore.md").exists()
    assert (DOCS_SITE / "docs/api/helios-web/createHeliosStorageManager.md").exists()
    assert (DOCS_SITE / "docs/api/helios-network-js-wasm/HeliosNetwork.md").exists()
    assert (DOCS_SITE / "docs/api/helios-network-js-wasm/section-methods.md").exists()
    assert (DOCS_SITE / "docs/api/helios-network-python/Network.md").exists()
    assert (DOCS_SITE / "docs/api/helios-network-native-c/section-attributes.md").exists()
    assert (DOCS_SITE / "docs/api/helios-network-native-c/CXNewNetwork.md").exists()
    assert "Helios Web is the browser visualization layer" in (DOCS_SITE / "docs/api/helios-web/index.md").read_text(encoding="utf-8")
    network_js_text = (DOCS_SITE / "docs/api/helios-network-js-wasm/index.md").read_text(encoding="utf-8")
    assert "HeliosNetwork" in network_js_text
    assert "nodeAttribute" in network_js_text
    assert "withBufferAccess" in network_js_text
    assert "direct buffer methods remain documented as the low-level performance path" in network_js_text
    assert "Network" in (DOCS_SITE / "docs/api/helios-network-python/index.md").read_text(encoding="utf-8")
    assert "CXNewNetwork" in (DOCS_SITE / "docs/api/helios-network-native-c/index.md").read_text(encoding="utf-8")
    web_text = (DOCS_SITE / "docs/api/helios-web/index.md").read_text(encoding="utf-8")
    assert "helios-logo.svg" in web_text
    assert "Source entry" not in web_text
    assert "src/index.d.ts" not in web_text
    assert "Declaration surface" not in web_text
    helios_web_package_pages = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [
            DOCS_SITE / "docs/api/helios-web/index.md",
            DOCS_SITE / "docs/api/helios-web/section-behaviors.md",
            DOCS_SITE / "docs/api/helios-web/section-mappers.md",
            DOCS_SITE / "docs/api/helios-web/section-filters.md",
            DOCS_SITE / "docs/api/helios-web/section-export.md",
        ]
    )
    assert "<span>method</span>" not in helios_web_package_pages
    assert 'href="clear/"' not in helios_web_package_pages
    assert 'href="replaceRules/"' not in helios_web_package_pages
    assert 'href="setChannelConfig/"' not in helios_web_package_pages
    assert 'href="exportFigureBlob/"' not in helios_web_package_pages
    assert "replaceRules" in (DOCS_SITE / "docs/api/helios-web/FilterBehavior.md").read_text(encoding="utf-8")
    assert "setChannelConfig" in (DOCS_SITE / "docs/api/helios-web/MappersBehavior.md").read_text(encoding="utf-8")
    helios_class_text = (DOCS_SITE / "docs/api/helios-web/Helios.md").read_text(encoding="utf-8")
    assert "exportFigureBlob" in helios_class_text
    assert "## API" not in helios_class_text
    assert "## Filtering And State { #api-filtering-and-state .helios-api-section-title }" in helios_class_text
    assert "## Appearance { #api-appearance .helios-api-section-title }" in helios_class_text
    assert "## Member Overview" not in helios_class_text
    assert "## Method Details" not in helios_class_text
    assert "helios-api-member-card" not in helios_class_text
    assert "helios-api-member-detail" in helios_class_text
    assert "helios-api-methods" not in helios_class_text
    assert "helios-api-params" in helios_class_text
    assert "<th>Attributes</th>" in helios_class_text
    assert "<th>Default</th>" in helios_class_text
    assert 'title="options.container"' in helios_class_text
    assert 'title="options.layout.options"' in helios_class_text
    assert "helios-api-signature" not in helios_class_text.split("## Static Properties", 1)[1]
    assert "edgeWidthScale(value)" in helios_class_text
    assert 'id="method-edgewidthscale"' in helios_class_text
    assert "&rarr;" in helios_class_text
    assert "options.nodeRules" in helios_class_text
    assert "This Helios instance." in helios_class_text
    assert "helios.setGraphFilter" in helios_class_text
    assert "captureSessionThumbnailBlob(options = {})" in helios_class_text
    assert "Capture a small PNG thumbnail from the current interaction canvas." in helios_class_text
    assert "/docs/api/helios-network-js-wasm/HeliosNetwork/" in helios_class_text
    assert "import('helios-network').default" not in helios_class_text
    assert "No generated member-summary fallbacks detected." in web_text
    persistence_section_text = (DOCS_SITE / "docs/api/helios-web/section-persistence.md").read_text(encoding="utf-8")
    assert "HeliosStorageManager" in persistence_section_text
    assert "HeliosStateManager" in persistence_section_text
    assert "SessionStore" in persistence_section_text
    assert "createHeliosStorageManager" in persistence_section_text
    assert "src/index.d.ts" not in (DOCS_SITE / "docs/api/reference.json").read_text(encoding="utf-8")
    behavior_section_text = (DOCS_SITE / "docs/api/helios-web/section-behaviors.md").read_text(encoding="utf-8")
    assert "## Core" in behavior_section_text
    assert "## Behavior Implementations" in behavior_section_text
    assert "## Auxiliary" in behavior_section_text
    api_index_text = (DOCS_SITE / "docs/api/index.md").read_text(encoding="utf-8")
    assert "data-api-search" in api_index_text
    assert (DOCS_SITE / "docs/assets/javascripts/api-search.js").exists()


def test_examples_first_pages_use_real_sidecode_fences():
    pages = [
        DOCS_SITE / "docs/getting-started/interactive.md",
        DOCS_SITE / "docs/examples/helios-web/basic.md",
        DOCS_SITE / "docs/examples/helios-web/attributes-mappers.md",
        DOCS_SITE / "docs/examples/helios-web/interaction-labels.md",
        DOCS_SITE / "docs/examples/helios-web/layouts-filters.md",
        DOCS_SITE / "docs/examples/helios-web/persistence-export.md",
        DOCS_SITE / "docs/examples/helios-web/mobile-custom.md",
        DOCS_SITE / "docs/examples/helios-network/graphs-attributes.md",
        DOCS_SITE / "docs/examples/helios-network/selectors-serialization.md",
        DOCS_SITE / "docs/examples/helios-network/buffer-access.md",
    ]
    for page in pages:
        text = page.read_text(encoding="utf-8")
        assert "```javascript sidecode" in text
        assert "//@BODY" in text
    visual = "\n".join(
        path.read_text(encoding="utf-8")
        for path in [
            DOCS_SITE / "docs/examples/helios-web/basic.md",
            DOCS_SITE / "docs/examples/helios-web/attributes-mappers.md",
            DOCS_SITE / "docs/examples/helios-web/interaction-labels.md",
            DOCS_SITE / "docs/examples/helios-web/layouts-filters.md",
            DOCS_SITE / "docs/examples/helios-web/persistence-export.md",
            DOCS_SITE / "docs/examples/helios-web/mobile-custom.md",
        ]
    )
    for required in [
        "helios_web_basic_rendering",
        "helios_web_loading_building",
        "helios_web_mappers_legends",
        "helios_web_selection_labels",
        "helios_web_layouts",
        "helios_web_filters",
        "helios_web_persistence",
        "helios_web_exporter",
        "helios_web_mobile_touch",
        "helios_web_custom_behavior",
    ]:
        assert required in visual
    basic_text = (DOCS_SITE / "docs/examples/helios-web/basic.md").read_text(encoding="utf-8")
    assert "helios.frameNetwork({ animate: false, paddingRatio: 0.02 });" in basic_text


def test_docs_build_path_succeeds():
    run([sys.executable, "scripts/build_docs.py"])
    index = DOCS_SITE / "site/index.html"
    assert index.exists()
    index_text = index.read_text(encoding="utf-8")
    assert "network-preview" in index_text
    assert "3D Watts-Strogatz preview" in index_text
    assert "/docs/assets/helios-logo.svg" in index_text
    assert "storage: false" in index_text
    assert "session: false" in index_text
    assert "hideCanvasUntilFirstFrame: false" in index_text
    assert "layoutIterations: 0" in index_text
    assert "layoutDurationMs: 0" in index_text
    assert "initialCameraFit: false" in index_text
    assert "warnOnUnsavedSessionChanges: false" in index_text
    assert "nodeCount: 2000" in index_text
    assert "panels: ['data', 'mappers', 'layout', 'camera']" in index_text
    assert "setSettings?.({ linkDistance: 6 }, { reheat: true, reason: 'landing-preview' })" in index_text
    assert "quickControls: false" not in index_text
    assert "renderer: 'webgl'" not in index_text
    assert "type: 'd3force3d'" not in index_text
    assert "helios.scheduler?.requestRender?.()" not in index_text
    assert "Interactive network visualization</h1>" in index_text
    assert "1M+ nodes with real-time GPU-based layout in 2D and 3D" in index_text
    assert "agentic skill integrations" in index_text
    assert "nav { position: relative; z-index: 5;" in index_text
    assert 'href="/docs/getting-started/">Quickstart</a>' in index_text
    assert 'href="/docs/apps/helios-cli/#agentic-skill">CLI & Skills</a>' in index_text
    assert 'aria-disabled="true" tabindex="0" data-tooltip="Coming soon..."' in index_text
    assert ">Desktop</span>" in index_text
    assert "margin-top: -50pt" in index_text
    assert "minmax(420px, 560px)" in index_text
    assert "helios.nodeSizeScale(2)" in index_text
    assert "helios.edgeWidthScale(3)" in index_text
    assert "import { Helios }" in index_text
    assert "setCameraPose?.({ distance: 1000, target: [0, 0, 0] }, { applyState: false })" in index_text
    assert "frameNetwork({ animate: false" not in index_text
    assert "autoFit: true" in index_text
    assert "autoFit: false" not in index_text
    assert "EVENTS.LAYOUT_STOP" not in index_text
    assert "enableAutoFitAfterLayoutStop" not in index_text
    assert "autoFitPaddingRatio: 0.04" in index_text
    assert "animation: true" in index_text
    assert "autoFitIntervalMs:" not in index_text
    assert "autoFitMinIntervalMs:" not in index_text
    assert "autoFitMaxIntervalMs:" not in index_text
    assert "animationDurationMs:" not in index_text
    assert "orbit: true" in index_text
    assert "orbitSpeed: 0.04" in index_text
    assert "orbitAngle: 16" in index_text
    assert "orbitAxis: [0.83, 0.75, 0]" in index_text
    assert (DOCS_SITE / "site/docs/index.html").exists()
    docs_index_text = (DOCS_SITE / "site/docs/index.html").read_text(encoding="utf-8")
    assert 'href="https://heliosweb.io/" title="Helios" class="md-header__button md-logo"' in docs_index_text
    assert (DOCS_SITE / "site/app/index.html").exists()
    app_main = (DOCS_SITE / "site/app/main.js").read_text(encoding="utf-8")
    assert "generateWattsStrogatz" in app_main
    assert "10_000" in app_main
    assert "HeliosUI" in app_main
    assert "rewiringProbability" in app_main
    visual_examples = (DOCS_SITE / "site/docs/examples/helios-web/basic/index.html").read_text(encoding="utf-8")
    assert "mkdocs-sidecode-page-data" in visual_examples
    assert '<template class="mkdocs-sidecode-page-data">' in visual_examples
    payload = visual_examples.split('class="mkdocs-sidecode-page-data">', 1)[1].split("</template>", 1)[0]
    assert json.loads(payload)["examples"]
    sidecode_css = (DOCS_SITE / "site/docs/assets/mkdocs-sidecode/styles.css").read_text(encoding="utf-8")
    assert "--sidecode-console-bg: #ffffff" in sidecode_css
    assert "--sidecode-console-text: #172033" in sidecode_css
    assert "height:var(--sidecode-height)" in sidecode_css
    assert ".sidecode__render>.helios-root" in sidecode_css
    light_block = sidecode_css.split("[data-md-color-scheme=slate]", 1)[0]
    assert "--sidecode-console-bg: #111827" not in light_block
    sidecode_runtime = (DOCS_SITE / "site/docs/assets/mkdocs-sidecode/runtime.js").read_text(encoding="utf-8")
    assert "sidecode:render-visible" in sidecode_runtime
    assert 'new Event("resize")' in sidecode_runtime
    assert (DOCS_SITE / "site/docs/versions.json").exists()
    assert (DOCS_SITE / "site/docs/assets/vendor/helios/helios-web.es.js").exists()
    assert (DOCS_SITE / "site/docs/assets/vendor/helios/helios-network.js").exists()
    api_index = (DOCS_SITE / "site/docs/api/index.html").read_text(encoding="utf-8")
    assert "data-api-search" in api_index
    assert "assets/javascripts/api-search.js" in api_index


def test_visual_validation_script_exists():
    script = DOCS_SITE / "scripts/validate_visual_examples.mjs"
    text = script.read_text(encoding="utf-8")
    assert "exampleIdsByBodyName" in text
    assert "assertNonBlankPng" in text
