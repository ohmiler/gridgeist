---
solodeveling_schema: 1
---

# EVIDENCE-0015: v1.1.2 release

- **Work item:** `WORK-0013-release-v1.1.2`
- **Opened:** 2026-07-18
- **Decision:** Released. Candidate validation, main/tag CI, GitHub publication,
  public Docs, and separate post-release installation checks passed.

## Candidate

- Version: `1.1.2`
- Source revision: `43664adf7a2db727655dcbfef8d7f4572c29ed47`
- Git tree: `113ce63fb1bc0b6d3190bb16c60eafb7da9a3371`
- Skill SHA-256: `75c46b3d85a12d1ea11a6f890a833f4388e8f47d7fbcabc2aaf3d210154785bf`
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
- An initial unquoted `git rev-parse HEAD^{tree}` command was interpreted incorrectly
  by PowerShell and emitted an ambiguous-argument error. The corrected quoted command
  `git rev-parse 'HEAD^{tree}'` returned the tree recorded above; the failed read-only
  probe did not change the candidate.

### Conditional delivery gate

Before publication the default shell did not expose `codex` on `PATH`, and the public
marketplace correctly pointed at the not-yet-created `v1.1.2` tag. Delivery proof was
therefore held behind tagged GitHub Actions and a separate post-release smoke run.
Both gates later passed.

## Publication and observation

- Pushed `main` from `c573501` to release commit `43664ad` and pushed annotated tag
  `v1.1.2`; an immediate pre-push fetch showed local ahead by one commit, remote
  behind by zero, and no existing remote tag.
- Main validation passed:
  https://github.com/ohmiler/gridgeist/actions/runs/29653127235
- Tag validation and clean-install/update smoke passed, including tag identity,
  Codex plugin install/refresh/reinstall, and universal installer install/update:
  https://github.com/ohmiler/gridgeist/actions/runs/29653127093
- The Docs version-label deployment passed:
  https://github.com/ohmiler/gridgeist/actions/runs/29653127185
- Published a public, non-draft, non-prerelease GitHub Release at
  `2026-07-18T17:03:21Z`:
  https://github.com/ohmiler/gridgeist/releases/tag/v1.1.2
- A separate post-release `python -X utf8 scripts/smoke_test_install.py --timeout 180`
  run passed from public `ohmiler/gridgeist`. Codex reported
  `gridgeist@gridgeist` installed and enabled at version `1.1.2`, sourced from
  `https://github.com/ohmiler/gridgeist.git` ref `v1.1.2`; marketplace refresh and
  reinstall returned no errors. The universal installer completed a clean copy and
  reported the global skill up to date on update.
- The local Codex smoke emitted non-blocking warnings that helper PATH aliases would
  not be created under a temporary home. Plugin discovery, version, source identity,
  enablement, refresh, reinstall, and both installer assertions still passed.
- Cache-busted public English and Thai Docs requests both returned HTTP 200 and
  displayed version `1.1.2`.
- One GitHub Release inspection requested unsupported `isLatest` JSON output and
  errored after the Docs check. A corrected query confirmed the published release
  identity and state; the read-only CLI error did not affect publication.

## Limitations

Scenarios 16–18 define behavioral expectations but do not prove general agent
behavior until independent forward-runs are recorded. This release does not claim
WCAG conformance, real-user usability, field Core Web Vitals, or external-project
validation.
