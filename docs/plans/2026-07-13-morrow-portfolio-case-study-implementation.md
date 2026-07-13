# Morrow Portfolio Case Study Implementation Plan

> Execute this plan inline in a normal Codex session. Do not use Superpowers or subagents. Track each checkbox and verify every checkpoint before committing.

**Goal:** Build and publish Morrow, a fictional creative-developer portfolio that tests whether Gridgeist preserves image-led, asymmetric brand character instead of applying a technical preset.

**Architecture:** Create `ohmiler/morrow-portfolio` as a standalone Next.js static-export repository. Generate one disclosed fictional artwork set shared by a conventional static baseline and the final typed React interface. Preserve the exact Gridgeist prompt, fixed rubric, image-generation prompt, and four-viewport evidence alongside the application.

**Tech Stack:** Next.js, TypeScript, React, CSS, Vitest, Playwright, AI-generated raster artwork, GitHub Actions, GitHub Pages.

**Fixed rubric:** Score Brand fidelity, Visual authorship, Image-led hierarchy, Case-study clarity, Responsive composition, and Accessibility and implementation from 1–5 each, for a total of 30.

---

## File map

```text
morrow-portfolio/
├── .github/workflows/pages.yml       Verify, build, and deploy static export
├── baseline/
│   ├── index.html                    Conventional portfolio baseline
│   └── styles.css                    Baseline-only styling
├── experiment/
│   ├── prompt.md                     Exact Gridgeist invocation and run metadata
│   ├── rubric.md                     Baseline/final evidence and scores
│   └── artwork-prompt.md             Image prompt and fictional-use disclosure
├── public/artworks/
│   ├── tidal-memory.webp             Shared hero artwork
│   ├── soft-circuit.webp             Shared installation artwork
│   └── afterlight.webp               Shared archive artwork
├── src/app/
│   ├── globals.css                   Tokens, editorial layout, responsive composition
│   ├── layout.tsx                    Metadata and document shell
│   └── page.tsx                      Portfolio composition
├── src/components/
│   ├── ArtworkFigure.tsx             Image, dimensions, caption, alternative text
│   ├── MobileMenu.tsx                Accessible menu, Escape, and focus return
│   ├── ProjectIndex.tsx              Stable work navigation
│   └── ProjectStory.tsx              Premise-to-reflection case-study structure
├── src/content/
│   └── portfolio.ts                  Typed deterministic practitioner/project content
├── tests/
│   ├── portfolio.test.ts             Content integrity and disclosure tests
│   └── morrow.spec.ts                Four-viewport browser checks
├── next.config.ts                    Static export and Pages base path
├── playwright.config.ts              360/768/1024/1440 projects
├── vitest.config.ts                  Unit-test boundary
├── README.md                         Method, run, verification, deployment, limits
└── LICENSE                           MIT license
```

## Task 1: Create and configure the repository

- [ ] Verify `gh repo view ohmiler/morrow-portfolio` returns repository-not-found. Stop if it exists.
- [ ] Scaffold `C:\Users\Miler\Downloads\morrow-portfolio` with Next.js TypeScript App Router and create a public GitHub repository with `origin` pointing to `ohmiler/morrow-portfolio`.
- [ ] Install `vitest`, `jsdom`, `@testing-library/react`, `@testing-library/jest-dom`, `@playwright/test`, and `serve` as development dependencies.
- [ ] Add `test`, `test:e2e`, and `verify` scripts. `verify` must run lint, unit tests, build, and Playwright in that order.
- [ ] Configure `next.config.ts` with `output: "export"`, `images.unoptimized: true`, local `turbopack.root`, and `/morrow-portfolio` base/asset paths only when `GITHUB_ACTIONS === "true"`.
- [ ] Run lint and production build; expect exit 0 without workspace-root warnings.
- [ ] Rename the branch to `main` and commit `chore: scaffold Morrow portfolio`.

## Task 2: Generate and disclose the shared artwork

