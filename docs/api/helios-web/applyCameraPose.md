# applyCameraPose

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/rendering/CameraTransitionController.js:257</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Apply a captured or merged pose to a renderer camera.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function applyCameraPose(camera, pose, { update = true } = {}) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>camera</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Renderer camera to update.</td></tr>
<tr><td class="helios-api-param-name"><code>pose</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Pose fields to apply.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Application options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.update"><span aria-hidden="true">|</span><code>update</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Run the camera update hook after applying values.</td></tr>
<tr><td class="helios-api-param-name"><code>update</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true } = {}</code></td><td class="helios-api-param-description">Value passed to <code>export function applyCameraPose</code>.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Updated camera, or <code>null</code> when no camera is supplied.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>null</code></span></div>
</div>

## Example

<div markdown="1" class="helios-api-template-section">

```js
applyCameraPose(helios.renderer.camera, pose);
```

</div>
