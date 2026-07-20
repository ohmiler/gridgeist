---
solodeveling_schema: 1
---

# EVIDENCE-0020: v1.2.0 release preparation

- **Work item:** `WORK-0018-release-v1.2.0`
- **Opened:** 2026-07-20
- **Decision:** Ready for a local release-preparation commit. Publication is not
  authorized; tagged delivery remains unverified.

## Current acceptance matrix

| Boundary | Evidence | Result |
| --- | --- | --- |
| Release notes and intended behavior | Changelog records the system contract, design-system coherence, provisional-direction hard stop, and explicit visual-skill ownership inherited from `EVIDENCE-0019`. | Pass |
| Version and distribution metadata | Plugin manifest, marketplace ref, changelog section/comparison links, and English/Thai Docs labels identify `1.2.0`; repository release validator passed. | Pass |
| Static local candidate gates | Plugin Creator validator, skill quick validator, release validator with `--release-version 1.2.0`, both fixture syntax checks, and `git diff --check` passed. | Pass |
| Codex pre-publication install | A temporary loopback HTTP Git marketplace containing the exact candidate passed clean install, discovery, enablement, refresh, reinstall, and version checks at `1.2.0`. | Pass |
| Universal installer boundary | Local-path installation found and copied the exact candidate skill, but intentionally did not create Git source-lock metadata; the full tagged Git install/update check remains a publication gate. | Partial; deferred |
| Exact candidate identity | Behavior base `a17064f0b0077aa88274b1d078d765bd711b0407`; preparation base `168a1870344cc2911ed063b9d05ce77e8acecc62`; installable skill Git tree `c30e6c2a359e7d94b9b56adaf14eb124efb519f9`. | Pass |
| Scope isolation | Exact-path staging contains only manifest, marketplace, state, WORK, EVIDENCE, changelog, and English/Thai Docs files. Pre-existing unrelated untracked files remain excluded. | Pass |
| Publication boundary | User authorized local preparation and commit only; push, tag, GitHub Release, marketplace publication, and production Docs remain unauthorized. | Pass |

## Inherited evidence

`EVIDENCE-0019-system-contract-behavioral-eval.md` records six clean bilingual
Scenario 19 runs, independent responsive browser checks, artifact-boundary checks,
and repaired English/Thai direction-alignment and companion-ownership guardrails for
behavior candidate `a17064f0b0077aa88274b1d078d765bd711b0407`.

## Preflight observations

- `python -X utf8 .../plugin-creator/scripts/validate_plugin.py .` passed:
  `Plugin validation passed`.
- `python -X utf8 .../skill-creator/scripts/quick_validate.py skills/gridgeist`
  passed: `Skill is valid!`.
- `python -X utf8 scripts/validate_release.py --release-version 1.2.0`
  passed: skill, release metadata, Docs, installation guidance, and bilingual eval
  numbering are aligned.
- `node --check` passed for the direction-alignment and design-system-coherence
  fixtures; `git diff --check` passed with non-blocking line-ending warnings.
- The first synthetic smoke construction used a working-tree patch against a temp
  clone; Docs line-ending differences prevented the patch from applying atomically,
  so the harness correctly rejected the unchanged `1.1.2` temp manifest. Rebuilding
  the fixture from exact-path copies removed that harness defect.
- A local-path marketplace proved initial `1.2.0` install but cannot run
  `marketplace upgrade`. A loopback HTTP Git marketplace then passed the complete
  Codex install/refresh/reinstall path without external network or a real tag.
- The universal installer successfully discovered and copied `gridgeist` from the
  exact local candidate. The repository harness then rejected the run because local
  paths do not create `.skill-lock.json`; dumb HTTP could not satisfy its shallow
  clone. The public tagged Git source remains the authoritative delivery check.
- All temporary roots created for these runs were removed. One unrelated
  `C:/tmp/gridgeist-remote-smoke-*` directory dated 2026-07-14 was inspected but not
  modified because it predates and is outside this work.

## Limitations

- Public delivery, main/tag CI, GitHub Release state, production Docs, and tagged
  clean installation cannot be claimed until separately authorized and observed.
- Fresh-agent behavior remains nondeterministic, and the behavioral evaluation's
  Windows full-access harness was not OS-hermetic.
- Scenario 13 remains a boundary smoke rather than a full post-repair implementation
  regression.
- Universal-installer Git source metadata and update behavior remain unverified for
  `v1.2.0` until the public tag exists; this is a publication gate, not evidence of a
  candidate-content failure.
