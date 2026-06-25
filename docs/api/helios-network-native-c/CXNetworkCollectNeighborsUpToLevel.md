# CXNetworkCollectNeighborsUpToLevel

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:466</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Collects neighbors up to (and including) the given concentric level. - `maxLevel == 0` returns only the source set when `includeSourceNodes` is true. - `outEdgeSelector` is optional; pass NULL to skip edge collection.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkCollectNeighborsUpToLevel( CXNetworkRef network, const CXIndex *sourceNodes, CXSize sourceCount, CXNeighborDirection direction, CXSize maxLevel, CXBool includeSourceNodes, CXNodeSelectorRef outNodeSelector, CXEdgeSelectorRef outEdgeSelector );
```

</div>
