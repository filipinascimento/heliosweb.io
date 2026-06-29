# CXNetworkGenerateBarabasiAlbert

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:403</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Creates a Barabasi-Albert preferential-attachment graph.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXNetworkRef CXNetworkGenerateBarabasiAlbert(CXSize nodeCount, CXSize edgesPerNewNode, CXSize initialCliqueSize, CXBool directed, uint32_t seed);
```

</div>
