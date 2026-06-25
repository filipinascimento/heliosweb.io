# Apps And Integrations

Helios is split into reusable packages and host applications. The browser
renderer and network core are the shared runtime; CLI, widget, and desktop hosts
wrap that runtime for different workflows.

## Surfaces

| Surface | Audience | Runtime | Persistence owner |
| --- | --- | --- | --- |
| Helios Web | Web applications and embedded graph tools | Browser canvas with WebGPU/WebGL fallback | `helios.storage` in the page or host storage client |
| Helios CLI | Automation, agents, batch export, reproducible sessions | Local daemon plus Helios Web client | CLI filesystem session store |
| Helios Widget | Jupyter notebooks and Python-first exploration | AnyWidget/Jupyter or local browser fallback | Python traitlets plus Helios Web storage client |
| Helios Desktop | Native document workflow for network files | NW.js shell backed by CLI sessions | Desktop document checkpoint plus CLI session |

## Project Links

- Helios Web package: https://www.npmjs.com/package/helios-web
- Helios CLI package: https://www.npmjs.com/package/helios-cli
- Helios Widget package: https://github.com/filipinascimento/helios-widget
- Helios Desktop package: https://github.com/filipinascimento/helios-desktop

## Shared Contract

All hosts should preserve the same state model:

- UI and programmatic controls write through `helios.states`.
- Session, autosave, storage status, portable visualization state, and network
  snapshots flow through `helios.storage`.
- There is no separate `helios.session` facade. Session save/list/load/delete
  methods live on the storage manager.
- Host integrations can replace browser persistence with a remote/custom
  storage client while keeping the same state paths and session envelopes.

Use the pages below for host-specific setup and expectations:

- [Helios CLI](helios-cli.md)
- [Helios Widget](helios-widget.md)
- [Helios Desktop](helios-desktop.md)
