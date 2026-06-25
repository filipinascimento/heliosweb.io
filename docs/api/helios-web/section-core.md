
# Core

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

The main visualization controller and primary user-facing entry points.

Use this section when wiring a visualization into an application. `Helios` owns
the renderer, behavior registry, camera, mapper collections, layout controller,
filter state, persistence state, and figure export entry points. The common
runtime path is to create or load a `HeliosNetwork`, instantiate `Helios` with a
DOM container, wait for readiness, then configure behaviors and mappers.

The core page is also the best place to check lifecycle details: initialization
promises, frame requests, renderer fallback behavior, and methods that bridge
application state to the visual scene.

<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../Helios/">
<span>class</span>
<strong>Helios</strong>
<em>Main Helios Web visualization controller for one `helios-network` graph.</em>
</a>
</div>
