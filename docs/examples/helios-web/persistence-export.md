# Persistence And Export

Persistence is about saving the visualization state, not just the graph data.
The exported state can include camera position, selected nodes, behavior state,
mapper configuration, and visual settings that make a session recoverable.

Figure export uses the active renderer, camera, mappers, labels, and legends.
That makes export code short: configure the view through public APIs, render the
view, then ask Helios for an image.

## Save And Restore State

This example selects a few nodes, exports visualization state to a string, clears
the selection, and restores the saved state.

```javascript sidecode title="Save And Restore View State" console=true height=460
//@BODY helios_web_persistence
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(18);

network.addEdges(Array.from(nodes, (node, index) => [node, nodes[(index + 3) % nodes.length]]));

const helios = new Helios(network, {
  container,
  mode: '2d',
});

await helios.ready;
helios.behavior.selection.selectNodes(Array.from(nodes).slice(2, 7), { mode: 'replace' });

const savedState = helios.exportVisualizationState({ format: 'string' });
helios.behavior.selection.clearSelection();
await helios.importVisualizationState(savedState);
helios.frameNetwork({ animate: false });
```

## Export A Figure Preview

This example maps node color, renders the graph, and appends a generated PNG
preview below the live canvas. In a production app, the same export call can be
attached to a download button, report builder, or publication workflow.

```javascript sidecode title="Export A Figure Preview" console=true height=500
//@BODY helios_web_exporter
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(20);

network.addEdges(Array.from(nodes).flatMap((node, index) => [
  [node, nodes[(index + 1) % nodes.length]],
  [node, nodes[(index + 4) % nodes.length]],
]));
network.nodeAttribute('score', (_current, _id, ordinal) => ordinal / nodes.length);

const helios = new Helios(network, {
  container,
  mode: '2d',
});

await helios.ready;
helios.behavior.mappers.setChannelConfig('node', 'color', {
  type: 'colormap',
  attributes: 'score',
  colormap: 'interpolateTurbo',
  domain: [0, 1],
});
helios.frameNetwork({ animate: false });

const blob = await helios.exportFigurePreviewBlob({ format: 'png', width: 960, height: 540 });
const preview = document.createElement('img');
preview.className = 'helios-export-preview';
preview.src = URL.createObjectURL(blob);
container.append(preview);
```
