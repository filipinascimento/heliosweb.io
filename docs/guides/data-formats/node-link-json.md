# Node-Link JSON

Node-link JSON is a D3/NetworkX-style interchange object. Use it when a web app,
Python script, or external tool already produces object-shaped graph data. It is
not a full Helios persistence format.

## Shape

```json
{
  "directed": true,
  "multigraph": false,
  "graph": { "title": "Example" },
  "nodes": [
    { "id": "left", "label": "Left", "score": 1.5 },
    { "id": "right", "attributes": { "score": 2.0 } }
  ],
  "links": [
    { "source": "left", "target": "right", "weight": 3.5 }
  ]
}
```

During load, `network` is accepted as an alias for `graph`, and `edges` is
accepted as an alias for `links`. External node ids are preserved in the
`_original_ids_` node string attribute. Reserved keys such as `id`, `source`,
and `target` stay topology fields; non-reserved inline keys and nested
`attributes` objects become Helios attributes.

## JavaScript

```js
import HeliosNetwork from "helios-network";

const data = {
  directed: true,
  nodes: [{ id: "a", score: 1 }, { id: "b", score: 2 }],
  links: [{ source: "a", target: "b", weight: 3 }],
};

const network = await HeliosNetwork.fromNodeLinkJSON(data);
const json = await network.saveNodeLinkJSON({ format: "string" });
```

## Helios Web

Helios Web does not currently expose node-link JSON through
`loadNetwork(...)` or `savePortableNetwork(...)`. Convert node-link JSON through
Helios Network first, then pass the resulting network to the renderer:

```js
import HeliosNetwork from "helios-network";
import { Helios } from "helios-web";

const network = await HeliosNetwork.fromNodeLinkJSON(data);
const helios = new Helios(network, {
  container: document.querySelector("#app"),
});
```

Use ZXNet or a Helios session envelope when UI state, mappers, filters, camera
position, or layout state must survive a round-trip.

## Python

```python
from helios_network import read_node_link_json

network = read_node_link_json("graph.json")
network.save_node_link_json("roundtrip.json")
```

## Native C

```c
#include <helios/CXNetwork.h>
#include <helios/CXNetworkNodeLinkJSON.h>

CXNetworkRef network = CXNewNetworkWithCapacity(CXTrue, 2, 1);
CXNetworkWriteNodeLinkJSON(network, "graph.json");
CXFreeNetwork(network);
```

The current native surface writes node-link JSON. Use JS/WASM or Python when
you need object-oriented JSON loading.

## CLI

The CLI does not currently load node-link JSON directly. Convert through
JavaScript or Python first, then use a Helios-native format with the CLI:

```bash
node convert-node-link-to-zxnet.mjs
helios session start --network ./graph.zxnet
```

For command-line automation, keep node-link JSON conversion in a small
Helios Network script and hand the resulting `.zxnet`, `.bxnet`, or `.xnet`
file to `helios session start`.
