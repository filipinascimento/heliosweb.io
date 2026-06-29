# LayoutBehavior

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/behaviors/LayoutBehavior.js:338</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Built-in behavior for choosing and controlling the active layout.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class LayoutBehavior extends Behavior {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Layout options such as <code>layoutType</code>, <code>positionAttribute</code>, low-level <code>parameters</code>, and <code>running</code> state.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Behavior wrapping static, worker, D3 force, and GPU force layouts.</p><span class="helios-api-return-type"><strong>Type</strong> <code>LayoutBehavior</code></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Use this behavior when UI or persistence needs to switch layouts,
copy numeric position attributes into current positions, or start/stop a
dynamic layout without replacing the Helios instance.
</div>

## Instance Properties { #api-instance-properties .helios-api-section-title }

<a id="property-id" class="helios-api-member-anchor"></a>

### `id`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:339</code></p>
<p>Id exposed by the class.</p>
</div>

## Filtering And State { #api-filtering-and-state .helios-api-section-title }

<p class="helios-api-section-description">Graph filtering and interaction state. When active, <a href="FilterBehavior.md">FilterBehavior</a> and <a href="SelectionBehavior.md">SelectionBehavior</a> coordinate this area.</p>

<a id="method-refreshparameterstateentries" class="helios-api-member-anchor"></a>

### `refreshParameterStateEntries()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:508</code></p>
<p>Configures or reads refresh parameter state entries.</p>
</div>

<a id="method-refreshpauseoninteractionstateentry" class="helios-api-member-anchor"></a>

### `refreshPauseOnInteractionStateEntry()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:518</code></p>
<p>Configures or reads refresh pause on interaction state entry.</p>
</div>

<a id="method-getpublicstate" class="helios-api-member-anchor"></a>

### `getPublicState()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:577</code></p>
<p>Returns the current public state value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.getPublicState();
</code></pre>
</div>

<a id="method-runstate" class="helios-api-member-anchor"></a>

### `runState()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:610</code></p>
<p>Configures or reads run state.</p>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-attach" class="helios-api-member-anchor"></a>

### `attach(context)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:357</code></p>
<p>Configures or reads attach.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>context</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>attach</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-serialize" class="helios-api-member-anchor"></a>

### `serialize()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:418</code></p>
<p>Handles serialize for the current graph or visualization state.</p>
</div>

<a id="method-restore" class="helios-api-member-anchor"></a>

### `restore(snapshot = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:527</code></p>
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

## Layout And Positions { #api-layout-and-positions .helios-api-section-title }

<p class="helios-api-section-description">Layout selection, position sources, interpolation, and position snapshots. <a href="LayoutBehavior.md">LayoutBehavior</a> handles the built-in layout UI.</p>

<a id="method-applypositionattribute" class="helios-api-member-anchor"></a>

### `applyPositionAttribute(value = this.state.positionAttribute, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:849</code></p>
<p>Updates the position attribute state on the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>this.state.positionAttribute</code></td><td class="helios-api-param-description">New apply position attribute value. Omit this argument to read the current value.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.applyPositionAttribute(1);
</code></pre>
</div>

## Configuration { #api-configuration .helios-api-section-title }

<p class="helios-api-section-description">General configuration setters and compatibility helpers.</p>

<a id="method-reset" class="helios-api-member-anchor"></a>

### `reset(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:893</code></p>
<p>Read or set the reset setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current reset value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.reset({
  enabled: true,
});
</code></pre>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-update" class="helios-api-member-anchor"></a>

### `update(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:381</code></p>
<p>Read or set the update setting.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Current update value when called without arguments; otherwise this instance for chaining.</p><span class="helios-api-return-type"><strong>Type</strong> <code>Object</code>|<code>this</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.update({
  enabled: true,
});
</code></pre>
</div>

<a id="method-stateentries" class="helios-api-member-anchor"></a>

### `stateEntries()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:430</code></p>
<p>Configures or reads state entries.</p>
</div>

<a id="method-emitchange" class="helios-api-member-anchor"></a>

### `emitChange(reason, detail = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:572</code></p>
<p>Configures or reads emit change.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
<tr><td class="helios-api-param-name"><code>detail</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Event payload passed to listeners.</td></tr>
</tbody>
</table>
</div>

<a id="method-descriptor" class="helios-api-member-anchor"></a>

### `descriptor()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:598</code></p>
<p>Configures or reads descriptor.</p>
</div>

<a id="method-choices" class="helios-api-member-anchor"></a>

### `choices()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:602</code></p>
<p>Configures or reads choices.</p>
</div>

<a id="method-bindings" class="helios-api-member-anchor"></a>

### `bindings()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:606</code></p>
<p>Configures or reads bindings.</p>
</div>

<a id="method-isdynamic" class="helios-api-member-anchor"></a>

### `isDynamic()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:614</code></p>
<p>Returns the current dynamic value or state.</p>
<h4>Example</h4>
<pre class="helios-api-example"><code>
const value = helios.isDynamic();
</code></pre>
</div>

<a id="method-type" class="helios-api-member-anchor"></a>

### `type(value, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:618</code></p>
<p>Configures or reads type.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New type value. Omit this argument to read the current value.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.type(1);
</code></pre>
</div>

<a id="method-parameter" class="helios-api-member-anchor"></a>

### `parameter(key, value, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:639</code></p>
<p>Configures or reads parameter.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>key</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>parameter</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New parameter value. Omit this argument to read the current value.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-parameters" class="helios-api-member-anchor"></a>

### `parameters(patch = {}, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:656</code></p>
<p>Configures or reads parameters.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>patch</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Value passed to <code>parameters</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-pauseoninteraction" class="helios-api-member-anchor"></a>

### `pauseOnInteraction(value, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:671</code></p>
<p>Configures or reads pause on interaction.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New pause on interaction value. Omit this argument to read the current value.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.pauseOnInteraction(1);
</code></pre>
</div>

<a id="method-positionattribute" class="helios-api-member-anchor"></a>

### `positionAttribute(value, options = {})`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:832</code></p>
<p>Configures or reads position attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>value</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">New position attribute value. Omit this argument to read the current value.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>{}</code></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.positionAttribute(1);
</code></pre>
</div>

<a id="method-positionattributechoices" class="helios-api-member-anchor"></a>

### `positionAttributeChoices()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:842</code></p>
<p>Configures or reads position attribute choices.</p>
</div>

<a id="method-start" class="helios-api-member-anchor"></a>

### `start()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:869</code></p>
<p>Configures or reads start.</p>
</div>

<a id="method-stop" class="helios-api-member-anchor"></a>

### `stop(reason = 'behavior:layout')`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:876</code></p>
<p>Configures or reads stop.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;behavior:layout&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
</tbody>
</table>
</div>

<a id="method-reheat" class="helios-api-member-anchor"></a>

### `reheat(reason = 'behavior:layout')`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/LayoutBehavior.js:882</code></p>
<p>Configures or reads reheat.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>reason</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;behavior:layout&#x27;</code></td><td class="helios-api-param-description">Reason for this operation.</td></tr>
</tbody>
</table>
</div>
