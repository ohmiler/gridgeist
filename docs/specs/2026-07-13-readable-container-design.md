# Readable Container System

## Goal

Improve reading comfort across the English homepage, Thai guide, and examples gallery without weakening Gridgeist's full-width grid, hero, or interactive specimens.

## Layout model

- Add shared responsive page gutters with `clamp()`.
- Add a wide container capped near 1280px for navigation, section composition, and examples.
- Add a copy measure capped near 760px for long prose.
- Keep section backgrounds, grid lines, and deliberate visual planes full bleed.
- Align header, hero content, and section content to the same wide-container edges.
- Give Thai prose a slightly tighter measure where it improves scanning.

## Scope

- Update `site/styles.css` as the shared layout foundation.
- Update `site/th/thai.css` only for Thai-specific measure adjustments.
- Update `site/examples/examples.css` for gallery composition where shared rules are insufficient.
- Make minimal HTML wrapper changes only if CSS cannot create the required inner container safely.
- Preserve copy, colors, interactions, animations, anchors, and accessibility behavior.

## Responsive behavior

- Desktop: wide content is capped and centered; prose remains substantially narrower.
- Tablet: gutters contract fluidly while compositions retain their hierarchy.
- Mobile: content uses approximately 16px side gutters and recomposes according to existing breakpoints.

## Verification

- Inspect the English, Thai, and examples pages at representative desktop and mobile widths.
- Confirm no horizontal overflow, clipped controls, broken anchors, or layout regressions.
- Confirm long paragraphs no longer span an uncomfortable reading width.
- Run static checks and review the final diff before commit.
