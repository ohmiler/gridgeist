# Gridgeist Review Checklist

Use this checklist after implementation or for a review-only request. Report only meaningful findings.

## 1. Product clarity

- Can a first-time visitor identify the product, audience, and next action quickly?
- Does each section answer a distinct question?
- Is the copy specific to the product rather than interchangeable SaaS language?
- Are real product evidence and outcomes visible?

## 2. Composition and hierarchy

- Is there one clear dominant element in each viewport?
- Do related elements share alignment and proximity?
- Does the page alternate density and breathing room intentionally?
- Do section layouts vary without losing the common grid?
- Are visible lines explaining structure rather than adding noise?

## 3. Typography

- Are type roles limited and consistent?
- Is body text comfortable to read at the rendered width?
- Do headings wrap deliberately at common breakpoints?
- Is mono type reserved for genuinely technical information?

## 4. Spacing and geometry

- Are gaps drawn from a coherent token scale?
- Are outer gutters, section padding, and component padding distinct?
- Are radius, border, and shadow choices consistent?
- Are optical misalignments corrected where mathematical alignment looks wrong?

## 5. Responsive behavior

Inspect at narrow mobile, wide mobile, tablet, laptop, and large desktop widths.

- Does content order still match priority?
- Do navigation and controls remain usable by touch?
- Are grids recomposed instead of squeezed?
- Are code, tables, and media handled without unintended overflow?
- Do long labels, localization, and dynamic content remain resilient?

## 6. Interaction and accessibility

- Use semantic landmarks, headings, buttons, links, labels, and lists.
- Verify keyboard order, visible focus, escape behavior, and focus return for overlays.
- Check text and state contrast.
- Provide useful alternative text or mark decorative visuals appropriately.
- Avoid conveying state by color alone.
- Respect reduced motion and zoom.

## 7. Implementation quality

- Follow existing component and styling conventions.
- Reuse real tokens rather than duplicating magic values.
- Keep components focused and avoid premature abstraction.
- Avoid unnecessary dependencies and layout-specific JavaScript.
- Run the relevant formatter, typecheck, lint, tests, and build.
- Inspect the rendered result after automated checks pass.

## Prioritizing findings

| Priority | Meaning |
|---|---|
| Critical | Blocks use, comprehension, accessibility, or core responsive behavior |
| High | Damages hierarchy, brand trust, or a primary workflow |
| Medium | Creates inconsistency or friction but has a clear workaround |
| Low | Polish improvement with limited user impact |

For each finding, state the evidence and the smallest coherent correction. Group repeated symptoms under one system-level cause.
