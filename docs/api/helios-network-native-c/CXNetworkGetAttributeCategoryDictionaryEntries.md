# CXNetworkGetAttributeCategoryDictionaryEntries

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:523</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Copies category ids and labels into caller-provided arrays.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkGetAttributeCategoryDictionaryEntries( CXNetworkRef network, CXAttributeScope scope, const CXString name, int32_t *outIds, CXString *outLabels, CXSize capacity );
```

</div>
