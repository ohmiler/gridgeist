---
solodeveling_schema: 1
---

# EVIDENCE-0021: README v1.2.0 showcase refresh

- **Work item:** `WORK-0019-readme-v1.2.0-showcase`
- **Opened:** 2026-07-20
- **Decision:** Accepted for local completion. Publication remains unauthorized.

## Current acceptance matrix

| Boundary | Evidence | Result |
| --- | --- | --- |
| README EN/TH v1.2.0 explanation | Both READMEs now describe the system contract, semantic roles, component grammar, direction safety, skill coordination, and evidence-bounded verification. Version labels and `rev=ab77ceb6` links match. | Pass |
| Genuine v1.2.0 After source | The workspace v1.2.0 skill and its design-language, system-contract, and review-checklist references informed a new semantic token layer, component/state grammar, connected layout, and reduced-motion behavior in `showcase-v120.css`. | Pass |
| Preserved Before and product truth | The Before source has no diff and `northline-before.png` retained SHA-256 `7AD874BC79E17DC351BD48D1756A44A0FDDFFC7E352D2D0CCA0B4691EFE3AC5E`. Northline identity, three lanes, metrics, topology, exception, and concept/sample labels remain. | Pass |
| Responsive, focus, states, motion, and console | Browser checks at 360, 768, 1280, 1440, and 1600 px observed equal client/scroll widths. Every non-placeholder fragment resolved once; states exposed `On time`, `Check`, `On time`; keyboard focus rendered a solid 3 px outline; reduced motion produced 0.01 ms animation/transition durations; console reported zero errors and warnings. | Pass |
| Fresh canonical image | Browser capture is 1440 x 900, 106,308 bytes, SHA-256 `2C9E49ECDAE9246DD53CC303C99C470B8F152CDCB6F9F90DB34EC58ED53D18F9`; the corrected final image was inspected visually after rejecting an invalid animation-disabled capture. | Pass |
| Repository quality and scope | `validate_release.py --release-version 1.2.0`, skill `quick_validate.py`, `node --check`, and `git diff --check` passed. Scoped diff and staged-file audit completed before commit. | Pass |
| Publication boundary | User authorized local implementation and commit; push and public deployment remain unauthorized. | Pass |

## Limitations

- Browser automation and static checks do not establish real-user usability, WCAG
  conformance, logistics correctness, or production performance.
- Google Fonts remain a remote dependency; the canonical capture waited for
  `document.fonts.ready` and retained system fallbacks.
