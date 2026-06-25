# Data Formats

Helios supports two families of graph files:

- **Native Helios snapshots** preserve topology, directedness, active/inactive
  rows, typed attributes, categorical dictionaries, and the details needed for
  fast round trips between the WebAssembly, Python, native C, CLI, Widget, and
  Desktop hosts.
- **Interchange formats** make it easy to exchange graphs with other tools, at
  the cost of some Helios-specific state or exact typed-buffer fidelity.

Use `.zxnet` as the default application format. It is compact, portable, and
preserves the native Helios graph model. Use `.bxnet` for uncompressed binary
snapshots, `.xnet` for readable fixtures and examples, `.gml` for graph-tooling
interchange, `.gt`/`.gt.zst` for graph-tool datasets, and node-link JSON for
D3/NetworkX-style web and Python data exchange.

Package imports in the examples use the public 0.10.0 package names
`helios-network` and `helios-web`.

## Format Summary

| Format | Extensions | Fidelity | Read | Write | Best Use |
| --- | --- | --- | --- | --- | --- |
| BXNet | `.bxnet` | Full Helios typed graph, uncompressed | JS/WASM, Python, C, CLI, Web, Desktop, Widget | JS/WASM, Python, C, CLI, Web, Desktop, Widget | Fast local snapshots and binary debugging |
| ZXNet | `.zxnet` | Full Helios typed graph, BGZF-compressed | JS/WASM, Python, C, CLI, Web, Desktop, Widget | JS/WASM, Python, C, CLI, Web, Desktop, Widget | Default durable/session/network payloads |
| XNet | `.xnet` | Human-readable Helios text graph | JS/WASM, Python, C, CLI, Web, Desktop, Widget | JS/WASM, Python, C, CLI, Web, Desktop, Widget | Examples, fixtures, readable archives |
| GML | `.gml` | Interchange graph plus simple attributes | JS/WASM, Python, C, CLI, Web, Desktop, Widget | JS/WASM, Python, C, CLI, Web, Desktop, Widget | External graph tools |
| graph-tool GT | `.gt`, `.gt.zst` | graph-tool binary graph. `.gt.zst` is read-only in Helios. | JS/WASM, Python, C, CLI, Web, Desktop, Widget | Plain `.gt` in JS/WASM, Python, C, CLI, Web, Desktop, Widget | Exchange with graph-tool |
| Node-link JSON | `.json` | D3/NetworkX-style object graph | JS/WASM, Python | JS/WASM, Python, C writer | Web/Python ecosystem handoff |

Portable visualization state can be embedded in `.xnet`, `.zxnet`, and
`.bxnet` outputs. GML, GT, and node-link JSON are graph interchange formats; if
Desktop or CLI needs to preserve Helios view state alongside them, it should
write a sidecar such as `.helios-state.json`.

## Choose A Format

- Pick **ZXNet** for application defaults, autosave, browser sessions, desktop
  documents, and most saved Helios files.
- Pick **BXNet** when compression is unnecessary and direct byte inspection or
  fastest local write speed matters.
- Pick **XNet** for small examples, fixtures, hand-authored graphs, and code
  review diffs.
- Pick **GML** only when another graph package explicitly wants GML.
- Pick **GT/GT.ZST** when exchanging data with graph-tool.
- Pick **node-link JSON** when a D3 or NetworkX shaped object is the easiest
  producer or consumer.

## Pages

- [BXNet and ZXNet](bxnet-zxnet.md)
- [XNet](xnet.md)
- [GML](gml.md)
- [graph-tool GT](gt.md)
- [Node-link JSON](node-link-json.md)
