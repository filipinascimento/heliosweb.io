# Selectors And Serialization

Selectors make graph queries explicit. They can be built from query strings,
lists of ids, or neighborhood operations, and they are useful for analysis,
filtering, exporting subsets, and handoff into visualization workflows.

Serialization preserves the graph and its attributes so data workflows can move
between browser sessions, Node scripts, Python, native code, and Helios Web.
For the complete format matrix and cross-language examples, see the
[data formats guide](../../guides/data-formats/index.md).

## Select Nodes And Edges With Queries

This example writes a numeric `score` attribute with the chainable writer API,
then selects nodes and edges with query expressions. Query expressions can refer
to node attributes, edge attributes, and endpoint attributes.

```javascript sidecode title="Select Nodes And Edges With Queries" console=true render=false height=440
//@BODY helios_network_selectors
import HeliosNetwork from "helios-network";

const network = await HeliosNetwork.create({ directed: true });
const nodes = network.addNodes(5);

network.addEdges([
  [nodes[0], nodes[1]],
  [nodes[1], nodes[2]],
  [nodes[2], nodes[3]],
  [nodes[3], nodes[4]],
  [nodes[0], nodes[4]],
]);

network.nodeAttribute('score', [0.1, 0.4, 0.8, 0.7, 0.2]);

const highScoreNodes = network.selectNodes('score >= 0.5');
const outgoingFromHighScore = network.selectEdges('$src.score >= 0.5');
const seed = network.createNodeSelector([nodes[1]]);
const neighbors = seed.neighbors({ mode: 'out', includeEdges: true });

console.log('score >= 0.5', Array.from(highScoreNodes));
console.log('$src.score >= 0.5', Array.from(outgoingFromHighScore));
console.log('neighbors from node 1', {
  nodes: Array.from(neighbors.nodes),
  edges: Array.from(neighbors.edges),
});
seed.dispose();
```

## Round Trip A Network Snapshot

ZXNet is the compact Helios network format. This example saves a graph to a
byte array, restores it, and then exports Node-Link JSON for interoperability.

```javascript sidecode title="Round Trip A Network Snapshot" console=true render=false height=420
//@BODY helios_network_serialization
import HeliosNetwork from "helios-network";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(6);

network.addEdges([
  [nodes[0], nodes[1]], [nodes[1], nodes[2]], [nodes[2], nodes[3]],
  [nodes[3], nodes[4]], [nodes[4], nodes[5]], [nodes[5], nodes[0]],
]);
network.nodeAttribute('label', (_current, _id, ordinal) => `node-${ordinal}`);

const bytes = await network.saveZXNet({ format: 'uint8array', compressionLevel: 3 });
const restored = await HeliosNetwork.fromZXNet(bytes);
const nodeLink = await restored.saveNodeLinkJSON({ format: 'string' });
const parsed = JSON.parse(nodeLink);

console.log(`zxnet bytes: ${bytes.byteLength}`);
console.log({
  restoredNodes: restored.nodeCount,
  restoredEdges: restored.edgeCount,
  nodeLinkNodes: parsed.nodes.length,
  nodeLinkLinks: parsed.links.length,
});
```

## Handoff Into Helios Web

The Network and Web packages meet at the `Helios` constructor. A Network example
becomes visual when the graph object is passed to Helios Web.

```javascript
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.fromZXNet(file);
const helios = new Helios(network, {
  container: document.querySelector('#app'),
  mode: '2d',
});
await helios.ready;
```

See [Helios Web basic rendering](../helios-web/basic.md) for the rendered
version of this workflow.
