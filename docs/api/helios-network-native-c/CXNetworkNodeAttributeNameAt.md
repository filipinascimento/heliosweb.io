# CXNetworkNodeAttributeNameAt

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:505</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Returns the node attribute name at `index` in the internal dictionary iteration order, or NULL when out of range.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN const CXString CXNetworkNodeAttributeNameAt(CXNetworkRef network, CXSize index);
```

</div>
