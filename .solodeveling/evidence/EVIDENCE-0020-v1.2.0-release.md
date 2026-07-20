---
solodeveling_schema: 1
---

# EVIDENCE-0020: v1.2.0 release

- **Work item:** `WORK-0018-release-v1.2.0`
- **Opened:** 2026-07-20
- **Decision:** Released. Candidate validation, main/tag CI, GitHub publication,
  public Docs, and independent post-release installation checks passed.

## Release identity

- Version: `1.2.0`
- Release revision: `d7700d0f961e862d3aca4f51ef4e512b4254d8d4`
- Release tree: `3e472d7a035c4d671bc943e566face56f3929a04`
- Annotated tag object: `004e7db39b5a9bb9df903b5fe3f630703d75d4f5`
- Installable skill Git tree: `c30e6c2a359e7d94b9b56adaf14eb124efb519f9`
- Last known-good before release: `v1.1.2`
- Release: https://github.com/ohmiler/gridgeist/releases/tag/v1.2.0

## Current acceptance matrix

| Boundary | Evidence | Result |
| --- | --- | --- |
| Release notes and intended behavior | Changelog records the system contract, design-system coherence, provisional-direction hard stop, and explicit visual-skill ownership inherited from `EVIDENCE-0019`. | Pass |
| Version and distribution metadata | Plugin manifest, marketplace ref, changelog section/comparison links, and English/Thai Docs labels identify `1.2.0`; repository release validator passed. | Pass |
| Static local candidate gates | Plugin Creator validator, skill quick validator, release validator with `--release-version 1.2.0`, both fixture syntax checks, and `git diff --check` passed. | Pass |
| Codex pre-publication install | A temporary loopback HTTP Git marketplace containing the exact candidate passed clean install, discovery, enablement, refresh, reinstall, and version checks at `1.2.0`. | Pass |
| Universal installer delivery | Tag CI and a separate public-source run installed `gridgeist` from `ohmiler/gridgeist`, created source metadata, and reported the global skill up to date on update. | Pass |
| Exact candidate identity | Behavior base `a17064f0b0077aa88274b1d078d765bd711b0407`; preparation base `168a1870344cc2911ed063b9d05ce77e8acecc62`; installable skill Git tree `c30e6c2a359e7d94b9b56adaf14eb124efb519f9`. | Pass |
| Scope isolation | Exact-path staging contains only manifest, marketplace, state, WORK, EVIDENCE, changelog, and English/Thai Docs files. Pre-existing unrelated untracked files remain excluded. | Pass |
| Publication and observation | `main` and annotated tag `v1.2.0` were atomically pushed; main/tag CI, Pages, public GitHub Release, English/Thai Docs, Codex plugin, and universal installer checks passed. | Pass |

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

## Publication observation

- Atomically pushed `main` from `8f4b885` to release revision `d7700d0` together
  with annotated tag `v1.2.0`. A post-push fetch found local/remote divergence `0 0`.
- Main validation passed:
  https://github.com/ohmiler/gridgeist/actions/runs/29751299052
- Tag validation and tagged installation smoke passed:
  https://github.com/ohmiler/gridgeist/actions/runs/29751297428
- GitHub Pages deployment passed:
  https://github.com/ohmiler/gridgeist/actions/runs/29751298764
- Published `Gridgeist v1.2.0` as a public, non-draft, non-prerelease GitHub Release
  at `2026-07-20T14:36:32Z`:
  https://github.com/ohmiler/gridgeist/releases/tag/v1.2.0
- Cache-busted English and Thai Docs requests returned HTTP 200, with 14,955 and
  22,284 response bytes respectively, and both displayed version `1.2.0`.
- Independent `python -X utf8 scripts/smoke_test_install.py --timeout 180` passed
  from public `ohmiler/gridgeist`. Codex installed and enabled
  `gridgeist@gridgeist` at `1.2.0` from Git ref `v1.2.0`, refreshed the marketplace,
  and reinstalled without errors. The universal installer completed a clean copy,
  recorded the public source, and reported the global skill up to date on update.
- Temporary-home warnings said Codex would not create helper PATH aliases under a
  temporary directory. Plugin discovery, version, source, enablement, refresh,
  reinstall, and universal installer assertions still passed.

## Limitations

- Fresh-agent behavior remains nondeterministic, and the behavioral evaluation's
  Windows full-access harness was not OS-hermetic.
- Scenario 13 remains a boundary smoke rather than a full post-repair implementation
  regression.
- This release does not claim WCAG conformance, real-user usability, field Core Web
  Vitals, or universal behavior across untested external projects.
