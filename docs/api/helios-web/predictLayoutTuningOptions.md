# predictLayoutTuningOptions

<div class="helios-api-kind">function</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>function</dd>
<dt>Source</dt>
<dd>src/layouts/layoutTuningModel.generated.js:199</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Predict layout option overrides for a network using the layout tuning model.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export function predictLayoutTuningOptions(network, {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Helios network or network-like object.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Prediction options.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.model"><span aria-hidden="true">|</span><code>model</code></span></td><td class="helios-api-param-type"><code>Object</code>|<code>Function</code>|<code>false</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Model descriptor, custom predictor, or false to disable.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.baseOptions"><span aria-hidden="true">|</span><code>baseOptions</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Base layout options multiplied by model outputs.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.hints"><span aria-hidden="true">|</span><code>hints</code></span></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Optional feature overrides.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Predicted layout options.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code></span></div>
</div>
