# Interaction And Labels

Selection, hover, and labels are default behaviors. Application code can call
the behavior namespace after `await helios.ready`, whether the user action came
from the canvas, a side panel, a search result, a keyboard shortcut, or a custom
behavior.

The example below writes a `label` attribute and configures labels to show only
for selected nodes. This keeps the visual output readable while demonstrating
how behavior options tune default behavior instead of enabling it from scratch.

```javascript sidecode title="Select Nodes And Show Labels" console=true height=460
//@BODY helios_web_selection_labels
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(12);

network.addEdges(Array.from(nodes, (node, index) => [node, nodes[(index + 1) % nodes.length]]));
network.nodeAttribute('label', (_current, _id, ordinal) => `node ${ordinal}`);

const helios = new Helios(network, {
  container,
  mode: '2d',
  behaviors: {
    labels: { enabled: true, source: 'label', selectionMode: 'selected-only' },
  },
});

await helios.ready;
helios.behavior.selection.selectNodes(Array.from(nodes).slice(0, 4), { mode: 'replace' });
helios.frameNetwork({ animate: false });
```

The important pattern is that selection state lives in the behavior layer. That
state can be serialized, restored, used by labels, reflected in UI controls, or
modified by custom application code without bypassing the visual system.
