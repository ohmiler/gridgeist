---
solodeveling_schema: 1
---

# Project

- **Name:** Gridgeist
- **Purpose:** Provide an installable agent skill and Codex plugin for creating, redesigning, and reviewing product-native web interfaces.
- **Users:** Developers and coding-agent users building web interfaces across Codex and other Agent Skills-compatible tools.
- **Architecture:** One installable skill under `skills/gridgeist/`, packaged by `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`, with behavioral evaluations, bilingual documentation, and a static GitHub Pages site.
- **Stack:** Markdown, YAML, JSON, static HTML/CSS/JavaScript, Git, GitHub Releases, and GitHub Actions.

## Durable constraints

- Follow `AGENTS.md`; never use `superpowers:*` or create `docs/superpowers/`.
- Keep `skills/gridgeist/SKILL.md` concise and route conditional detail through direct references.
- Treat `.codex-plugin/plugin.json` as the released plugin-version source of truth.
- Preserve English and Thai installation, update, and evaluation guidance together.
- Do not claim behavioral, accessibility, safety, or release verification without recorded evidence.

## Authoritative sources

- `AGENTS.md` — repository workflow instructions.
- `README.md` and `README.th.md` — public installation and usage guidance.
- `skills/gridgeist/` — installable skill source.
- `.codex-plugin/plugin.json` — plugin manifest and release version.
- `.agents/plugins/marketplace.json` — Git-backed marketplace source.
- `evals/prompts.md` and `evals/prompts.th.md` — behavioral evaluation protocol.
- `CHANGELOG.md` — user-facing release history.
