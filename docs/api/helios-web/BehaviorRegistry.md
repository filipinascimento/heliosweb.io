# BehaviorRegistry

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/behaviors/BehaviorRegistry.js:13</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
Registry mapping behavior ids to behavior constructors or factories.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class BehaviorRegistry {
```

</div>

## Returns

<div class="helios-api-template-section">
<div class="helios-api-return"><p>Empty registry ready for built-in or custom behavior registration.</p><span class="helios-api-return-type"><strong>Type</strong> <a href="/docs/api/helios-web/BehaviorRegistry/"><code>BehaviorRegistry</code></a></span></div>
</div>

## Notes

<div markdown="1" class="helios-api-template-section">
The registry is the public extension point behind
`helios.registerBehavior(...)`; created behaviors still attach through
`BehaviorManager`, so persistence and cleanup flow remains consistent.
</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-register" class="helios-api-member-anchor"></a>

### `register(id, behavior)` &rarr; &#123;this&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorRegistry.js:18</code></p>
<p>Manages register for the current instance.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>register</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>behavior</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>register</code>.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>This instance.</p><span class="helios-api-return-type"><strong>Type</strong> <code>this</code></span></div>
</div>

<a id="method-has" class="helios-api-member-anchor"></a>

### `has(id)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorRegistry.js:28</code></p>
<p>Returns the current has value or state.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>has</code>.</td></tr>
</tbody>
</table>
</div>

<a id="method-create" class="helios-api-member-anchor"></a>

### `create(id, options)`

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/behaviors/BehaviorRegistry.js:32</code></p>
<p>Configures or reads create.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>id</code></td><td class="helios-api-param-type"></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Value passed to <code>create</code>.</td></tr>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes"></td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Options object for this operation.</td></tr>
</tbody>
</table>
</div>


## Example

<div markdown="1" class="helios-api-template-section">

```js
const registry = new BehaviorRegistry().register('custom', CustomBehavior);
```

</div>
