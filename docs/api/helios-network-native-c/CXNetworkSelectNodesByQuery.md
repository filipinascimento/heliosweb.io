# CXNetworkSelectNodesByQuery

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:213</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Evaluates a query string against the network, populating the provided selector. Returns CXFalse on parse or evaluation errors. Use CXNetworkQueryLastError* to retrieve details about the last failure.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXNetworkSelectNodesByQuery(CXNetworkRef network, const CXString query, CXNodeSelectorRef selector);
```

</div>
