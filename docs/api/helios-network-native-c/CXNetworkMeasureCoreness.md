# CXNetworkMeasureCoreness

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:745</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Measures node coreness (k-core index) for all node capacity indices. - Uses iterative peeling over the chosen degree policy (`direction`). - For directed graphs: - `Out` uses outgoing degree. - `In` uses incoming degree. - `Both` uses incoming + outgoing degree. - For undirected graphs, direction is normalized to undirected degree. Output buffer length must be at least `CXNetworkNodeCapacity(network)`. Inactive nodes receive coreness 0.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkMeasureCoreness( CXNetworkRef network, CXNeighborDirection direction, CXMeasurementExecutionMode executionMode, uint32_t *outNodeCoreness, uint32_t *outMaxCore );
```

</div>
