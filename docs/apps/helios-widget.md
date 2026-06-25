# Helios Widget

Helios Widget is the Python and Jupyter host for live Helios visualization. It
connects a Python `helios_network.Network` to the Helios Web renderer through an
AnyWidget-backed frontend in notebooks, and can also open a local browser view
from a plain Python process.

Project link: https://github.com/filipinascimento/helios-widget

## Minimal Notebook Use

```python
from helios_network import Network
from helios_widget import show

net = Network(directed=False)
nodes = net.add_nodes(3)
net.add_edges([(nodes[0], nodes[1])])
net.nodes["weight"] = [1.0, 2.0, 3.0]

view = show(net, ui=True)
view.appearance(node_size_scale=1.8, edge_width_scale=0.6)
view.labels(enabled=True, source="label", max_visible=100)
view.selection.select_nodes([0, 2], {"mode": "replace"})
view.frame(animate=True)
```

## Controls

The widget exposes high-level Python control groups that map to Helios Web
behaviors:

- `view.appearance(...)`
- `view.labels(...)`
- `view.legends(...)`
- `view.layout(...)`
- `view.filters(...)`
- `view.selection(...)`

Attribute assignment works for common settings, and `view.helios.<method>(...)`
can call public Helios methods directly using snake_case or camelCase names.

## UI Panels

Enable the built-in Helios Web panels with:

```python
view = show(net, ui=True)
```

Choose a subset when the notebook should expose only specific workflows:

```python
view = show(net, ui={"panels": ["mappers", "layout", "legends", "camera", "selection"]})
```

## Persistence

Notebook persistence uses the centralized Helios Web storage pipeline with a
traitlet-backed remote storage client. The synchronized `persistence_state`
traitlet stores a widget-owned session record and side records for network and
position payloads when they fit within widget storage limits.

The Python-owned network remains the source of truth for live notebooks. Widget
runs hide browser network loading and saved-session selection UI by default
because notebook code usually controls the graph data lifecycle.

Useful constructor options include:

- `workspaceId="..."` to isolate widget state;
- `networkPersistence={...}` and `positionPersistence={...}` to tune payload
  persistence;
- `autosyncPayloadLimits={...}` to prevent large notebooks from storing too much
  binary state in notebook metadata.

## Export

Save a standalone HTML snapshot with:

```python
view.save_html("graph.html")
```

This writes an HTML file plus a runtime asset folder. The graph snapshot is
embedded, so opening the export later does not require a running Python kernel.

For live notebook reloads, save Jupyter widget state with the notebook before
closing. Without saved widget state, old outputs can show missing model errors
and should be re-executed.
