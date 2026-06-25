# UIAttribute

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/ui/state/UIAttribute.js:26</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Observable UI attribute descriptor used to bind controls to Helios state.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class UIAttribute {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute descriptor.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.id"><span aria-hidden="true">|</span><code>id</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Stable attribute id.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.get"><span aria-hidden="true">|</span><code>get</code></span></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Read callback.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.set"><span aria-hidden="true">|</span><code>set</code></span></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Write callback.</td></tr>
</tbody>
</table>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-value" class="helios-api-member-anchor"></a>

### `value()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/state/UIAttribute.js:49</code></p>
<p>Configures or reads value.</p>
</div>

<a id="method-write" class="helios-api-member-anchor"></a>

### `write(value, context)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/state/UIAttribute.js:53</code></p>
<p>Configures or reads write.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New write value. Omit this argument to read the current value.</td></tr>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>write</code>.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.write(1);
</code></pre>
</div>

<a id="method-notify" class="helios-api-member-anchor"></a>

### `notify()` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/state/UIAttribute.js:59</code></p>
<p>Configures or reads notify.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-subscribe" class="helios-api-member-anchor"></a>

### `subscribe(listener, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/ui/state/UIAttribute.js:69</code></p>
<p>Configures or reads subscribe.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>listener</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>subscribe</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>
