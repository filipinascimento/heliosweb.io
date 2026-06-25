
# Layouts

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

Layout controllers and position delegates for static, worker, D3 force, and GPU force layouts.

Layouts are responsible for producing node positions, not for drawing nodes.
Static layouts consume existing coordinates; worker-backed and GPU-backed
layouts update positions over time. Position delegates expose the buffer bridge
between layout algorithms and renderable node positions.

Choose the layout page based on where work should run: static data, JavaScript
worker force simulation, or GPU force simulation.

<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../D3Force3DLayout/">
<span>class</span>
<strong>D3Force3DLayout</strong>
<em>Worker-backed layout adapter for the D3 Force 3D engine.</em>
</a>
<a class="helios-api-directory-item" href="../DEFAULT_LAYOUT_TUNING_MODEL/">
<span>symbol</span>
<strong>DEFAULT_LAYOUT_TUNING_MODEL</strong>
<em>Default model used to tune GPU force layout options from graph statistics.</em>
</a>
<a class="helios-api-directory-item" href="../extractLayoutTuningFeatures/">
<span>function</span>
<strong>extractLayoutTuningFeatures</strong>
<em>Extract graph features used by the layout tuning model.</em>
</a>
<a class="helios-api-directory-item" href="../GpuForceLayout/">
<span>class</span>
<strong>GpuForceLayout</strong>
<em>GPU-backed force layout that can run through WebGPU or WebGL2 delegates.</em>
</a>
<a class="helios-api-directory-item" href="../GpuForcePositionDelegate/">
<span>class</span>
<strong>GpuForcePositionDelegate</strong>
<em>Position delegate used by GPU force layouts.</em>
</a>
<a class="helios-api-directory-item" href="../Layout/">
<span>class</span>
<strong>Layout</strong>
<em>Base class for layout algorithms.</em>
</a>
<a class="helios-api-directory-item" href="../PositionDelegate/">
<span>class</span>
<strong>PositionDelegate</strong>
<em>Abstract source for layout positions owned outside the network buffers.</em>
</a>
<a class="helios-api-directory-item" href="../predictLayoutTuningOptions/">
<span>function</span>
<strong>predictLayoutTuningOptions</strong>
<em>Predict layout option overrides for a network using the layout tuning model.</em>
</a>
<a class="helios-api-directory-item" href="../StaticLayout/">
<span>class</span>
<strong>StaticLayout</strong>
<em>Layout that keeps existing node positions fixed.</em>
</a>
<a class="helios-api-directory-item" href="../WorkerLayout/">
<span>class</span>
<strong>WorkerLayout</strong>
<em>Worker-backed force or jitter layout.</em>
</a>
</div>
