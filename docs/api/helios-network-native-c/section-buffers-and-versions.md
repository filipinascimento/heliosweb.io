
# Buffers And Versions

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

Direct buffer access and version counters used by high-performance integrations.



<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../CXNetworkActiveEdgeIndexCount/">
<span>function</span>
<strong>CXNetworkActiveEdgeIndexCount</strong>
<em>Returns the number of entries in the stable active edge index buffer.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkActiveEdgeIndices/">
<span>function</span>
<strong>CXNetworkActiveEdgeIndices</strong>
<em>Returns a stable buffer of active edge indices in native active order.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkActiveNodeIndexCount/">
<span>function</span>
<strong>CXNetworkActiveNodeIndexCount</strong>
<em>Returns the number of entries in the stable active node index buffer.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkActiveNodeIndices/">
<span>function</span>
<strong>CXNetworkActiveNodeIndices</strong>
<em>Returns a stable buffer of active node indices in native active order.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkEdgeActivityBuffer/">
<span>function</span>
<strong>CXNetworkEdgeActivityBuffer</strong>
<em>Provides a pointer to the edge activity bitmap.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkEdgesBuffer/">
<span>function</span>
<strong>CXNetworkEdgesBuffer</strong>
<em>Returns a pointer to the flattened edge buffer `[from, to, ...]`.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkEdgeTopologyVersion/">
<span>function</span>
<strong>CXNetworkEdgeTopologyVersion</strong>
<em>Returns the edge topology version.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkIsEdgeActive/">
<span>function</span>
<strong>CXNetworkIsEdgeActive</strong>
<em>Returns CXTrue if the edge index is active.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkIsNodeActive/">
<span>function</span>
<strong>CXNetworkIsNodeActive</strong>
<em>Returns CXTrue if the given node index is currently active.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkNodeActivityBuffer/">
<span>function</span>
<strong>CXNetworkNodeActivityBuffer</strong>
<em>Provides a pointer to the node activity bitmap in linear memory.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkNodeTopologyVersion/">
<span>function</span>
<strong>CXNetworkNodeTopologyVersion</strong>
<em>Returns the node topology version (increments on topology edits and repacks).</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkPromoteActiveEdgesForNodesToRenderEnd/">
<span>function</span>
<strong>CXNetworkPromoteActiveEdgesForNodesToRenderEnd</strong>
<em>Moves active edges incident to the supplied active nodes to the end of the native active edge order.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkPromoteActiveEdgesToRenderEnd/">
<span>function</span>
<strong>CXNetworkPromoteActiveEdgesToRenderEnd</strong>
<em>Moves active edge indices to the end of the native active order, preserving batch order.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkPromoteActiveNodesToRenderEnd/">
<span>function</span>
<strong>CXNetworkPromoteActiveNodesToRenderEnd</strong>
<em>Moves active node indices to the end of the native active order, preserving batch order.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkVersionString/">
<span>function</span>
<strong>CXNetworkVersionString</strong>
<em>Returns the semantic version string for the compiled library (e.g. &quot;1.2.3&quot;).</em>
</a>
</div>
