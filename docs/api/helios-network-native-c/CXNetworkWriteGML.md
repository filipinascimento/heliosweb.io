# CXNetworkWriteGML

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetworkGML.h:33</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Serializes a network as GML. Lossy cases (for example unsupported attribute payloads or renamed keys) are reported via `CXNetworkSerializationLastWarningMessage()`. @param network Network to serialize. @param path Output path for the `.gml` file. @return CXTrue on success, CXFalse on failure.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkWriteGML(struct CXNetwork *network, const char *path);
```

</div>
