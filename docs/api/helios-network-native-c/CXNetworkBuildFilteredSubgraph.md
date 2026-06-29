# CXNetworkBuildFilteredSubgraph

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:1044</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Builds an induced filtered subgraph from optional node/edge filters. - `nodeFilter` / `edgeFilter` may be NULL to indicate "all active". - Node output is always active-only. - Edge output is always active-only and induced by the resulting node set (edges with at least one endpoint outside `outNodeSelector` are removed). - Output order follows native active index order.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkBuildFilteredSubgraph( CXNetworkRef network, CXNodeSelectorRef nodeFilter, CXEdgeSelectorRef edgeFilter, CXSize minComponentSize, CXNodeSelectorRef outNodeSelector, CXEdgeSelectorRef outEdgeSelector );
```

</div>
