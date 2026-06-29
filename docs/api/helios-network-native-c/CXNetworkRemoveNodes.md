# CXNetworkRemoveNodes

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:369</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Removes the supplied nodes, reclaiming their indices for future use.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkRemoveNodes(CXNetworkRef network, const CXIndex *indices, CXSize count);
```

</div>
