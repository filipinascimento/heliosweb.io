# CXAttributeInterpolateFloatBuffer

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/native/include/helios/CXNetwork.h:609</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Interpolates a float attribute buffer toward target values and bumps the attribute version. Returns CXTrue when further interpolation steps are recommended based on minDisplacementRatio.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
CX_EXTERN CXBool CXAttributeInterpolateFloatBuffer( CXAttributeRef attribute, const float *target, CXSize targetCount, float elapsedMs, float layoutElapsedMs, float smoothing, float minDisplacementRatio );
```

</div>
