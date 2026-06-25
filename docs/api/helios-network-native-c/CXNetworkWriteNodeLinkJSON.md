# CXNetworkWriteNodeLinkJSON

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetworkNodeLinkJSON.h:22</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Serializes a network as node-link JSON compatible with common D3/NetworkX style payloads. Lossy cases are reported via `CXNetworkSerializationLastWarningMessage()`. @param network Network to serialize. @param path Output path for the `.json` file. @return CXTrue on success, CXFalse on failure.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkWriteNodeLinkJSON(struct CXNetwork *network, const char *path);
```

</div>
