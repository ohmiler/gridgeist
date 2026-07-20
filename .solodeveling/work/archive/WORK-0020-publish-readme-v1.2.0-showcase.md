---
solodeveling_schema: 1
---

# WORK-0020: Publish the README v1.2.0 showcase refresh

- **Status:** Completed
- **Class:** Standard release
- **Opened:** 2026-07-20
- **Operator:** Codex, acting on the repository owner's instruction
- **Authority:** On 2026-07-20 the user replied “จัดการ” after being told the
  local commit required publication authority. This explicitly authorizes pushing
  the verified README/showcase refresh to `origin/main` and allowing the existing
  GitHub Pages workflow to deploy it. It does not authorize a new version tag,
  release asset, or unrelated repository changes.

## Release candidate

- **Product version:** Gridgeist v1.2.0 documentation/showcase refresh
- **Content commit:** `7ee27a5726c544bced75b7c0134dd821c1caa0c9`
- **Target:** `origin/main` and the production GitHub Pages site
- **Compatibility:** Documentation and static-site only; no API, dependency,
  package, schema, or data compatibility change
- **Last known good:** `cf8cc880c2b42750e7f52583a873aa1a8690bbb3`

## Readiness and recovery

- Local responsive, interaction, console, image, release, skill, syntax, and diff
  checks passed in `EVIDENCE-0021`.
- `origin/main...HEAD` was `0 1` after a fresh fetch, so publication is a clean
  fast-forward.
- GitHub Pages deploys `site/**` on pushes to `main`; repository validation also
  runs on pushes to `main`.
- Roll back by reverting the publication commits and pushing the revert if either
  required GitHub check fails or the production After page does not identify and
  render the v1.2.0 system correctly.
- Observe workflow completion and the public README/showcase immediately after push.

## Evidence

- `.solodeveling/evidence/EVIDENCE-0022-publish-readme-v1.2.0-showcase.md`
