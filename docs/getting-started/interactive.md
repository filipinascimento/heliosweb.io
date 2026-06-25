# First Visual Graph

This is the shortest path from graph data to a rendered Helios view. It creates a
small WASM-backed graph, mounts Helios Web into the example render area, and lets
the default renderer and GPU-force layout behavior produce the first view.

```javascript sidecode title="Render A Small Graph" console=true height=420
//@BODY helios_web_first_visual_graph
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });

const nodes = network.addNodes(6);
network.addEdges([
  [nodes[0], nodes[1]],
  [nodes[1], nodes[2]],
  [nodes[2], nodes[3]],
  [nodes[3], nodes[4]],
  [nodes[4], nodes[5]],
  [nodes[5], nodes[0]],
  [nodes[0], nodes[3]],
]);

const helios = new Helios(network, {
  container,
  mode: '2d',
});

await helios.ready;
await new Promise((resolve) => setTimeout(resolve, 900));
helios.frameNetwork({ animate: false });
```

The full [Helios Web visual examples](../examples/helios-web/index.md) expand
from this baseline into labels, mappers, legends, layouts, filters,
persistence, exporter output, touch behavior, and custom behaviors.
