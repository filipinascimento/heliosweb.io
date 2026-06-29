# CXLeidenSessionGetProgress

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
Returns current progress metrics. Any output pointer may be NULL. `outProgressCurrent` and `outProgressTotal` are best-effort and may change as the algorithm advances (i.e. the total may be revised).
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN void CXLeidenSessionGetProgress( CXLeidenSessionRef session, double *outProgressCurrent, double *outProgressTotal, CXLeidenPhase *outPhase, CXSize *outLevel, CXSize *outMaxLevels, CXSize *outPass, CXSize *outMaxPasses, CXSize *outVisitedThisPass, CXSize *outNodeCount, uint32_t *outCommunityCount );
```

</div>
