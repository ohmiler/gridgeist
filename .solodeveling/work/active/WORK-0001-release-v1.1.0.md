---
solodeveling_schema: 1
---

# WORK-0001: Release Gridgeist v1.1.0

- **Status:** Verifying
- **Class:** Standard, Audited release work
- **Candidate:** Gridgeist plugin v1.1.0 payload at release-candidate commit `316e0b1`.
- **Target:** Public GitHub repository, Git-backed Codex marketplace, GitHub Release, and Agent Skills-compatible Git installers.
- **Operator:** Repository owner through Codex in the current workspace.
- **Compatibility:** Preserve the `gridgeist` skill and plugin identifiers and existing Create, Redesign, and Review invocation patterns.

## Goal

Publish the brand-adaptive Gridgeist revision with a stable version identity, simple update commands, automated consistency checks, and evidence that existing users can move from v1.0.1.

## In scope

- Make Solodeveling the durable repository workflow.
- Add English and Thai update guidance.
- Align plugin manifest, marketplace release ref, changelog, and release tag at v1.1.0.
- Add automated structural and release-consistency validation.
- Run skill/plugin validation and targeted behavioral evaluation.
- Test clean install and upgrade behavior before publication.
- Publish the Git tag and GitHub Release only after a ready decision.

## Out of scope

- Automatic network checks from inside the Gridgeist skill.
- Silent background updates.
- Publishing untracked `.agents/skills/` content without separate authorization.
- Claims of real-user usability or accessibility conformance from automated checks.

## Acceptance

- `AGENTS.md` requires Solodeveling for every repository task.
- Public docs give exact update commands for Codex plugins, global/project `npx skills`, Git clones, and manual copies.
- Release metadata consistently identifies v1.1.0 and the marketplace installs the tagged source.
- CI detects invalid skill structure, JSON/YAML errors, bilingual eval drift, and release-version mismatch.
- Targeted eval results and limitations are recorded at scenario level.
- A clean install and an upgrade from installed v1.0.1 are exercised or explicitly block publication.
- Release readiness is recorded as ready, not ready, or ready with accepted gaps before push/tag/release.

## Recovery

- Last known-good public artifact: v1.0.1.
- Rollback trigger: installation failure, missing skill discovery, invalid plugin metadata, or a material regression in preserved workflows.
- Recovery action: keep v1.0.1 as latest or repoint marketplace release ref to v1.0.1, document the failure, and issue a corrected patch release.

## Current evidence

- See `.solodeveling/evidence/EVIDENCE-0001-v1.1.0-preflight.md`.
- Independent behavioral runs are not yet authorized or recorded; publication remains not ready.
