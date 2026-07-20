---
solodeveling_schema: 1
---

# WORK-0018: Prepare Gridgeist v1.2.0

- **Status:** Ready
- **Class:** Standard, audited release preparation
- **Opened:** 2026-07-20
- **Operator:** Codex, acting on the repository owner's instruction
- **Authority:** The user authorized version alignment, local validation, evidence,
  and a release-preparation commit. Push, tag creation, GitHub Release publication,
  and other production-changing actions are not authorized.

## Goal

Prepare the verified system-contract and alignment behavior as a reviewable
Gridgeist v1.2.0 release candidate without publishing it.

## Release boundary

- **Version:** `1.2.0`
- **Behavior base:** `a17064f0b0077aa88274b1d078d765bd711b0407`
- **Preparation base:** `168a1870344cc2911ed063b9d05ce77e8acecc62`
- **Source:** current `main` plus release metadata and release records; the final
  preparation revision and tree will be recorded after commit.
- **Artifact:** A local release-preparation commit. The future public artifact would
  be annotated tag `v1.2.0`, but creating it is outside current authority.
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
6. No push, tag, GitHub Release, marketplace publication, or production Docs action
   occurs without a separate explicit authorization.

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
