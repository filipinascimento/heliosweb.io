# CXNetworkPromoteActiveEdgesForNodesToRenderEnd

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:300</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Moves active edges incident to the supplied active nodes to the end of the native active edge order.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkPromoteActiveEdgesForNodesToRenderEnd( CXNetworkRef network, const CXIndex *nodeIndices, CXSize nodeCount, CXNeighborDirection direction, CXSize *changedStart, CXSize *changedCount );
```

</div>
