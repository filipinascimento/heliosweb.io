# CXNetworkMeasureBetweennessCentrality

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:724</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Runs Brandes betweenness centrality (weighted when an edge weight attribute is provided, unweighted otherwise). - `sourceNodes` can restrict the set of source nodes used by the algorithm. When NULL/empty, all active nodes are used. - Set `accumulate` to CXTrue to add into `inOutNodeBetweenness` instead of clearing it first (useful for chunked stepping). - Output buffer length must be at least `CXNetworkNodeCapacity(network)`. Returns the number of source nodes actually processed.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXSize CXNetworkMeasureBetweennessCentrality( CXNetworkRef network, const CXString edgeWeightAttribute, CXMeasurementExecutionMode executionMode, const CXIndex *sourceNodes, CXSize sourceCount, CXBool normalize, CXBool accumulate, float *inOutNodeBetweenness );
```

</div>
