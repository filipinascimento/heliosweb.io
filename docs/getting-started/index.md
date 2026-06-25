# Getting Started

Helios is split into two layers:

- **Helios Network** is the graph data layer. It creates graphs, owns typed
  attributes, runs selectors and queries, and reads/writes graph formats.
- **Helios Web** is the visual layer. It renders a Helios Network graph with
  WebGPU or WebGL2 and adds camera controls, layouts, mappers, labels, legends,
  filtering, persistence, export, and UI behavior modules.

Most browser applications use both layers: create or load a `HeliosNetwork`,
then pass it to `new Helios(network, options)`.

## What To Install

Use matching 0.10.0 package versions across the renderer, graph core, and host
tools.

For a visual browser app:

```bash
npm install helios-network helios-web
```

For data-only JavaScript or Node.js scripts:

```bash
npm install helios-network
```

For Python workflows:

```bash
pip install helios-network
```

The hosted docs and app stage the same 0.10.0 bundles under
`https://heliosweb.io/docs/assets/vendor/helios/` for browser-only examples.

## Runtime Requirements

- A modern browser with WebGL2. WebGPU is used when available and falls back to
  WebGL2.
- Node.js 18 or newer for local builds, Vite examples, and docs tooling.
- A bundler that understands ESM and WebAssembly assets. Vite is the easiest
  default.
- Python and native C users can use Helios Network without the browser renderer.

## Minimal Browser App

```js
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(3);
network.addEdges([[nodes[0], nodes[1]], [nodes[1], nodes[2]]]);
network.nodeAttribute("label", ["Alpha", "Beta", "Gamma"]);
network.nodeAttribute("score", [0.2, 0.8, 1.0]);

const helios = new Helios(network, {
  container: document.querySelector("#app"),
  mode: "2d",
});

await helios.ready;
helios.nodeSizeScale(8);
helios.behavior.labels.labels({ enabled: true, source: "label" });
helios.frameNetwork({ animate: false });
```

## Vite Setup

Create a package:

```json
{
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build"
  },
  "dependencies": {
    "helios-network": "<version>",
    "helios-web": "<version>"
  },
  "devDependencies": {
    "vite": "^5"
  },
}
```

Use a normal HTML entry:

```html
<div id="app" style="width: 100vw; height: 100vh"></div>
<script type="module" src="/src/main.js"></script>
```

Then run:

```bash
npm install
npm run dev
```

## Import Styles

Use package imports when a bundler resolves dependencies:

```js
import HeliosNetwork from "helios-network";
import { Helios, HeliosFilter } from "helios-web";
```

Use CDN ESM imports for quick prototypes once published artifacts are available:

```js
import HeliosNetwork from "https://heliosweb.io/docs/assets/vendor/helios/helios-network.js";
import { Helios } from "https://heliosweb.io/docs/assets/vendor/helios/helios-web.es.js";
```

Use local checkout bundles for docs-site and repository examples:

```js
import HeliosNetwork from "/assets/vendor/helios/helios-network.js";
import { Helios } from "/assets/vendor/helios/helios-web.es.js";
```

Avoid mixing two different Helios Network copies in the same page. The Web
layer and your app should import the same graph package instance.

## Which Path Should I Use?

- Use **Helios Web** when users need to see, inspect, select, filter, lay out,
  label, or export a graph.
- Use **Helios Network** when the task is graph construction, format conversion,
  attributes, selectors, measurements, or Python/native integration.
- Use **Helios CLI** when automation or file conversion should run outside the
  browser.
- Use **Helios Widget** for notebooks.
- Use **Helios Desktop** for local document workflows.

Continue with the [first visual graph](interactive.md), then use the
[Visual Examples](../examples/helios-web/index.md) for rendering/UI workflows or the
[Data/API Examples](../examples/helios-network/index.md) for graph-data workflows.
