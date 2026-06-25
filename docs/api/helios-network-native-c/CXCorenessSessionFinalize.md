# CXCorenessSessionFinalize

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:779</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Finalizes a completed session, copying per-node coreness values into `outNodeCoreness` (length >= nodeCapacity).
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXCorenessSessionFinalize( CXCorenessSessionRef session, uint32_t *outNodeCoreness, CXSize outNodeCorenessCount, uint32_t *outMaxCore );
```

</div>
