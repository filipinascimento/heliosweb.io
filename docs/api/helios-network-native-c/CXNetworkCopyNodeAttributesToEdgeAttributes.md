# CXNetworkCopyNodeAttributesToEdgeAttributes

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:347</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Copies node attributes into an edge attribute buffer using the network's topology. `endpointMode` controls which endpoint is copied: -1 = both, 0 = source only, 1 = destination only. When copying a single endpoint and `duplicateSingleEndpoint` is true, the chosen endpoint is written twice sequentially (for double-width edge attributes).
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXSize CXNetworkCopyNodeAttributesToEdgeAttributes( CXNetworkRef network, const uint8_t *nodeAttributes, CXSize nodeStrideBytes, uint8_t *edgeAttributes, CXSize edgeStrideBytes, int endpointMode, CXBool duplicateSingleEndpoint );
```

</div>
