---
solodeveling_schema: 1
---

# EVIDENCE-0011: v1.1.1 release

- **Work item:** `WORK-0009-release-v1.1.1`
- **Opened:** 2026-07-18
- **Decision:** Released. Candidate validation, tag CI, GitHub publication, and
  post-release installation checks passed.

## Candidate

- Version: `1.1.1`
- Source revision: `d47389ac98fcd28ed8b6e1303c77634840b70ee3`
- Git tree: `26fde3f017dc0aed514706c3c0e73aeddc744e28`
- Skill SHA-256: `3e6efb82129a82edf504d6a7ef5a24afa2a11c35badc2b78a2f3d9938ed1545e`
- Target: public Git-backed Codex marketplace and GitHub Release
- Last known-good: `v1.1.0`

## Inherited behavioral evidence

`EVIDENCE-0010-direction-alignment.md` records the reproduced v1.1.0 gap, the
conditional gate, EN/TH ambiguous and explicit controls, Review and narrow-repair
regressions, executable fixture checks, raw outputs, and limitations.

## Preflight

- `python scripts/validate_release.py --release-version 1.1.1` passed.
- Plugin Creator `validate_plugin.py .` passed against the repository plugin.
- Skill Creator `quick_validate.py skills/gridgeist` passed.
- `node --check evals/fixtures/direction-alignment/script.js` passed.
- `python -m py_compile scripts/validate_release.py scripts/smoke_test_install.py`
  passed; its generated `scripts/__pycache__` was removed afterward.
- `git diff --check` passed with only line-ending conversion warnings.
- The candidate contains no dependency, lockfile, schema, migration, secret,
  production-data, or runtime configuration change.
- Scoped status review identified `.agents/skills/` as an unrelated untracked local
  bundle; it is explicitly excluded from staging and the release artifact.

### Installer preflight boundary

- The first isolated universal-installer run could not reach npm inside the sandbox
  (`EACCES`). The approved network retry installed the local `gridgeist` skill and
  validated that the CLI discovered the repository source, but the smoke harness
  stopped because local-copy installs do not create the remote source lock required
  by its update assertion.
- The public Codex catalog intentionally points to the not-yet-created `v1.1.1` Git
  tag, so an authentic clean marketplace install cannot pass before publication.
- This gap is bounded to delivery verification, not candidate content. The tag CI
  runs the same smoke harness against `ohmiler/gridgeist`; publication and closure
  remain conditional on that tagged remote smoke and one post-release install.

## Publication and observation

- Pushed `main` from `6fe2d98` to release commit `d47389a` and pushed annotated
  tag `v1.1.1`; the remote was fetched immediately beforehand and was a clean
  fast-forward with no pre-existing local or remote `v1.1.1` tag.
- Main validation passed:
  https://github.com/ohmiler/gridgeist/actions/runs/29635907170
- Tag validation and live clean-install smoke passed, including tag identity, Codex
  plugin clean install/refresh/reinstall, and universal installer install/update:
  https://github.com/ohmiler/gridgeist/actions/runs/29635907206
- The release commit's GitHub Pages deployment passed:
  https://github.com/ohmiler/gridgeist/actions/runs/29635907172
- Published a public, non-draft, non-prerelease GitHub Release at 2026-07-18
  14:33 Asia/Bangkok:
  https://github.com/ohmiler/gridgeist/releases/tag/v1.1.1
- A separate post-release `python scripts/smoke_test_install.py --timeout 180` run
  passed from the public `ohmiler/gridgeist` source in disposable homes. Codex
  reported `gridgeist@gridgeist` installed and enabled at version `1.1.1`, sourced
  from `https://github.com/ohmiler/gridgeist.git` ref `v1.1.1`; marketplace refresh
  and reinstall returned no errors. The universal installer then completed a clean
  install and reported the skill up to date on update.
- The post-release Codex CLI emitted non-blocking warnings that it would not create
  PATH helper aliases under a temporary directory. Plugin discovery, version,
  enablement, source identity, refresh, reinstall, and both installer assertions
  still passed.
- Cache-busted requests to the public English and Thai Docs both returned HTTP 200;
  each contained version `1.1.1` and its localized direction-alignment guidance.
- The post-release evidence closure commit `f2c4deb` passed repository validation:
  https://github.com/ohmiler/gridgeist/actions/runs/29636053827

## Limitations

- The direction-decision behavior remains nondeterministic and was sampled once per
  language/scenario, with one focused English rerun after the threshold repair.
- The release claims the conditional pre-edit collaboration behavior and the scoped
  executable fixture checks in EVIDENCE-0010. It does not claim general usability
  research, accessibility conformance, performance, or validation across 3–5
  external projects.
- Two disposable pre-release CLI directories may remain locked in `C:\tmp` until
  their Windows handles are released; they contain only fictional fixture copies and
  are unrelated to the published artifact.