- [ ] Use the `imagegen` skill to create three distinct abstract raster artworks without imitating a living artist: tidal data currents, a soft luminous circuit installation, and a fragmented afterimage archive.
- [ ] Keep the set visually related through warm charcoal, bone, faded violet, and red-orange, while giving each image a different dominant composition.
- [ ] Export web-appropriate assets to `public/artworks/` with intrinsic dimensions of at least 1600 × 1200 and use WebP when the generation result permits lossless project handling.
- [ ] Write `experiment/artwork-prompt.md` with the exact generation prompt, date, tool/surface, filenames, fictional-use disclosure, and confirmation that baseline/final share the same files.
- [ ] Inspect all three images for accidental text, signatures, recognizable copyrighted characters, or documentary claims. Regenerate any failing asset.
- [ ] Commit `assets: add fictional Morrow artwork set`.

## Task 3: Preserve the generic baseline

- [ ] Create a conventional portfolio using the same practitioner copy, three projects, and artwork: centered hero, equal rounded project cards, skills row, about block, and contact CTA.
- [ ] Keep semantic headings, meaningful alt text, working anchors, and readable contrast; do not manufacture accessibility failures.
- [ ] At 1440 and 360 px, record weaknesses in authorship, image hierarchy, case-study depth, and responsive recomposition.
- [ ] Create `experiment/rubric.md`; score all six baseline dimensions from 1–5 with one concrete observation each. Leave final scores unset.
- [ ] Commit `test: preserve Morrow portfolio baseline`.

## Task 4: Record the exact Gridgeist run

- [ ] Before final UI work, write this prompt verbatim to `experiment/prompt.md`:

```text
Use $gridgeist to redesign this working creative-developer portfolio.
Preserve all Morrow content, artwork, project anchors, captions, and the fictional-work disclosure.
The practitioner works across code, space, and moving image; preserve a human, image-led, asymmetric brand instead of applying a Swiss or technical preset.
Let artwork lead while premise, role, constraints, process, outcome, and reflection remain findable for Tidal Memory, Soft Circuit, and Afterlight.
Create deliberate compositions for 360 px, 768 px, 1024 px, and 1440 px; do not shrink the desktop collage or turn every project into the same card.
Implement working mobile navigation, Escape and focus return, meaningful alternative text, visible focus, reduced motion, and no document-level horizontal overflow.
Do not use a custom cursor, scroll hijacking, skill clouds, WebGL, fabricated clients, exhibitions, or real-world outcomes.
```

- [ ] Record date, agent/model, surface, Gridgeist release/commit, baseline commit, and that no other visual-design skill was used in the final-design run.
- [ ] Invoke only the installed `gridgeist/SKILL.md` for final interface direction and record its one-sentence thesis.
- [ ] Commit `docs: record Morrow Gridgeist prompt`.

## Task 5: Define and test portfolio content

- [ ] Write failing tests requiring unique anchors; all three project records; premise, role, constraints, process, outcome, and reflection; meaningful artwork alt text; and a disclosure containing “fictional” and “AI-generated”.
- [ ] Run `npm test`; expect import failure before `src/content/portfolio.ts` exists.
- [ ] Define `Practitioner`, `Artwork`, `Project`, and `PortfolioContent` types and export one immutable content object.
- [ ] Keep every claim fictional and modest: no real clients, attendance, awards, sales, or performance metrics.
- [ ] Run unit tests and lint; expect all to pass.
- [ ] Commit `feat: define Morrow portfolio content`.

## Task 6: Build the accessible shell and navigation

- [ ] Implement semantic header, navigation, main, work index, about, contact, and footer landmarks.
- [ ] Implement `MobileMenu` with `aria-expanded`, `aria-controls`, Escape close, focus return, backdrop behavior, and 44 px controls.
- [ ] Implement `ProjectIndex` with stable anchors for all three projects and non-color-only hover/focus treatment.
- [ ] Establish warm charcoal/bone/violet/red-orange tokens, expressive serif plus neutral sans roles, and an underlying layout grid without technical chrome.
- [ ] Run tests, lint, and build; expect all to pass.
- [ ] Commit `feat: add Morrow portfolio shell`.

