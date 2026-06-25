# CameraTransitionController

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/rendering/CameraTransitionController.js:346</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Time-based camera transition controller used by Helios camera animations.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class CameraTransitionController {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Controller dependencies.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.camera"><span aria-hidden="true">|</span><code>camera</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Renderer camera to animate.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.requestRender"><span aria-hidden="true">|</span><code>requestRender</code></span></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Callback used to schedule a render.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.now"><span aria-hidden="true">|</span><code>now</code></span></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Clock function returning milliseconds.</td></tr>
<tr><td class="helios-api-param-name"><code>requestRender</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null } = {}</code></td><td class="helios-api-param-description">Value passed to <code>constructor</code>.</td></tr>
</tbody>
</table>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-stop" class="helios-api-member-anchor"></a>

### `stop()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/rendering/CameraTransitionController.js:353</code></p>
<p>Configures or reads stop.</p>
</div>

<a id="method-transition" class="helios-api-member-anchor"></a>

### `transition(camera, { fromPose, toPose, durationMs = 320 } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/rendering/CameraTransitionController.js:365</code></p>
<p>Configures or reads transition.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>camera</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>transition</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>fromPose</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Camera pose fields to apply.</td></tr>
<tr><td class="helios-api-param-name"><code>toPose</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Camera pose fields to apply.</td></tr>
<tr><td class="helios-api-param-name"><code>durationMs</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>320 } = {}</code></td><td class="helios-api-param-description">Value passed to <code>transition</code>.</td></tr>
</tbody>
</table>
</div>
