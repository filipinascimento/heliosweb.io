# CXLeidenSessionStep

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:971</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Advances the session by at most `budget` node-visits (best effort). Returns the current phase after stepping.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXLeidenPhase CXLeidenSessionStep(CXLeidenSessionRef session, CXSize budget);
```

</div>
