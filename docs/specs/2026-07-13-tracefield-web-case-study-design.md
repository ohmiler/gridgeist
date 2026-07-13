# Tracefield Web Case Study Design

## Goal

Turn the completed Tracefield experiment into a concise, verifiable web case study that helps visitors understand what Gridgeist changed, what evidence supports the result, and where the experiment remains limited.

## Site architecture

- Add a short `07 / Field proof` teaser to the English homepage between Evaluation and Install.
- Create `/case-studies/tracefield/` as the canonical detailed case study.
- Link to the deployed Tracefield application, its source repository, experiment artifacts, and Gridgeist installation section.
- Keep the existing examples gallery unchanged; it demonstrates breadth while the case study demonstrates depth and evidence.

## Homepage teaser

Use the rubric total `10 → 28` as the dominant visual anchor. Pair it with one short explanation and one link to the detailed case study. The teaser must remain cardless, align with the shared 1280px container, and preserve the existing page rhythm.

## Case study sequence

1. Opening: product, user problem, experiment question, Live demo, and source links.
2. Baseline: a compact HTML/CSS reconstruction of the generic welcome banner and metric cards, accompanied by prioritized shortcomings.
3. Intervention: the exact Gridgeist prompt and the key constraints it imposed.
4. Final system: a compact live specimen of the trace stream and span waterfall, built with native HTML/CSS rather than a screenshot.
5. Rubric: six dimensions comparing baseline and final scores, with a total of 10 and 28.
6. Verification: unit, lint, build, browser, responsive, focus-return, and deployment evidence.
7. Limitations: one project, one model run, deterministic local data, and no claim of a controlled benchmark.
8. Final action: open Tracefield or install Gridgeist.

## Visual direction

Treat the page as an evidence dossier. The Gridgeist paper surface frames a dark Tracefield operational plane; scores, trace IDs, latency, and findings carry the composition. Use the existing typefaces and cobalt blue, with Tracefield acid green only inside the final-system evidence. Avoid floating screenshots, ornamental cards, and repeated marketing claims.

## Responsive and accessible behavior

- Use two-column evidence layouts on wide screens and one sequential column on small screens.
- Keep prose within a readable measure and preserve 16px mobile gutters.
- Ensure the reconstructed specimens do not create horizontal overflow.
- Use semantic headings, descriptive links, visible focus, and the site's existing reduced-motion behavior.

## Verification

- Validate all internal and external links.
- Inspect the homepage and case study at representative desktop and mobile widths.
- Confirm rubric arithmetic and evidence labels match the Tracefield repository.
- Confirm no horizontal overflow or browser console errors.
- Run the existing static checks and GitHub Pages workflow, then verify the production URL.
