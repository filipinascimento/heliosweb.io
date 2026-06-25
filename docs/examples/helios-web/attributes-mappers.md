# Attributes, Mappers, And Legends

Visual encodings begin with graph attributes. The recommended everyday API is
the chainable attribute writer API from `helios-network`: use
`nodeAttribute(...)`, `edgeAttribute(...)`, `nodeAttributes(...)`, and
`edgeAttributes(...)` for normal application code. These helpers define missing
attributes, write values, and bump attribute versions while preserving the
WASM-buffer safety rules internally.

The raw `withBufferAccess(...)` API still exists and is important for very large
bulk writes or advanced integrations, but it is not the clearest API for most
examples. Use the chainable writers first; drop down to buffer access only when
you need tight control over typed-array views and write loops.

## Loading Data With Attributes

This example builds a graph from ordinary application rows. The label attribute
is written with `nodeAttribute(...)`, and the labels behavior is configured to
read from that attribute. The graph rows could come from JSON, CSV parsing, a
database query, or any other loading step.

```javascript sidecode title="Load Data Into A Network" console=true height=440
//@BODY helios_web_loading_building
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const nodeRows = ['Ada', 'Grace', 'Katherine', 'Mary', 'Radia', 'Evelyn'];
const edgeRows = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 3]];

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(nodeRows.length);

network.addEdges(edgeRows.map(([source, target]) => [nodes[source], nodes[target]]));
network.nodeAttribute('label', (_current, _id, ordinal) => nodeRows[ordinal]);

const helios = new Helios(network, {
  container,
  mode: '2d',
  behaviors: {
    labels: { enabled: true, source: 'label', selectionMode: 'ranked' },
  },
});

await helios.ready;
helios.frameNetwork({ animate: false });
```

## Mapping Numeric Attributes

This example maps data attributes onto visual channels. The `score` node
attribute drives node color and size, while the `strength` edge attribute drives
edge width. Mappers and legends are built-in behaviors, so the code uses
`helios.behavior.mappers` after the instance is ready rather than manipulating
renderer internals.

```javascript sidecode title="Map Attributes To Visual Channels" console=true height=470
//@BODY helios_web_mappers_legends
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(18);
const edges = network.addEdges(Array.from(nodes).flatMap((node, index) => [
  [node, nodes[(index + 1) % nodes.length]],
  [node, nodes[(index + 5) % nodes.length]],
]));

network
  .nodeAttribute('score', (_current, _id, ordinal) => ordinal / (nodes.length - 1))
  .edgeAttribute('strength', (_current, _id, ordinal) => 0.25 + (ordinal % 8) / 10);

const helios = new Helios(network, {
  container,
  mode: '2d',
  behaviors: {
    legends: { showNodeColor: true, showNodeSize: true, showEdgeWidth: true },
  },
});

await helios.ready;
helios.behavior.mappers.setChannelConfig('node', 'color', {
  type: 'colormap',
  attributes: 'score',
  colormap: 'interpolateViridis',
  domain: [0, 1],
});
helios.behavior.mappers.setChannelConfig('node', 'size', {
  type: 'linear',
  attributes: 'score',
  domain: [0, 1],
  range: [4, 12],
});
helios.behavior.mappers.setChannelConfig('edge', 'width', {
  type: 'linear',
  attributes: 'strength',
  domain: [0, 1],
  range: [0.8, 2.8],
});
helios.frameNetwork({ animate: false });
```

The mapper examples deliberately use named graph attributes instead of hard-coded
visual arrays. That keeps the graph portable: the same attributes can also be
used by selectors, filters, legends, exports, and saved sessions.
