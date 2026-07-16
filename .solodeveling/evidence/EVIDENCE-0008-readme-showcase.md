---
solodeveling_schema: 1
---

# EVIDENCE-0008: GridGeist v1.1.0 README showcase refresh

- **Work item:** `WORK-0006-refresh-readme-showcase`
- **Date:** 2026-07-17
- **Target:** Northline After page, README EN/TH comparison, and rendered README asset.
- **Result:** Pass.

## Baseline

- Commit `6a6725c` added the Northline comparison before commit `316e0b1` introduced the GridGeist v1.1.0 skill and its design-language/review references.
- Existing Before and After screenshots are both 1440 x 900; only the After screenshot is in scope for replacement.
- The current After page already uses route topology and operating values, but it does not identify sample data on the rendered page and predates the v1.1.0 brand-adaptation and verification contract.

## Acceptance verification

| Criterion | Method | Result |
| --- | --- | --- |
| EN/TH v1.1.0 and truth context | README inspection plus UTF-8 content audit | Pass: both READMEs identify the After refresh as Gridgeist v1.1.0, describe sample operating data, and state that Northline/data are fictional. |
| Product evidence and preserved comparison | Source/content audit and desktop visual inspection | Pass: the original Northline copy, 148 / 96.4% / 03 values, three lane IDs/routes, arrival times, and route cities remain; the network topology and visible exception state lead the After composition. |
| Responsive, targets, focus, and motion | Playwright at 360, 768, 1280, 1440, and 1600 px; HTML fragment audit; CSS inspection | Pass: client/scroll widths matched at every checked width; all fragment links resolve to unique IDs; Tab focused `NORTHLINE_` with a solid 3 px acid outline; reduced-motion rules remain present. |
| Fresh README image and stable baseline | Playwright viewport capture, image metadata, Git diff | Pass: `northline-after.png` is a fresh 1440 x 900 PNG with SHA-256 `CA1B9377E3A27B33EDC03D1E60DDAB6DBC0BC21197073086CE63A0CC20B41DD5`; `northline-before.png` is unchanged. |
| Project and browser checks | Release validator, official skill validator, HTML parser, Node syntax check, browser console, `git diff --check` | Pass: validators and syntax checks succeeded, final browser console reported zero errors/warnings, and the repository diff check passed with only expected Windows line-ending warnings. |

## Rendered observations

- At 1440 x 900 the route topology occupies the dominant right-hand surface, while the operational headline, lane rows, and metrics form one connected scan path.
- The SGN to HKG row and orange Exceptions metric expose the `CHECK` / `03` state without relying on color alone.
- At 360 x 800 the page recomposes into headline, network, lanes, then metrics with no horizontal page overflow; controls retain readable labels and the desktop grid is not squeezed onto mobile.
- The final tracked image was opened and visually inspected after a specificity correction made the `03` value visible against the orange exception surface.

## Commands and observed results

- `python -X utf8 scripts/validate_release.py` — pass.
- Official Gridgeist `quick_validate.py` — `Skill is valid!`.
- `node --check site/readme-showcase/showcase.js` — pass.
- Python stdlib HTML parse/ID/fragment/preserved-copy/README audit — pass.
- Playwright snapshots, viewport resizes, screenshots, focus inspection, and console inspection — pass at the viewports named above; zero console errors/warnings.
- Image metadata and Git scope inspection — After 1440 x 900; Before unchanged.
- `git diff --check` — pass; Git emitted expected LF-to-CRLF warnings on Windows.

## Scope and limits

- The Before source and screenshot were intentionally preserved so the comparison remains stable.
- The example is an illustrative concept with sample data; verification does not represent user research, live logistics behavior, or a production accessibility audit.
- Google Fonts remain a remote enhancement with system fallbacks; the final capture was taken after the rendered page settled.
- An initial auxiliary UTF-8 audit misencoded em dashes through a PowerShell here-string. The harness was corrected to use Unicode escapes and the scoped audit passed; this was not treated as a product failure.
