# HeliosNetwork

<div class="helios-api-kind">class</div>

<p class="helios-api-back"><a href="index.md">Back to Helios Network JS/WASM API</a></p>

<dl class="helios-api-definition-list">
<dt>Kind</dt>
<dd>class</dd>
<dt>Source</dt>
<dd>src/js/HeliosNetwork.js:3200</dd>
</dl>

## Description

<div markdown="1" class="helios-api-template-section">
High-level JavaScript wrapper around the Helios WASM network implementation. Manages lifetime, attribute registration, and buffer views.
</div>

## Signature

<div markdown="1" class="helios-api-template-section">

```text
export class HeliosNetwork extends BaseEventTarget {
```

</div>

## Utilities { #api-utilities .helios-api-section-title }

<p class="helios-api-section-description">Additional public helpers that do not belong to a narrower API area.</p>

<a id="method-measurelocalclusteringcoefficient" class="helios-api-member-anchor"></a>

### `measureLocalClusteringCoefficient(options = {})` &rarr; &#123;{nodeIndices:Uint32Array, values:Float32Array, valuesByNode:Float32Array, direction:number, variant:number}&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/js/HeliosNetwork.js:9924</code></p>
<p>Measures local clustering coefficients.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description"></td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.variant"><span aria-hidden="true">|</span><code>variant</code></span></td><td class="helios-api-param-type">(<code>number</code>|<code>string</code>)</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;unweighted&#x27;</code></td><td class="helios-api-param-description">unweighted/onnela/newman</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.edgeWeightAttribute"><span aria-hidden="true">|</span><code>edgeWeightAttribute</code></span></td><td class="helios-api-param-type"><code>string</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Required for weighted variants.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.direction"><span aria-hidden="true">|</span><code>direction</code></span></td><td class="helios-api-param-type">(<code>number</code>|<code>string</code>)</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;both&#x27;</code></td><td class="helios-api-param-description">out/in/both</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.nodes"><span aria-hidden="true">|</span><code>nodes</code></span></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Optional node subset.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.outNodeAttribute"><span aria-hidden="true">|</span><code>outNodeAttribute</code></span></td><td class="helios-api-param-type"><code>string</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Optional node attribute name to store local clustering values.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><span class="helios-api-return-type"><strong>Type</strong> {<code>nodeIndices</code>:<code>Uint32Array</code>, <code>values</code>:<code>Float32Array</code>, <code>valuesByNode</code>:<code>Float32Array</code>, <code>direction</code>:<code>number</code>, <code>variant</code>:<code>number</code>}</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.measureLocalClusteringCoefficient({
  enabled: true,
});
</code></pre>
</div>

<a id="method-measurecoreness" class="helios-api-member-anchor"></a>

### `measureCoreness(options = {})` &rarr; &#123;{nodeIndices:Uint32Array, values:Uint32Array, valuesByNode:Uint32Array, direction:number, executionMode:number, maxCore:number}&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/js/HeliosNetwork.js:9978</code></p>
<p>Measures node coreness (k-core index).</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description"></td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.direction"><span aria-hidden="true">|</span><code>direction</code></span></td><td class="helios-api-param-type">(<code>number</code>|<code>string</code>)</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;both&#x27;</code></td><td class="helios-api-param-description">out/in/both</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.executionMode"><span aria-hidden="true">|</span><code>executionMode</code></span></td><td class="helios-api-param-type">(<code>number</code>|<code>string</code>)</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;single-thread&#x27;</code></td><td class="helios-api-param-description">auto/single-thread/parallel</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.nodes"><span aria-hidden="true">|</span><code>nodes</code></span></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Optional node subset.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.outNodeCorenessAttribute"><span aria-hidden="true">|</span><code>outNodeCorenessAttribute</code></span></td><td class="helios-api-param-type"><code>string</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Optional node attribute name to store coreness.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><span class="helios-api-return-type"><strong>Type</strong> {<code>nodeIndices</code>:<code>Uint32Array</code>, <code>values</code>:<code>Uint32Array</code>, <code>valuesByNode</code>:<code>Uint32Array</code>, <code>direction</code>:<code>number</code>, <code>executionMode</code>:<code>number</code>, <code>maxCore</code>:<code>number</code>}</span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.measureCoreness({
  enabled: true,
});
</code></pre>
</div>

<a id="method-createcorenesssession" class="helios-api-member-anchor"></a>

