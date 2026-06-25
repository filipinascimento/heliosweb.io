
# Measurement Sessions

<p class="helios-api-back"><a href="index.md">Back to Helios Network Native C API</a></p>

Steppable native measurement sessions for long-running algorithms.



<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../CXConnectedComponentsSessionCreate/">
<span>function</span>
<strong>CXConnectedComponentsSessionCreate</strong>
<em>Creates a steppable connected-components session.</em>
</a>
<a class="helios-api-directory-item" href="../CXConnectedComponentsSessionDestroy/">
<span>function</span>
<strong>CXConnectedComponentsSessionDestroy</strong>
<em>Releases all resources held by a connected-components session.</em>
</a>
<a class="helios-api-directory-item" href="../CXConnectedComponentsSessionFinalize/">
<span>function</span>
<strong>CXConnectedComponentsSessionFinalize</strong>
<em>Finalizes a completed session, copying per-node component ids into `outNodeComponent` (length &gt;= nodeCapacity).</em>
</a>
<a class="helios-api-directory-item" href="../CXConnectedComponentsSessionGetProgress/">
<span>function</span>
<strong>CXConnectedComponentsSessionGetProgress</strong>
<em>Returns current progress metrics. Any output pointer may be NULL.</em>
</a>
<a class="helios-api-directory-item" href="../CXConnectedComponentsSessionStep/">
<span>function</span>
<strong>CXConnectedComponentsSessionStep</strong>
<em>Advances the session by at most `budget` node-visits (best effort).</em>
</a>
<a class="helios-api-directory-item" href="../CXCorenessSessionCreate/">
<span>function</span>
<strong>CXCorenessSessionCreate</strong>
<em>Creates a steppable coreness session.</em>
</a>
<a class="helios-api-directory-item" href="../CXCorenessSessionDestroy/">
<span>function</span>
<strong>CXCorenessSessionDestroy</strong>
<em>Releases all resources held by a coreness session.</em>
</a>
<a class="helios-api-directory-item" href="../CXCorenessSessionFinalize/">
<span>function</span>
<strong>CXCorenessSessionFinalize</strong>
<em>Finalizes a completed session, copying per-node coreness values into `outNodeCoreness` (length &gt;= nodeCapacity).</em>
</a>
<a class="helios-api-directory-item" href="../CXCorenessSessionGetProgress/">
<span>function</span>
<strong>CXCorenessSessionGetProgress</strong>
<em>Returns current progress metrics. Any output pointer may be NULL.</em>
</a>
<a class="helios-api-directory-item" href="../CXCorenessSessionStep/">
<span>function</span>
<strong>CXCorenessSessionStep</strong>
<em>Advances the session by at most `budget` peeled nodes (best effort).</em>
</a>
<a class="helios-api-directory-item" href="../CXLeidenSessionCreate/">
<span>function</span>
<strong>CXLeidenSessionCreate</strong>
<em>Creates a steppable Leiden session. The network topology and relevant edge weight attribute must not change while the session is active. Returns NULL on failure.</em>
</a>
<a class="helios-api-directory-item" href="../CXLeidenSessionDestroy/">
<span>function</span>
<strong>CXLeidenSessionDestroy</strong>
<em>Releases all resources held by a Leiden session.</em>
</a>
<a class="helios-api-directory-item" href="../CXLeidenSessionFinalize/">
<span>function</span>
<strong>CXLeidenSessionFinalize</strong>
<em>Finalizes a completed session, writing the resulting community ids into a node attribute of type `CXUnsignedIntegerAttributeType` (dimension 1). Returns CXFalse if the session has not completed or on failure.</em>
</a>
<a class="helios-api-directory-item" href="../CXLeidenSessionGetProgress/">
<span>function</span>
<strong>CXLeidenSessionGetProgress</strong>
<em>Returns current progress metrics. Any output pointer may be NULL. `outProgressCurrent` and `outProgressTotal` are best-effort and may change as the algorithm advances (i.e. the total may be revised).</em>
</a>
<a class="helios-api-directory-item" href="../CXLeidenSessionStep/">
<span>function</span>
<strong>CXLeidenSessionStep</strong>
<em>Advances the session by at most `budget` node-visits (best effort). Returns the current phase after stepping.</em>
</a>
</div>
