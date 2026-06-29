# CXNetworkWriteActiveEdgeNodeAttributes

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:344</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Writes `componentsPerNode` values for each endpoint of active edges from the provided node attribute buffer into a caller-managed destination. Values are copied verbatim; the caller controls element width (`componentSizeBytes`) and must ensure the typed views line up with the provided byte offsets. Returns the number of edges that would be written; when `dstCapacityEdges` is too small, the required count is returned and no writes occur.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXSize CXNetworkWriteActiveEdgeNodeAttributes( CXNetworkRef network, const uint8_t *nodeAttributes, CXSize componentsPerNode, CXSize componentSizeBytes, uint8_t *dst, CXSize dstCapacityEdges );
```

</div>
