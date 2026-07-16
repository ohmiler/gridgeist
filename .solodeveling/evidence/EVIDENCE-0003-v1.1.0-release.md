---
solodeveling_schema: 1
---

# EVIDENCE-0003: v1.1.0 release

- **Release:** Gridgeist v1.1.0.
- **Tag commit:** `be518e96140944107cb65358b39f9672fb783b8e`.
- **Published:** 2026-07-16 Asia/Bangkok.
- **GitHub Release:** https://github.com/ohmiler/gridgeist/releases/tag/v1.1.0

## Publication evidence

- Pushed `main` and annotated tag `v1.1.0` to `origin`.
- GitHub Actions validation passed for the main push and tag push:
  - https://github.com/ohmiler/gridgeist/actions/runs/29506833703
  - https://github.com/ohmiler/gridgeist/actions/runs/29506830697
- Published a non-draft, non-prerelease GitHub Release named `Gridgeist v1.1.0`.

## Installation and upgrade evidence

### Codex plugin

- `codex plugin marketplace upgrade gridgeist` completed successfully.
- `codex plugin add gridgeist@gridgeist` completed successfully.
- `codex plugin list` reported `gridgeist@gridgeist` as installed and enabled at version `1.1.0`, sourced from `https://github.com/ohmiler/gridgeist.git` at ref `v1.1.0`.
- The local plugin cache moved from the previously installed v1.0.1 surface to `C:\Users\Miler\.codex\plugins\cache\gridgeist\gridgeist\1.1.0`.

### Agent Skills CLI

- In an isolated temporary project, `npx skills add ohmiler/gridgeist -s gridgeist -a codex -y --copy` completed successfully.
- `npx skills update gridgeist -p -y` reported `Updated gridgeist` and `Updated 1 skill(s)`.
- `npx skills list --json` reported the project-scoped `gridgeist` installation.
- `git diff --no-index` found no content difference between the installed `SKILL.md` and the tagged release source. File hashes differed only because the installer normalized line endings.
- The CLI emitted a non-blocking warning while checking for deleted skills from the repository; installation and update still completed successfully.

## Readiness decision

**Released.** Structural validation, behavioral evaluation, tagged-source installation, upgrade verification, CI, and GitHub Release publication passed.

Accepted gap: the 30 targeted evaluations were behavioral-only because no executable fixtures were supplied. The release does not claim rendered implementation, real-user usability, or accessibility conformance from those runs.
