# createYawPitchQuaternion

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/rendering/CameraTransitionController.js:153</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Build a normalized camera rotation quaternion from yaw and pitch angles.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function createYawPitchQuaternion(yawRadians = 0, pitchRadians = 0) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>yawRadians</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>0</code></td><td class="helios-api-param-description">Horizontal rotation in radians.</td></tr>
<tr><td class="helios-api-param-name"><code>pitchRadians</code></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>0</code></td><td class="helios-api-param-description">Vertical rotation in radians.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Quaternion in <code>[x, y, z, w]</code> order.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Float32Array</code></span></div>
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
const rotation = createYawPitchQuaternion(Math.PI / 4, 0);
```

</div>
