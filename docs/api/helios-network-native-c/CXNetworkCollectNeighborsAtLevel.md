# CXNetworkCollectNeighborsAtLevel

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:463</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Collects neighbors at exactly the given concentric level (shortest-path hop distance). - `level == 0` refers to the source set itself. - `includeSourceNodes` only affects whether level-0 source nodes are included. - `outEdgeSelector` is optional; pass NULL to skip edge collection.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkCollectNeighborsAtLevel( CXNetworkRef network, const CXIndex *sourceNodes, CXSize sourceCount, CXNeighborDirection direction, CXSize level, CXBool includeSourceNodes, CXNodeSelectorRef outNodeSelector, CXEdgeSelectorRef outEdgeSelector );
```

</div>
