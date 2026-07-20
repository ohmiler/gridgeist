---
solodeveling_schema: 1
---

# WORK-0017: Evaluate the system-contract behavior

- **Status:** Done
- **Class:** Tracked Standard behavioral evaluation
- **Opened:** 2026-07-20
- **Authority:** The user explicitly authorized continuing with the checkpoint and
  fresh-agent evaluation sequence previously recommended.

## Candidate

- **Commit:** `a17064f0b0077aa88274b1d078d765bd711b0407`
- **Scope:** Scenario 19 design-system coherence and persistent-artifact boundaries.
- **Release state:** Local checkpoint only; no version bump, push, tag, or release.

## Acceptance

1. Run Scenario 19 in three independent English and three independent Thai fresh
   Codex CLI sessions using the same recorded model and runner version.
2. Give every run a disposable workspace containing only the fictional fixture and
   an exact local copy of the checkpointed Gridgeist skill; exclude repository
   memory, eval criteria, prior outputs, Git history, and project rules.
3. Use ephemeral sessions with user config and rules ignored, workspace-write
   authority limited to the disposable target, and no other visual-direction skill.
4. Preserve the exact prompts, raw final responses, runner/model metadata, target
   hashes, source-diff summaries, and whether the stale DESIGN.md hash changed.
5. Judge each run only after capture against the published Scenario 19 criteria:
   inspect and reconcile sources, define a proportional semantic/component system,
   preserve behavior, avoid preset/dependency/artifact overreach, and bind
   implementation claims to rendered evidence.
6. Run targeted guardrail smoke checks after Scenario 19: narrow frontend work must
   remain proportional, ambiguous redesign must align direction, explicit direction
   must proceed, state/recovery must remain primary, and companion ownership must
   remain clear.
7. Record failures and limitations without silently repairing the candidate. If a
   systemic failure appears, return to debugging before release planning.
8. Preserve all pre-existing untracked repository files and clean only exact
   disposable targets created by this work.

## Plan

1. Persist this contract and verify an isolated skill-discovery probe.
2. Create six fresh disposable targets from the checkpoint and record baseline
   hashes.
3. Run and capture EN1–EN3, then TH1–TH3 sequentially.
4. Inspect source changes and run fixture/browser verification for each completed
   implementation.
5. Judge the six runs, then execute the targeted guardrail smoke set.
6. Reconcile evidence and decide whether the candidate is ready for minor-release
   planning or requires a focused repair.

## Risks

- Full implementation runs may be slow or exceed runner limits; preserve timeouts as
  failed or unverified runs rather than substituting primary-agent implementation.
- A local skill copy may not be discovered under a clean runner; prove discovery
  before counting formal runs.
- Model nondeterminism means a single pass is not a stable pattern.
- Rendering tools may be unavailable inside a disposable runner; distinguish
  implementation behavior from independently verified browser evidence.

## Next action

No implementation work remains in this item. Candidate `a17064f` may enter
proportional minor-release planning if the user authorizes that next lifecycle step;
no version bump, push, tag, marketplace update, or publication has been performed.

## Outcome

- Six clean final-candidate Scenario 19 runs passed: EN2, EN3, EN4, and TH1–TH3.
- Writable guardrails exposed direction-alignment and companion-ownership control
  gaps. Both were diagnosed, repaired, and passed post-repair English and Thai
  checks; the explicit-direction control still implemented without over-questioning.
- Repository and skill validators, fixture syntax checks, diff checks, per-run hash
  audits, and primary Playwright verification passed.
- Raw responses, prompts, hashes, renders, failures, metadata, and judgment are in
  `evals/runs/2026-07-20-system-contract-a17064f/`.
