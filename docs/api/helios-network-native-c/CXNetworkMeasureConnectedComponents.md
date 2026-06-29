# CXNetworkMeasureConnectedComponents

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:816</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Measures connected components. - Weak mode treats directed edges as undirected (weakly-connected components). - Strong mode computes strongly-connected components on directed graphs. Undirected graphs behave like weak mode. Component ids are written into `outNodeComponent` (length must be at least `CXNetworkNodeCapacity(network)`). Inactive nodes receive id `0`. Returns the number of detected components.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXSize CXNetworkMeasureConnectedComponents( CXNetworkRef network, CXConnectedComponentsMode mode, uint32_t *outNodeComponent, uint32_t *outLargestComponentSize );
```

</div>
