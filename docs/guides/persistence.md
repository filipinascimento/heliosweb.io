# Persistence, Sessions, And State

Helios persistence is built around two runtime facades:

- `helios.states` is the live state graph. It owns registered state entries,
  defaults, aliases, bindings, values, sparse overrides, reset status, and UI
  metadata.
- `helios.storage` is the durable/session layer. It observes `helios.states`,
  coalesces override deltas, serializes session records, restores sessions, and
  attaches portable visualization state to network exports.

Live visual feedback should never wait for storage. Controls write to
`helios.states`; storage decides when and where to persist the resulting sparse
overrides, network bytes, position bytes, and session metadata.

## Constructor Shape

Plain library construction uses dummy storage:

```js
const helios = new Helios(network, {
  container: '#app',
});
```

Dummy storage keeps export/import snapshots working, but it does not create a
browser backend, persistent UI chrome, resume prompt, sync button, or URL
session id.

Enable browser storage explicitly:

```js
const helios = new Helios(network, {
  container: '#app',
  storage: { type: 'browser' },
  workspaceId: 'project:demo',
  session: {
    id: 'demo-session',
    url: true,
    restore: true,
    restoreNetwork: true,
    networkPersistence: {
      enabled: true,
      format: 'zxnet',
    },
  },
  networkPersistence: { enabled: true, autosave: false },
  positionPersistence: { enabled: true, autosave: true },
});
await helios.ready;
```

The top-level options matter:

- `storage` selects the storage manager: `false`, `true`, `{ type: 'browser' }`,
  `{ type: 'remote', client }`, or a custom manager instance.
- `workspaceId` scopes browser/remote sessions.
- `session` controls URL routing, restore, initial save, thumbnail policy, and
  session network format.
- `networkPersistence` controls graph payload persistence.
- `positionPersistence` controls layout/current-position payload persistence.

Passing `workspaceId`, `session`, `sessionId`, `networkPersistence`, or
`positionPersistence` opts into browser storage when `storage` is omitted.

## State Entries

State entries describe values and bindings. They do not define panel placement.

```js
helios.states.register(component, 'layout.parameters', {
  gravity: {
    default: 0.0008,
    type: 'number',
    scope: 'network',
    ui: {
      label: 'Gravity',
      controller: 'slider',
      min: 0,
      max: 0.01,
    },
    getter: () => layout.gravity(),
    setter: (value) => layout.gravity(value),
  },
});
```

UI panels reference state keys through panel schemas. This keeps state ownership
independent from where a control appears in the interface.

## Override Model

The state manager keeps current live values separate from persisted overrides.

- `values` are the current values used by UI and runtime bindings.
- `overrides` are intentional user/program/CLI changes.
- `scope` metadata (`user`, `workspace`, `network`, `session`) tells storage
  where the override belongs.

Dirty status means a key or descendant has an override. It does not mean the
current value differs from the default. Reset removes the override:

```js
helios.states.set('appearance.nodeStyle.sizeScale', 1.4, {
  source: 'ui',
  reason: 'appearance-control',
});

helios.states.reset('appearance.nodeStyle.sizeScale');
```

Default writes, binding refreshes, restore heuristics, and startup syncs should
avoid creating overrides unless they explicitly carry user/program/CLI intent.

## Session API

There is no separate `helios.session` facade. Session operations live on
`helios.storage`.

```js
helios.storage.configureSession({ url: true });
await helios.storage.flush({ includeNetwork: true });
await helios.storage.sync({ includeNetwork: true, includePositions: true });

const summaries = await helios.storage.listSessionSummaries();
const prompt = await helios.storage.getResumePrompt();
await helios.storage.resumeSession(sessionId);
await helios.storage.saveSession({ nickname: 'experiment A' });
await helios.storage.startNewSession({ nickname: 'experiment B' });
await helios.storage.deleteSession(sessionId);
await helios.storage.markSessionFinished(sessionId);
```

When URL routing is enabled, Helios uses the `sessionId` query parameter by
default. A valid explicit session id restores directly. Without a valid explicit
id, storage can expose resumable unfinished sessions for the UI prompt.

## Session Record Contents

A session record can include:

- session metadata: id, workspace id, nickname, timestamps, status;
- preferences and UI/behavior state;
- a visualization envelope with sparse storage overrides;
- optional graph bytes in `networkData`;
- optional compressed layout/current positions in `positionData`;
- optional thumbnail data for resume/session lists.

State-only autosave is incremental: storage merges changed/deleted override
deltas into the existing session manifest. Position autosave writes the
position side record without rewriting the full graph payload. Full manual sync
or Save Session can save graph bytes and positions together.

## Portable Network State

Explicit network exports can carry tracked visualization state:

```js
const blob = await helios.savePortableNetwork('zxnet', {
  output: 'blob',
  includeVisualization: true,
});
```

Portable state is suitable for network-scoped visualization defaults and
positions. Do not store credentials, private host state, or global user
preferences in network files.

## Remote Storage

Remote storage delegates session records to a host client:

```js
const helios = new Helios(network, {
  container: '#app',
  workspaceId: 'project:demo',
  storage: {
    type: 'remote',
    client: {
      putSession: (record) => api.saveSession(record),
      getSession: (id) => api.loadSession(id),
      listSessions: (options) => api.listSessions(options),
      deleteSession: (id) => api.deleteSession(id),
      getUnfinishedSessionId: (workspaceId) => api.getUnfinishedSessionId(workspaceId),
      setUnfinishedSessionId: (id, workspaceId) => api.setUnfinishedSessionId(id, workspaceId),
    },
  },
});
```

Host apps own authentication, tenant routing, object storage, quotas, and
network transport. The record shape remains a Helios session envelope.

## Host Expectations

Different hosts own durable state differently:

- Helios Web can use browser storage or a remote/custom manager.
- Helios CLI stores sessions and side records in its filesystem storage root.
- Helios Widget mirrors one widget-owned session through Python traitlets and
  keeps the Python network as the source of truth.
- Helios Desktop treats the document file as the primary persistence object and
  delegates runtime state to CLI-backed sessions.

All hosts should write user-requested setting changes through `helios.states`
and expose storage status through `helios.storage.status()` or host-specific
wrappers around it.

