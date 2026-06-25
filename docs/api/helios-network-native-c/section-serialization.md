
# Serialization

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

Readers and writers for BXNet, ZXNet, XNet, GML, and node-link JSON.

Serialization functions are the source of truth for file-format support in the
native graph core. Higher-level JavaScript, Python, CLI, widget, and desktop
surfaces delegate to these readers and writers when possible.

Use the data-format guides for file structure explanations and language-level
load/save examples. Use this reference for exact native function signatures.

<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../CXNetworkReadBXNet/">
<span>function</span>
<strong>CXNetworkReadBXNet</strong>
<em>Reads an uncompressed BXNet file from disk.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkReadGML/">
<span>function</span>
<strong>CXNetworkReadGML</strong>
<em>Reads a graph from a GML file. Accepts standard GML and a looser dialect that tolerates quoted keys and unquoted scalar strings. @param path Path to the `.gml` file on disk. @return Newly allocated network when successful, otherwise NULL.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkReadGT/">
<span>function</span>
<strong>CXNetworkReadGT</strong>
<em>Reads a graph-tool `.gt` binary graph file. Supports the v1 graph-tool wire format, including endian-aware topology loading and the scalar/vector property-map types that map cleanly to Helios attributes. Unsupported or lossy property maps are skipped and reported via `CXNetworkSerializationLastWarningMessage()`. @param path Path to the `.gt` file on disk. @return Newly allocated network when successful, otherwise NULL.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkReadXNet/">
<span>function</span>
<strong>CXNetworkReadXNet</strong>
<em>Reads a graph from an `.xnet` (XNET 1.0.0 or legacy) container. @param path Path to the XNET file on disk. @return Newly allocated network when successful, otherwise NULL.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkReadZXNet/">
<span>function</span>
<strong>CXNetworkReadZXNet</strong>
<em>Reads a BGZF-compressed ZXNet file from disk.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkSerializationLastWarningMessage/">
<span>function</span>
<strong>CXNetworkSerializationLastWarningMessage</strong>
<em>Returns the last non-fatal serialization warning emitted by a save/load helper.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkSerializationWarningAppend/">
<span>function</span>
<strong>CXNetworkSerializationWarningAppend</strong>
<em>Appends a formatted message to the shared serialization warning buffer.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkSerializationWarningClear/">
<span>function</span>
<strong>CXNetworkSerializationWarningClear</strong>
<em>Clears the shared serialization warning buffer.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteActiveEdgeNodeAttributes/">
<span>function</span>
<strong>CXNetworkWriteActiveEdgeNodeAttributes</strong>
<em>Writes `componentsPerNode` values for each endpoint of active edges from the provided node attribute buffer into a caller-managed destination. Values are copied verbatim; the caller controls element width (`componentSizeBytes`) and must ensure the typed views line up with the provided byte offsets. Returns the number of edges that would be written; when `dstCapacityEdges` is too small, the required count is returned and no writes occur.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteActiveEdges/">
<span>function</span>
<strong>CXNetworkWriteActiveEdges</strong>
<em>Writes active edge indices into caller-provided storage. When `capacity` is insufficient the required size is returned and no writes occur.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteActiveEdgeSegments/">
<span>function</span>
<strong>CXNetworkWriteActiveEdgeSegments</strong>
<em>Writes two position vectors per active edge directly into the provided buffer. `componentsPerNode` describes how many floats to copy per endpoint (commonly 4 for vec4 data). Returns the number of edges that would be written; when `dstCapacityEdges` is too small, the required count is returned and no writes occur.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteActiveNodes/">
<span>function</span>
<strong>CXNetworkWriteActiveNodes</strong>
<em>Writes active node indices into caller-provided storage. When `capacity` is insufficient the required size is returned and no writes occur.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteBXNet/">
<span>function</span>
<strong>CXNetworkWriteBXNet</strong>
<em>Writes an uncompressed binary BXNet file to disk.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteBXNetFiltered/">
<span>function</span>
<strong>CXNetworkWriteBXNetFiltered</strong>
<em>Writes a BXNet file while allowing or ignoring selected attributes by scope.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteGML/">
<span>function</span>
<strong>CXNetworkWriteGML</strong>
<em>Serializes a network as GML. Lossy cases (for example unsupported attribute payloads or renamed keys) are reported via `CXNetworkSerializationLastWarningMessage()`. @param network Network to serialize. @param path Output path for the `.gml` file. @return CXTrue on success, CXFalse on failure.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteGT/">
<span>function</span>
<strong>CXNetworkWriteGT</strong>
<em>Serializes a network as a graph-tool `.gt` binary graph file. `.gt` is an interoperability format. Helios-specific state and unsupported attributes may be skipped or converted, with warnings reported via `CXNetworkSerializationLastWarningMessage()`. @param network Network to serialize. @param path Output path for the `.gt` file. @return CXTrue on success, CXFalse on failure.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteNodeLinkJSON/">
<span>function</span>
<strong>CXNetworkWriteNodeLinkJSON</strong>
<em>Serializes a network as node-link JSON compatible with common D3/NetworkX style payloads. Lossy cases are reported via `CXNetworkSerializationLastWarningMessage()`. @param network Network to serialize. @param path Output path for the `.json` file. @return CXTrue on success, CXFalse on failure.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteXNet/">
<span>function</span>
<strong>CXNetworkWriteXNet</strong>
<em>Serializes a network using the XNET 1.0.0 human-readable container. Performs compaction to ensure contiguous node and edge indices before writing. Adds the `_original_ids_` vertex attribute to preserve the original node identifiers. @param network Network to serialize. @param path Output path for the `.xnet` file. @return CXTrue on success, CXFalse on failure.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteXNetFiltered/">
<span>function</span>
<strong>CXNetworkWriteXNetFiltered</strong>
<em>Serializes an XNET file while allowing or ignoring selected attributes. Attribute filters are split by node, edge, and graph/network scope. @param network Network to serialize. @param path Output path for the `.xnet` file. @return CXTrue on success, CXFalse on failure.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteZXNet/">
<span>function</span>
<strong>CXNetworkWriteZXNet</strong>
<em>Writes a BGZF-compressed ZXNet file to disk.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkWriteZXNetFiltered/">
<span>function</span>
<strong>CXNetworkWriteZXNetFiltered</strong>
<em>Writes a ZXNet file while allowing or ignoring selected attributes by scope.</em>
</a>
</div>
