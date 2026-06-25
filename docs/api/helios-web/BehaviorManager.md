# BehaviorManager

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/behaviors/BehaviorManager.js:17</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Runtime owner for active behavior instances on a Helios visualization.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class BehaviorManager {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>helios</code></td><td class="helios-api-param-type"><code>import</code>(&#x27;../<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a>.<code>js</code>&#x27;).<a href="/docs/api/helios-web/Helios/"><code>Helios</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Visualization controller that behaviors will attach to.</td></tr>
<tr><td class="helios-api-param-name"><code>registry</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-web/BehaviorRegistry/"><code>BehaviorRegistry</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Registry used to instantiate named behaviors.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Manager with no active behaviors attached.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/BehaviorManager/"><code>BehaviorManager</code></a></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
The manager creates, attaches, detaches, serializes, and restores
behavior instances against a shared Helios context. Use the higher-level
`helios.behavior` namespace for most app code.
</div>

## Lifecycle { #api-lifecycle .helios-api-section-title }

<p class="helios-api-section-description">Creation, initialization, prewarming, cleanup, and renderer lifetime.</p>

<a id="method-destroy" class="helios-api-member-anchor"></a>

### `destroy()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorManager.js:92</code></p>
<p>Manages destroy for the current instance.</p>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-serialize" class="helios-api-member-anchor"></a>

### `serialize()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorManager.js:98</code></p>
<p>Handles serialize for the current graph or visualization state.</p>
</div>

<a id="method-restore" class="helios-api-member-anchor"></a>

### `restore(snapshot = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorManager.js:107</code></p>
<p>Updates the restore state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>restore</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-setui" class="helios-api-member-anchor"></a>

### `setUI(ui)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorManager.js:26</code></p>
<p>Set the ui setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>ui</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setUI</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-get" class="helios-api-member-anchor"></a>

### `get(id)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorManager.js:35</code></p>
<p>Returns the current get value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>get</code>.</td></tr>
</tbody>
</table>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-has" class="helios-api-member-anchor"></a>

### `has(id)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorManager.js:31</code></p>
<p>Returns the current has value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>has</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-entries" class="helios-api-member-anchor"></a>

### `entries()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorManager.js:39</code></p>
<p>Configures or reads entries.</p>
</div>

<a id="method-values" class="helios-api-member-anchor"></a>

### `values()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorManager.js:43</code></p>
<p>Configures or reads values.</p>
</div>

<a id="method-use" class="helios-api-member-anchor"></a>

### `use(idOrBehavior, options = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorManager.js:47</code></p>
<p>Manages use for the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>idOrBehavior</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>use</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-detach" class="helios-api-member-anchor"></a>

### `detach(id)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorManager.js:68</code></p>
<p>Manages detach for the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>detach</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-detachall" class="helios-api-member-anchor"></a>

### `detachAll()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorManager.js:79</code></p>
<p>Manages all for the current instance.</p>
</div>
