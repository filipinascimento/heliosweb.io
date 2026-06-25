
# Persistence

<p class="helios-api-back"><a href="index.md">Back to Helios Web API</a></p>

State manager, storage manager, session, preference, and envelope APIs for saving and restoring visualization state.

Persistence APIs save visualization state, preferences, sessions, and storage
envelopes. The state manager captures runtime settings such as active mappers,
panels, layouts, and behavior state. Storage managers decide where those
snapshots live: browser storage, remote storage, dummy storage, or a host
application bridge.

Use these APIs when an application needs autosave, named sessions, portable
state files, or host-specific save/restore integration.

<div class="helios-api-directory">
<a class="helios-api-directory-item" href="../applyOverridesToVisualizationState/">
<span>function</span>
<strong>applyOverridesToVisualizationState</strong>
<em>Apply sparse dotted-path overrides to a visualization state object.</em>
</a>
<a class="helios-api-directory-item" href="../BrowserStorageManager/">
<span>class</span>
<strong>BrowserStorageManager</strong>
<em>Browser storage manager backed by IndexedDB and Web Storage fallbacks.</em>
</a>
<a class="helios-api-directory-item" href="../createDefaultNetworkSource/">
<span>function</span>
<strong>createDefaultNetworkSource</strong>
<em>Normalize source-network metadata stored with visualization state.</em>
</a>
<a class="helios-api-directory-item" href="../createDefaultPreferencesState/">
<span>function</span>
<strong>createDefaultPreferencesState</strong>
<em>Normalize a preferences payload into the current public preference shape.</em>
</a>
<a class="helios-api-directory-item" href="../createDefaultUIState/">
<span>function</span>
<strong>createDefaultUIState</strong>
<em>Normalize a UI payload into the current serializable UI state shape.</em>
</a>
<a class="helios-api-directory-item" href="../createHeliosStorageManager/">
<span>function</span>
<strong>createHeliosStorageManager</strong>
<em>Create the storage manager selected by a Helios `storage` constructor option.</em>
</a>
<a class="helios-api-directory-item" href="../createMemoryIndexedDBFactory/">
<span>function</span>
<strong>createMemoryIndexedDBFactory</strong>
<em>Create an in-memory IndexedDB-like factory for persistence tests.</em>
</a>
<a class="helios-api-directory-item" href="../createMemoryStorage/">
<span>function</span>
<strong>createMemoryStorage</strong>
<em>Create an in-memory Storage-compatible object.</em>
</a>
<a class="helios-api-directory-item" href="../createPersistenceEnvelope/">
<span>function</span>
<strong>createPersistenceEnvelope</strong>
<em>Create a versioned persistence envelope.</em>
</a>
<a class="helios-api-directory-item" href="../diffOverrideMaps/">
<span>function</span>
<strong>diffOverrideMaps</strong>
<em>Compute sparse override differences between two flattened override maps.</em>
</a>
<a class="helios-api-directory-item" href="../DummyStorageManager/">
<span>class</span>
<strong>DummyStorageManager</strong>
<em>In-memory storage facade used when durable persistence is disabled.</em>
</a>
<a class="helios-api-directory-item" href="../flattenVisualizationOverrides/">
<span>function</span>
<strong>flattenVisualizationOverrides</strong>
<em>Flatten visualization state into sparse dotted override paths.</em>
</a>
<a class="helios-api-directory-item" href="../HeliosStateManager/">
<span>class</span>
<strong>HeliosStateManager</strong>
<em>Central live state graph for Helios defaults, bindings, overrides, and reset status.</em>
</a>
<a class="helios-api-directory-item" href="../HeliosStorageManager/">
<span>class</span>
<strong>HeliosStorageManager</strong>
<em>Base storage facade for Helios state snapshots, sessions, and portable network state.</em>
</a>
<a class="helios-api-directory-item" href="../IndexedDBSessionStore/">
<span>class</span>
<strong>IndexedDBSessionStore</strong>
<em>Session store backed by IndexedDB.</em>
</a>
<a class="helios-api-directory-item" href="../LocalStoragePreferenceStore/">
<span>class</span>
<strong>LocalStoragePreferenceStore</strong>
<em>Preference store backed by the browser `localStorage` API.</em>
</a>
<a class="helios-api-directory-item" href="../migratePersistenceEnvelope/">
<span>function</span>
<strong>migratePersistenceEnvelope</strong>
<em>Normalize a partial persistence object into the current envelope.</em>
</a>
<a class="helios-api-directory-item" href="../parsePersistenceEnvelope/">
<span>function</span>
<strong>parsePersistenceEnvelope</strong>
<em>Parse and migrate persistence input.</em>
</a>
<a class="helios-api-directory-item" href="../PERSISTENCE_KINDS/">
<span>symbol</span>
<strong>PERSISTENCE_KINDS</strong>
<em>Supported persistence envelope kinds.</em>
</a>
<a class="helios-api-directory-item" href="../PERSISTENCE_SCHEMA_VERSION/">
<span>symbol</span>
<strong>PERSISTENCE_SCHEMA_VERSION</strong>
<em>Current schema version for Helios Web persistence envelopes.</em>
</a>
<a class="helios-api-directory-item" href="../RemoteStorageManager/">
<span>class</span>
<strong>RemoteStorageManager</strong>
<em>Storage manager that delegates session records to a host-provided client.</em>
</a>
<a class="helios-api-directory-item" href="../serializePersistenceEnvelope/">
<span>function</span>
<strong>serializePersistenceEnvelope</strong>
<em>Serialize a persistence envelope to JSON.</em>
</a>
<a class="helios-api-directory-item" href="../SessionStore/">
<span>class</span>
<strong>SessionStore</strong>
<em>Low-level session record store used by Helios storage managers.</em>
</a>
<a class="helios-api-directory-item" href="../StateBindingController/">
<span>class</span>
<strong>StateBindingController</strong>
<em>Binding controller that keeps registered state entries synchronized with runtime owners.</em>
</a>
<a class="helios-api-directory-item" href="../StateTransaction/">
<span>class</span>
<strong>StateTransaction</strong>
<em>Helper passed to `HeliosStateManager.transaction()` for grouped state writes.</em>
</a>
<a class="helios-api-directory-item" href="../UIAttribute/">
<span>class</span>
<strong>UIAttribute</strong>
<em>Observable UI attribute descriptor used to bind controls to Helios state.</em>
</a>
</div>
