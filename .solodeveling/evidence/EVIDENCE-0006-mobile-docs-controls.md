---
solodeveling_schema: 1
---

# EVIDENCE-0006: Mobile Docs index and Copy control repair

- **Work item:** `WORK-0004-repair-mobile-docs-controls`
- **Date:** 2026-07-16
- **Target:** Shared EN/TH Docs CSS and GitHub Pages.
- **Result before publication:** Pass locally; production observation pending.

## Diagnosis

- At 390 px before repair, `.docs-sidebar` computed to `position: sticky` because the mobile media rule explicitly set `position: sticky; top: 76px`.
- The selector `.install-methods article > div` matched both the method heading wrapper and `.install-command`. At 390 px it forced the command shell into the heading grid: the first Copy button measured about 300 px inside a 335 px shell while the code column was squeezed.
- The smallest falsifiable correction was to remove mobile stickiness, scope heading grid rules to `div:first-child`, and retain a two-column command/action shell on narrow screens.

## Local verification

| Check | Result |
| --- | --- |
| Mobile index position | EN/TH computed `relative` at 390 px; after navigating to Install its top moved to approximately -1189 px EN / -1153 px TH, confirming it scrolls away. |
| Installation composition | EN/TH first command code width measured about 271 px and Copy width 64 px at 390 px. Copy retained a touch height above 44 px. |
| Copy feedback | Playwright observed `Copied` and `คัดลอกแล้ว`. |
| Overflow | EN 390/390, TH 390/390 and 360/360 client/scroll widths. EN desktop remained 1280/1280. |
| Desktop behavior | Sidebar remained sticky at 1280 px. |
| Console | Zero errors and warnings in checked EN/TH sessions. |
| Project checks | Release validator, JavaScript syntax, and `git diff --check` passed. |

## Scope and limits

- Only shared Docs CSS and Solodeveling records changed; HTML, commands, routes, and copy JavaScript were preserved.
- Pixel-level screenshot inspection remains unavailable because the environment image viewer cannot launch without the Windows sandbox helper.
- Production workflow and route observation are pending publication.

## Post-push observation

Pending.
