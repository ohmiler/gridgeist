# README Before/After Design

## Goal

Show prospective users the practical difference between a generic interface and one directed by Gridgeist, using rendered project evidence rather than a mockup.

## Selected example

Use the Tracefield specimen from `site/examples/`. Its generic SaaS baseline and product-specific observability workspace make the contrast legible without requiring additional explanation, and it connects to the existing Tracefield case study.

## README composition

Insert a new `See the difference` section after the opening product description and before `60-second Quickstart`.

The section contains:

- one short sentence explaining that both images are rendered from the live HTML/CSS specimen;
- a two-column HTML table that remains valid in GitHub Markdown;
- the baseline screenshot labeled `Without Gridgeist — generic baseline`;
- the redesigned screenshot labeled `With Gridgeist — product-specific system`;
- concise alt text describing the meaningful visual difference;
- a short link to the live examples and Tracefield case study.

## Assets

Store two PNG files in `docs/assets/`:

- `tracefield-before.png`
- `tracefield-after.png`

Capture both from the same Tracefield stage at the same desktop viewport and rendered dimensions. Images should contain the specimen only, without browser chrome or unrelated page sections.

## Verification

- Confirm both image files exist and have matching dimensions.
- Confirm README image paths resolve from the repository root.
- Render or inspect the README Markdown structure.
- Verify the live specimen can still switch between Before and After during capture.
- Keep asset sizes reasonable for GitHub README loading.

## Scope

This change adds one flagship Before/After pair only. It does not add screenshots for Northline or Syntax, redesign the README beyond the new section, or alter the website examples.
