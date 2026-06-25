# CXNetworkAddEdges

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:367</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Inserts the provided edges, writing the new indices to `outIndices` when supplied. Edges are expressed as contiguous (from,to) pairs.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkAddEdges(CXNetworkRef network, const CXEdge *edges, CXSize count, CXIndex *outIndices);
```

</div>
