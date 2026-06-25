# withBufferAccess

<div class="helios-api-kind">method</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network JS/WASM API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>method</dd>
<dt>Source</dt>
<dd>src/js/HeliosNetwork.js:3894</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Runs a callback inside a buffer access session, ensuring cleanup even on throw.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
withBufferAccess(fn, options = null) {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>fn</code></td><td class="helios-api-param-type"><code>function</code>(): <code>T</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Callback to execute.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Callback result.</p><span class="helios-api-return-type"><strong>Type</strong> <code>T</code></span></div>
</div>
