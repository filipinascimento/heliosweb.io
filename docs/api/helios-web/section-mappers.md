
# Mappers

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

Visual attribute mapping primitives used to bind graph data to colors, sizes, opacity, and related channels.

Mappers translate graph attributes into visual channels. A mapper can connect
node or edge attributes to color, size, width, opacity, labels, outlines, or
other renderer inputs. Mapper collections keep related mapper state grouped so
behaviors and UI panels can read and update it consistently.

Use mapper APIs when the visualization should react to data values rather than
constant style settings.

<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../Mapper/">
<span>class</span>
<strong>Mapper</strong>
<em>Low-level mapper for one node or edge visual mode.</em>
</a>
<a class="helios-api-directory-item" href="../MapperCollection/">
<span>class</span>
<strong>MapperCollection</strong>
<em>Collection of named mappers for either node or edge visuals.</em>
</a>
<a class="helios-api-directory-item" href="../VISUAL_ATTRIBUTES/">
<span>symbol</span>
<strong>VISUAL_ATTRIBUTES</strong>
<em>Map of public mapper channel names to internal Helios visual attribute names.</em>
</a>
<a class="helios-api-directory-item" href="../VisualAttributes/">
<span>class</span>
<strong>VisualAttributes</strong>
<em>Ensures required visual attributes exist on the Helios network, seeds defaults, and provides helpers to apply mappers into sparse buffers.</em>
</a>
</div>
