---
solodeveling_schema: 1
---

# EVIDENCE-0024: Site v1.2.0 production release

- **Work item:** WORK-0022-site-v1.2.0-production-release
- **Released:** 2026-07-20
- **Candidate:** 9d5bbabe2a96a99ea1f0e2da01165b2bdfab0352
- **Environment:** GitHub Pages production
- **Decision:** Released and healthy within the recorded smoke-test window.

## Release evidence

| Boundary | Evidence | Result |
| --- | --- | --- |
| Authority | User affirmatively authorized the named origin/main push, automatic GitHub Pages production deployment, workflow observation, and production smoke test. | Pass |
| Source synchronization | git push advanced origin/main from a07170b to 9d5bbab without divergence. | Pass |
| Repository validation | GitHub Actions run 29758361997 completed success for revision 9d5bbab. | Pass |
| Production deployment | GitHub Pages run 29758362079 completed success for revision 9d5bbab. | Pass |
| Production routes | Playwright checked EN/TH home, EN/TH docs, Examples, Tracefield, and Northline After at 360 and 1600 px: 14/14 returned HTTP 200 with zero horizontal overflow, broken images, console errors, or page errors. | Pass |
| Version identity | Home, docs, examples, and Tracefield exposed their v1.2 markers. The Northline marker assertion initially used an all-uppercase case-sensitive string; a targeted DOM check confirmed view=after, aria-hidden=false, and Gridgeist v1.2.0 concept sample-data text. | Pass |
| OG production source | /og/ returned HTTP 200 at a 1200 x 630 viewport, exposed GG—1.2, and had zero overflow. The canonical og-image.png had already been locally measured at 1200 x 630. | Pass |
| Production interactions | Mobile menu opened, closed with Escape, and restored focus. Home After synchronized data-state, aria-pressed, and both aria-hidden values. All three Examples switched to After with hidden state [true, false]. | Pass |
| Recovery | Last known-good site revision b43972d and revert-of-9d5bbab recovery path are recorded. No data or schema recovery is required. | Pass |

## Observation and limitations

- Observation covered workflow completion and immediate production smoke checks
  from approximately 16:09 to 16:12 UTC on 2026-07-20.
- This proves deployment and the checked journeys during that window. It does not
  establish long-term availability, real-user usability, formal WCAG conformance,
  CDN behavior in every region, or production performance under load.
