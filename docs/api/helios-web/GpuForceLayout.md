# GpuForceLayout

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/layouts/GpuForceLayout.js:263</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
GPU-backed force layout that can run through WebGPU or WebGL2 delegates.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class GpuForceLayout extends Layout {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Source graph.</td></tr>
<tr><td class="helios-api-param-name"><code>visuals</code></td><td class="helios-api-param-type"><code>import</code>(&#x27;../<code>pipeline</code>/<code>VisualAttributes</code>.<code>js</code>&#x27;).<code>VisualAttributes</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Visual attribute owner.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Force, UMAP-like force, sampling, damping, recentering, and renderer delegate options.</td></tr>
</tbody>
</table>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Renderer support and graph size determine whether WebGPU or WebGL2
backing is selected. Position output is written into Helios visual position
buffers for rendering.
</div>

## Lifecycle { #api-lifecycle .helios-api-section-title }

<p class="helios-api-section-description">Creation, initialization, prewarming, cleanup, and renderer lifetime.</p>

<a id="method-initialize" class="helios-api-member-anchor"></a>

### `initialize()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/GpuForceLayout.js:301</code></p>
<p>Configures or reads initialize.</p>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-syncautosettingsfornetwork" class="helios-api-member-anchor"></a>

### `syncAutoSettingsForNetwork(network = this.network, { reheat = false, reason = 'layout-auto-tune' } = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/GpuForceLayout.js:349</code></p>
<p>Configures or reads sync auto settings for network.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>network</code></td><td class="helios-api-param-type"><a href="/docs/api/helios-network-js-wasm/HeliosNetwork/"><code>HeliosNetwork</code></a></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>this.network</code></td><td class="helios-api-param-description">Network instance to read from or mutate.</td></tr>
<tr><td class="helios-api-param-name"><code>reheat</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false</code></td><td class="helios-api-param-description">Value passed to <code>syncAutoSettingsForNetwork</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;layout-auto-tune&#x27; } = {}</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-seedfromnetworkpositions" class="helios-api-member-anchor"></a>

### `seedFromNetworkPositions(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/GpuForceLayout.js:443</code></p>
<p>Read or set the seed from network positions setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current seed from network positions value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.seedFromNetworkPositions({
  enabled: true,
});
</code></pre>
</div>

## Layout And Positions { #api-layout-and-positions .helios-api-section-title }

<p class="helios-api-section-description">Layout selection, position sources, interpolation, and position snapshots. <a href="LayoutBehavior.md">LayoutBehavior</a> handles the built-in layout UI.</p>

<a id="method-getpositiondelegate" class="helios-api-member-anchor"></a>

### `getPositionDelegate()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/GpuForceLayout.js:297</code></p>
<p>Returns the current position delegate value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getPositionDelegate();
</code></pre>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-setsettings" class="helios-api-member-anchor"></a>

### `setSettings(next = {}, { reheat = false, reason = 'layout-settings' } = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/GpuForceLayout.js:388</code></p>
<p>Set the settings setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>next</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>setSettings</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>reheat</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>false</code></td><td class="helios-api-param-description">Value passed to <code>setSettings</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;layout-settings&#x27; } = {}</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-getparameterbindings" class="helios-api-member-anchor"></a>

### `getParameterBindings()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/GpuForceLayout.js:454</code></p>
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

<p class="helios-api-source">Source: <code>src/layouts/GpuForceLayout.js:305</code></p>
<p>Configures or reads should run.</p>
</div>

<a id="method-step" class="helios-api-member-anchor"></a>

### `step(deltaMs = 16)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/GpuForceLayout.js:309</code></p>
<p>Configures or reads step.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>deltaMs</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>16</code></td><td class="helios-api-param-description">Value passed to <code>step</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-resize" class="helios-api-member-anchor"></a>

### `resize(size)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/GpuForceLayout.js:330</code></p>
<p>Configures or reads resize.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>size</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>resize</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-reheat" class="helios-api-member-anchor"></a>

### `reheat(reason = 'layout')`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/layouts/GpuForceLayout.js:437</code></p>
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

<p class="helios-api-source">Source: <code>src/layouts/GpuForceLayout.js:807</code></p>
<p>Configures or reads dispose.</p>
</div>
