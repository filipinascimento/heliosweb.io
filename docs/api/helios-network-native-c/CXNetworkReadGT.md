# CXNetworkReadGT

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetworkGT.h:23</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Reads a graph-tool `.gt` binary graph file. Supports the v1 graph-tool wire format, including endian-aware topology loading and the scalar/vector property-map types that map cleanly to Helios attributes. Unsupported or lossy property maps are skipped and reported via `CXNetworkSerializationLastWarningMessage()`. @param path Path to the `.gt` file on disk. @return Newly allocated network when successful, otherwise NULL.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN struct CXNetwork* CXNetworkReadGT(const char *path);
```

</div>
