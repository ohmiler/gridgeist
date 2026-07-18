---
solodeveling_schema: 1
---

# WORK-0013: Release Gridgeist v1.1.2

- **Status:** Done
- **Class:** Standard, Audited release work
- **Opened:** 2026-07-18
- **Operator:** Codex, acting on the repository owner's instruction
- **Authority:** The user explicitly authorized the proposed v1.1.2 implementation and release, including skill and evaluation changes, version alignment, validation, commit, tag, push, GitHub Release publication, and post-release checks.
- **Released:** 2026-07-18
- **Tag:** `v1.1.2` at `43664adf7a2db727655dcbfef8d7f4572c29ed47`
- **Release:** https://github.com/ohmiler/gridgeist/releases/tag/v1.1.2

## Goal

Publish the verified resilience guidance already on `main` plus the smallest core
coordination rule that prevents silent blending of competing art-direction skills.

## Release candidate

- **Version:** `1.1.2`
- **Source:** current `main` plus companion coordination, paired scenario 18, and release metadata; final revision and digests will be recorded before tagging.
- **Artifact:** Annotated Git tag `v1.1.2` and public GitHub Release backed by the repository plugin source.
- **Target:** Public Git-backed Codex marketplace, universal installer, GitHub Release, and version labels on the existing Docs site.
- **Compatibility:** Patch-compatible with `1.1.x`; no schema, dependency, migration, production-data, API, or runtime configuration change.

## Acceptance

1. Gridgeist remains the sole default owner of product and visual direction while companions remain optional and capability-based.
2. Explicit requests for overlapping art-direction skills establish one owner before editing rather than silently blending defaults.
3. English and Thai suites contain equivalent contiguous scenarios 1–18.
4. Plugin manifest, marketplace ref, changelog, Docs version labels, and tag identify `1.1.2`.
5. Skill, plugin, repository, syntax, diff, and broadest practical install gates pass for the exact candidate.
6. Only release-scoped files and the directly inherited WORK-0012/EVIDENCE-0014 memory are committed; unrelated local dogfood/prototype artifacts remain excluded.
7. `main` and annotated tag `v1.1.2` are pushed, CI succeeds, a public GitHub Release is published, and a fresh post-release install exposes the updated skill.

## Risks and recovery

- **Known gaps:** Scenarios 16–18 specify behavioral expectations but have not been independently forward-run; model behavior remains nondeterministic.
- **Last known-good:** `v1.1.1`.
- **Rollback trigger:** Invalid metadata, failed tagged install, missing skill discovery, CI failure, or material regression in explicit-direction, Review, or narrow-repair behavior.
- **Recovery:** Stop before publication on failed preflight. After publication, issue a forward patch or temporarily repoint the marketplace to `v1.1.1`; do not move an existing tag.
- **Observation window:** Through main/tag CI, GitHub Release publication, and one fresh isolated post-release plugin/universal installation check.

## Plan

1. Add compact coordination behavior and paired scenario 18.
2. Align v1.1.2 release metadata and public version labels.
3. Run local candidate validation and inspect the exact staged scope.
4. Commit and tag the candidate, push main/tag, and observe CI.
5. Publish the GitHub Release and run fresh installation verification.
6. Reconcile evidence and state, archive this work, and push the closure record.

## Delivered

- Added a 3-rule, capability-based companion boundary while keeping Gridgeist the
  default owner of product and visual direction and adding no dependency.
- Added equivalent English and Thai scenario 18 alongside the inherited resilience
  scenarios 16–17.
- Aligned plugin version, marketplace tag, changelog, and English/Thai Docs labels at
  `1.1.2` without changing the production site design or behavior.
- Passed local validators, main/tag CI, tagged and separate post-release installation
  smoke, public Docs checks, and GitHub Release publication.
- Preserved unrelated dogfood/prototype runs and local `.agents/skills/` outside the
  release and closure commits.

## Evidence

- `.solodeveling/evidence/EVIDENCE-0014-resilience-guidance.md`
- `.solodeveling/evidence/EVIDENCE-0015-v1.1.2-release.md`
