# CXNetworkSetAttributeCategoryDictionary

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:533</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Replaces or remaps the category dictionary for a categorical attribute.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkSetAttributeCategoryDictionary( CXNetworkRef network, CXAttributeScope scope, const CXString name, const CXString *labels, const int32_t *ids, CXSize count, CXBool remapExisting );
```

</div>
