# CXNetworkWriteGT

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetworkGT.h:36</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Serializes a network as a graph-tool `.gt` binary graph file. `.gt` is an interoperability format. Helios-specific state and unsupported attributes may be skipped or converted, with warnings reported via `CXNetworkSerializationLastWarningMessage()`. @param network Network to serialize. @param path Output path for the `.gt` file. @return CXTrue on success, CXFalse on failure.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkWriteGT(struct CXNetwork *network, const char *path);
```

</div>
