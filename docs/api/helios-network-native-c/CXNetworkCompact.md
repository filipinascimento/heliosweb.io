# CXNetworkCompact

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:636</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Compacts the network so that node and edge indices become contiguous starting at zero and capacities shrink to match the number of active elements. When `nodeOriginalIndexAttr` or `edgeOriginalIndexAttr` are provided, the function records the previous indices in attributes of type `CXUnsignedIntegerAttributeType`. Returns CXFalse on allocation failure or when incompatible attributes are encountered.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkCompact( CXNetworkRef network, const CXString nodeOriginalIndexAttr, const CXString edgeOriginalIndexAttr );
```

</div>
