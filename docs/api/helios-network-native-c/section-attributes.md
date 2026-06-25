
# Attributes

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

Attribute definition, lookup, categorization, and multi-category APIs.



<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../CXAttributeData/">
<span>function</span>
<strong>CXAttributeData</strong>
<em>Returns a pointer to the raw backing buffer for an attribute (or NULL when missing).</em>
</a>
<a class="helios-api-directory-item" href="../CXAttributeInterpolateFloatBuffer/">
<span>function</span>
<strong>CXAttributeInterpolateFloatBuffer</strong>
<em>Interpolates a float attribute buffer toward target values and bumps the attribute version. Returns CXTrue when further interpolation steps are recommended based on minDisplacementRatio.</em>
</a>
<a class="helios-api-directory-item" href="../CXAttributeStride/">
<span>function</span>
<strong>CXAttributeStride</strong>
<em>Returns the byte stride between consecutive entries of an attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXAttributeVersion/">
<span>function</span>
<strong>CXAttributeVersion</strong>
<em>Returns the version counter for an attribute descriptor.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkBumpEdgeAttributeVersion/">
<span>function</span>
<strong>CXNetworkBumpEdgeAttributeVersion</strong>
<em>Manually bumps an edge attribute version and returns the new value.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkBumpNetworkAttributeVersion/">
<span>function</span>
<strong>CXNetworkBumpNetworkAttributeVersion</strong>
<em>Manually bumps a network attribute version and returns the new value.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkBumpNodeAttributeVersion/">
<span>function</span>
<strong>CXNetworkBumpNodeAttributeVersion</strong>
<em>Manually bumps a node attribute version and returns the new value.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkCategorizeAttribute/">
<span>function</span>
<strong>CXNetworkCategorizeAttribute</strong>
<em>Converts a string attribute into category ids using the requested sort policy.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkClearMultiCategoryEntry/">
<span>function</span>
<strong>CXNetworkClearMultiCategoryEntry</strong>
<em>Clears all category ids and weights for one multi-category entry.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkCopyNodeAttributesToEdgeAttributes/">
<span>function</span>
<strong>CXNetworkCopyNodeAttributesToEdgeAttributes</strong>
<em>Copies node attributes into an edge attribute buffer using the network&#x27;s topology. `endpointMode` controls which endpoint is copied: -1 = both, 0 = source only, 1 = destination only. When copying a single endpoint and `duplicateSingleEndpoint` is true, the chosen endpoint is written twice sequentially (for double-width edge attributes).</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkDecategorizeAttribute/">
<span>function</span>
<strong>CXNetworkDecategorizeAttribute</strong>
<em>Converts category ids back to string labels for the named attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkDefineEdgeAttribute/">
<span>function</span>
<strong>CXNetworkDefineEdgeAttribute</strong>
<em>Declares an edge attribute backing buffer.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkDefineMultiCategoryAttribute/">
<span>function</span>
<strong>CXNetworkDefineMultiCategoryAttribute</strong>
<em>Defines a multi-category attribute with optional per-entry weights.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkDefineNetworkAttribute/">
<span>function</span>
<strong>CXNetworkDefineNetworkAttribute</strong>
<em>Declares a network-level attribute backing buffer.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkDefineNodeAttribute/">
<span>function</span>
<strong>CXNetworkDefineNodeAttribute</strong>
<em>Declares a node attribute backing buffer. Dimension defaults to 1.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkEdgeAttributeCount/">
<span>function</span>
<strong>CXNetworkEdgeAttributeCount</strong>
<em>Returns the number of edge attributes currently defined on the network.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkEdgeAttributeNameAt/">
<span>function</span>
<strong>CXNetworkEdgeAttributeNameAt</strong>
<em>Returns the edge attribute name at `index`, or NULL when out of range.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetAttributeCategoryDictionary/">
<span>function</span>
<strong>CXNetworkGetAttributeCategoryDictionary</strong>
<em>Returns the category dictionary for a categorical attribute, or NULL when unavailable.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetAttributeCategoryDictionaryCount/">
<span>function</span>
<strong>CXNetworkGetAttributeCategoryDictionaryCount</strong>
<em>Returns how many category entries are defined for a categorical attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetAttributeCategoryDictionaryEntries/">
<span>function</span>
<strong>CXNetworkGetAttributeCategoryDictionaryEntries</strong>
<em>Copies category ids and labels into caller-provided arrays.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetEdgeAttribute/">
<span>function</span>
<strong>CXNetworkGetEdgeAttribute</strong>
<em>Fetches an edge attribute descriptor by name.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetEdgeAttributeBuffer/">
<span>function</span>
<strong>CXNetworkGetEdgeAttributeBuffer</strong>
<em>Returns a pointer to the raw edge attribute buffer for the named attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetMultiCategoryEntryCount/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryEntryCount</strong>
<em>Returns the number of category entries stored for a multi-category attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetMultiCategoryEntryRange/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryEntryRange</strong>
<em>Returns the [start,end) range for one entry inside the packed multi-category buffers.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetMultiCategoryIds/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryIds</strong>
<em>Returns the packed category id buffer for a multi-category attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetMultiCategoryOffsetCount/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryOffsetCount</strong>
<em>Returns the number of offsets stored for a multi-category attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetMultiCategoryOffsets/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryOffsets</strong>
<em>Returns the packed offsets buffer for a multi-category attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetMultiCategoryWeights/">
<span>function</span>
<strong>CXNetworkGetMultiCategoryWeights</strong>
<em>Returns the packed weight buffer, or NULL when the attribute is unweighted.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetNetworkAttribute/">
<span>function</span>
<strong>CXNetworkGetNetworkAttribute</strong>
<em>Fetches a network attribute descriptor by name.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetNetworkAttributeBuffer/">
<span>function</span>
<strong>CXNetworkGetNetworkAttributeBuffer</strong>
<em>Returns a pointer to the raw network attribute buffer for the named attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetNodeAttribute/">
<span>function</span>
<strong>CXNetworkGetNodeAttribute</strong>
<em>Fetches a node attribute descriptor by name.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkGetNodeAttributeBuffer/">
<span>function</span>
<strong>CXNetworkGetNodeAttributeBuffer</strong>
<em>Returns a pointer to the raw node attribute buffer for the named attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkMultiCategoryHasWeights/">
<span>function</span>
<strong>CXNetworkMultiCategoryHasWeights</strong>
<em>Returns CXTrue when the multi-category attribute stores per-entry weights.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkNetworkAttributeCount/">
<span>function</span>
<strong>CXNetworkNetworkAttributeCount</strong>
<em>Returns the number of network attributes currently defined on the network.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkNetworkAttributeNameAt/">
<span>function</span>
<strong>CXNetworkNetworkAttributeNameAt</strong>
<em>Returns the network attribute name at `index`, or NULL when out of range.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkNodeAttributeCount/">
<span>function</span>
<strong>CXNetworkNodeAttributeCount</strong>
<em>Returns the number of node attributes currently defined on the network.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkNodeAttributeNameAt/">
<span>function</span>
<strong>CXNetworkNodeAttributeNameAt</strong>
<em>Returns the node attribute name at `index` in the internal dictionary iteration order, or NULL when out of range.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkRemoveEdgeAttribute/">
<span>function</span>
<strong>CXNetworkRemoveEdgeAttribute</strong>
<em>Removes a sparse edge attribute and its storage.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkRemoveNetworkAttribute/">
<span>function</span>
<strong>CXNetworkRemoveNetworkAttribute</strong>
<em>Removes a sparse network attribute and its storage.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkRemoveNodeAttribute/">
<span>function</span>
<strong>CXNetworkRemoveNodeAttribute</strong>
<em>Removes a sparse node attribute and its storage.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkSetAttributeCategoryDictionary/">
<span>function</span>
<strong>CXNetworkSetAttributeCategoryDictionary</strong>
<em>Replaces or remaps the category dictionary for a categorical attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkSetMultiCategoryBuffers/">
<span>function</span>
<strong>CXNetworkSetMultiCategoryBuffers</strong>
<em>Replaces the packed offset/id/weight buffers for a multi-category attribute.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkSetMultiCategoryEntry/">
<span>function</span>
<strong>CXNetworkSetMultiCategoryEntry</strong>
<em>Writes one entry of a multi-category attribute using category ids.</em>
</a>
<a class="helios-api-directory-item" href="../CXNetworkSetMultiCategoryEntryByLabels/">
<span>function</span>
<strong>CXNetworkSetMultiCategoryEntryByLabels</strong>
<em>Writes one entry of a multi-category attribute using category labels.</em>
</a>
</div>
