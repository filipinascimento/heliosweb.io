# CXNetworkMeasureDimension

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:908</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Computes global multiscale dimension statistics over a node set. - If `nodes` is NULL or `nodeCount` is 0, all active nodes are used. - Invalid/inactive node ids in `nodes` are ignored. - Output buffers, when non-null, must each have length `maxLevel + 1`. Returns the number of nodes actually measured.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXSize CXNetworkMeasureDimension( CXNetworkRef network, const CXIndex *nodes, CXSize nodeCount, CXSize maxLevel, CXDimensionDifferenceMethod method, CXSize order, float *outAverageCapacity, float *outGlobalDimension, float *outAverageNodeDimension, float *outNodeDimensionStddev );
```

</div>
