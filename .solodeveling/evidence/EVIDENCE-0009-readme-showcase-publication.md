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

## Cache-coherence follow-up

- User screenshots showed the refreshed README image but a hybrid public route: new labels and markup combined with the old light After styling.
- The deployed plain and query-string CSS responses both returned HTTP 200, 18,703 bytes, SHA-256 `B43807269A50F8EFAAAFFD3C8CA63D1525FD28D64273D1F65684C60365F5FA3F`, and the v1.1.0 refresh marker.
- Response headers included `Cache-Control: max-age=600`; the HTML still referenced the unchanged `./showcase.css` URL. This isolates the mismatch to a returning browser's stale asset cache rather than a failed Pages deployment or missing CSS.
- Local hotfix verification passed: a fresh Playwright session opened the ordinary `?view=after` route, loaded `showcase.css?v=b4380726`, rendered the same 1440 x 900 design as the README capture, and reported zero console errors/warnings.
- Hotfix commit `b534a64ae60d4d29ce1a134c4e914864255dd3f0` reached `origin/main`; validation run `29534603049` and Pages run `29534603216` completed successfully.
- Cache-busted production HTML returned HTTP 200 with `showcase.css?v=b4380726` and `Live lane topology`. The versioned CSS returned HTTP 200 and SHA-256 `B43807269A50F8EFAAAFFD3C8CA63D1525FD28D64273D1F65684C60365F5FA3F`, matching the locally verified stylesheet.
- README EN/TH After links now include `rev=b4380726`, giving returning browsers a fresh top-level navigation cache key as well as the versioned stylesheet cache key.
