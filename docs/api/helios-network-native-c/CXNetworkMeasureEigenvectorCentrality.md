# CXNetworkMeasureEigenvectorCentrality

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:688</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Runs power-iteration eigenvector centrality. - `initialNodeCentrality`, when non-null, must have one value per node capacity index and is used as the initial vector. - `outNodeCentrality` must have one value per node capacity index. - `executionMode` allows callers to force single-thread or parallel mode.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkMeasureEigenvectorCentrality( CXNetworkRef network, const CXString edgeWeightAttribute, CXNeighborDirection direction, CXMeasurementExecutionMode executionMode, CXSize maxIterations, double tolerance, const float *initialNodeCentrality, float *outNodeCentrality, double *outEigenvalue, double *outDelta, CXSize *outIterations, CXBool *outConverged );
```

</div>
