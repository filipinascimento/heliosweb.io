# StateBindingController

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/state/HeliosStateManager.js:831</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Binding controller that keeps registered state entries synchronized with runtime owners.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class StateBindingController {
```

</div>

## Lifecycle { #api-lifecycle .helios-api-section-title }

<p class="helios-api-section-description">Creation, initialization, prewarming, cleanup, and renderer lifetime.</p>

<a id="method-destroy" class="helios-api-member-anchor"></a>

### `destroy()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/state/HeliosStateManager.js:921</code></p>
<p>Manages destroy for the current instance.</p>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-bind" class="helios-api-member-anchor"></a>

### `bind(key, entry, owner = null)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/state/HeliosStateManager.js:839</code></p>
<p>Configures or reads bind.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>key</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>bind</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>entry</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>bind</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>owner</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Value passed to <code>bind</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-apply" class="helios-api-member-anchor"></a>

### `apply(key, value, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/state/HeliosStateManager.js:897</code></p>
<p>Updates the apply state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>key</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>apply</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New apply value. Omit this argument to read the current value.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-unbind" class="helios-api-member-anchor"></a>

### `unbind(key)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/state/HeliosStateManager.js:914</code></p>
<p>Configures or reads unbind.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>key</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>unbind</code>.</td></tr>
</tbody>
</table>
</div>
