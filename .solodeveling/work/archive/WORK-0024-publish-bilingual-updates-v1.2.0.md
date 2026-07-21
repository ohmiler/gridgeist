---
solodeveling_schema: 1
---

# WORK-0024: Publish the bilingual v1.2.0 Updates story

- **Status:** Completed
- **Class:** Standard
- **Opened:** 2026-07-21
- **Operator:** Codex, acting on the repository owner's instruction
- **Authority:** After local implementation and verification were reported, the
  user explicitly authorized commit, push to main, deployment observation, and
  production verification.
- **Completed:** 2026-07-21

## Release boundary

- **Candidate:** The scoped bilingual Updates implementation completed by
  WORK-0023, on top of local main revision 042972b.
- **Target:** GitHub Pages production at https://ohmiler.github.io/gridgeist/
- **Mechanism:** Commit the scoped site and lifecycle files, push main, allow
  pages.yml to publish `site/`, and observe both validation and Pages workflows.
- **Compatibility:** Static HTML, CSS, JavaScript references, XML, TXT, and PNG
  assets. No application runtime, dependency, data, schema, or secret change.

## Acceptance

1. The commit contains only the authorized Updates, navigation, discovery,
   social-image, and lifecycle records; unrelated untracked files remain unstaged.
2. origin/main advances to the exact candidate without remote divergence.
3. Repository validation and GitHub Pages deployment complete successfully.
4. The four public EN/TH Updates routes, social image, sitemap, and robots file
   return successfully and expose the expected production identity and metadata.
5. Representative production desktop/mobile routes have no unintended horizontal
   overflow, broken images, page errors, or console errors.

## Recovery and observation

- **Last known-good production:** revision 9d5bbab, recorded in EVIDENCE-0024.
- **Rollback trigger:** failed validation or Pages deployment, missing/broken
  Updates routes, incorrect language/canonical identity, broken social image,
  console error, or horizontal overflow in the production smoke window.
- **Recovery owner:** Repository owner, assisted by Codex.
- **Recovery action:** Revert the scoped publication commit and push main to
  republish the prior static site. There are no data implications.
- **Observation window:** Workflow completion plus immediate production route,
  metadata, asset, responsive, and browser-console smoke checks.

## Evidence

- `.solodeveling/evidence/EVIDENCE-0026-publish-bilingual-updates-v1.2.0.md`

## Outcome

- Candidate 7911a8f8ab2b660c46411dc72044eeedd81aad96 was committed and pushed
  to origin/main without divergence.
- Validation run 29834100269 and Pages run 29834100320 completed successfully.
- Eight production route/viewport checks passed across the four EN/TH Updates
  routes at 360 and 1600 px with HTTP 200, zero overflow, no broken images, and
  no runtime errors.
- Production canonical/hreflang, TechArticle identity, sitemap discovery, robots
  identity, and the 1200 x 630 social PNG passed as recorded in EVIDENCE-0026.