### `createCorenessSession(options = {})` &rarr; &#123;CorenessSession&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/js/HeliosNetwork.js:10048</code></p>
<p>Creates a steppable coreness session for incremental execution. Run <code>session.step({budget})</code> in a loop until <code>phase</code> becomes <code>3</code> (done), then call <code>session.finalize()</code> to retrieve coreness values.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description"></td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.direction"><span aria-hidden="true">|</span><code>direction</code></span></td><td class="helios-api-param-type">(<code>number</code>|<code>string</code>)</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;both&#x27;</code></td><td class="helios-api-param-description">out/in/both</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.executionMode"><span aria-hidden="true">|</span><code>executionMode</code></span></td><td class="helios-api-param-type">(<code>number</code>|<code>string</code>)</td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;single-thread&#x27;</code></td><td class="helios-api-param-description">auto/single-thread/parallel</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.nodes"><span aria-hidden="true">|</span><code>nodes</code></span></td><td class="helios-api-param-type"><code>Array</code>&lt;<code>number</code>&gt;|<code>TypedArray</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Optional node subset for finalize() return payload.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.outNodeCorenessAttribute"><span aria-hidden="true">|</span><code>outNodeCorenessAttribute</code></span></td><td class="helios-api-param-type"><code>string</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Optional node attribute to write coreness in finalize().</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Session handle.</p><span class="helios-api-return-type"><strong>Type</strong> <code>CorenessSession</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createCorenessSession({
  enabled: true,
});
</code></pre>
</div>

<a id="method-createleidensession" class="helios-api-member-anchor"></a>

### `createLeidenSession(options = {})` &rarr; &#123;LeidenSession&#125;

<div class="helios-api-member-detail">

<p class="helios-api-source">Source: <code>src/js/HeliosNetwork.js:10768</code></p>
<p>Creates a steppable Leiden session for incremental execution. Run <code>session.step({budget})</code> in a loop until <code>phase</code> becomes <code>5</code> (done), then call <code>session.finalize()</code> to write the output attribute.</p>
<h4>Parameters</h4>
<table class="helios-api-params">
<thead><tr><th>Name</th><th>Type</th><th>Attributes</th><th>Default</th><th>Description</th></tr></thead>
<tbody>
<tr><td class="helios-api-param-name"><code>options</code></td><td class="helios-api-param-type"><code>Object</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description"></td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.resolution"><span aria-hidden="true">|</span><code>resolution</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>1</code></td><td class="helios-api-param-description">Modularity resolution parameter (gamma).</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.edgeWeightAttribute"><span aria-hidden="true">|</span><code>edgeWeightAttribute</code></span></td><td class="helios-api-param-type"><code>string</code>|<code>null</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>null</code></td><td class="helios-api-param-description">Edge weight attribute name (dimension 1).</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.seed"><span aria-hidden="true">|</span><code>seed</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>0</code></td><td class="helios-api-param-description">RNG seed (0 uses a default seed).</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.maxLevels"><span aria-hidden="true">|</span><code>maxLevels</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>32</code></td><td class="helios-api-param-description">Maximum aggregation levels.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.maxPasses"><span aria-hidden="true">|</span><code>maxPasses</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>8</code></td><td class="helios-api-param-description">Max local-moving passes per phase.</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.passes"><span aria-hidden="true">|</span><code>passes</code></span></td><td class="helios-api-param-type"><code>number</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"></td><td class="helios-api-param-description">Alias for <code>maxPasses</code> (<code>passes</code> takes precedence when both are set).</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.outNodeCommunityAttribute"><span aria-hidden="true">|</span><code>outNodeCommunityAttribute</code></span></td><td class="helios-api-param-type"><code>string</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>&#x27;community&#x27;</code></td><td class="helios-api-param-description">Default output name for finalize().</td></tr>
<tr><td class="helios-api-param-name"><span class="helios-api-param-nested" title="options.categoricalCommunities"><span aria-hidden="true">|</span><code>categoricalCommunities</code></span></td><td class="helios-api-param-type"><code>boolean</code></td><td class="helios-api-param-attributes">optional</td><td class="helios-api-param-default"><code>true</code></td><td class="helios-api-param-description">Store communities as categorical codes instead of integers.</td></tr>
</tbody>
</table>
<h4>Returns</h4>
<div class="helios-api-return"><p>Session handle.</p><span class="helios-api-return-type"><strong>Type</strong> <code>LeidenSession</code></span></div>
<h4>Example</h4>
<pre class="helios-api-example"><code>
helios.createLeidenSession({
  enabled: true,
});
</code></pre>
</div>
