# Basic Rendering

This page starts with the smallest complete Helios Web program. It creates a
WASM-backed graph, adds a few nodes and edges, mounts Helios into the render
area provided by the example, and lets Helios choose the renderer and default
GPU-force layout. In browsers with WebGPU support, Helios can use WebGPU;
otherwise it falls back to WebGL2.

Nothing in this first example configures mappers, labels, legends, cleanup,
renderer preferences, or layout parameters. Those features matter, but they are
not needed to understand the basic contract: a `helios-network` graph goes into
the `Helios` constructor, and the `Helios` instance owns the visual view.

```javascript sidecode title="Render A Small Graph" console=true height=420
//@BODY helios_web_basic_rendering
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });

const nodes = network.addNodes(8);
network.addEdges([
  [nodes[0], nodes[1]], [nodes[1], nodes[2]], [nodes[2], nodes[3]],
  [nodes[3], nodes[4]], [nodes[4], nodes[5]], [nodes[5], nodes[6]],
  [nodes[6], nodes[7]], [nodes[7], nodes[0]], [nodes[0], nodes[4]],
]);

const helios = new Helios(network, {
  container,
  mode: '2d',
});

await helios.ready;
await new Promise((resolve) => setTimeout(resolve, 900));
helios.frameNetwork({ animate: false });
```

The default behaviors are already attached. That means later examples can call
`helios.behavior.selection`, `helios.behavior.mappers`,
`helios.behavior.filters`, and the rest of the behavior namespace without
enabling those behaviors one by one.
