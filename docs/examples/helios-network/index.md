# Data/API Examples

Helios Network examples are API/data-first. They focus on graph construction,
attribute writing, selectors, serialization, language bindings, and the low-level
WASM buffer path that powers high-performance workflows.

For ordinary JavaScript code, prefer the chainable attribute writers:
`nodeAttribute`, `edgeAttribute`, `nodeAttributes`, `edgeAttributes`,
`networkAttribute`, and `networkAttributes`. They keep examples readable while
still handling schema inference, version bumps, and safe WASM access internally.

Use `withBufferAccess(...)` when you deliberately need direct typed-array views
for very large writes, custom importers, or tight loops.

## Categories

- [Graphs and attributes](graphs-attributes.md) covers graph creation and
  chainable node, edge, and network attributes.
- [Selectors and serialization](selectors-serialization.md) covers query
  selection, neighbors, ZXNet round trips, and handoff into Helios Web.
- [Low-level buffer access](buffer-access.md) documents the fast path and the
  WASM view lifetime rules.
- [Language bindings](language-bindings.md) shows Python and native C usage.
- [Data formats](../../guides/data-formats/index.md) describes every supported file
  format and shows load/save examples across JavaScript, Helios Web, Python,
  native C, and CLI.
