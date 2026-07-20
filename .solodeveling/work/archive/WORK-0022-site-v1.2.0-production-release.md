---
solodeveling_schema: 1
---

# WORK-0022: Release the v1.2.0 public site to production

- **Status:** Completed
- **Class:** Critical
- **Opened:** 2026-07-20
- **Completed:** 2026-07-20
- **Operator:** Codex, acting on the repository owner's instruction
- **Authority:** After a release-readiness report named the exact action and target,
  the user replied affirmatively to authorizing push of commit 9d5bbab to
  origin/main, its automatic GitHub Pages production deployment, workflow
  observation, and production smoke testing.

## Release boundary

- **Candidate:** Gridgeist public site v1.2.0
- **Source revision:** 9d5bbabe2a96a99ea1f0e2da01165b2bdfab0352
- **Target:** GitHub Pages production at https://ohmiler.github.io/gridgeist/
- **Mechanism:** Push main; pages.yml publishes the static site directory.
- **Compatibility:** Static HTML, CSS, JavaScript, and PNG assets; no data or schema
  migration and no runtime dependency change.

## Readiness and recovery

- Local release, skill, syntax, responsive, interaction, image, and diff gates were
  already green in EVIDENCE-0023.
- origin/main was one commit behind the candidate and had no divergent commits.
- GitHub authentication and workflow permissions were available without exposing
  secret values.
- Last known-good site deployment was revision b43972d via Pages run 29754266552.
- Rollback trigger: failed deployment/validation, missing v1.2 identity, broken
  critical route, application console error, or horizontal overflow on the checked
  production widths.
- Recovery: repository owner reverts 9d5bbab and pushes main, which republishes the
  previous static site. There are no data implications.

## Outcome

- Push a07170b..9d5bbab to origin/main succeeded.
- Validate run 29758361997 completed successfully.
- GitHub Pages run 29758362079 completed successfully.
- Production route, responsive, asset, console, OG, navigation, comparison, and
  ARIA state smoke checks passed.
- Evidence: .solodeveling/evidence/EVIDENCE-0024-site-v1.2.0-production-release.md
