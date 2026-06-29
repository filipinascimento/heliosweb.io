# CXNetworkGenerateStochasticBlockModel

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:401</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Creates a stochastic block model graph from block sizes and a flattened block-to-block probability matrix.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXNetworkRef CXNetworkGenerateStochasticBlockModel( CXSize blockCount, const CXSize *blockSizes, const double *probabilities, CXBool directed, uint32_t seed );
```

</div>
