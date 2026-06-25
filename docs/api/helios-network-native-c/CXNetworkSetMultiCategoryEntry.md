# CXNetworkSetMultiCategoryEntry

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:538</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Writes one entry of a multi-category attribute using category ids.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkSetMultiCategoryEntry( CXNetworkRef network, CXAttributeScope scope, const CXString name, CXIndex index, const uint32_t *ids, CXSize count, const float *weights );
```

</div>
