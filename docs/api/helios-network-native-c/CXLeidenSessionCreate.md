# CXLeidenSessionCreate

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:949</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Creates a steppable Leiden session. The network topology and relevant edge weight attribute must not change while the session is active. Returns NULL on failure.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXLeidenSessionRef CXLeidenSessionCreate( CXNetworkRef network, const CXString edgeWeightAttribute, double resolution, uint32_t seed, CXSize maxLevels, CXSize maxPasses );
```

</div>
