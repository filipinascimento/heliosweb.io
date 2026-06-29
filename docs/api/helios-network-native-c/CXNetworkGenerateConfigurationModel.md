# CXNetworkGenerateConfigurationModel

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:421</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Creates a graph with the requested degree sequence using the configuration model.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXNetworkRef CXNetworkGenerateConfigurationModel( CXSize nodeCount, const CXSize *degrees, CXBool directed, CXBool allowSelfLoops, CXBool allowMultiEdges, uint32_t seed );
```

</div>
