# CXLeidenSessionFinalize

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:990</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Finalizes a completed session, writing the resulting community ids into a node attribute of type `CXUnsignedIntegerAttributeType` (dimension 1). Returns CXFalse if the session has not completed or on failure.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXLeidenSessionFinalize( CXLeidenSessionRef session, const CXString outNodeCommunityAttribute, double *outModularity, uint32_t *outCommunityCount );
```

</div>
