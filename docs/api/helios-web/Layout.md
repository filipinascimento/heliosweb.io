# Layout

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/layouts/Layout.js:34</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Base class for layout algorithms.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class Layout {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Source graph.</td></tr>
<tr><td class="helios-api-param-name"><code>visuals</code></td><td class="helios-api-param-type"><code>import</code>(&#x27;../<code>pipeline</code>/<code>VisualAttributes</code>.<code>js</code>&#x27;).<code>VisualAttributes</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Visual attribute owner used by renderers.</td></tr>
</tbody>
</table>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Concrete implementations override lifecycle hooks to move nodes by
writing into `_helios_visuals_position`.
</div>

## Lifecycle { #api-lifecycle .helios-api-section-title }

<p class="helios-api-section-description">Creation, initialization, prewarming, cleanup, and renderer lifetime.</p>

<a id="method-initialize" class="helios-api-member-anchor"></a>

### `initialize()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:44</code></p>
<p>Configures or reads initialize.</p>
</div>

## Layout And Positions { #api-layout-and-positions .helios-api-section-title }

<p class="helios-api-section-description">Layout selection, position sources, interpolation, and position snapshots. <a href="LayoutBehavior.md">LayoutBehavior</a> handles the built-in layout UI.</p>

<a id="method-ispositionhandoffpending" class="helios-api-member-anchor"></a>

### `isPositionHandoffPending()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:86</code></p>
<p>Returns the current position handoff pending value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.isPositionHandoffPending();
</code></pre>
</div>

<a id="method-beginpositionhandoff" class="helios-api-member-anchor"></a>

### `beginPositionHandoff()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:90</code></p>
<p>Configures or reads begin position handoff.</p>
</div>

<a id="method-completepositionhandoff" class="helios-api-member-anchor"></a>

### `completePositionHandoff(snapshot = null, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:96</code></p>
<p>Configures or reads complete position handoff.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Value passed to <code>completePositionHandoff</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-seedfrompositionsnapshot" class="helios-api-member-anchor"></a>

### `seedFromPositionSnapshot(snapshot, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:105</code></p>
<p>Configures or reads seed from position snapshot.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>snapshot</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>seedFromPositionSnapshot</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-setupdatelistener" class="helios-api-member-anchor"></a>

### `setUpdateListener(listener)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:61</code></p>
<p>Set the update listener setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>listener</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>setUpdateListener</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-getparameterbindings" class="helios-api-member-anchor"></a>

### `getParameterBindings()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:71</code></p>
<p>Returns the current parameter bindings value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getParameterBindings();
</code></pre>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-shouldrun" class="helios-api-member-anchor"></a>

### `shouldRun()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:46</code></p>
<p>Configures or reads should run.</p>
</div>

<a id="method-requestupdate" class="helios-api-member-anchor"></a>

### `requestUpdate()` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:50</code></p>
<p>Configures or reads request update.</p>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-step" class="helios-api-member-anchor"></a>

### `step()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:54</code></p>
<p>Configures or reads step.</p>
</div>

<a id="method-resize" class="helios-api-member-anchor"></a>

### `resize()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:59</code></p>
<p>Configures or reads resize.</p>
</div>

<a id="method-emitupdate" class="helios-api-member-anchor"></a>

### `emitUpdate(payload)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:65</code></p>
<p>Configures or reads emit update.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>payload</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>emitUpdate</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-reheat" class="helios-api-member-anchor"></a>

### `reheat(reason = 'layout')`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:80</code></p>
<p>Configures or reads reheat.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;layout&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-dispose" class="helios-api-member-anchor"></a>

### `dispose()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/Layout.js:148</code></p>
<p>Configures or reads dispose.</p>
</div>
