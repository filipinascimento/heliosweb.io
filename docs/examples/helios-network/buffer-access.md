# Low-Level Buffer Access

The chainable attribute writers are the recommended default for examples and
application code, but the low-level buffer API is still essential. Use
`withBufferAccess(...)` when you need to write millions of values, integrate a
custom parser, fill several typed arrays in a carefully controlled loop, or
avoid intermediate JavaScript objects.

The key rule is: allocate first, view second. WASM memory can grow after
allocation-prone calls, and growth can invalidate `TypedArray` views. Helios
Network enforces this by requiring direct buffer access inside
`withBufferAccess(...)`, where allocation-prone operations can throw instead of
silently invalidating a view.

## Fast Bulk Attribute Writes

Define attributes and perform any allocation-prone setup before entering
`withBufferAccess(...)`. Inside the callback, take the views, write them, and
leave. Bump attribute versions once after the bulk write so downstream renderers
and mappers know the data changed.

```javascript sidecode title="Use Direct WASM Buffer Views" console=true render=false height=470
//@BODY helios_network_buffer_access
import HeliosNetwork, { AttributeType } from "helios-network";

const network = await HeliosNetwork.create({ directed: false });
const nodes = network.addNodes(10);
const edges = network.addEdges(Array.from(nodes).map((node, index) => [
  node,
  nodes[(index + 1) % nodes.length],
]));

network.defineNodeAttribute('score', AttributeType.Float, 1);
network.defineEdgeAttribute('weight', AttributeType.Float, 1);

network.withBufferAccess(() => {
  const score = network.getNodeAttributeBuffer('score').view;
  const weight = network.getEdgeAttributeBuffer('weight').view;

  nodes.forEach((node, index) => {
    score[node] = index / (nodes.length - 1);
  });
  edges.forEach((edge, index) => {
    weight[edge] = 1 + index * 0.1;
  });
}, { nodeIndices: true, edgeIndices: true });

network.bumpNodeAttributeVersion('score');
network.bumpEdgeAttributeVersion('weight');

console.log({
  score: network.getNodeAttributeInfo('score'),
  weight: network.getEdgeAttributeInfo('weight'),
});
```

## When To Prefer Each API

Use chainable writers when:

- values come from ordinary row data;
- examples need to stay readable;
- attribute schemas can be inferred or expressed with simple options;
- callbacks are clear enough and performance is not dominated by the writer.

Use `withBufferAccess(...)` when:

- you are filling large typed arrays;
- you need one tight loop over multiple buffers;
- you are adapting an existing binary parser or scientific data format;
- you need explicit control over every allocation and version bump.

Both APIs write into the same graph. The high-level helpers use safe buffer
access internally; the low-level API exposes that mechanism directly.
