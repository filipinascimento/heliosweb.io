# CXNetworkWriteActiveEdges

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:292</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Writes active edge indices into caller-provided storage. When `capacity` is insufficient the required size is returned and no writes occur.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXSize CXNetworkWriteActiveEdges(CXNetworkRef network, CXIndex *dst, CXSize capacity);
```

</div>
