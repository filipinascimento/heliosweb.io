# CXCorenessSessionGetProgress

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:769</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Returns current progress metrics. Any output pointer may be NULL.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN void CXCorenessSessionGetProgress( CXCorenessSessionRef session, double *outProgressCurrent, double *outProgressTotal, CXCorenessPhase *outPhase, CXSize *outPeeledNodes, CXSize *outActiveNodes, uint32_t *outCurrentCore, uint32_t *outMaxCore );
```

</div>
