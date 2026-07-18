---
solodeveling_schema: 1
---

# EVIDENCE-0011: v1.1.1 release

- **Work item:** `WORK-0009-release-v1.1.1`
- **Opened:** 2026-07-18
- **Decision:** Ready with one bounded pre-publication gap: tagged remote install
  verification must run after the `v1.1.1` tag exists.

## Candidate

- Version: `1.1.1`
- Source revision: pending release commit
- Artifact digest: pending release commit
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

Pending.

## Limitations

Pending final reconciliation.
