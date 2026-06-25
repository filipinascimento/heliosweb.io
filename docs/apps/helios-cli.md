# Helios CLI

Helios CLI is the automation and agent-facing host for Helios Web sessions. It
starts a local session daemon, serves a Helios Web client, optionally opens a
browser, and exposes JSON-RPC methods for scene, network, camera, layout,
mappers, filters, labels, legends, density, metrics, picking, persistence, and
figure export.

Project link: https://www.npmjs.com/package/helios-cli

## When To Use It

Use the CLI when you need:

- reproducible local sessions from scripts or agents;
- headless or headed browser control without wiring a web app;
- network inspection and conversion from the terminal;
- figure export from a saved or generated scene;
- a bridge that desktop and other hosts can reuse.

## Basic Commands

```sh
helios version
helios browser install
helios inspect ./graph.xnet --json
helios session start --network ./graph.zxnet
helios session list
helios session state <sessionId>
helios state set <sessionId> scene.dimension '"3d"'
helios state reset <sessionId> scene.dimension
helios call <sessionId> camera.frame --json '{"animate":true}'
helios call <sessionId> persistence.status
helios call <sessionId> persistence.save --json '{"fullSession":true}'
helios call <sessionId> export.figure --json '{"format":"png","preset":"window","outputPath":"./figure.png"}'
helios session stop <sessionId>
```

Supported network inputs are `.xnet`, `.zxnet`, `.bxnet`, `.gml`, `.gt`, and
`.gt.zst`. GML and GT are lossy graph interchange formats in the
browser/desktop workflow and should not be used for full Helios state
round-trips. See the [data formats guide](../guides/data-formats/index.md) for the
full matrix.

## Session Modes

`helios session start` defaults to server mode and opens the URL with the
platform browser opener. Use:

- `--mode server --no-open` to serve without opening a browser;
- `--mode headless` for automated rendering and export;
- `--mode headed` for Playwright-managed visual debugging;
- `--renderer webgl` or `--renderer webgpu` to request a renderer.

Managed browser sessions are independent from the user's browser profile unless
an explicit Playwright channel is requested.

## Persistence

CLI sessions use the same frontend state machine as Helios Web, but the durable
store is owned by the CLI daemon:

- sparse state overrides mirror `helios.states`;
- full session checkpoints default to compact `.zxnet` network payloads;
- position side records are stored separately from network payloads;
- thumbnails are kept in the private session JSON payload;
- runtime daemon metadata lives under the CLI runtime storage root.

The default storage root is under the user's Helios CLI storage directory. Use
global `--storage-dir <path>` or `HELIOS_CLI_STORAGE_DIR` to choose another root.

CLI-origin changes should use `helios state set` or RPC methods that write
through `helios.states` with source `cli`. This keeps durable state sparse and
prevents binding refreshes from being mistaken for user overrides.

## RPC Groups

Common RPC groups include:

- `scene.*` for scene status, render requests, and dimension changes;
- `network.*` for stats, load/replace/save, inspect, and attribute mutation;
- `camera.*` for pose, transitions, controls, and framing;
- `layout.*` for layout selection, parameters, start/stop, and position source;
- `mappers.*`, `filters.*`, `labels.*`, `legends.*`, and `density.*` for
  visualization behavior state;
- `metrics.measure` and `aesthetic.measure` for measurements;
- `persistence.*` and `state.*` for storage status, sparse overrides, reset,
  checkpoint, flush, and session save/restore;
- `export.figure` for PNG/SVG figure export.

## Relationship To Desktop

Helios Desktop uses CLI sessions as its document backend. A desktop window is
therefore visible to CLI tooling through session list/info/state/call commands
while the app is running.
