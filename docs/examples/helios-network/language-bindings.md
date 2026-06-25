# Language Bindings

Helios Network is built around a native graph core, so the same data model can
be used from JavaScript/WASM, Python, and C. The JavaScript examples elsewhere
in this section focus on the browser and Node wrapper. This page shows equivalent
data-first workflows in Python and native C.

## Python Usage

Python code is useful for batch import, analysis, notebooks, and data pipelines
that produce files later consumed by Helios Web.

```python
from helios_network import AttributeScope, AttributeType, Network, read_zxnet

network = Network(directed=True, node_capacity=5, edge_capacity=5)
nodes = network.add_nodes(5)
edges = network.add_edges([
    (nodes[0], nodes[1]),
    (nodes[1], nodes[2]),
    (nodes[2], nodes[3]),
    (nodes[3], nodes[4]),
])

network.define_attribute(AttributeScope.Node, "score", AttributeType.Double, 1)
network.nodes["score"] = [0.1, 0.4, 0.8, 0.7, 0.2]
network.nodes[[nodes[2], nodes[3]]]["label"] = ["hub", "bridge"]
network.edges["weight"] = [0.9, 0.4, 0.6, 0.3]

selected = network.select_nodes("score >= 0.7")
print(selected.ids)

network.save_zxnet("example.zxnet")
restored = read_zxnet("example.zxnet")
print(restored.node_count(), restored.edge_count())
```

## Native C Usage

Native C access is the lowest-level API. It is appropriate for embedding the
graph core in native applications, building language bindings, or writing
performance-critical import/export code.

```c
#include <helios/CXNetwork.h>
#include <helios/CXNetworkBXNet.h>

int main(void) {
    CXNetwork *network = CXNewNetworkWithCapacity(CXTrue, 5, 5);
    CXIndex nodes[5];
    CXNetworkAddNodes(network, 5, nodes);

    CXEdge pairs[4] = {
        {nodes[0], nodes[1]},
        {nodes[1], nodes[2]},
        {nodes[2], nodes[3]},
        {nodes[3], nodes[4]},
    };
    CXIndex edges[4];
    CXNetworkAddEdges(network, pairs, 4, edges);

    CXNetworkDefineNodeAttribute(network, "score", CXDoubleAttributeType, 1);
    double *score = (double *)CXNetworkGetNodeAttributeBuffer(network, "score");
    score[nodes[0]] = 0.1;
    score[nodes[1]] = 0.4;
    score[nodes[2]] = 0.8;
    score[nodes[3]] = 0.7;
    score[nodes[4]] = 0.2;

    CXNodeSelector *selected = CXNodeSelectorCreate(0);
    CXNetworkSelectNodesByQuery(network, "score >= 0.7", selected);

    CXNetworkWriteBXNet(network, "example.bxnet");
    CXNodeSelectorDestroy(selected);
    CXFreeNetwork(network);
    return 0;
}
```
