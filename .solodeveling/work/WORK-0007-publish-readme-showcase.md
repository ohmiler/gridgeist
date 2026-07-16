---
solodeveling_schema: 1
---

# WORK-0007: Publish the GridGeist v1.1.0 README showcase

- **Status:** Active
- **Class:** Audited release
- **Authority:** On 2026-07-17 the user explicitly requested `commit & push`, authorizing a commit to `main`, push to `origin/main`, and the resulting GitHub Pages deployment.

## Goal and boundary

Publish the verified WORK-0006 Northline showcase refresh to the public GitHub repository and GitHub Pages, then confirm the hosted After route serves the new v1.1.0 design.

## Release contract

- **Candidate:** The staged README EN/TH, Northline After HTML/CSS, 1440 x 900 screenshot, and Solodeveling records from WORK-0006 plus this publication record.
- **Target:** `origin/main` and the `github-pages` environment deployed by `.github/workflows/pages.yml`.
- **Operator:** Primary Codex agent under the user's explicit authority.
- **Readiness:** Local browser, responsive, content, image, syntax, release, skill, and diff checks passed in EVIDENCE-0008.
- **Recovery:** Revert the publication commit and push the revert if the Pages workflow fails persistently or the public After route does not match the verified candidate.
- **Observation:** Follow the validation and Pages workflows to completion, then inspect public content markers for the new design.

## Acceptance criteria

1. Only authorized showcase, README, image, and Solodeveling files are committed; `.agents/skills/` remains untracked.
2. The candidate commit reaches `origin/main` and validation succeeds.
3. GitHub Pages deploys the same candidate successfully.
4. The public After route exposes v1.1.0 design markers such as `Illustrative concept · sample data` and `Live lane topology`.

## Outcome

Candidate `7569c8e1ca732da6b34d12a2237faf6e5bc9a87e` was pushed to `origin/main`. Validation run `29533987330` and GitHub Pages run `29533987299` succeeded, and cache-busted production requests returned HTTP 200 with the expected v1.1.0 HTML/CSS markers. Publication evidence is recorded in `EVIDENCE-0009-readme-showcase-publication.md`.

## Cache-coherence follow-up

- **Observed:** A returning browser rendered the new HTML with the old unversioned stylesheet, producing a hybrid layout that did not match the README capture.
- **Root cause:** GitHub Pages serves `showcase.css` with `Cache-Control: max-age=600`, while both the previous and refreshed HTML used the same stylesheet URL.
- **Repair:** Reference the unchanged verified CSS through its content-hash prefix, `showcase.css?v=b4380726`, so refreshed HTML selects a distinct browser cache key.
- **Authority:** The user's instruction to continue authorizes committing, pushing, and observing this bounded production hotfix.
- **Acceptance:** The deployed HTML contains the versioned stylesheet URL; that URL returns the verified v1.1.0 CSS; validation and Pages deployment succeed; the public After layout matches the README design without requiring a hard refresh.
