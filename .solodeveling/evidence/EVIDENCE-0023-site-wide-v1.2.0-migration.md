---
solodeveling_schema: 1
---

# EVIDENCE-0023: Site-wide v1.2.0 migration

- **Work item:** WORK-0021-site-wide-v1.2.0-migration
- **Opened:** 2026-07-20
- **Verified:** 2026-07-20
- **Decision:** Acceptance satisfied for the local site migration and local commit.
  Publication remains outside this work item's authority.

## Current acceptance matrix

| Boundary | Evidence | Result |
| --- | --- | --- |
| Route and content truth | EN/TH home and docs now show v1.2 identity, 19 published scenarios, six clean bilingual Scenario 19 runs, independent responsive checks, repaired guardrails, and the remaining real-user evidence limit. A stale-marker search across site returned zero v1.1 or legacy proof labels. | Pass |
| Shared v1.2 contract | site/styles.css now separates foundation values, semantic roles, and shared component rules. Current, pressed, copied, focus, status, forced-color, and reduced-motion behavior use non-color cues where applicable. | Pass |
| Home and docs | EN/TH home pages expose the compact system contract. EN/TH docs add a contract section, aligned navigation and numbering, workflow guidance, and v1.2 evidence while preserving install commands and anchors. Visual inspection covered both languages at desktop and mobile widths. | Pass |
| Examples, case study, showcase, and OG | Examples gained v1.2 field-set framing and synchronized visual/ARIA Before/After states. Tracefield remains explicitly historical while inheriting the current site framing. Northline keeps its dedicated verified v1.2 presentation and query states. The OG source and fresh PNG identify v1.2. | Pass |
| Responsive route matrix | Playwright exercised /, /th/, /docs/, /th/docs/, /examples/, /case-studies/tracefield/, and /readme-showcase/?view=after at 360, 768, 1280, and 1600 px: 28/28 responses were 200 with zero horizontal overflow, duplicate IDs, missing same-page fragments, broken images, console errors, or page errors. | Pass |
| Interaction and access states | Mobile menu opened, closed with Escape, and restored summary focus. Home and all three Examples toggles synchronized pressed/hidden state. Clipboard feedback reached Copied with aria-live=polite. Docs details opened. Reduced motion exposed reveal content with opacity 1, no transform, and effectively zero transition. Northline query states resolved to before/after correctly. | Pass |
| Image and favicon integrity | site/og-image.png is a fresh browser render measured at exactly 1200 x 630. Visual inspection confirmed the v1.2 foundation/semantic/component composition. All eight HTML entry points contain exactly one relative favicon declaration and /favicon.ico returned HTTP 200 locally. | Pass |
| Repository quality | validate_release.py --release-version 1.2.0, Skill Creator quick_validate.py, three JavaScript syntax checks, and git diff --check passed after the final source change. | Pass |
| Scope and publication boundary | Scoped source/lifecycle files are selected for the local commit. Pre-existing unrelated untracked files are left untouched. No push or deploy occurred. | Pass |

## Reproducible checks

- python -X utf8 scripts/validate_release.py --release-version 1.2.0 returned
  [OK] Gridgeist v1.2.0 skill, release metadata, docs, and evals are aligned.
- Skill Creator quick_validate.py against skills/gridgeist returned Skill is valid!
- node --check passed for site/script.js, site/examples/examples.js, and
  site/readme-showcase/showcase.js.
- git diff --check passed; line-ending notices are advisory Windows checkout
  messages rather than diff errors.
- Playwright CLI session gridgeist12 ran the route matrix and focused state checks
  against http://127.0.0.1:4178/. QA captures are under the ignored
  output/playwright/v12-* paths.

## Visual review notes

- The shared paper/ink/cobalt system remains recognizable without flattening the
  docs, examples, historical case study, or product-native Northline surface.
- The contract composition is a wide flow plus four evidence cards on desktop and
  a readable stacked sequence on mobile.
- Thai headings, prose, contract cards, evidence strip, and navigation recompose
  without clipping or horizontal scrolling.
- Full-page screenshots must scroll first to complete IntersectionObserver reveal
  transitions; a focused scroll audit confirmed all eight English home reveals.

## Limitations

- Local browser and static checks do not establish real-user usability, formal WCAG
  conformance, universal agent behavior, production hosting behavior, or field
  performance.
- The in-app browser surface was unavailable in this environment. Visual review was
  performed from Playwright browser captures instead.
- The migration is committed locally only; publication and production smoke checks
  require separate authority.
