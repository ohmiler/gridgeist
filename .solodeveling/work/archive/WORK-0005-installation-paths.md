---
solodeveling_schema: 1
---

# WORK-0005: Align installation guidance and verify release installs

- **Status:** Done
- **Class:** Standard
- **Problem:** The public Quickstart leads with manual cloning even though the accepted distribution decision makes the Codex Git marketplace and `npx skills` the primary channels. Release validation checks metadata and documentation strings but does not exercise clean installation, refresh, or update behavior.

## Goal

Make the recommended installation paths the first public experience and add an isolated release smoke test for both supported distribution channels.

## Acceptance criteria

1. English and Thai Quickstarts present the Codex plugin and universal installer before manual copying.
2. Detailed installation guidance consistently treats the Codex plugin as primary, `npx skills` as the cross-agent channel, and manual copying as fallback.
3. A dependency-free, cross-platform script exercises a clean Codex plugin install, Git marketplace refresh, reinstall, and installed skill/version checks in a temporary `CODEX_HOME`.
4. The same script exercises a clean universal install, documented update command, and installed skill checks in an isolated temporary user home.
5. Release-tag and manual CI runs install the required current CLIs and execute the smoke test after metadata validation; ordinary pull requests retain the fast offline validator.
6. Release validation, smoke tests, script syntax, documentation consistency, and repository whitespace checks pass without touching the user's existing agent installation.

## Plan

1. Add a Python smoke runner that isolates homes, invokes native commands without a shell, validates JSON/files/version, and always cleans temporary state.
2. Update English and Thai Quickstart and installation ordering while preserving the same source-of-truth commands.
3. Extend validation to require the recommended Quickstart ordering and smoke-test CI wiring.
4. Add a tag/manual CI job that installs Codex, invokes the smoke runner, and depends on metadata validation.
5. Run focused local tests for both real distribution channels, then the full offline validation and diff checks.

## Risks and recovery

- The release smoke job depends on GitHub, npm, Codex CLI, and the open agent skills CLI; keep it off ordinary pull requests so upstream/network instability does not block routine contributions.
- The script must isolate `CODEX_HOME`, `HOME`, `USERPROFILE`, and npm cache so it cannot mutate personal installations.
- Rollback is a normal revert of the documentation, script, validator, and workflow changes; no production data or user configuration is changed.

## Pre-implementation findings

- Codex CLI requires the temporary `CODEX_HOME` directory to exist before invocation.
- `codex plugin marketplace upgrade` applies only to configured Git marketplaces, so the smoke path must add `ohmiler/gridgeist`, not the local checkout.
- A clean Git marketplace install, refresh, and reinstall succeeded with Codex CLI 0.144.5 in an isolated probe.
- A clean `npx skills add` followed by `npx skills update gridgeist -g -y` succeeded in an isolated probe.

## Outcome

English and Thai Quickstarts now lead with the Codex plugin and universal installer, while clone/copy instructions are explicitly a manual fallback. A cross-platform, dependency-free Python runner exercises both live distribution lifecycles in temporary homes, release validation protects the intended ordering and workflow wiring, and tag/manual GitHub Actions runs now execute the smoke test after metadata validation. Local verification passed; the first hosted workflow execution remains to be observed on a future tag or manual dispatch. Evidence is recorded in `EVIDENCE-0007-installation-paths.md`.
