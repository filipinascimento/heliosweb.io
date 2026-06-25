# XNet

XNet is the human-readable Helios graph format. It is useful for fixtures,
examples, small graphs, and reviewable text artifacts. It preserves the Helios
graph model better than generic interchange formats while staying readable.

## Format Shape

Canonical XNet starts with:

```text
#XNET 1.0.0
#vertices <count>
#g "<graph-attribute>" <type>
#edges directed|undirected
<from> <to>
#v "<node-attribute>" <type>
...
#e "<edge-attribute>" <type>
...
```

Rules:

- Node and edge ids are zero-based integers.
- String values are quoted when needed and support `\n`, `\r`, `\t`, `\\`, and
  `\"` escapes.
- Numeric vectors are written on one line with space-separated components.
- Type tokens include `s`, `f`, `fN`, `i`, `iN`, `u`, `uN`, `I`, `IN`, `U`,
  `UN`, `c`, `cN`, `m`, and `mw`.
- Categorical dictionaries use `#vdict`, `#edict`, or `#gdict` immediately
  after the attribute declaration.
- Multi-category values are scalar sets. Weighted entries use
  `"label":<weight>`.
- `saveXNet()` compacts node ids and writes `_original_ids_` so callers can map
  back to pre-compaction ids.

Legacy XNet files may omit the version banner, include optional label lines
after `#vertices`, and encode edge weights directly in the edge list. Helios
readers normalize those payloads into regular attributes.

## JavaScript

```js
import HeliosNetwork from "helios-network";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(2);
network.addEdges([[nodes[0], nodes[1]]]);
network.nodeAttribute("label", ["A", "B"]);

const text = await network.saveXNet({ format: "string" });
const restored = await HeliosNetwork.fromXNet(text);
```

## Helios Web

```js
await helios.loadNetwork(file, { format: "xnet" });

const blob = await helios.savePortableNetwork("xnet", {
  output: "blob",
  includeVisualization: true,
});
```

XNet is a good teaching and debugging format, but large production documents
should usually use ZXNet.

## Python

```python
from helios_network import Network, read_xnet

network = Network(directed=False, node_capacity=2, edge_capacity=1)
nodes = network.add_nodes(2)
network.add_edges([(nodes[0], nodes[1])])
network.nodes["label"] = ["A", "B"]

network.save_xnet("graph.xnet")
restored = read_xnet("graph.xnet")
```

## Native C

```c
#include <helios/CXNetwork.h>
#include <helios/CXNetworkXNet.h>

CXNetworkRef network = CXNewNetworkWithCapacity(CXFalse, 2, 1);
CXNetworkWriteXNet(network, "graph.xnet");

CXNetworkRef restored = CXNetworkReadXNet("graph.xnet");
CXFreeNetwork(restored);
CXFreeNetwork(network);
```

## CLI

```bash
helios inspect ./graph.xnet --json
helios session start --network ./graph.xnet
helios call <sessionId> network.save --json '{"format":"zxnet","outputPath":"./graph.zxnet"}'
helios call <sessionId> network.save --json '{"format":"xnet","outputPath":"./roundtrip.xnet"}'
```

Use XNet output from the CLI when the result should be reviewable in a pull
request or easy to paste into an issue. Use ZXNet for large durable files.
