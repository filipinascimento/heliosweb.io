# Builder Skill

Short name: **Builder Skill**.

The Helios Web Builder Skill helps agents create standalone Helios Web
visualizations instead of only editing snippets. It bundles reference notes,
Vite starter templates, richer analytics-interface templates, reusable UI
snippets, conversion scripts, and verification guidance for apps built with
`helios-web` and `helios-network`.

Project link: https://github.com/filipinascimento/helios-web-builder-skill

## When To Use It

Use the Builder Skill when an agent needs to:

- create a new standalone Helios visualization app;
- adapt or debug an existing browser-based Helios visualization;
- package local XNET, ZXNet JSON, GT/Netzschleuder, graph, or embedding data;
- build compact panels, filters, search, hover cards, legends, density controls,
  or quick controls around a full-screen canvas;
- verify a generated visualization with install, build, and browser smoke
  checks.

For controlling a running Helios session, use the [Helios CLI](helios-cli.md)
and its CLI Skill instead.

## Install In Codex

```sh
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
git clone https://github.com/filipinascimento/helios-web-builder-skill.git \
  "${CODEX_HOME:-$HOME/.codex}/skills/helios-web-builder-skill"
```

Restart Codex or start a new thread, then invoke it explicitly:

```text
Use $helios-web-builder-skill to build a standalone Helios visualization.
```

## Install In Claude

```sh
mkdir -p "$HOME/.claude/skills"
git clone https://github.com/filipinascimento/helios-web-builder-skill.git \
  "$HOME/.claude/skills/helios-web-builder-skill"
```

Then ask Claude to use the skill by name:

```text
Use the helios-web-builder-skill to build a standalone helios-web visualization.
```

## What It Provides

- Minimal Vite standalone template for small static visualizations.
- Analytics-interface template for search, filters, panels, density toggles, and
  richer exploration tools.
- UI snippets for sliders, segmented controls, checklists, relationship
  browsers, hover cards, and compact panels.
- Data-loading recipes for XNET, ZXNet, GT/Netzschleuder, programmatic graphs,
  and embedding maps.
- Remote-query guidance for API probing, visible download caps, progress,
  cancellation, and frontend-only workflows.
- Verification guidance for `npm install`, `npm run build`, browser checks, and
  canvas/console smoke tests.

## Quick Test

```sh
cd helios-web-builder-skill
node scripts/create-standalone-viz.mjs /tmp/helios-skill-demo \
  --name helios-skill-demo \
  --title "Helios Skill Demo"
cd /tmp/helios-skill-demo
npm install
npm run build
```

The generated app should be self-contained: it should not depend on parent
directories from the original Helios workspace.
