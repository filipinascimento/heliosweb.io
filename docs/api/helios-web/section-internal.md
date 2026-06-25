
# Internal

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

Advanced exported utilities that are usually consumed by Helios Web itself or custom integrations.



<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../applyCameraPose/">
<span>function</span>
<strong>applyCameraPose</strong>
<em>Apply a captured or merged pose to a renderer camera.</em>
</a>
<a class="helios-api-directory-item" href="../base64ToUint8Array/">
<span>function</span>
<strong>base64ToUint8Array</strong>
<em>Decode base64-encoded binary colormap data.</em>
</a>
<a class="helios-api-directory-item" href="../CameraTransitionController/">
<span>class</span>
<strong>CameraTransitionController</strong>
<em>Time-based camera transition controller used by Helios camera animations.</em>
</a>
<a class="helios-api-directory-item" href="../captureCameraPose/">
<span>function</span>
<strong>captureCameraPose</strong>
<em>Capture a renderer camera into a serializable pose object.</em>
</a>
<a class="helios-api-directory-item" href="../colormaps/">
<span>symbol</span>
<strong>colormaps</strong>
<em>Built-in color map registry grouped by source collection.</em>
</a>
<a class="helios-api-directory-item" href="../colormapToInterpolator/">
<span>function</span>
<strong>colormapToInterpolator</strong>
<em>Resolve a colormap to an interpolation function.</em>
</a>
<a class="helios-api-directory-item" href="../colormapToScheme/">
<span>function</span>
<strong>colormapToScheme</strong>
<em>Resolve a colormap to a discrete color scheme.</em>
</a>
<a class="helios-api-directory-item" href="../createCategoricalColormap/">
<span>function</span>
<strong>createCategoricalColormap</strong>
<em>Create a categorical palette from a colormap.</em>
</a>
<a class="helios-api-directory-item" href="../createColormapScale/">
<span>function</span>
<strong>createColormapScale</strong>
<em>Create a numeric colormap scale.</em>
</a>
<a class="helios-api-directory-item" href="../createDefaultMappers/">
<span>function</span>
<strong>createDefaultMappers</strong>
<em>Create the default node and edge mapper collections for a network.</em>
</a>
<a class="helios-api-directory-item" href="../createPanelSchemaIndicator/">
<span>function</span>
<strong>createPanelSchemaIndicator</strong>
<em>Create a DOM indicator that reflects dirty status for a panel schema.</em>
</a>
<a class="helios-api-directory-item" href="../createYawPitchQuaternion/">
<span>function</span>
<strong>createYawPitchQuaternion</strong>
<em>Build a normalized camera rotation quaternion from yaw and pitch angles.</em>
</a>
<a class="helios-api-directory-item" href="../decodeColormapData/">
<span>function</span>
<strong>decodeColormapData</strong>
<em>Decode packed RGB colormap bytes into color tuples.</em>
</a>
<a class="helios-api-directory-item" href="../DEFAULT_NODE_COLORMAP/">
<span>symbol</span>
<strong>DEFAULT_NODE_COLORMAP</strong>
<em>Default node colormap used by Helios when no explicit node color mapper is set.</em>
</a>
<a class="helios-api-directory-item" href="../defineHeliosWebComponents/">
<span>function</span>
<strong>defineHeliosWebComponents</strong>
<em>Register Helios Web custom elements in a document or window.</em>
</a>
<a class="helios-api-directory-item" href="../ensureDefaultStyles/">
<span>function</span>
<strong>ensureDefaultStyles</strong>
<em>Ensure the default Helios UI stylesheet is present in a document.</em>
</a>
<a class="helios-api-directory-item" href="../FILTERS_PANEL_SCHEMA/">
<span>symbol</span>
<strong>FILTERS_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Filters panel.</em>
</a>
<a class="helios-api-directory-item" href="../HeliosUI/">
<span>class</span>
<strong>HeliosUI</strong>
<em>Optional built-in control surface for a Helios visualization.</em>
</a>
<a class="helios-api-directory-item" href="../humanizeControlLabel/">
<span>function</span>
<strong>humanizeControlLabel</strong>
<em>Convert a state key or control identifier into a display label.</em>
</a>
<a class="helios-api-directory-item" href="../LABELS_PANEL_SCHEMA/">
<span>symbol</span>
<strong>LABELS_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Labels panel.</em>
</a>
<a class="helios-api-directory-item" href="../LAYOUT_PANEL_SCHEMA/">
<span>symbol</span>
<strong>LAYOUT_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Layout panel.</em>
</a>
<a class="helios-api-directory-item" href="../LEGENDS_PANEL_SCHEMA/">
<span>symbol</span>
<strong>LEGENDS_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Legends panel.</em>
</a>
<a class="helios-api-directory-item" href="../MAPPERS_PANEL_SCHEMA/">
<span>symbol</span>
<strong>MAPPERS_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Mappers panel.</em>
</a>
<a class="helios-api-directory-item" href="../mergeCameraPose/">
<span>function</span>
<strong>mergeCameraPose</strong>
<em>Merge a partial camera pose into an existing pose.</em>
</a>
<a class="helios-api-directory-item" href="../normalizePanelSchema/">
<span>function</span>
<strong>normalizePanelSchema</strong>
<em>Normalize a panel schema into the canonical shape used by Helios UI panels.</em>
</a>
<a class="helios-api-directory-item" href="../panelSchemaKeys/">
<span>function</span>
<strong>panelSchemaKeys</strong>
<em>Return all state keys referenced by a panel schema.</em>
</a>
<a class="helios-api-directory-item" href="../panelSchemaSectionKeys/">
<span>function</span>
<strong>panelSchemaSectionKeys</strong>
<em>Return all state keys referenced by one panel schema section.</em>
</a>
<a class="helios-api-directory-item" href="../panelSchemaSectionStatus/">
<span>function</span>
<strong>panelSchemaSectionStatus</strong>
<em>Compute the dirty status for one panel schema section.</em>
</a>
<a class="helios-api-directory-item" href="../panelSchemaStatus/">
<span>function</span>
<strong>panelSchemaStatus</strong>
<em>Compute the dirty status for a full panel schema.</em>
</a>
<a class="helios-api-directory-item" href="../PanelStack/">
<span>class</span>
<strong>PanelStack</strong>
<em>Collapsible stack of UI subpanels used by the optional Helios UI.</em>
</a>
<a class="helios-api-directory-item" href="../resolvePanelItemLabel/">
<span>function</span>
<strong>resolvePanelItemLabel</strong>
<em>Resolve the display label for a panel schema item.</em>
</a>
<a class="helios-api-directory-item" href="../SCENE_PANEL_SCHEMA/">
<span>symbol</span>
<strong>SCENE_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Scene panel.</em>
</a>
<a class="helios-api-directory-item" href="../SELECTION_PANEL_SCHEMA/">
<span>symbol</span>
<strong>SELECTION_PANEL_SCHEMA</strong>
<em>Built-in state schema for the Selection panel.</em>
</a>
<a class="helios-api-directory-item" href="../TabbedPanel/">
<span>class</span>
<strong>TabbedPanel</strong>
<em>Small tabbed panel primitive used by the optional Helios UI.</em>
</a>
</div>
