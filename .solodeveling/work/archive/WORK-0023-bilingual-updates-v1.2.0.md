---
solodeveling_schema: 1
---

# WORK-0023: Publish a bilingual v1.2.0 update story

- **Status:** Completed
- **Class:** Standard
- **Opened:** 2026-07-21
- **Operator:** Codex, acting on the repository owner's instruction
- **Authority:** The user authorized implementing an Updates section that explains
  how important versions improve Gridgeist, starting with v1.2.0 in English and
  Thai. Local site, SEO, social-preview, verification, and lifecycle changes are in
  scope. Push and production deployment are not authorized.

## Goal

Help existing users understand Gridgeist's progress while creating a durable,
shareable, search-readable explanation of why v1.2.0 is materially better than
v1.1.2.

## Direction

An evidence-led release field note that turns the established Gridgeist system into
a readable Before / After argument: the release moved from good page-level choices
to one coherent interface system.

The direction is **brand-derived** from the current public site's rational grid,
paper/ink/cobalt/acid palette, Inter and DM Mono roles, square adjacent surfaces,
operational labels, bilingual voice, and evidence-first composition.

## Scope

- English and Thai Updates index routes.
- English and Thai v1.2.0 article routes with paired language navigation.
- Accurate v1.1.2 versus v1.2.0 comparison, grounded in the changelog, released
  skill, README, evaluation evidence, and existing Northline Before/After demo.
- Shared Updates presentation integrated with the existing v1.2 site contract.
- Discoverability from relevant site navigation, canonical and hreflang metadata,
  article structured data, sitemap/robots discovery, and a release-specific social
  preview image.
- Responsive, keyboard, reduced-motion, link, metadata, and repository verification.

## Out of scope

- A CMS, feed subscription, comments, analytics, search, categories, or authoring UI.
- Retrospective articles for every historical release.
- New claims about users, conversion, usability, performance, accessibility
  conformance, or adoption.
- Changes to the released Gridgeist skill, version metadata, or GitHub Release.
- Push, deployment, or production observation.

## Acceptance

1. `/updates/`, `/th/updates/`, `/updates/v1-2-0/`, and
   `/th/updates/v1-2-0/` are complete, mutually linked, and reachable from the
   relevant public navigation without breaking existing routes or anchors.
2. Both article languages communicate the same supported thesis: v1.2.0 connects
   foundation values, semantic roles, component grammar, alignment safety, skill
   ownership, and evidence-bounded verification into one coherent system.
3. The comparison distinguishes confirmed release behavior from interpretation,
   uses the authentic Northline demo, labels fictional/sample material, and avoids
   unsupported outcome or compliance claims.
4. Each new route has a correct title, description, canonical, reciprocal hreflang,
   locale metadata, favicon/assets, and social metadata. Article routes include
   appropriate article structured data and a 1200 x 630 release-specific PNG.
5. Sitemap and robots discovery cover the public canonical routes and bilingual
   alternates without implying Thai equivalents that do not exist.
6. At representative mobile and desktop widths, new routes have no unintended
   overflow, preserve readable English/Thai hierarchy, expose meaningful focus and
   current states, and keep content available under reduced motion.
7. Internal links, images/frames, metadata pairs, HTML identity, JavaScript syntax,
   release validation, and diff integrity pass. Existing unrelated untracked files
   remain untouched.

## Risks and recovery

- Marketing copy may overstate behavioral evidence; bind every claim to release
  sources and retain explicit evidence limits.
- Thai expansion and dense comparison layouts may overflow; recompose into stacked
  mobile sequences and inspect Thai independently.
- Shared navigation edits can break relative paths; audit every changed route from
  its own directory depth.
- Social crawlers require raster images and absolute URLs; generate and inspect the
  release-specific PNG from a versioned HTML source.
- Recover by reverting the single scoped implementation commit before publication.

## Alternatives considered

- **Recommended:** paired Updates indexes plus a full bilingual release story. Best
  balance of existing-user clarity, search discovery, and sharing.
- **Smaller:** one bilingual page with both languages. Less source work, but poorer
  language-specific sharing and search semantics.
- **Do nothing:** retain README and GitHub Release notes. Accurate but hard to
  discover from the public site and too technical for the intended narrative.

## Ordered implementation

1. Add a shared `site/updates/updates.css` layer that consumes the established
   `site/styles.css` tokens and primitives, with article, comparison, release-card,
   source-note, embedded-demo, and responsive Thai content-stress rules.
2. Build the English Updates index and v1.2.0 article, including release metadata,
   narrative comparison, authentic Northline Before/After frames, evidence limits,
   source links, language pairing, and previous/next release semantics.
3. Build structurally equivalent Thai routes with natural Thai copy and matching
   evidence meaning rather than literal line-by-line translation.
4. Add release-specific social-card source and raster output, reciprocal canonical/
   hreflang metadata, JSON-LD article identity, sitemap/robots discovery, and
   Updates links in the English/Thai home and docs navigation.
5. Run a local static server and focused route/metadata/link checks, then use the
   existing Playwright capability at mobile and desktop widths to exercise overflow,
   frames, focus, language links, mobile menus, reduced motion, and console state.
6. Run release validation, JavaScript syntax, image-dimension, HTML identity, and
   diff-integrity gates; reconcile WORK, EVIDENCE, and state without touching or
   staging unrelated user files.

## Verification mapping

| Acceptance | Planned proof |
| --- | --- |
| 1, routes and navigation | Local HTTP route matrix, same-origin link audit, mobile navigation exercise, reciprocal language-link assertions |
| 2–3, narrative and evidence | Static source comparison against v1.1.2...v1.2.0 changelog/skill/README/evidence plus visible article inspection |
| 4–5, SEO and sharing | DOM metadata/JSON-LD assertions, hreflang pair audit, sitemap/robots parse, 1200 x 630 PNG inspection |
| 6, responsive/access states | Playwright at 360, 768, 1280, and 1600 px; overflow, focus, frame, reduced-motion, console, and Thai content checks |
| 7, repository integrity | Release validator, JavaScript syntax checks, duplicate-ID/fragment/image audit, `git diff --check`, and scoped Git status review |

## Next executable action

Implement the shared Updates presentation and four paired routes, beginning with the
English content model so the Thai route can preserve the same evidence topology.

## Completion

- **Completed:** 2026-07-21
- English and Thai Updates indexes and v1.2.0 articles now present the release as
  an evidence-led shift from page-level decisions to one coherent interface system.
- Canonical/hreflang metadata, TechArticle JSON-LD, sitemap/robots discovery,
  release navigation, and a visually inspected 1200 x 630 social card are complete.
- Forty route/viewport combinations returned HTTP 200 with zero horizontal
  overflow. Focus restoration, reduced motion, source integrity, repository gates,
  and scoped status were verified as recorded in EVIDENCE-0025.
- Completion is local and uncommitted. Push, deployment, and production observation
  remain outside this work item's authority.

## Evidence

- `.solodeveling/evidence/EVIDENCE-0025-bilingual-updates-v1.2.0.md`
