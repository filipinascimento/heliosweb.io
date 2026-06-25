# CXEdgeSelectorFilterByNodes

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:1067</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Keeps only active edges whose endpoints are both present in `nodeSelector`.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXEdgeSelectorFilterByNodes(CXEdgeSelectorRef selector, CXNetworkRef network, CXNodeSelectorRef nodeSelector);
```

</div>
