# GML

GML is an interoperability format, not a complete Helios state container. Use it
when another graph tool needs GML. Use ZXNet, BXNet, or XNet when a Helios
workflow needs full typed attributes and visualization state.

Helios accepts standard GML and a looser dialect with quoted keys and unquoted
scalar strings. Export sanitizes unsafe keys, deduplicates collisions, skips
values that cannot be represented safely, and exposes serialization warnings.

## JavaScript

```js
import HeliosNetwork from "helios-network";

const network = await HeliosNetwork.create({ directed: true });
const nodes = network.addNodes(2);
network.addEdges([[nodes[0], nodes[1]]]);
network.nodeAttribute("label", ["source", "target"]);

await network.saveGML({ path: "./graph.gml" });
const restored = await HeliosNetwork.fromGML("./graph.gml");
```

## Helios Web

```js
await helios.loadNetwork(file, { format: "gml" });

const graphOnly = await helios.savePortableNetwork("gml", {
  output: "blob",
  includeVisualization: false,
});
```

`includeVisualization: true` is rejected for GML because GML has no native place
for Helios view state.

## Python

```python
from helios_network import Network, read_gml

network = Network(directed=True, node_capacity=2, edge_capacity=1)
nodes = network.add_nodes(2)
network.add_edges([(nodes[0], nodes[1])])
network.nodes["label"] = ["source", "target"]

network.save_gml("graph.gml")
restored = read_gml("graph.gml")
```

## Native C

```c
#include <helios/CXNetwork.h>
#include <helios/CXNetworkGML.h>

CXNetworkRef network = CXNewNetworkWithCapacity(CXTrue, 2, 1);
CXNetworkWriteGML(network, "graph.gml");

CXNetworkRef restored = CXNetworkReadGML("graph.gml");
CXFreeNetwork(restored);
CXFreeNetwork(network);
```

After lossy reads or writes, check `CXNetworkSerializationLastWarningMessage()`
when warnings are important to the workflow.

## CLI

```bash
helios session start --network ./graph.gml
helios call <sessionId> network.save --json '{"format":"zxnet","outputPath":"./graph.zxnet"}'
helios call <sessionId> network.save --json '{"format":"gml","outputPath":"./roundtrip.gml"}'
```

GML is graph-only. Use a Helios-native format such as ZXNet when the saved file
must keep visualization state.
