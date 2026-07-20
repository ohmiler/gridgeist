---
solodeveling_schema: 1
---

# WORK-0018: Release Gridgeist v1.2.0

- **Status:** Done
- **Class:** Standard, audited release work
- **Opened:** 2026-07-20
- **Operator:** Codex, acting on the repository owner's instruction
- **Authority:** The user first authorized version alignment, local validation,
  evidence, and a release-preparation commit, then explicitly instructed Codex to
  proceed with the proposed publication on 2026-07-20. This covers remote preflight,
  pushing `main`, annotated tag creation and push, GitHub Release publication,
  production Docs observation, tagged installation checks, and release closure.
- **Released:** 2026-07-20
- **Tag:** `v1.2.0` at `d7700d0f961e862d3aca4f51ef4e512b4254d8d4`
- **Release:** https://github.com/ohmiler/gridgeist/releases/tag/v1.2.0

## Goal

Publish the verified system-contract and alignment behavior as Gridgeist v1.2.0 and
observe the public delivery paths through their release gates.

## Release boundary

- **Version:** `1.2.0`
- **Behavior base:** `a17064f0b0077aa88274b1d078d765bd711b0407`
- **Preparation base:** `168a1870344cc2911ed063b9d05ce77e8acecc62`
- **Preparation revision:** `c91c5aaa23155da2a8034adc0e1b57bcc1225557`
- **Preparation tree:** `9a6f8bcf1f874313c3c6f259e35205cd58cb0c73`
- **Release revision:** `d7700d0f961e862d3aca4f51ef4e512b4254d8d4`
- **Release tree:** `3e472d7a035c4d671bc943e566face56f3929a04`
- **Annotated tag object:** `004e7db39b5a9bb9df903b5fe3f630703d75d4f5`
- **Artifact:** Annotated tag `v1.2.0` and a public GitHub Release backed by the
  repository plugin source.
- **Target:** Public Git-backed Codex marketplace, universal installer, GitHub
  Release, and version labels on the Docs site.
- **Compatibility:** Backward-compatible with `1.x`; no dependency, schema,
  migration, production-data, API, secret, or runtime-configuration change.

## Acceptance

1. The v1.2.0 notes accurately describe the system contract, design-system
   coherence, provisional-direction hard stop, and explicit visual-skill ownership.
2. Plugin manifest, marketplace ref, changelog, comparison links, and English/Thai
   Docs labels identify `1.2.0`.
3. Skill, plugin, repository, syntax, and diff-integrity gates pass. A synthetic
   Git-backed Codex marketplace proves clean install, refresh, and reinstall for
   `1.2.0`; the public tagged universal-install/update smoke remains a publication
   gate.
4. The prepared scope contains only release metadata and WORK/EVIDENCE/state records;
   unrelated local dogfood, prototype, and skill files remain excluded.
5. The prepared candidate is bound to its behavior and preparation bases plus the
   installable skill Git tree. The resulting local commit is reported at handoff and
   must be recorded before publication.
6. `main` and annotated tag `v1.2.0` are pushed, main/tag CI succeeds, a public
   GitHub Release is published, public English/Thai Docs identify `1.2.0`, and fresh
   tagged Codex plugin and universal-installer checks pass.

## Risks and recovery

- **Known gaps:** Fresh-agent behavior is nondeterministic; the Windows evaluation
  harness was not OS-hermetic; Scenario 13 is a boundary smoke rather than a full
  post-repair import regression; two empty temporary directories remain locked.
- **Last known-good:** `v1.1.2`.
- **Stop trigger:** Invalid metadata, validator failure, install smoke failure,
  unexpected staged scope, or loss of bilingual/version parity.
- **Recovery before publication:** Correct or revert the local preparation commit;
  `v1.1.2` remains the public marketplace ref and no tag is moved.
- **Post-publication recovery:** Prefer a forward patch or temporarily repoint the
  marketplace to `v1.1.2`; never move the existing release tag.
- **Observation window:** Completed through main/tag CI, GitHub Release publication,
  public English/Thai Docs, and an independent tagged installation/update check.

## Plan

1. Align v1.2.0 release metadata and public version labels.
2. Run local candidate validation and inspect the exact staged scope.
3. Record candidate identity, checks, limitations, and publication boundary.
4. Create a local release-preparation commit and stop before external effects.
5. Reconfirm remote identity and publish `main` plus annotated tag `v1.2.0`.
6. Observe main/tag CI, publish the GitHub Release, and verify public Docs and tagged
   installation paths.
7. Reconcile evidence and state, archive the work, and push the closure record.

## Preparation result

- Release metadata and English/Thai Docs labels identify `1.2.0`.
- Plugin, skill, release, fixture-syntax, and diff-integrity validators pass.
- A loopback Git-backed synthetic marketplace passed Codex clean install, discovery,
  enablement, refresh, reinstall, and version checks at `1.2.0`.
- The universal installer found and copied the exact local candidate skill. Its
  source-lock/update assertion requires a shallow-capable Git source, so the public
  tagged install/update run remains an explicit publication gate.
- Exact-path staging contains only the eight release metadata and lifecycle files;
  unrelated untracked dogfood, prototype, and local skill files remain excluded.
- No push, tag, GitHub Release, marketplace publication, or production Docs action
  occurred.

## Release result

- Atomically pushed `main` and annotated tag `v1.2.0`; remote tag identity matches
  the local annotated tag object and points to release revision `d7700d0`.
- Main validation, tag validation with installation smoke, and GitHub Pages
  deployment passed for the release revision.
- Published a public, non-draft, non-prerelease GitHub Release at
  https://github.com/ohmiler/gridgeist/releases/tag/v1.2.0.
- Cache-busted public English and Thai Docs returned HTTP 200 and displayed `1.2.0`.
- A separate public-source smoke passed Codex plugin clean install, discovery,
  marketplace refresh, reinstall, and enablement at `1.2.0`, plus universal installer
  clean install and update from `ohmiler/gridgeist`.
- Unrelated local dogfood, prototype, and workspace skill files remained untracked
  and outside every release commit.

## Evidence

- `.solodeveling/evidence/EVIDENCE-0019-system-contract-behavioral-eval.md`
- `.solodeveling/evidence/EVIDENCE-0020-v1.2.0-release.md`
