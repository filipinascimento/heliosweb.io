# Extension Patterns

These examples cover public helper APIs that are useful in applications but do
not need to appear in the first rendering examples. Each snippet keeps the graph
small and focuses on one feature at a time.

## Programmatic Filters

`HeliosFilter` is a reusable filter model. Build it once, add one or more rules,
and activate it through the Helios instance. The same filter can later be
serialized, edited by UI code, or re-applied after data changes.

```javascript sidecode title="Activate A HeliosFilter" console=true height=460
//@BODY helios_web_advanced_filter
import HeliosNetwork from "helios-network";
import { Helios, HeliosFilter } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(12);

network.addEdges(Array.from(nodes, (node, index) => [node, nodes[(index + 1) % nodes.length]]));
network.nodeAttribute('score', (_current, _id, ordinal) => ordinal / (nodes.length - 1));

const helios = new Helios(network, { container, mode: '2d' });
await helios.ready;

const filter = new HeliosFilter({ scope: 'render' });
filter.upsertRule({
  id: 'high-score',
  type: 'numeric',
  scope: 'node',
  attribute: 'score',
  min: 0.45,
  max: 1,
});

helios.activateHeliosFilter(filter);
helios.frameNetwork({ animate: false });

console.log(filter.toGraphFilterOptions());
```

## Categorical Colormaps

`createCategoricalColormap(...)` samples a named or custom colormap into a fixed
number of RGBA colors. Use it when app data has discrete categories but the
visual language should still follow the same palette family as continuous
attributes.

```javascript sidecode title="Sample A Categorical Palette" console=true render=false height=330
//@BODY helios_web_advanced_colormap
import { createCategoricalColormap } from "helios-web";

const palette = createCategoricalColormap('CET_R1-BalancedRainbow', 4);
const cssColors = palette.map(([r, g, b, a]) =>
  `rgba(${Math.round(r * 255)}, ${Math.round(g * 255)}, ${Math.round(b * 255)}, ${a.toFixed(2)})`
);

console.log(cssColors);
```

## Web Components

`defineHeliosWebComponents(...)` registers the optional custom elements exposed
by Helios Web. Call it once during app startup before rendering markup that uses
those elements.

```javascript sidecode title="Register Web Components" console=true render=false height=320
//@BODY helios_web_advanced_components
import { defineHeliosWebComponents } from "helios-web";

const result = defineHeliosWebComponents(document);

console.log(result);
console.log(customElements.get('helios-panel') !== undefined);
```

## Custom UI Controller

Helios UI controls are usually built around `UIAttribute`: a small getter/setter
object with metadata that panel rows can read. This keeps custom controls
consistent with built-in controls and gives them a clear place to connect state,
validation, and persistence.

The example below creates a tiny controller for node size. The important pieces
are the attribute getter/setter, a DOM input that writes through the attribute,
and a panel created through the public `HeliosUI` surface.

```js
import { UIAttribute } from "helios-web";

// Assumes `helios` is an existing Helios instance with `helios.ui` enabled.
const sizeAttribute = UIAttribute.number({
  id: 'demo.nodeSizeScale',
  label: 'Node size',
  min: 0,
  max: 20,
  step: 0.25,
  get: () => helios.nodeSizeScale(),
  set: (value) => helios.nodeSizeScale(value),
});

const row = document.createElement('label');
row.textContent = 'Node size';

const input = document.createElement('input');
input.type = 'range';
input.min = '0';
input.max = '20';
input.step = '0.25';
input.value = String(sizeAttribute.value());
input.addEventListener('input', () => sizeAttribute.write(Number(input.value)));
sizeAttribute.subscribe((value) => { input.value = String(value); });
row.append(input);

const panel = helios.ui.createPanel({
  id: 'demo-size-panel',
  title: 'Size',
  dock: 'right',
  content: row,
});

console.log(panel.id);
```

For persistence-aware controls, register the state path first and pass a
matching accessor through `HeliosUI.bindHeliosAccessor(...)` or
`HeliosUI.bindBehaviorAccessor(...)`. That lets the same control show dirty
indicators and participate in session restore.
