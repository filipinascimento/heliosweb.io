# Layouts And Filters

The default layout is enough for many graphs, so layout configuration should not
appear in every snippet. Use the layout behavior when an application needs to
start, stop, switch, or parameterize layout execution explicitly.

Filtering is a view-level operation unless you ask for a filter to also affect
layout. That means the original graph can remain available while the rendered
view narrows to nodes and edges that match the current rules.

## Controlling Layout Execution

This example builds a larger graph, creates a Helios view with default options,
then starts and stops the force layout through `helios.behavior.layout`.

```javascript sidecode title="Control The Layout Behavior" console=true height=460
//@BODY helios_web_layouts
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(28);

network.addEdges(Array.from(nodes).flatMap((node, index) => [
  [node, nodes[(index + 1) % nodes.length]],
  index % 2 === 0 ? [node, nodes[(index + 7) % nodes.length]] : null,
]).filter(Boolean));

const helios = new Helios(network, {
  container,
  mode: '2d',
});

await helios.ready;
helios.behavior.layout.update({ layoutType: 'gpu-force', running: true });
setTimeout(() => helios.behavior.layout.stop(), 1600);
```

## Filtering By Attributes

This example creates numeric node and edge attributes with chainable writers,
then creates render filters from those attributes. The graph object is not
rebuilt; the filters behavior updates the rendered view.

```javascript sidecode title="Filter By Attribute Values" console=true height=470
//@BODY helios_web_filters
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(24);

network.addEdges(Array.from(nodes).flatMap((node, index) => [
  [node, nodes[(index + 1) % nodes.length]],
  [node, nodes[(index + 6) % nodes.length]],
]));

network
  .nodeAttribute('score', (_current, _id, ordinal) => (ordinal % 9) / 8)
  .edgeAttribute('strength', (_current, _id, ordinal) => (ordinal % 7) / 6);

const helios = new Helios(network, {
  container,
  mode: '2d',
});

await helios.ready;
helios.behavior.filters.replaceRules({
  scope: 'render',
  nodeRules: [{ id: 'visible-score', scope: 'node', type: 'numeric', attribute: 'score', min: 0.35 }],
  edgeRules: [{ id: 'strong-edges', scope: 'edge', type: 'numeric', attribute: 'strength', min: 0.25 }],
});
helios.frameNetwork({ animate: false });
```

The same filter behavior is the right place for categorical filters, string
filters, query-backed filters, and filters that should rebuild the active layout
topology.
