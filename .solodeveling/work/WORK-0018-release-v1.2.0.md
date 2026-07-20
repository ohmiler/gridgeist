---
solodeveling_schema: 1
---

# WORK-0018: Release Gridgeist v1.2.0

- **Status:** Active
- **Class:** Standard, audited release preparation
- **Opened:** 2026-07-20
- **Operator:** Codex, acting on the repository owner's instruction
- **Authority:** The user first authorized version alignment, local validation,
  evidence, and a release-preparation commit, then explicitly instructed Codex to
  proceed with the proposed publication on 2026-07-20. This covers remote preflight,
  pushing `main`, annotated tag creation and push, GitHub Release publication,
  production Docs observation, tagged installation checks, and release closure.

## Goal

Publish the verified system-contract and alignment behavior as Gridgeist v1.2.0 and
observe the public delivery paths through their release gates.

## Release boundary

- **Version:** `1.2.0`
- **Behavior base:** `a17064f0b0077aa88274b1d078d765bd711b0407`
- **Preparation base:** `168a1870344cc2911ed063b9d05ce77e8acecc62`
- **Preparation revision:** `c91c5aaa23155da2a8034adc0e1b57bcc1225557`
- **Preparation tree:** `9a6f8bcf1f874313c3c6f259e35205cd58cb0c73`
- **Source:** current `main` plus this publication-authority record; the tagged
  release revision and tree will be recorded after commit.
- **Artifact:** Annotated tag `v1.2.0` and a public GitHub Release backed by the
  repository plugin source.
- **Target:** Public Git-backed Codex marketplace, universal installer, GitHub
  Release, and version labels on the Docs site after separate publication authority.
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
- **Future publication recovery:** Stop before publication on failed preflight. After
  publication, prefer a forward patch or temporarily repoint the marketplace to
  `v1.1.2`; never move an existing release tag.
- **Observation window:** Local preparation checks now; main/tag CI, public release,
  Docs, and fresh tagged installation remain future publication gates.

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

## Evidence

- `.solodeveling/evidence/EVIDENCE-0019-system-contract-behavioral-eval.md`
- `.solodeveling/evidence/EVIDENCE-0020-v1.2.0-preparation.md`