## Task 7: Build image-led project stories

- [ ] Implement `ArtworkFigure` with explicit width/height, meaningful alt text, visible caption, project/year metadata, and no layout shift.
- [ ] Implement `ProjectStory` with distinct composition variants for Tidal Memory, Soft Circuit, and Afterlight rather than one repeated card component appearance.
- [ ] Render premise, role, constraints, process, outcome, and reflection for each project from the typed content model.
- [ ] Add a process section that includes sketches/fragments and one failed experiment per project without inventing real-world validation.
- [ ] Use short reveal transitions only as progressive enhancement and disable them under `prefers-reduced-motion: reduce`.
- [ ] Run tests, lint, and build; expect all to pass.
- [ ] Commit `feat: compose Morrow project stories`.

## Task 8: Complete responsive recomposition

- [ ] At 1440 px, verify large image fields, offset narrative, asymmetric whitespace, and lateral project index.
- [ ] At 1024 px, reduce overlap while keeping editorial order and readable captions.
- [ ] At 768 px, alternate a deliberate two-column artwork/narrative rhythm.
- [ ] At 360 px, enforce artwork → premise → metadata → reflection order, working mobile navigation, readable text, and no document overflow.
- [ ] Ensure images never exceed containers, captions remain associated, focus is visible, and touch controls meet 44 px.
- [ ] Commit `style: refine Morrow across viewports` after lint/tests/build pass.

## Task 9: Add browser verification

- [ ] Configure Playwright projects `mobile-360`, `tablet-768`, `compact-1024`, and `desktop-1440` on an isolated local port.
- [ ] Verify practice statement and fictional disclosure, all three project anchors, mobile menu open/Escape/focus return, meaningful loaded artwork dimensions, keyboard-focusable controls, zero console errors, and `scrollWidth <= innerWidth`.
- [ ] Verify reduced-motion media query exists and essential content remains visible when reduced motion is emulated.
- [ ] Capture full-page screenshots for all projects as ignored test artifacts.
- [ ] Run `npm run verify`; expect unit tests and all four browser projects to pass.
- [ ] Commit `test: verify Morrow interactions and layout`.

## Task 10: Score, document, and deploy

- [ ] Complete final rubric scores from rendered evidence without changing baseline values or setting a target retroactively.
- [ ] Write README with live URL, experiment method, repository map, setup, verification, artwork disclosure, limitations, and links to exact prompt/rubric/Gridgeist.
- [ ] Add MIT license and ignore Playwright artifacts.
- [ ] Add a least-privilege Pages workflow using current official action majors; run `npm ci`, lint, unit tests, and build before deploy.
- [ ] Push `main`, enable Pages with build type `workflow`, and watch deployment to completion.
- [ ] Verify production returns 200, loads all three artworks/assets, contains the disclosure, and hydrates navigation.
- [ ] Tag the verified production commit as annotated `v0.1.0` and push the tag.

## Task 11: Link the evidence from Gridgeist

- [ ] In the Gridgeist repository, add Morrow as a third case study to `README.md` and `README.th.md` only after production evidence is public.
- [ ] Add English and Thai evaluation scenarios for brand-conflicting, image-led portfolio work. Link Morrow as evidence without requiring its visual style or score.
- [ ] Check both public URLs, Gridgeist frontmatter, UTF-8 Thai content, scenario counts, and clean diffs.
- [ ] Commit `docs: add Morrow creative portfolio case study` and push Gridgeist main.

## Final acceptance checklist

- [ ] Public repository, shared artwork, baseline, exact prompt, rubric, and limitations are independently reachable.
- [ ] Baseline and final use identical source images and content requirements.
- [ ] `npm run verify` passes from the final commit.
- [ ] Four viewport projects pass without document-level overflow.
- [ ] The final visual language is materially different from Tracefield and Ledgerline.
- [ ] Production deployment succeeds and returns 200 with all artwork assets.
- [ ] Gridgeist links Morrow only after its evidence is public.
