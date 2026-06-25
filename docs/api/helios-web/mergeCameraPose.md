# mergeCameraPose

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/rendering/CameraTransitionController.js:203</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Merge a partial camera pose into an existing pose.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function mergeCameraPose(basePose, patch = {}) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>basePose</code></td><td class="helios-api-param-type"><code>Object</code>|<code>null</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Existing pose to use as defaults.</td></tr>
<tr><td class="helios-api-param-name"><code>patch</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Pose fields to replace.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Normalized camera pose.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
const next = mergeCameraPose(currentPose, { zoom: 2 });
```

</div>
