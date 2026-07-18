---
solodeveling_schema: 1
---

# EVIDENCE-0015: v1.1.2 release

- **Work item:** `WORK-0013-release-v1.1.2`
- **Opened:** 2026-07-18
- **Decision:** Preflight in progress. Publication remains conditional on the recorded gates.

## Candidate

- Version: `1.1.2`
- Source revision: pending release commit
- Git tree: pending release commit
- Skill SHA-256: pending release commit
- Target: public Git-backed Codex marketplace, universal installer, GitHub Release, and Docs version labels
- Last known-good: `v1.1.1`

## Inherited evidence

`EVIDENCE-0014-resilience-guidance.md` records scoped review-checklist resilience
guidance, paired scenarios 16–17, validation, limitations, and commit `50b36c5` on
`origin/main`. Scenarios 16–17 remain specified but not independently forward-run.

## Preflight

- `python -X utf8 .../skill-creator/scripts/quick_validate.py ./skills/gridgeist`
  passed: `Skill is valid!`.
- Plugin Creator `validate_plugin.py .` passed against the repository plugin.
- `python -X utf8 ./scripts/validate_release.py --release-version 1.1.2` passed:
  skill, plugin, marketplace, changelog, Docs, installation instructions, and paired
  evaluation numbering are aligned at `1.1.2`.
- `node --check ./evals/fixtures/direction-alignment/script.js` passed.
- `git diff --check` passed with only line-ending conversion warnings.
- Static count after the core edit: `SKILL.md` is 85 lines and 1,090 words, below
  the 500-line progressive-disclosure boundary and without a new reference or
  dependency.
- Scoped inspection found only manifest/ref/version-label changes, compact core
  coordination, paired scenario 18, changelog, and release memory. Production Docs
  layout and behavior are unchanged; only their displayed version moves to `1.1.2`.
- A supplementary ad hoc regex command printed the English 1–18 sequence but used an
  invalid Thai regex and errored. It is not release evidence; the repository
  validator's successful bilingual equality and contiguous-number checks are the
  authoritative parity result.
- Remote preflight fetched `origin/main` and found local/remote counts `0 0`; no local
  or remote `v1.1.2` tag and no GitHub Release exist. GitHub CLI authentication for
  `ohmiler` has repository and workflow scopes.
- No dependency, lockfile, schema, migration, secret, production-data, API, or runtime
  configuration change is present.

### Conditional delivery gate

The current shell does not expose `codex` on `PATH`, and the public marketplace
correctly points at the not-yet-created `v1.1.2` tag. Authentic marketplace and
universal installation proof therefore remains conditional on tagged GitHub Actions
and one post-release smoke run, matching the established v1.1.1 release procedure.

## Publication and observation

Pending.

## Limitations

Scenarios 16–18 define behavioral expectations but do not prove general agent
behavior until independent forward-runs are recorded. This release does not claim
WCAG conformance, real-user usability, field Core Web Vitals, or external-project
validation.
