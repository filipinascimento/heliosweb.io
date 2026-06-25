# captureCameraPose

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/rendering/CameraTransitionController.js:171</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Capture a renderer camera into a serializable pose object.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function captureCameraPose(camera) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>camera</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Camera object owned by the active renderer.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Pose snapshot, or <code>null</code> when no camera is supplied.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code></span></div>
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
const pose = captureCameraPose(helios.renderer.camera);
```

</div>
