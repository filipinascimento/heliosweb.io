# Helios Desktop

Helios Desktop is the native document shell for Helios network files. It uses
NW.js for the app window and delegates each document view to a Helios CLI
session, so the desktop app does not maintain a separate visualization runtime.

Project link: https://github.com/filipinascimento/helios-desktop

Status: coming soon on the hosted website. The development documentation below
describes the desktop package shape and CLI-backed document model.

## When To Use It

Use Desktop when users need:

- double-clickable `.xnet`, `.zxnet`, `.bxnet`, `.gml`, `.gt`, or `.gt.zst`
  graph documents;
- native Open, Save, Save As, and Export Figure commands;
- platform file associations and file previews;
- native dirty-document prompts;
- a GUI document workflow that still remains scriptable through CLI sessions.

## Development

```sh
cd helios-desktop
npm install
npm run dev -- ../path/to/network.xnet
```

Build packages with:

```sh
npm run build:mac
npm run build:win
npm run build:linux
npm run build:all
```

Build artifacts are written under `helios-desktop/dist/<platform>-<arch>`.

## Document Model

Each document window starts a CLI daemon in desktop server mode and opens the
Helios Web client for that document. Native menu actions call CLI RPC methods:

- Open creates or replaces the active network document.
- Save and Save As call `network.save` with tracked Helios state and current
  positions attached.
- Export Figure calls `export.figure`.
- Dirty indicators combine Helios storage status with the desktop document
  checkpoint.

Browser-style session controls are hidden in desktop runtime. The document file
is the user's primary persistence object.

## File Formats

Desktop preserves Helios state directly in `.xnet`, `.zxnet`, and `.bxnet`
documents. `.gml`, `.gt`, and `.gt.zst` remain lossy graph interchange formats,
so desktop writes a sibling `<file>.helios-state.json` sidecar when it must
preserve tracked Helios state for those graph files.

## Native Integration

Platform-specific integration lives in native package folders:

- macOS document type and UTI declarations;
- macOS Quick Look preview using `helios inspect <path> --json`;
- Windows per-user file association registration;
- Linux `.desktop` and shared MIME metadata.

Signing and notarization are environment-driven. Packaged macOS builds should
merge document type declarations, embed the Quick Look extension, then sign and
notarize with Developer ID credentials.

## CLI Interoperability

Because Desktop windows are CLI-backed sessions, automation can inspect and
modify an open document with:

```sh
helios session list
helios session info <sessionId>
helios state get <sessionId>
helios state set <sessionId> scene.dimension '"3d"'
helios call <sessionId> camera.frame --json '{"animate":true}'
```
