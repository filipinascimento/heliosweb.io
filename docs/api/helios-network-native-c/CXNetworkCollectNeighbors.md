# CXNetworkCollectNeighbors

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:433</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Collects unique one-hop neighbors for one or more source nodes. - `sourceNodes` can contain any node ids; inactive/out-of-range entries are ignored. - `direction` controls traversal for directed graphs (`out`, `in`, `both`). - `includeSourceNodes` controls whether source nodes can appear in `outNodeSelector`. - `outEdgeSelector` is optional; pass NULL to skip edge collection.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkCollectNeighbors( CXNetworkRef network, const CXIndex *sourceNodes, CXSize sourceCount, CXNeighborDirection direction, CXBool includeSourceNodes, CXNodeSelectorRef outNodeSelector, CXEdgeSelectorRef outEdgeSelector );
```

</div>
