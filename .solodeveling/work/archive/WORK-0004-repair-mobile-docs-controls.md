---
solodeveling_schema: 1
---

# WORK-0004: Repair mobile Docs navigation and command controls

- **Status:** Done
- **Class:** Standard (production follow-up)
- **Problem:** At mobile width, the on-page Docs navigation remains sticky below the site header. A broad installation selector also overrides the command container grid, squeezing code into a narrow column while the Copy button occupies most of the row.
- **Root cause evidence:** At 390 px, `.docs-sidebar` computed to `position: sticky`. The first installation Copy button measured about 300 px inside a 335 px command container because `.install-methods article > div` also matches `.install-command`.

## Goal

Let the mobile documentation index scroll naturally with the page and restore a balanced, touch-usable code/Copy composition in both languages.

## Acceptance criteria

1. At widths up to 800 px, the documentation index is not sticky and remains horizontally scrollable.
2. Installation header grid rules do not apply to `.install-command`.
3. At narrow mobile width, command text receives the flexible column and Copy remains a compact right-hand control with at least a 44 px touch target.
4. EN/TH Docs retain copy feedback, no horizontal page overflow, valid anchors, and zero console errors.
5. Project checks pass; the repair is committed, pushed, and observed on the public EN/TH Docs routes.

## Plan

1. Narrow the installation header selectors and remove mobile sidebar stickiness.
2. Keep the mobile command shell in a two-column code/action composition.
3. Verify computed layout, copy feedback, overflow, and console in EN/TH.
4. Commit, push, observe workflows and public routes, then archive the work item.

## Rollback

Revert the repair commit if navigation access or command copying regresses.

## Outcome

Repaired, published, and observed on 2026-07-16. Mobile Docs indexes now scroll naturally, command text retains the flexible column, and Copy controls remain compact and functional in EN/TH. Evidence is recorded in `EVIDENCE-0006-mobile-docs-controls.md`.
