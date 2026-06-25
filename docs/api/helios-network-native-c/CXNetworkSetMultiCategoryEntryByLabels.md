# CXNetworkSetMultiCategoryEntryByLabels

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:548</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Writes one entry of a multi-category attribute using category labels.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkSetMultiCategoryEntryByLabels( CXNetworkRef network, CXAttributeScope scope, const CXString name, CXIndex index, const CXString *labels, CXSize count, const float *weights );
```

</div>
