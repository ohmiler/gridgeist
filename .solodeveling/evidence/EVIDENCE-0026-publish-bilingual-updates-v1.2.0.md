---
solodeveling_schema: 1
---

# EVIDENCE-0026: Publish bilingual v1.2.0 Updates story

- **Work item:** WORK-0024-publish-bilingual-updates-v1.2.0
- **Opened:** 2026-07-21
- **Environment:** GitHub Pages production
- **Candidate:** 7911a8f8ab2b660c46411dc72044eeedd81aad96
- **Released:** 2026-07-21
- **Decision:** Released and healthy within the recorded production smoke window.

## Current acceptance matrix

| Boundary | Evidence | Result |
| --- | --- | --- |
| Authority | User authorized the scoped commit, main push, deployment observation, and production verification after reviewing the local result. | Pass |
| Candidate integrity | Candidate 7911a8f contains the 21 authorized Updates, navigation, discovery, social-image, and lifecycle files. The release validator, three JavaScript syntax checks, cached diff integrity, and exact staged-name audit passed before commit. Unrelated pre-existing untracked files were not staged. | Pass |
| Source synchronization | `git fetch` showed origin/main had no commits absent locally. Push advanced origin/main from 903e56f to 7911a8f, necessarily including the pre-existing lifecycle-only revision 042972b. | Pass |
| Repository validation | GitHub Actions run 29834100269 completed successfully for exact head SHA 7911a8f. | Pass |
| Production deployment | GitHub Pages run 29834100320 completed successfully for exact head SHA 7911a8f. | Pass |
| Production routes | Chrome DevTools Protocol checked EN/TH index and article routes at 360 and 1600 px: 8/8 returned HTTP 200 with zero horizontal overflow, zero broken images, and zero runtime/console/log errors. All exposed v1.2.0 and language-correct document identity. | Pass |
| SEO and structured identity | All eight browser checks returned the expected language-specific canonical plus reciprocal en, th, and x-default hreflang values. Both article routes exposed TechArticle JSON-LD and the release-specific absolute OG image URL. | Pass |
| Production assets and discovery | The OG PNG returned HTTP 200 as image/png and parsed to 1200 x 630. Sitemap returned HTTP 200 as XML and contained Updates routes. Robots returned HTTP 200 as text/plain and named the production sitemap. Fresh production HTML for both language homepages contained the relative Updates navigation link. | Pass |

## Known release context

- Local main contains revision 042972b (`docs: queue v1.2 consistency benchmark`),
  a pre-existing lifecycle-only commit ahead of origin/main. It does not change
  `site/**`, but will necessarily be included when main advances.
- Local implementation evidence is recorded in EVIDENCE-0025.
- Last known-good production revision is 9d5bbab.

## Observation and limitations

- Observation covered workflow completion and immediate production checks after
  the Pages deployment completed at 13:22:23 UTC on 2026-07-21.
- Playwright CLI sessions hung in the Windows daemon and the in-app browser had no
  available instance. The production browser matrix therefore used temporary
  headless Chrome controlled directly through the Chrome DevTools Protocol; the
  exact route, viewport, layout, image, DOM metadata, and runtime-error assertions
  remained equivalent and the temporary profile was removed afterward.
- This proves deployment and the checked journeys during the immediate smoke
  window. It does not establish indexing timing, social-crawler cache refresh,
  long-term availability, real-user usability, formal WCAG conformance, global CDN
  behavior, or field performance.
