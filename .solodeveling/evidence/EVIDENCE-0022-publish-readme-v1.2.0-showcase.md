---
solodeveling_schema: 1
---

# EVIDENCE-0022: Publish the README v1.2.0 showcase refresh

- **Work item:** `WORK-0020-publish-readme-v1.2.0-showcase`
- **Opened:** 2026-07-20
- **Decision:** Published and production-verified; no rollback triggered.

## Release matrix

| Boundary | Evidence | Result |
| --- | --- | --- |
| Authority | User explicitly authorized publication after the assistant identified push/deploy as the remaining action. | Pass |
| Candidate | Content commit `7ee27a5726c544bced75b7c0134dd821c1caa0c9`; static README/showcase only. | Pass |
| Fast-forward safety | Fresh fetch observed `origin/main` at `cf8cc880c2b42750e7f52583a873aa1a8690bbb3` and `origin/main...HEAD` at `0 1`. | Pass |
| Pre-release proof | Scoped local acceptance is recorded in `EVIDENCE-0021`; release, skill, syntax, diff, browser, and image checks passed. | Pass |
| Recovery | Revert publication commits and push if required checks fail or the production After page is incorrect. | Ready |
| GitHub checks | Validation run `29754266347` and Pages run `29754266552` both completed successfully for release head `b43972d961778b731d0c94a237a14669fd8fed37`. | Pass |
| Production README/showcase | GitHub API returned the v1.2.0 README copy and `rev=ab77ceb6` link from `main`. A real browser loaded the production After page and its `showcase-v120.css?v=ab77ceb6`; at 360 and 1440 px it observed no overflow, three semantic lane rows, the v1.2.0 truth label, and `On time / Check / On time` state text. The 1440 x 900 production capture was visually consistent with the canonical image. | Pass |
| Production console | The page produced no application errors. The browser reported one non-blocking request failure for the pre-existing root `/favicon.ico` (404). | Accepted gap |

## Limitations

- GitHub Pages and Actions are external systems; completion will be claimed only
  after their observable checks and the public page support it.
- The observation covered immediate post-deploy behavior at 360 and 1440 px; local
  pre-release evidence covers the wider five-viewport matrix and reduced motion.
