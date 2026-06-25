
# Selectors

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

Node and edge selector containers used for filtering and set operations.



<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../CXEdgeSelectorClear/">
<span>function</span>
<strong>CXEdgeSelectorClear</strong>
<em>Clears all indices from an edge selector without releasing its capacity.</em>
</a>
<a class="helios-api-directory-item" href="../CXEdgeSelectorCount/">
<span>function</span>
<strong>CXEdgeSelectorCount</strong>
<em>Returns how many indices are currently stored in the selector.</em>
</a>
<a class="helios-api-directory-item" href="../CXEdgeSelectorCreate/">
<span>function</span>
<strong>CXEdgeSelectorCreate</strong>
<em>Creates a selector object for edges.</em>
</a>
<a class="helios-api-directory-item" href="../CXEdgeSelectorData/">
<span>function</span>
<strong>CXEdgeSelectorData</strong>
<em>Returns a pointer to the selector&#x27;s index data.</em>
</a>
<a class="helios-api-directory-item" href="../CXEdgeSelectorDestroy/">
<span>function</span>
<strong>CXEdgeSelectorDestroy</strong>
<em>Releases all heap memory associated with an edge selector.</em>
</a>
<a class="helios-api-directory-item" href="../CXEdgeSelectorFillAll/">
<span>function</span>
<strong>CXEdgeSelectorFillAll</strong>
<em>Populates the selector with every active edge.</em>
</a>
<a class="helios-api-directory-item" href="../CXEdgeSelectorFillFromArray/">
<span>function</span>
<strong>CXEdgeSelectorFillFromArray</strong>
<em>Fills the selector with the provided edge indices.</em>
</a>
<a class="helios-api-directory-item" href="../CXEdgeSelectorFilterActive/">
<span>function</span>
<strong>CXEdgeSelectorFilterActive</strong>
<em>Removes invalid/inactive indices in-place from an edge selector.</em>
</a>
<a class="helios-api-directory-item" href="../CXEdgeSelectorFilterByNodes/">
<span>function</span>
<strong>CXEdgeSelectorFilterByNodes</strong>
<em>Keeps only active edges whose endpoints are both present in `nodeSelector`.</em>
</a>
<a class="helios-api-directory-item" href="../CXEdgeSelectorIntersect/">
<span>function</span>
<strong>CXEdgeSelectorIntersect</strong>
<em>Intersects an edge selector in-place with another selector (active indices only).</em>
</a>
<a class="helios-api-directory-item" href="../CXNodeSelectorClear/">
<span>function</span>
<strong>CXNodeSelectorClear</strong>
<em>Clears all indices from a node selector without releasing its capacity.</em>
</a>
<a class="helios-api-directory-item" href="../CXNodeSelectorCount/">
<span>function</span>
<strong>CXNodeSelectorCount</strong>
<em>Returns how many indices are currently stored in the selector.</em>
</a>
<a class="helios-api-directory-item" href="../CXNodeSelectorCreate/">
<span>function</span>
<strong>CXNodeSelectorCreate</strong>
<em>Creates a selector object for nodes with an optional initial capacity.</em>
</a>
<a class="helios-api-directory-item" href="../CXNodeSelectorData/">
<span>function</span>
<strong>CXNodeSelectorData</strong>
<em>Returns a pointer to the selector&#x27;s contiguous index data.</em>
</a>
<a class="helios-api-directory-item" href="../CXNodeSelectorDestroy/">
<span>function</span>
<strong>CXNodeSelectorDestroy</strong>
<em>Releases all heap memory associated with a node selector.</em>
</a>
<a class="helios-api-directory-item" href="../CXNodeSelectorFillAll/">
<span>function</span>
<strong>CXNodeSelectorFillAll</strong>
<em>Populates the selector with every active node.</em>
</a>
<a class="helios-api-directory-item" href="../CXNodeSelectorFillFromArray/">
<span>function</span>
<strong>CXNodeSelectorFillFromArray</strong>
<em>Fills the selector with the provided node indices.</em>
</a>
<a class="helios-api-directory-item" href="../CXNodeSelectorFilterActive/">
<span>function</span>
<strong>CXNodeSelectorFilterActive</strong>
<em>Removes invalid/inactive indices in-place from a node selector.</em>
</a>
<a class="helios-api-directory-item" href="../CXNodeSelectorIntersect/">
<span>function</span>
<strong>CXNodeSelectorIntersect</strong>
<em>Intersects a node selector in-place with another selector (active indices only).</em>
</a>
</div>
