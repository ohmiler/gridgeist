## Direction

A restrained, ledger-like account workspace using a quiet grid, compact status markers, and clear transactional hierarchy. Existing routes, content, themes, and behaviors remain intact.

## Implementation

- Consolidated colors, spacing, radii, surfaces, and states into semantic tokens in [styles.css](C:/tmp/gridgeist-s19-eval-a17064f-20260720/en1/styles.css).
- Unified buttons, inputs, status badges, cards, focus treatments, and dark-theme behavior.
- Reworked profile statistics into adjacent account records.
- Improved plan and invoice hierarchy and responsive table handling.
- Added mobile recomposition, reduced-motion handling, and forced-color state cues.
- Updated shared component classes in [index.html](C:/tmp/gridgeist-s19-eval-a17064f-20260720/en1/index.html) and [billing.html](C:/tmp/gridgeist-s19-eval-a17064f-20260720/en1/billing.html).
- Left `script.js` and `DESIGN.md` unchanged.

## Verification

Rendered at 360, 768, 1280, and 1600px in light and dark themes. Exercised:

- Route navigation and theme persistence
- Profile save disabled/success feedback
- Paid/open invoice filtering
- Invoice preparation feedback
- Unavailable plan-management state
- Keyboard traversal
- Mobile table overflow
- Browser console: zero errors or warnings

The local preview server and browser session were stopped. No build or lint configuration exists in this static fixture.
