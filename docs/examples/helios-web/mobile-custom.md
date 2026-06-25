# Touch And Mobile Controls

Touch-oriented views use the same graph, renderer, and behavior APIs as desktop
views. A few options tell Helios how much of the touch interaction surface it
should own and how the interface behavior should classify compact layouts.

Custom behaviors are for app-specific logic that needs lifecycle, state,
subscriptions, or coordination with built-in behaviors. They are not required
for small scripts, but they are useful when a feature should attach and detach
cleanly.

## Configure Touch Interaction

`suppressBrowserGestures` tells Helios that the canvas should own gestures such
as pan and pinch inside the visualization area. The interface behavior options
configure compact-state thresholds, while hover options show how behavior tuning
can remain declarative.

```javascript sidecode title="Configure Touch Interaction" console=true height=470
//@BODY helios_web_mobile_touch
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(14);

network.addEdges(Array.from(nodes).flatMap((node, index) => [
  [node, nodes[(index + 1) % nodes.length]],
  [node, nodes[(index + 5) % nodes.length]],
]));

const helios = new Helios(network, {
  container,
  mode: '2d',
  suppressBrowserGestures: true,
  behaviors: {
    interface: { compactBreakpoint: 520, preferredDockSide: 'right' },
    hover: { edgeHover: true },
  },
});

await helios.ready;
helios.behavior.interface.setViewportWidth(360);
helios.frameNetwork({ animate: false });
```

## Register A Custom Behavior

This custom behavior selects the first few nodes when it attaches. The important
detail is that it composes with the default behavior namespace: custom code uses
`context.helios.behavior.selection` instead of duplicating selection state.

```javascript sidecode title="Register A Custom Behavior" console=true height=480
//@BODY helios_web_custom_behavior
import HeliosNetwork from "helios-network";
import { Behavior, Helios } from "helios-web";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(18);

network.addEdges(Array.from(nodes).flatMap((node, index) => [
  [node, nodes[(index + 1) % nodes.length]],
  [node, nodes[(index + 6) % nodes.length]],
]));

class SelectFirstNodesBehavior extends Behavior {
  static id = 'select-first-nodes';

  attach(context) {
    super.attach(context);
    context.helios.behavior.selection.selectNodes(
      Array.from(nodes).slice(0, 4),
      { mode: 'replace' },
    );
    return this;
  }
}

const helios = new Helios(network, {
  container,
  mode: '2d',
});

await helios.ready;
helios.registerBehavior('select-first-nodes', SelectFirstNodesBehavior);
helios.useBehavior('select-first-nodes');
helios.frameNetwork({ animate: false });
```
