# CXNetworkGenerateWattsStrogatz

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:392</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Creates a Watts-Strogatz small-world graph.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXNetworkRef CXNetworkGenerateWattsStrogatz(CXSize nodeCount, CXSize neighborLevel, double rewiringProbability, CXBool directed, uint32_t seed);
```

</div>
