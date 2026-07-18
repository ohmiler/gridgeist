---
solodeveling_schema: 1
---

# WORK-0009: Release Gridgeist v1.1.1

- **Status:** Active
- **Class:** Standard, Audited release work
- **Opened:** 2026-07-18
- **Operator:** Codex, acting on the repository owner’s instruction
- **Authority:** The user explicitly authorized continuing the proposed v1.1.1 release sequence, including version alignment, validation, commit/tag, push, GitHub Release publication, and post-release installation checks.

## Goal

Publish the verified conditional direction-alignment behavior as patch release
`v1.1.1`, while preserving explicit-direction, Review, and narrow-repair behavior and
including the already-landed installation and documentation improvements since
`v1.1.0`.

## Release candidate

- **Version:** `1.1.1`
- **Source:** current `main` plus the scoped direction-alignment work and release metadata; final commit and digest will be recorded before tagging.
- **Artifact:** Git tag `v1.1.1` and GitHub Release backed by the repository plugin source.
- **Target:** public Git-backed Codex marketplace and GitHub release channel.
- **Compatibility:** patch-compatible with the public `1.1.x` skill interface; no schema, dependency, migration, or production-data change.

## Acceptance

1. Plugin manifest, marketplace ref, changelog, bilingual version surfaces, and tag all identify `1.1.1`.
2. Direction-alignment evidence and raw EN/TH controls remain preserved and the repository validator passes for the release version.
3. Skill/plugin validation, fixture syntax, diff checks, and the broadest practical install smoke pass from the intended candidate.
4. Only release-scoped changes are committed; the unrelated untracked `.agents/skills/` bundle remains excluded.
5. `main` and annotated tag `v1.1.1` are pushed, CI succeeds, and a non-draft, non-prerelease GitHub Release is published.
6. A fresh post-release marketplace install reports version `1.1.1` and exposes the updated skill.
7. Release identity, observation, limitations, and recovery are recorded before closure.

## Risks and recovery

- **Known gaps:** behavioral output is nondeterministic and sampled once per language/scenario; full implementation usability and accessibility conformance are not claimed.
- **Last known-good:** `v1.1.0`.
- **Rollback trigger:** failed tagged installation, invalid metadata, missing skill discovery, CI failure, or a material regression in preserved workflows.
- **Recovery:** do not publish when preflight fails; after publication, restore availability by repointing the marketplace ref to `v1.1.0` in a corrective release or issue a forward patch. No data rollback is required.
- **Observation window:** through CI completion and one fresh isolated install/skill-surface verification after publication.

## Plan

1. Align release metadata and public version surfaces at `1.1.1`.
2. Run repository, skill, fixture, diff, and release-version validation.
3. Stage only scoped files, review the candidate, and create the release commit.
4. Tag and push the exact candidate, then observe CI.
5. Publish the GitHub Release and verify a fresh tagged marketplace installation.
6. Reconcile evidence and project memory, then archive this work.
