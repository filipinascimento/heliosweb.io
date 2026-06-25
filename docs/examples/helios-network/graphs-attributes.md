# Graphs And Attributes

Helios Network is a WebAssembly-backed graph store. The graph topology lives in
the WASM core, while the JavaScript wrapper provides ergonomic methods for
building graphs, attaching attributes, querying data, and serializing snapshots.

The examples on this page use the chainable attribute writer API. These helpers
are the recommended default for application code because they define missing
attributes, infer practical schemas, write values, and bump versions in one
place.

## Create A WASM-Backed Graph

This first data example creates a directed graph, adds nodes and edges, and logs
the allocated ids. Node and edge ids are stable integer identifiers; they are
not necessarily the same thing as ordinal position in an active subset.

```javascript sidecode title="Create A WASM-Backed Graph" console=true render=false height=360
//@BODY helios_network_js_creation
import HeliosNetwork from "helios-network";

const network = await HeliosNetwork.create({ directed: true, initialEdges: 5 });

const nodes = network.addNodes(5);
const edges = network.addEdges([
  [nodes[0], nodes[1]],
  [nodes[1], nodes[2]],
  [nodes[2], nodes[3]],
  [nodes[3], nodes[4]],
  [nodes[0], nodes[4]],
]);

console.log({
  directed: network.directed,
  nodes: network.nodeCount,
  edges: network.edgeCount,
  nodeIds: Array.from(nodes),
  edgeIds: Array.from(edges),
});
```

## Write Attributes With Chainable Helpers

The chainable writers accept scalars, arrays, typed arrays, callbacks, and
multi-attribute records. By default, array-like values are indexed by active
ordinal, which is the right behavior for most imported row data. Pass
`{ indexBy: 'id' }` when your data array is keyed by graph id.

```javascript sidecode title="Use Chainable Attributes" console=true render=false height=430
//@BODY helios_network_attributes
import HeliosNetwork from "helios-network";

const network = await HeliosNetwork.create({ directed: true });
const nodes = network.addNodes(4);
const edges = network.addEdges([
  [nodes[0], nodes[1]],
  [nodes[1], nodes[2]],
  [nodes[2], nodes[3]],
]);

network
  .nodeAttribute('score', [0.1, 0.4, 0.8, 0.7])
  .nodeAttribute('label', (_current, _id, ordinal) => `node-${ordinal}`)
  .edgeAttribute('weight', (_current, _id, ordinal) => 0.25 + ordinal * 0.25)
  .networkAttribute('title', 'Attribute example');

console.log({
  label: network.getNodeStringAttribute('label', nodes[2]),
  scoreInfo: network.getNodeAttributeInfo('score'),
  weightInfo: network.getEdgeAttributeInfo('weight'),
  title: network.getNetworkStringAttribute('title'),
});
```

## Write Multiple Attributes Together

Use `nodeAttributes(...)` and `edgeAttributes(...)` when several attributes come
from the same row. The callback receives the current value record, entity id,
active ordinal, and the network instance. It can return an array aligned with
the requested names or an object keyed by attribute name.

```javascript sidecode title="Write Multiple Attributes" console=true render=false height=420
//@BODY helios_network_multi_attributes
import HeliosNetwork from "helios-network";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(6);
const edges = network.addEdges([
  [nodes[0], nodes[1]], [nodes[1], nodes[2]], [nodes[2], nodes[3]],
  [nodes[3], nodes[4]], [nodes[4], nodes[5]], [nodes[5], nodes[0]],
]);

network
  .nodeAttributes(['x', 'y'], (_current, _id, ordinal) => [
    Math.cos(ordinal / nodes.length * Math.PI * 2),
    Math.sin(ordinal / nodes.length * Math.PI * 2),
  ])
  .edgeAttributes(['capacity', 'visible'], (_current, _id, ordinal) => ({
    capacity: 10 + ordinal,
    visible: true,
  }));

console.log({
  nodeAttributes: network.getNodeAttributeNames(),
  edgeAttributes: network.getEdgeAttributeNames(),
  xInfo: network.getNodeAttributeInfo('x'),
  capacityInfo: network.getEdgeAttributeInfo('capacity'),
  edgeCount: edges.length,
});
```

When writing a graph for visualization, these attributes can be used directly by
Helios Web mappers, filters, labels, and selectors.
