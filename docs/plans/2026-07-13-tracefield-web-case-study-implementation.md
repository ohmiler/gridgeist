# Tracefield Web Case Study Implementation Plan

**Goal:** Add a homepage proof teaser and a detailed, evidence-led Tracefield case study to the Gridgeist GitHub Pages site.

**Architecture:** Keep the homepage teaser in the shared stylesheet and isolate the detailed page in `site/case-studies/tracefield/` with its own additive CSS. Reconstruct baseline and final evidence with semantic HTML/CSS rather than external screenshots, while linking canonical evidence back to the Tracefield repository.

**Tech Stack:** Static HTML, CSS, JavaScript, GitHub Pages, Playwright CLI

---

### Task 1: Homepage field-proof teaser

**Files:**
- Modify: `site/index.html`
- Modify: `site/styles.css`

- [ ] Insert `07 / Field proof` between Evaluation and Install and renumber Install to `08`.
- [ ] Use `12 → 28` as the dominant visual, one explanatory paragraph, and one descriptive case-study link.
- [ ] Add responsive styles using the existing container and mobile breakpoint.

### Task 2: Detailed Tracefield case study

**Files:**
- Create: `site/case-studies/tracefield/index.html`
- Create: `site/case-studies/tracefield/case-study.css`

- [ ] Add canonical and social metadata, shared navigation, and semantic section headings.
- [ ] Build the opening, baseline reconstruction, exact prompt, final trace specimen, six-row rubric, verification record, limitations, and final actions.
- [ ] Link the Live demo, repository, experiment artifacts, and Gridgeist install section.
- [ ] Recompose all evidence layouts at 800px without horizontal overflow.

### Task 3: Verification and publication

**Files:**
- Verify: `site/index.html`
- Verify: `site/case-studies/tracefield/index.html`
- Verify: `.github/workflows/pages.yml`

- [ ] Check score arithmetic, link targets, semantic labels, and CSS syntax.
- [ ] Serve the site locally and inspect homepage/case-study desktop and mobile layouts with browser automation.
- [ ] Verify navigation, external links, console output, and horizontal overflow.
- [ ] Commit, push `main`, wait for Pages deployment, and verify the production case-study URL.
