---
solodeveling_schema: 1
---

# EVIDENCE-0009: README showcase publication

- **Work item:** `WORK-0007-publish-readme-showcase`
- **Date:** 2026-07-17
- **Target:** `origin/main` and GitHub Pages.
- **Result:** Pass.

## Preflight

- User authority explicitly covers commit and push; the push changes `site/**` and therefore triggers the Pages workflow.
- EVIDENCE-0008 records passing local visual, responsive, content, image, accessibility-rule, console, syntax, skill, release, and diff checks.
- `HEAD` and `origin/main` matched at `ef5a46e151e1b9ab44136123ad5da50c386ea522` before publication.
- `.agents/skills/` is excluded from the intended staging set.

## Publication and observation

- **Published candidate:** `7569c8e1ca732da6b34d12a2237faf6e5bc9a87e` (`docs: refresh gridgeist readme showcase`).
- **Push:** `origin/main` advanced from `ef5a46e151e1b9ab44136123ad5da50c386ea522` to the candidate; local `HEAD` and `origin/main` matched after deployment.
- **Validation:** GitHub Actions run `29533987330` completed successfully for the candidate.
- **Deployment:** GitHub Pages run `29533987299` completed successfully for the same candidate.
- **Production observation:** Cache-busted requests to the public After route and its stylesheet returned HTTP 200. The HTML contained `Illustrative concept · sample data`, `Live lane topology`, and `metric-exception`; the CSS contained the `Gridgeist v1.1.0 After refresh` marker.
- **Scope:** `.agents/skills/` remained untracked and was not included in either the candidate or release staging.

## Recovery and limits

- No rollback trigger was observed; validation, deployment, candidate identity, and public content markers all matched.
- Production observation verified delivery and expected content, not external user comprehension or a full production accessibility audit.
