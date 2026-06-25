# CXNetworkMeasureLocalClusteringCoefficient

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:665</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Measures local clustering coefficients for all node indices. - `variant` selects the unweighted or weighted formulation. - Weighted variants read `edgeWeightAttribute` (unit weights when omitted). Output buffer length must be at least `CXNetworkNodeCapacity(network)`.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkMeasureLocalClusteringCoefficient( CXNetworkRef network, const CXString edgeWeightAttribute, CXNeighborDirection direction, CXClusteringCoefficientVariant variant, float *outNodeCoefficient );
```

</div>
