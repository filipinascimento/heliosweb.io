# CXNetworkGenerateWaxman

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:396</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Creates a Waxman random graph using distance-weighted edge probabilities.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXNetworkRef CXNetworkGenerateWaxman(CXSize nodeCount, double alpha, double beta, CXBool directed, uint32_t seed);
```

</div>
