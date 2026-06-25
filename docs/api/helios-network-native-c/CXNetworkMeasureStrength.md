# CXNetworkMeasureStrength

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:649</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Measures node strength from an edge weight attribute (or unit weights when `edgeWeightAttribute` is NULL/empty). Output buffer length must be at least `CXNetworkNodeCapacity(network)`.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkMeasureStrength( CXNetworkRef network, const CXString edgeWeightAttribute, CXNeighborDirection direction, CXStrengthMeasure measure, float *outNodeStrength );
```

</div>
