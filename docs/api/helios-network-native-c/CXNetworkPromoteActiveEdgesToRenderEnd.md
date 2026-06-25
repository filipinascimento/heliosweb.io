# CXNetworkPromoteActiveEdgesToRenderEnd

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:291</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Moves active edge indices to the end of the native active order, preserving batch order.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkPromoteActiveEdgesToRenderEnd( CXNetworkRef network, const CXIndex *indices, CXSize count, CXSize *changedStart, CXSize *changedCount );
```

</div>
