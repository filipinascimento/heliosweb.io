# StaticLayout

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/layouts/Layout.js:164</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Layout that keeps existing node positions fixed.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class StaticLayout extends Layout {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Source graph.</td></tr>
<tr><td class="helios-api-param-name"><code>visuals</code></td><td class="helios-api-param-type"><code>import</code>(&#x27;../<code>pipeline</code>/<code>VisualAttributes</code>.<code>js</code>&#x27;).<code>VisualAttributes</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Visual attribute owner.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Static bounds and sizing options.</td></tr>
</tbody>
</table>
</div>

## Lifecycle { #api-lifecycle .helios-api-section-title }

<p class="helios-api-section-description">Creation, initialization, prewarming, cleanup, and renderer lifetime.</p>

<a id="method-initialize" class="helios-api-member-anchor"></a>

### `initialize()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:170</code></p>
<p>Configures or reads initialize.</p>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-getparameterbindings" class="helios-api-member-anchor"></a>

### `getParameterBindings()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:200</code></p>
<p>Returns the current parameter bindings value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getParameterBindings();
</code></pre>
</div>
