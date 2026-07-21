---
solodeveling_schema: 1
---

# EVIDENCE-0025: Bilingual v1.2.0 update story

- **Work item:** WORK-0023-bilingual-updates-v1.2.0
- **Opened:** 2026-07-21
- **Verified:** 2026-07-21
- **Decision:** Acceptance satisfied for the local bilingual Updates implementation.
  Commit, publication, and production observation remain outside this work item's
  authority.

## Current acceptance matrix

| Boundary | Evidence | Result |
| --- | --- | --- |
| Routes and navigation | The four new routes returned HTTP 200 at 360, 768, 1280, and 1600 px with zero horizontal overflow. Six changed existing routes passed the same matrix. Static audit found every local href/src target. Mobile navigation opened, exposed the expected links, closed with Escape, and returned focus to Menu. | Pass |
| Bilingual release narrative | English and Thai articles each contain six structurally paired Before/Now comparisons, the same system-flow topology, bounded evidence, natural localized copy, and paired language routes. Static source review reconciled the story with the v1.1.2...v1.2.0 changelog, released skill, README, and release evidence. | Pass |
| Evidence integrity | Northline is labeled fictional/sample material in both languages. Both embedded Before/After URLs returned HTTP 200 and preserve their query states. Copy distinguishes six behavioral fixture runs and technical checks from unestablished real-user usability, formal WCAG, field-performance, and universal-agent claims. | Pass |
| SEO and social metadata | All four routes have one canonical and reciprocal en, th, and x-default links. Both articles parse as language-correct TechArticle JSON-LD. Sitemap XML parses, robots points to it, and the release PNG is a visually inspected 1200 x 630 cobalt/grid composition. | Pass |
| Responsive and access states | New-route browser matrix passed 16/16 combinations; affected-route matrix passed 24/24. English desktop, English mobile index, Thai mobile article, and the social card were visually inspected. Reduced motion produced opacity 1, transform none, and 0.00001s transition duration. The final browser session reported zero console errors. | Pass |
| Repository and scope integrity | Release validation, three JavaScript syntax checks, HTML/reference/JSON-LD/XML audits, OG dimension check, and git diff integrity passed. Git status confirms pre-existing unrelated untracked skill/evaluation files remain untouched. | Pass |

## Observation log

- 2026-07-21: Work shaped from the user's selected Updates direction and the
  v1.1.2...v1.2.0 release diff. No completion evidence recorded yet.
- 2026-07-21: The first social-card render exposed a malformed empty content
  declaration caused by Windows native-argument quote loss. A focused regression
  failed before repair and passed after restoring the declaration; computed card
  background changed to cobalt and the regenerated image passed dimension and
  visual inspection.
- 2026-07-21: Playwright CLI frame-DOM inspection caused the named daemon to hang
  twice. Exact session processes were stopped; frame verification was bounded to
  source references, direct HTTP 200 checks, the unmodified previously verified
  showcase behavior, and successful article route rendering without claiming fresh
  inner-frame DOM proof.

## Reproducible checks

- python -X utf8 scripts/validate_release.py --release-version 1.2.0
- node --check site/script.js
- node --check site/examples/examples.js
- node --check site/readme-showcase/showcase.js
- Temporary read-only Python route, metadata, JSON-LD, reference, sitemap, and
  robots audit
- Playwright CLI route matrices: 16 new-route combinations and 24 changed-route
  combinations at 360, 768, 1280, and 1600 px
- Playwright CLI mobile snapshot/click/Escape/focus and reduced-motion checks
- git diff --check

## Limitations

- Local static and browser checks do not establish production hosting behavior,
  indexing, social-crawler cache refresh, real-user usability, formal accessibility
  conformance, or field performance.
- Publication was not authorized, so public URLs still serve the previously
  deployed site until a separate commit/push/deploy action is approved.
