# Gridgeist Review Checklist

Use this checklist after implementation or for a review-only request. Report only meaningful findings and distinguish observed evidence from inference.

## 1. Product clarity and truth

- Can a first-time user identify the product, audience, primary task, and next action quickly?
- Does each section or workflow stage answer a distinct question?
- Is copy specific rather than interchangeable SaaS language?
- Are authentic product evidence and outcomes visible?
- Are sample, fictional, estimated, or unverified claims labeled honestly?

## 2. Brand fidelity and direction

- Does the interface preserve recognizable voice, imagery, geometry, palette, and interaction character?
- Was a brand-derived direction supported by converging visual implementation,
  assets, or documented conventions rather than product content alone?
- If a broad replacement direction was provisional, did implementation wait for
  the user to choose or authorize the recommendation?
- Does the visual thesis fit the audience and task rather than merely looking fashionable?
- Is the grid visible, quiet, or invisible for a clear reason?
- Would the product remain recognizable after removing generic technical chrome?

## 3. Composition and hierarchy

- Is there one clear dominant element in each viewport or workflow stage?
- Do related elements share alignment and proximity?
- Does the page alternate density and breathing room intentionally?
- Do sections vary without losing shared structural logic?
- Are rules, overlap, asymmetry, or empty space explaining structure rather than adding noise?

## 4. Color and theming

- Do foundation, semantic, and component colors have distinct roles rather than
  accumulating one-off values?
- Are foreground/background pairs, borders, focus, destructive actions, and status
  colors mapped consistently across applicable themes and states?
- Do hover, active, selected, disabled, loading, success, warning, and error
  relationships remain coherent without relying on color alone?
- Are light, dark, forced-color, or user-defined themes handled when the product
  supports them, without undocumented component exceptions?
- Does rendered contrast support hierarchy and readability rather than merely
  passing a token-level calculation?

## 5. Typography, spacing, and geometry

- Are type roles limited, consistent, and appropriate to the brand?
- Is body text comfortable to read at the rendered width?
- Do headings wrap deliberately at common breakpoints?
- Are gaps drawn from a coherent token scale?
- Are radius, border, shadow, crop, and aspect-ratio choices systematic?
- Are optical misalignments corrected where mathematical alignment looks wrong?

## 6. Component system

- Do related components share intentional anatomy, tokens, variants, size or
  density rules, and state behavior?
- Are variants named from product purpose rather than isolated visual treatments?
- Do reusable components preserve behavior with long labels, localization, missing
  media, dynamic data, and loading or error content?
- Are near-duplicate components or magic values symptoms of a missing shared rule?
- Are intentional local exceptions documented by product, content, or interaction
  need instead of convenience?
- Do component APIs and composition rules preserve semantics, focus, touch, and
  recovery behavior?

## 7. Responsive behavior

Inspect project-defined widths or, when absent, approximately 360, 768, 1280, and 1600 px.

- Does content and control order still match priority?
- Do navigation and controls remain usable by touch and keyboard?
- Are grids and narratives recomposed instead of squeezed or blindly stacked?
- Are code, tables, artwork, canvas, and media handled without unintended overflow?
- Do long translated labels, language expansion, zoom, dynamic content, document and in-content language/direction, logical order and properties, and locale-aware dates and numbers remain resilient across LTR and RTL?
- Do reusable components adapt to narrow and wide containers when viewport-only breakpoints are insufficient? Use container queries only when they fit project conventions and browser support.

## 8. Interaction states and recovery

- Inventory default, hover, focus, active, selected, disabled, loading, empty, error, success, and destructive states when applicable.
- Does the primary task remain clear in every important state?
- Do errors explain recovery without destroying valid input?
- Are destructive actions confirmed or reversible in proportion to risk?
- Do overlays close with Escape and restore focus correctly?
- Do pointer, touch, keyboard, and resize behavior preserve the same underlying task?

## 9. Accessibility and constraints

- Use semantic landmarks, headings, buttons, links, labels, and lists.
- Verify keyboard order, visible and unobscured focus, accessible names, contrast, and non-color state cues around sticky regions, overlays, and scroll containers.
- Check applicable target-size and spacing requirements, provide a single-pointer alternative for nonessential dragging, and ensure boundaries and state cues survive forced-colors or user-defined high-contrast palettes.
- Provide useful alternative text or mark decorative visuals appropriately.
- Respect reduced motion without removing essential feedback.
- Preserve privacy, safety, data, and platform constraints.
- Do not turn automated checks into claims of usability, compliance, safety, or user research.

## 10. Implementation quality

- Follow existing component and styling conventions.
- Reuse real tokens rather than duplicating magic values.
- Keep components focused and avoid premature abstraction.
- Avoid unnecessary dependencies and layout-specific JavaScript.
- Reserve media geometry and inspect font, image, and dynamic-content loading for unintended layout shift; when performance is in scope, measure relevant LCP, INP, and CLS evidence and distinguish local or lab observations from field results.
- Run the relevant formatter, typecheck, lint, tests, and build.
- Inspect the rendered result after automated checks pass.

## 11. Verification evidence

Record:

- Viewports and themes actually rendered.
- Primary flows, input methods, and states actually exercised.
- Automated commands run and their results.
- Visual, interaction, accessibility, or content issues observed and corrected.
- Remaining gaps, assumptions, and checks requiring real users or domain experts.

Never write “verified,” “accessible,” “safe,” or “compliant” when only code inspection or automated checks support the claim.

## Prioritizing findings

| Priority | Meaning |
|---|---|
| Critical | Blocks use, comprehension, accessibility, or core responsive behavior |
| High | Damages hierarchy, brand trust, or a primary workflow |
| Medium | Creates inconsistency or friction but has a clear workaround |
| Low | Polish improvement with limited user impact |

For each finding, state the location, evidence, impact, and smallest coherent correction. Group repeated symptoms under one system-level cause.
