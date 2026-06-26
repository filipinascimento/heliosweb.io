# Installation And Bundling

This page collects the practical setup patterns for Helios applications. The
short version is: use ESM, keep the Helios Network and Helios Web packages on
matching versions, and prefer Vite unless your application already has a
bundler.

Use the current 0.10 package train for `helios-network` and `helios-web`. The hosted
docs also stage browser bundles under
`https://heliosweb.io/docs/assets/vendor/helios/` for direct ESM examples.

## Browser With Vite

```bash
npm create vite@latest helios-app -- --template vanilla
cd helios-app
npm install helios-network helios-web
npm run dev
```

`package.json` should be ESM:

```json
{
  "type": "module",
  "scripts": {
    "dev": "vite",
    "build": "vite build",
    "preview": "vite preview"
  },
  "dependencies": {
    "helios-network": "^0.10.2",
    "helios-web": "^0.10.3"
  },
  "devDependencies": {
    "vite": "^5"
  }
}
```

`src/main.js`:

```js
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });
network.addNodes(2);
network.addEdges([[0, 1]]);

const helios = new Helios(network, {
  container: document.querySelector("#app"),
});

await helios.ready;
helios.frameNetwork({ animate: false });
```

## Node.js Data Scripts

Use Helios Network directly when there is no renderer:

```js
import HeliosNetwork from "helios-network";

const network = await HeliosNetwork.create({ directed: true });
network.addNodes(10);
await network.saveZXNet({ path: "graph.zxnet" });
```

Node.js scripts still need ESM:

```json
{ "type": "module" }
```

## CDN Or Static ESM

A static page can import prebuilt ESM bundles:

```html
<div id="app"></div>
<script type="module">
  import HeliosNetwork from "https://heliosweb.io/docs/assets/vendor/helios/helios-network.js";
  import { Helios } from "https://heliosweb.io/docs/assets/vendor/helios/helios-web.es.js";

  const network = await HeliosNetwork.create();
  network.addNodes(2);
  network.addEdges([[0, 1]]);
  new Helios(network, { container: document.querySelector("#app") });
</script>
```

For local docs and demos inside this checkout, `scripts/build_docs.py` stages
bundles under `docs/assets/vendor/helios/`. That keeps examples runnable without
depending on a public CDN while package names are finalized.

## Local Checkout Development

From this repository:

```bash
cd helios-network-v2
npm install
npm run build:wasm
npm run build
npm test
```

```bash
cd ../helios-web
npm install
npm run build
npm test
```

Then rebuild heliosweb.io:

```bash
cd ../heliosweb.io
python3 scripts/build_docs.py
```

## Common Problems

- **Blank canvas**: make sure the container has a width and height.
- **Duplicate network package**: ensure the visual package and app code import
  the same Helios Network version.
- **WASM asset 404**: let the bundler copy package assets, or use the staged
  heliosweb.io vendor bundles.
- **WebGPU unavailable**: Helios falls back to WebGL2. Use WebGPU-specific tests
  only on a browser/profile that exposes WebGPU.
