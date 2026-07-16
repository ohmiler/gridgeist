---
solodeveling_schema: 1
---

# EVIDENCE-0004: Main-site refresh

- **Work item:** `WORK-0002-refresh-main-site`
- **Date:** 2026-07-16
- **Environment:** Local static server at `127.0.0.1:8765`, Chromium through Playwright CLI, Windows.
- **Result:** Pass for the scoped source refresh and local verification. Not published.

## Acceptance evidence

| Criterion | Result | Evidence |
| --- | --- | --- |
| EN/TH product-native, brand-adaptive positioning | Pass | Both homepages now use the same v1.1 positioning while preserving the wordmark, paper/ink/cobalt palette, editorial type, and visible-grid hero. |
| Multiple structural modes, honestly labeled | Pass | The adaptation section demonstrates visible/technical, quiet/image-led, invisible/direct-manipulation, and state-led/transactional modes; both languages label them as illustrative specimens rather than client work. |
| Current evaluation evidence | Pass | Both homepages state 13 scenarios and 30 targeted fresh behavioral runs, and explicitly state that implementation fixtures were not run. |
| Install and update paths | Pass | Codex marketplace commands are primary; Agent Skills install and both update paths are present and copyable. The shared copy handler was exercised in Chromium and changed the English button state to `Copied`. |
| Mobile route and section access | Pass | Native `details`/`summary` navigation exposes Docs, Method, Adaptation, Examples, and Install in EN and TH. Opening, following Adaptation, and automatic close were exercised at 360 px. |
| Interaction and reduced motion | Pass | The Before/After control changed the demo state to `SYSTEMIC`; copy interaction passed; with `prefers-reduced-motion: reduce`, both hero axis and coordinate overlays computed to `display: none`. Pointer tracking is also gated by fine-pointer capability. |
| Responsive hierarchy and overflow | Pass | EN and TH homepages had equal client and scroll widths at 360, 768, 1280, and 1600 px after fixing the mobile install heading. Docs EN/TH, Examples, and Tracefield also measured 390/390 at mobile width. |
| Validator, keyboard/focus, and console | Pass with recorded limits | `node --check site/script.js`, `python -X utf8 scripts/validate_release.py`, and `git diff --check` passed. Keyboard Tab progression was observed and focus-visible styling is present. Console errors were zero on EN/TH homepages and the four regression routes. |

## Verification details

- Release validator: `[OK] Gridgeist v1.1.0 skill, release metadata, docs, and evals are aligned.`
- Browser geometry:
  - EN: 360/360, 768/768, 1280/1280, 1600/1600 client/scroll width.
  - TH: 360/360, 768/768, 1280/1280, 1600/1600 client/scroll width.
  - Regression routes at 390 px: `/docs/`, `/th/docs/`, `/examples/`, and `/case-studies/tracefield/` all 390/390.
- Browser console: zero errors on all checked routes.
- Responsive screenshots and accessibility snapshots were generated for representative widths.

## Recorded limits

- The environment could generate screenshots but its local image viewer could not launch because the Windows sandbox helper executable was unavailable. Layout was therefore checked through rendered accessibility snapshots, computed geometry, interactions, and browser console rather than a final pixel-level screenshot review.
- This work does not establish accessibility conformance, cross-browser parity beyond Chromium, production deployment health, analytics impact, or real-user comprehension.
- The targeted 30/30 result remains behavioral evaluation evidence, not implementation-fixture evidence.

## Publication boundary

No push or production deployment was performed. Publishing this source change is a separate release action requiring explicit user authorization.
