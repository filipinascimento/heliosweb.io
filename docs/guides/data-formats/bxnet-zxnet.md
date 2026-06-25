# BXNet And ZXNet

BXNet and ZXNet are the native binary Helios graph formats. They share the same
logical container. BXNet writes the byte stream directly; ZXNet writes the same
stream through BGZF compression. Use ZXNet as the default persisted graph file,
and BXNet when uncompressed speed or low-level inspection is more useful than a
smaller file.

## Format Layout

All multi-byte values are little-endian. The file contains:

```text
64 byte header
ordered chunk stream
512 byte footer
```

The header starts with `ZXNETFMT`, records semantic format version `1.0.0`, a
codec id (`0` for BXNet, `1` for ZXNet), directedness flags, active node/edge
counts, and node/edge capacities.

Every chunk has a 16 byte header:

```text
uint32 chunk id
uint32 flags
uint64 payload byte length
```

The current chunk order is fixed:

| Chunk | Purpose |
| --- | --- |
| `META` | Directed flag, counts, capacities, and attribute counts |
| `NODE` | Node activity bitmap |
| `EDGE` | Edge activity bitmap plus `from`/`to` endpoint table |
| `NATT` | Node attribute declarations |
| `EATT` | Edge attribute declarations |
| `GATT` | Network/graph attribute declarations |
| `NVAL` | Node attribute values |
| `EVAL` | Edge attribute values |
| `GVAL` | Network/graph attribute values |

Chunk payloads are built from blocks stored as `uint64 byte_length` followed by
raw bytes. Attribute declarations store the UTF-8 name, `CXAttributeType`,
dimension, storage width, capacity, flags, and optional categorical dictionary.
Numeric, boolean, categorical, BigInteger, and multi-category attributes are
supported. Multi-category values use a CSR-like payload with offsets, category
ids, and optional float weights.

The footer starts with `ZXFOOTER`, contains a chunk directory, mirrors graph and
attribute counts, and stores a CRC32 over the header plus chunk stream. A
compatible reader should validate magic strings, version, chunk order, lengths,
and CRC before trusting offsets.

## JavaScript

```js
import HeliosNetwork from "helios-network";

const network = await HeliosNetwork.create({ directed: true });
const nodes = network.addNodes(3);
network.addEdges([[nodes[0], nodes[1]], [nodes[1], nodes[2]]]);
network.nodeAttribute("label", ["left", "middle", "right"]);

await network.saveZXNet({ path: "./graph.zxnet", compressionLevel: 6 });
await network.saveBXNet({ path: "./graph.bxnet" });

const fromZx = await HeliosNetwork.fromZXNet("./graph.zxnet");
const fromBx = await HeliosNetwork.fromBXNet("./graph.bxnet");
```

In a browser, use bytes or blobs instead of file paths:

```js
const bytes = await network.saveZXNet({ format: "uint8array" });
const restored = await HeliosNetwork.fromZXNet(bytes);
```

## Helios Web

```js
import { Helios } from "helios-web";

const helios = new Helios(network, { container: "#app", fileDrop: true });
await helios.ready;

await helios.loadNetwork(file, { format: "zxnet" });

const blob = await helios.savePortableNetwork("zxnet", {
  output: "blob",
  includeVisualization: true,
});
```

`includeVisualization: true` stores Helios visualization state in the portable
network payload. Use it for user-facing documents; omit it for graph-only data
exchange.

## Python

```python
from helios_network import Network, read_bxnet, read_zxnet

network = Network(directed=True, node_capacity=3, edge_capacity=2)
nodes = network.add_nodes(3)
network.add_edges([(nodes[0], nodes[1]), (nodes[1], nodes[2])])
network.nodes["label"] = ["left", "middle", "right"]

network.save_zxnet("graph.zxnet", compression=6)
network.save_bxnet("graph.bxnet")

from_zx = read_zxnet("graph.zxnet")
from_bx = read_bxnet("graph.bxnet")
```

## Native C

```c
#include <helios/CXNetwork.h>
#include <helios/CXNetworkBXNet.h>

CXNetworkRef network = CXNewNetworkWithCapacity(CXTrue, 3, 2);
CXIndex nodes[3];
CXNetworkAddNodes(network, 3, nodes);

CXNetworkWriteZXNet(network, "graph.zxnet", 6);
CXNetworkWriteBXNet(network, "graph.bxnet");

CXNetworkRef restored = CXNetworkReadZXNet("graph.zxnet");
CXFreeNetwork(restored);
CXFreeNetwork(network);
```

## CLI

```sh
helios inspect ./graph.zxnet --json
helios session start --network ./graph.zxnet
helios call <sessionId> network.save --json '{"outputPath":"./graph.zxnet","includeVisualization":true}'
```

