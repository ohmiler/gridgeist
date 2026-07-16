---
solodeveling_schema: 1
---

# EVIDENCE-0007: Installation guidance and release smoke tests

- **Work item:** `WORK-0005-installation-paths`
- **Date:** 2026-07-17
- **Target:** README installation guidance, release validation, and isolated installer behavior.
- **Result:** Pass locally; hosted GitHub Actions execution remains unobserved until a tag or manual run.

## Pre-implementation probes

| Check | Result |
| --- | --- |
| Codex CLI surface | Codex CLI 0.144.5 exposes JSON-capable marketplace add/upgrade, plugin add, and plugin list commands. |
| Missing temporary home | Confirmed Codex fails when `CODEX_HOME` points to a directory that does not exist; the smoke runner must create it first. |
| Local marketplace refresh | Confirmed local marketplace installation works but refresh fails by design because upgrade accepts Git marketplaces only. |
| Git marketplace lifecycle | In an isolated temporary `CODEX_HOME`, adding `ohmiler/gridgeist`, installing `gridgeist@gridgeist`, upgrading the marketplace, reinstalling, and listing the enabled v1.1.0 plugin all succeeded. |
| Universal lifecycle | In an isolated temporary home, `npx skills add ohmiler/gridgeist -g -a codex -s gridgeist -y --copy`, list, `npx skills update gridgeist -g -y`, and a second list all succeeded; the complete skill directory was present under `.agents/skills/gridgeist`. |

## Scope and limits

- Probes used temporary directories under `C:\tmp` and restored environment variables before cleanup.
- The first two Codex probes were diagnostic failures that established required preconditions; neither changed the repository or personal Codex configuration.
- The universal updater exposed an upstream Windows shutdown assertion only when `DISABLE_TELEMETRY=1` was set. Isolated reruns proved that `CI` and `NO_COLOR` are safe; the smoke runner does not override telemetry.
- The GitHub-hosted `smoke-install` job was parsed and inspected but not observed on GitHub because this work did not push a tag or dispatch the workflow.

## Acceptance verification

| Criterion | Method | Result |
| --- | --- | --- |
| EN/TH Quickstart ordering | Release validator plus diff inspection | Pass: first documented paths are Codex plugin, universal installer, then manual fallback. |
| Detailed channel priority | Diff inspection of both README files and existing EN/TH website cards | Pass: plugin is primary, `npx skills` is cross-agent, clone/copy is fallback. |
| Codex lifecycle | `python -X utf8 scripts/smoke_test_install.py` | Pass: temporary `CODEX_HOME`, Git marketplace add, v1.1.0 install, enabled listing, refresh, reinstall, manifest and skill-tree checks. |
| Universal lifecycle | Same combined smoke command | Pass: temporary user home/npm cache, GitHub install, lock metadata, skill-tree/list checks, documented update, and second list. |
| Release CI wiring | PyYAML parse and static workflow inspection | Pass: tag/manual-only `smoke-install` depends on `validate`, provisions Python 3.12 and Node 22, installs Codex, and runs the combined smoke script. Hosted execution is not yet observed. |
| Project checks and isolation | Release validator, official quick validator, in-memory Python compile, PyYAML parse, `git diff --check`, temporary-path assertions | Pass; only task files changed and the pre-existing untracked `.agents/skills/` directory was preserved. |

## Commands and observed results

- `python -X utf8 scripts/smoke_test_install.py` — pass for both live channels.
- `python -X utf8 scripts/validate_release.py` — `[OK] Gridgeist v1.1.0 skill, release metadata, docs, and evals are aligned.`
- `python -X utf8 "$HOME\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\skills\gridgeist` — `Skill is valid!`
- In-memory `compile(...)` for both Python scripts — pass without generating cache files.
- `yaml.safe_load(...)` plus smoke-job assertions — pass.
- `git diff --check` — pass; Git reported only expected future LF-to-CRLF conversion warnings on Windows.
