# CXNetworkLeidenModularity

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:933</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Runs Leiden community detection optimizing (weighted) modularity. - For undirected graphs, uses the standard modularity objective. - For directed graphs, uses the directed modularity formulation. - `resolution` corresponds to the modularity resolution parameter (gamma). - When `edgeWeightAttribute` is NULL/empty, every edge has weight 1. Writes the resulting community id into a node attribute (created when missing) of type `CXUnsignedIntegerAttributeType` and dimension 1. Returns the number of detected communities, or 0 on failure.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXSize CXNetworkLeidenModularity( CXNetworkRef network, const CXString edgeWeightAttribute, double resolution, uint32_t seed, CXSize maxLevels, CXSize maxPasses, const CXString outNodeCommunityAttribute, double *outModularity );
```

</div>
