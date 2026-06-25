# D3Force3DLayout

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/layouts/d3force3dLayoutWorker.js:99</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Worker-backed layout adapter for the D3 Force 3D engine.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class D3Force3DLayout extends Layout {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Source graph.</td></tr>
<tr><td class="helios-api-param-name"><code>visuals</code></td><td class="helios-api-param-type"><code>import</code>(&#x27;../<code>pipeline</code>/<code>VisualAttributes</code>.<code>js</code>&#x27;).<code>VisualAttributes</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Visual attribute owner.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">D3 force settings and worker options.</td></tr>
</tbody>
</table>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Use this when CPU worker force layout behavior is preferred over
GPU force layout, especially for compatibility testing.
</div>

## Lifecycle { #api-lifecycle .helios-api-section-title }

<p class="helios-api-section-description">Creation, initialization, prewarming, cleanup, and renderer lifetime.</p>

<a id="method-initialize" class="helios-api-member-anchor"></a>

### `initialize()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:165</code></p>
<p>Configures or reads initialize.</p>
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-adopthandoffstate" class="helios-api-member-anchor"></a>

### `adoptHandoffState(state = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:382</code></p>
<p>Configures or reads adopt handoff state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>state</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>adoptHandoffState</code>.</td></tr>
</tbody>
</table>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-seedfromnetworkpositions" class="helios-api-member-anchor"></a>

### `seedFromNetworkPositions()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:364</code></p>
<p>Configures or reads seed from network positions.</p>
</div>

## Layout And Positions { #api-layout-and-positions .helios-api-section-title }

<p class="helios-api-section-description">Layout selection, position sources, interpolation, and position snapshots. <a href="LayoutBehavior.md">LayoutBehavior</a> handles the built-in layout UI.</p>

<a id="method-completepositionhandoff" class="helios-api-member-anchor"></a>

### `completePositionHandoff(snapshot = null, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:373</code></p>
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

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-setsettings" class="helios-api-member-anchor"></a>

### `setSettings(next = {}, { reheat = false } = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:304</code></p>
<p>Set the settings setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>next</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>setSettings</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>reheat</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false } = {}</code></td><td class="helios-api-param-description">Value passed to <code>setSettings</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-getparameterbindings" class="helios-api-member-anchor"></a>

### `getParameterBindings()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:408</code></p>
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

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:178</code></p>
<p>Configures or reads should run.</p>
</div>

<a id="method-step" class="helios-api-member-anchor"></a>

### `step()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:182</code></p>
<p>Configures or reads step.</p>
</div>

<a id="method-handlemessage" class="helios-api-member-anchor"></a>

### `handleMessage(message)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:225</code></p>
<p>Configures or reads handle message.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>message</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>handleMessage</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-dispose" class="helios-api-member-anchor"></a>

### `dispose()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:271</code></p>
<p>Configures or reads dispose.</p>
</div>

<a id="method-reheat" class="helios-api-member-anchor"></a>

### `reheat(reason = 'layout')`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:357</code></p>
<p>Configures or reads reheat.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;layout&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-buildgraphpayload" class="helios-api-member-anchor"></a>

### `buildGraphPayload()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/d3force3dLayoutWorker.js:572</code></p>
<p>Configures or reads build graph payload.</p>
</div>
