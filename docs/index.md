<section class="helios-hero">
  <div class="helios-hero-copy">
    <img class="helios-home-logo" src="assets/helios-logo.svg" alt="Helios Web">
    <p class="helios-eyebrow">Open-source graph visualization</p>
    <h1>Interactive network visualization with a WebAssembly graph store.</h1>
    <p>
      Helios pairs a visual WebGPU/WebGL renderer with a data-first graph core.
      Use Helios Web when you need an interactive graph view. Use Helios Network
      when you need graph creation, attributes, selection, and serialization
      across JavaScript/WASM, Python, and native C. Use the CLI, Widget, and
      Desktop hosts when you need automation, notebooks, or native documents.
    </p>
    <div class="helios-actions">
      <a class="helios-action helios-action-primary" href="https://heliosweb.io/app/">Launch online app</a>
      <a class="helios-action" href="getting-started/index.md">Start docs</a>
      <a class="helios-action" href="examples/index.md">Browse examples</a>
      <a class="helios-action" href="https://github.com/filipinascimento/helios-web">Source</a>
    </div>
  </div>
  <div class="helios-hero-signal" aria-hidden="true">
    <span>WebGPU/WebGL visual layer</span>
    <span>WASM graph data layer</span>
    <span>CLI, Widget, and Desktop hosts</span>
    <span>Generated API reference</span>
  </div>
</section>

<section class="helios-panel-grid">
  <article>
    <h2>Helios Web</h2>
    <p>
      The browser visualization package: rendering, camera controls, behaviors,
      mappers, filters, labels, legends, layouts, persistence, and figure export.
    </p>
    <p><a href="examples/helios-web/index.md">Open visual examples</a></p>
  </article>
  <article>
    <h2>Helios Network</h2>
    <p>
      The graph data package: a native C core compiled to WebAssembly, with
      JavaScript, Python, and C surfaces for attributes, selectors, queries,
      and import/export.
    </p>
    <p><a href="examples/helios-network/index.md">Open API/data examples</a></p>
  </article>
  <article>
    <h2>Source-first API docs</h2>
    <p>
      API pages are regenerated from public exports plus JSDoc, Python
      docstrings, and Doxygen comments. Declaration files are downstream
      compatibility artifacts, not the place where API documentation is authored.
    </p>
    <p><a href="api/index.md">Open API reference</a></p>
  </article>
  <article>
    <h2>Apps and integrations</h2>
    <p>
      Helios CLI, Helios Widget, and Helios Desktop reuse the same Web and
      Network runtime with host-specific persistence and workflow surfaces.
    </p>
    <p><a href="apps/index.md">Open app docs</a></p>
  </article>
</section>

## How The Pieces Fit

Helios is not a single monolithic viewer. The graph store, renderer, behaviors,
UI panels, persistence, and host applications are separate layers that can be
used together or independently.

1. **Graph data** lives in Helios Network. It owns topology, typed attributes,
   selectors, queries, measurements, and import/export.
2. **Visual state** lives in Helios Web. Mappers translate attributes into
   colors, sizes, opacity, widths, outlines, labels, legends, and density
   overlays.
3. **Interaction behavior** is modular. Selection, hover, labels, legends,
   filters, layouts, export, interface state, and persistence are behaviors that
   can be configured or replaced.
4. **Host state** belongs to the app. Browser storage, CLI sessions, notebook
   widget state, and desktop documents reuse the same runtime but persist data
   differently.

That split is why the documentation has both visual examples and data/API
examples. Start with the visual examples when you are building an interface;
start with the data/API examples when you are converting files, writing Python,
or manipulating graphs programmatically.

## Install

Use the 0.10.0 release packages for browser and data workflows.

```bash
npm install helios-network helios-web
```

For data-only JavaScript:

```bash
npm install helios-network
```

For Python:

```bash
pip install helios-network
```

See [Getting Started](getting-started/index.md) and
[Installation And Bundling](guides/installation.md) for Vite, package.json,
CDN-style imports, and local checkout setup.

## First Choices

| Goal | Start With |
| --- | --- |
| Render a graph in a browser | [First visual graph](getting-started/interactive.md) |
| Build visual controls, mappers, filters, labels, or legends | [Visual examples](examples/helios-web/index.md) |
| Load/save graph files or manipulate attributes | [Data/API examples](examples/helios-network/index.md) |
| Choose a file format | [Data formats](guides/data-formats/index.md) |
| Understand sessions, autosave, and portable visualization state | [Persistence guide](guides/persistence.md) |
| Inspect every public class and method | [API reference](api/index.md) |

## Minimal App Shape

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

## Documentation Status

This preview build is source-first: API pages are generated from public exports
and source annotations, while guides and examples are written around runnable
code. When a guide says a behavior, format, option, or import path is supported,
it should either link to the generated API reference or show a minimal working
example.

The rendered examples import the same staged bundles that power the hosted docs and app routes.
