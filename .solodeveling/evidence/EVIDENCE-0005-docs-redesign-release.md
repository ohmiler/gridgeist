---
solodeveling_schema: 1
---

# EVIDENCE-0005: Bilingual Docs redesign and publication

- **Work item:** `WORK-0003-redesign-docs`
- **Date:** 2026-07-16
- **Target:** GitHub `origin/main`; Pages workflow publication.
- **Remote baseline:** `9ab925de7e282852458ea5a19bf9d2d234e018d5`
- **Last known good local source:** `83583b01198ab537b2c65a7d3b1f6ef6150cba7b`
- **Published source candidate:** `121bac3bc104d15047131b4ee42ea1d35bca675a` plus favicon repair `33aac840abd8a17eea7ef4169dd01421601122f5`.
- **Release result:** Published and observed with the recorded visual-inspection gap below.

## Acceptance evidence

| Criterion | Result | Evidence |
| --- | --- | --- |
| EN/TH v1.1 first-use path | Pass locally | Both pages identify v1.1 and render a three-step quickstart, installation paths, and invocation prompt in the accessibility tree. |
| Current information architecture | Pass locally | Create/Redesign/Review, four structural visibility modes, the current Inspect-to-Verify workflow, and six evidence categories render in both languages. |
| Accurate, copyable install/update paths | Pass locally | Release validator passed; Codex, Agent Skills, manual, and update paths remain present. Playwright observed `Copied` and `คัดลอกแล้ว` after activating the prompt copy buttons. |
| Anchors, routes, and mobile navigation | Pass locally | Eight required anchors are unique in each page; `#adaptation` resolved to an existing target in EN/TH. The native mobile menu exposed cross-site routes and toggled in Chromium. |
| Responsive hierarchy and overflow | Pass locally | Client width equaled scroll width at 360, 768, 1280, and 1600 px in EN and TH. Accessibility snapshots showed complete reading order at 360 px. |
| Interaction, focus, motion, console | Pass locally | Prompt details opened in EN/TH. The skip link was the first Tab target in each language. Reduced-motion emulation reported zero running document animations. Console errors and warnings were zero. |
| Project and scope checks | Pass locally | `node --check site/script.js`, `python -X utf8 scripts/validate_release.py`, `git diff --check`, stale-v1.0 search, and unique-anchor checks passed. |
| Commit, push, and post-push observation | Pass | `121bac3` and repair `33aac84` were pushed to `origin/main`. Validation and Pages workflows succeeded for both. Public EN/TH routes rendered v1.1 at 390 px with valid `#adaptation`, 390/390 client/scroll width, and zero console errors/warnings after repair. |

## Browser matrix

- English: 360/360, 768/768, 1280/1280, and 1600/1600 client/scroll width.
- Thai: 360/360, 768/768, 1280/1280, and 1600/1600 client/scroll width.
- Interactions: native mobile menu, copy feedback, prompt details, first keyboard focus, and fragment navigation.
- Representative 1280 px screenshots and accessibility snapshots were generated.

## Release readiness

- Local `main` is one commit ahead of `origin/main` before the Docs candidate and has no divergence after `git fetch origin`.
- This publication includes the previously verified homepage refresh commit `83583b0` followed by the Docs redesign candidate.
- No dependencies, secrets, configuration, schema, data, backend, or runtime package inputs changed.
- Recovery owner: repository owner/operator.
- Rollback trigger: broken Docs route, missing primary navigation/content, horizontal overflow, command corruption, or material production rendering regression.
- Recovery: revert the Docs redesign commit and push the revert; revert `83583b0` separately only if the homepage refresh is the failing boundary.

## Recorded limits

- Chromium screenshots were generated, but the environment's local image viewer could not launch because `codex-windows-sandbox-setup.exe` is unavailable. Final pixel-level screenshot inspection is unverified; rendered hierarchy was checked through accessibility snapshots, geometry, interactions, and console state.
- Automated and browser checks do not establish accessibility conformance, real-user comprehension, cross-browser parity, or production health.
- The 30/30 figure remains targeted behavioral evidence; implementation fixtures were not run.

## Post-push observation

- `121bac3`: validation run `29513489338` succeeded; Pages run `29513489335` succeeded.
- Initial production observation found one console error: the browser requested `https://ohmiler.github.io/favicon.ico`, which returned 404.
- Root cause: Docs pages did not declare a favicon, while the deployed asset exists at `/gridgeist/favicon.ico` and returned 200.
- Focused regression first failed for missing `rel="icon"`; EN and TH were repaired with route-relative favicon links, and the regression then passed.
- `33aac84`: validation run `29513830401` succeeded; Pages run `29513830918` succeeded.
- Fresh production Chromium sessions after the repair:
  - `https://ohmiler.github.io/gridgeist/docs/#adaptation`: 390/390 client/scroll width, target present, 0 errors, 0 warnings.
  - `https://ohmiler.github.io/gridgeist/th/docs/#adaptation`: 390/390 client/scroll width, target present, 0 errors, 0 warnings.
