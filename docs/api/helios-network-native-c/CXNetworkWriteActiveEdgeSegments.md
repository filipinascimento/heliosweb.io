# CXNetworkWriteActiveEdgeSegments

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:327</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Writes two position vectors per active edge directly into the provided buffer. `componentsPerNode` describes how many floats to copy per endpoint (commonly 4 for vec4 data). Returns the number of edges that would be written; when `dstCapacityEdges` is too small, the required count is returned and no writes occur.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXSize CXNetworkWriteActiveEdgeSegments( CXNetworkRef network, const float *positions, CXSize componentsPerNode, float *dstSegments, CXSize dstCapacityEdges );
```

</div>
