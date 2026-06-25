# CXNetworkWriteXNet

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetworkXNet.h:31</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Serializes a network using the XNET 1.0.0 human-readable container. Performs compaction to ensure contiguous node and edge indices before writing. Adds the `_original_ids_` vertex attribute to preserve the original node identifiers. @param network Network to serialize. @param path Output path for the `.xnet` file. @return CXTrue on success, CXFalse on failure.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkWriteXNet(struct CXNetwork *network, const char *path);
```

</div>
