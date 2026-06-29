# CXNetworkMeasureNodeDimension

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:886</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Computes local multiscale capacity and dimension for a single node. - `maxLevel` controls the largest geodesic radius r evaluated. - `method` and `order` select the derivative estimator (FW/BK/CE/LS). - `outCapacity` and `outDimension`, when non-null, must point to buffers of length `maxLevel + 1`. Returns CXFalse when the node is invalid/inactive or on allocation failure.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkMeasureNodeDimension( CXNetworkRef network, CXIndex node, CXSize maxLevel, CXDimensionDifferenceMethod method, CXSize order, uint32_t *outCapacity, float *outDimension );
```

</div>
