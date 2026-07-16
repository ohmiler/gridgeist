---
solodeveling_schema: 1
---

# EVIDENCE-0002: v1.1.0 behavioral evaluation

- **Candidate:** Gridgeist v1.1.0 payload at commit `316e0b1`.
- **Date:** 2026-07-16 Asia/Bangkok.
- **Method:** 30 fresh isolated Codex subagent runs: scenarios 5, 10, 11, 12, and 13; English and Thai; three runs per language and scenario.
- **Isolation:** Each agent used a fresh context, could not read evaluation criteria, prior run output, Solodeveling memory, or Git history. Scenario 12 was not given or allowed to inspect Gridgeist.

## Results

| Scenario | English | Thai | Behavioral decision | Implementation |
|---:|---:|---:|---|---|
| 5 — Accessibility repair | 3 / 3 | 3 / 3 | Pass | Not run — no fixture |
| 10 — Brand-adaptive portfolio | 3 / 3 | 3 / 3 | Pass | Not run — no fixture |
| 11 — Child drawing app | 3 / 3 | 3 / 3 | Pass | Not run — no fixture |
| 12 — Negative trigger | 3 / 3 | 3 / 3 | Pass | Not run — no fixture |
| 13 — State-complete import flow | 3 / 3 | 3 / 3 | Pass | Not run — no fixture |
| **Total** | **15 / 15** | **15 / 15** | **30 / 30 pass** | **0 / 30 run** |

## Observed behavior

- Accessibility reviews covered visible focus, non-color status cues, reduced motion, dialog focus containment, Escape behavior, and focus restoration without claiming rendered proof.
- Portfolio responses used quiet or invisible grids and preserved artwork, captions, project evidence, and fictional-work disclosure instead of imposing Swiss technical styling.
- Drawing-app responses made touch controls, pointer behavior, undo/redo branching, clear recovery, and local export concrete while preserving privacy and rejecting unsupported COPPA or child-research claims.
- All six negative-trigger runs kept the requested Save-handler change narrowly scoped and did not invoke Gridgeist or propose a redesign.
- Import-flow responses modeled file, row, partial-success, interruption, cancellation, and retry states before styling and did not assume backend idempotency or rollback guarantees.
- All explicit-skill runs separated proposed checks from observed verification and stated that no implementation or rendered viewport had been tested.

## Artifacts

- English scenario log: `evals/prompts.md`.
- Thai scenario log: `evals/prompts.th.md`.
- Raw responses: `evals/runs/2026-07-16-v1.1.0/` (30 files).

## Limitations

- These runs evaluate agent reasoning and scope control, not implementation quality.
- No executable fixture was supplied, so responsive rendering, browser interactions, accessibility behavior, and project checks remain untested.
- The evaluator was the primary Codex agent applying the prewritten pass criteria; this is independent generation, not independent human review.

## Decision

**Behavioral gate passed.** The release may proceed to a staged tag push and real installation/upgrade verification. Do not create the GitHub Release until the tagged marketplace source installs successfully.
