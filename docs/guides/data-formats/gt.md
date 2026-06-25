# graph-tool GT

GT is graph-tool's binary graph format. Helios reads `.gt` and zstd-compressed
`.gt.zst` payloads and writes plain `.gt` payloads. If you need `.gt.zst`, write
`.gt` and compress it outside Helios.

For the authoritative format description, use graph-tool's own
[Graph I/O documentation](https://graph-tool.skewed.de/doc/quickstart.html#graph-io).
Helios maps graph-tool graph, vertex, and edge property maps to network, node,
and edge attributes when their scalar/vector property-map types can be
represented by Helios. Unsupported or lossy property maps are skipped with a
warning.

## JavaScript

```js
import HeliosNetwork from "helios-network";

const network = await HeliosNetwork.create({ directed: false });
network.addNodes(2);
network.addEdges([[0, 1]]);

await network.saveGT({ path: "./graph.gt" });

const fromGt = await HeliosNetwork.fromGT("./graph.gt");
const fromCompressedGt = await HeliosNetwork.fromGT("./graph.gt.zst");
```

## Helios Web

```js
await helios.loadNetwork(file, { format: "gt" });

const gtBlob = await helios.savePortableNetwork("gt", {
  output: "blob",
  includeVisualization: false,
});
```

GT is graph-only in Helios Web. Use ZXNet when saving a Helios document with
visualization state.

## Python

```python
from helios_network import Network, read_gt

network = Network(directed=False, node_capacity=2, edge_capacity=1)
network.add_nodes(2)
network.add_edges([(0, 1)])

network.save_gt("graph.gt")
payload = network.to_gt_bytes()

from_gt = read_gt("graph.gt")
from_gt_zst = read_gt("graph.gt.zst")
```

## Native C

```c
#include <helios/CXNetwork.h>
#include <helios/CXNetworkGT.h>

CXNetworkRef network = CXNewNetworkWithCapacity(CXFalse, 2, 1);
CXNetworkWriteGT(network, "graph.gt");

CXNetworkRef restored = CXNetworkReadGT("graph.gt.zst");
CXFreeNetwork(restored);
CXFreeNetwork(network);
```

## CLI

```bash
helios inspect ./graph.gt --format gt --json
helios session start --network ./graph.gt
helios call <sessionId> network.save --json '{"format":"zxnet","outputPath":"./graph.zxnet"}'
helios call <sessionId> network.save --json '{"format":"gt","outputPath":"./roundtrip.gt"}'
```

Helios writes plain `.gt`. Use an external zstd compressor when the destination
must be `.gt.zst`.
