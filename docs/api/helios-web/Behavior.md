# Behavior

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/behaviors/Behavior.js:33</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Base class for reusable Helios application behaviors.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class Behavior extends EventTarget {
```

</div>

## Parameters

<div class="helios-api-template-section">
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Serializable configuration owned by the behavior.</td></tr>
</tbody>
</table>
</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Detached behavior instance; Helios attaches it through <code>helios.useBehavior(...)</code> or <code>BehaviorManager.use(...)</code>.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/Behavior/"><code>Behavior</code></a></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
Behaviors attach to a Helios context, own serializable state, emit
change events, and register cleanup hooks for listeners, timers, and UI
bindings. Custom behaviors should override `attach`, `detach`, `serialize`,
and `restore` only where needed.
</div>

## Instance Properties { #api-instance-properties .helios-api-section-title }

<a id="property-id" class="helios-api-member-anchor"></a>

### `id`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/Behavior.js:34</code></p>
<p>Id exposed by the class.</p>
</div>

## Network And Persistence { #api-network-and-persistence .helios-api-section-title }

<p class="helios-api-section-description">Network replacement, serialization, and visualization state persistence. <a href="ExporterBehavior.md">ExporterBehavior</a> and <a href="InterfaceBehavior.md">InterfaceBehavior</a> can surface parts of this flow in the UI.</p>

<a id="method-attach" class="helios-api-member-anchor"></a>

### `attach(context)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/Behavior.js:44</code></p>
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

<p class="helios-api-source">Source: <code>src/behaviors/Behavior.js:69</code></p>
<p>Handles serialize for the current graph or visualization state.</p>
</div>

<a id="method-restore" class="helios-api-member-anchor"></a>

### `restore(snapshot = {})` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/Behavior.js:73</code></p>
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

## Events { #api-events .helios-api-section-title }

<p class="helios-api-section-description">Event subscription helpers and emitted interaction events.</p>

<a id="method-emit" class="helios-api-member-anchor"></a>

### `emit(type, detail)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/Behavior.js:91</code></p>
<p>Configures or reads emit.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>type</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute value type.</td></tr>
<tr><td class="helios-api-param-name"><code>detail</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Event payload passed to listeners.</td></tr>
</tbody>
</table>
</div>

<a id="method-on" class="helios-api-member-anchor"></a>

### `on(type, handler, options)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/Behavior.js:96</code></p>
<p>Configures or reads on.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>type</code></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Attribute value type.</td></tr>
<tr><td class="helios-api-param-name"><code>handler</code></td><td class="helios-api-param-type"><code>Function</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Callback invoked for the registered event.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-detach" class="helios-api-member-anchor"></a>

### `detach()`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/Behavior.js:49</code></p>
<p>Manages detach for the current instance.</p>
</div>

<a id="method-update" class="helios-api-member-anchor"></a>

### `update(options = {})` &rarr; &#123;Object|this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/Behavior.js:62</code></p>
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

<a id="method-addcleanup" class="helios-api-member-anchor"></a>

### `addCleanup(cleanup)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/Behavior.js:80</code></p>
<p>Manages cleanup for the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>cleanup</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>addCleanup</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-removecleanup" class="helios-api-member-anchor"></a>

### `removeCleanup(cleanup)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/Behavior.js:86</code></p>
<p>Manages cleanup for the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>cleanup</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>removeCleanup</code>.</td></tr>
</tbody>
</table>
</div>


## Example

<div markdown="1" class="helios-api-template-section">

```js
class PulseBehavior extends Behavior {
  static id = 'pulse';
  attach(context) {
    super.attach(context);
    const timer = setInterval(() => context.helios.requestRender(), 500);
    this.addCleanup(() => clearInterval(timer));
    return this;
  }
}
```

</div>
