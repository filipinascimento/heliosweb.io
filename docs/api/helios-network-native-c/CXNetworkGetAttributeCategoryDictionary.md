# CXNetworkGetAttributeCategoryDictionary

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:512</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Returns the category dictionary for a categorical attribute, or NULL when unavailable.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXStringDictionaryRef CXNetworkGetAttributeCategoryDictionary(CXNetworkRef network, CXAttributeScope scope, const CXString name);
```

</div>
