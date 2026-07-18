---
solodeveling_schema: 1
---

# WORK-0008: Validate direction alignment before GridGeist redesigns

- **Status:** Done
- **Class:** Tracked Standard
- **Completed:** 2026-07-18
- **Authority:** On 2026-07-18 the user authorized execution of this ready work item. This authorizes fixture, evaluation, evidence, and—only if the recorded threshold is met—minimum core-skill changes. It does not authorize publishing a release, modifying an external project, or production changes.

## Goal and boundary

Determine whether GridGeist needs a conditional direction-alignment gate before broad Create or Redesign implementation, while preserving autonomous execution for explicit directions, evidence-backed brand continuation, reviews, and narrow frontend repairs.

The motivating observation is that an agent implicitly selected GridGeist for a broad webpage-adjustment request and proceeded directly to design and implementation without first aligning on the user's preferred direction. Treat that report as a useful product signal, not as an independently reproduced failure.

## Scope

- Add the smallest paired English/Thai behavioral evaluation that contrasts an underspecified broad redesign with an explicit-direction control on the same inspectable fixture.
- Use existing Review and narrow-frontend scenarios as controls against unnecessary questioning.
- Capture current v1.1.0 behavior before changing core guidance.
- If the evidence threshold is met, make the smallest conditional workflow change between **Inspect** and **Set a thesis**, then rerun affected behavioral and repository checks.
- Keep public English and Thai guidance aligned if the behavior becomes user-facing documentation.

## Out of scope

- A mandatory questionnaire or brainstorming ceremony for every web task.
- Asking for preferences already established by repository evidence, brand tokens, or explicit user constraints.
- Adding style presets, categories, or a default GridGeist visual aesthetic.
- Release, marketplace, installation, or production changes without separate user authority.

## Decisions

- Prefer a conditional **direction-alignment gate**, not universal clarification.
- Ask only when a missing choice materially changes the visual thesis or would replace core brand expression, color, imagery, hierarchy, or motion.
- Do not default to asking “which color?”; preserve established palettes and ask about color only when no palette exists or changing it is in scope.
- For an underspecified broad redesign, present two or three evidence-grounded directions with trade-offs and a recommendation before editing.
- For Review, report evidence immediately and label an unconfirmed replacement direction as provisional; do not block the review on aesthetic preferences.
- Treat the current user report as motivating evidence. Do not revise the frozen v1.1.0 core until the behavior is severe or reproduced as a pattern in at least two independent project contexts, consistent with the roadmap.

## Acceptance criteria

1. English and Thai eval coverage uses the same fixture and distinguishes an underspecified broad redesign from an explicit-direction control.
2. The ambiguous case checks whether the agent inspects first, grounds questions in observed product/brand evidence, offers coherent options and trade-offs, recommends one, and avoids editing before alignment.
3. The explicit case checks that the agent states the evidence-backed direction and proceeds without redundant preference questions.
4. Existing Review and narrow frontend controls confirm that the gate does not turn reviews, accessibility or defect repair, or small implementation work into unnecessary brainstorming.
5. Current v1.1.0 baseline runs are preserved with prompt, language, agent/model context, skill revision, raw output, result, and limitations; repeated behavior follows the existing three-run evaluation convention where practical.
6. No core change is made from the motivating report alone. A core edit requires the roadmap evidence threshold or a separately documented severe finding.
7. If a core edit is justified, it remains conditional, sits between Inspect and Set a thesis, distinguishes user-confirmed, brand-derived, and provisional direction, and does not impose a universal questionnaire.
8. A justified edit passes affected EN/TH behavioral regressions, existing Review and negative-trigger controls, skill validation, `python scripts/validate_release.py`, and scoped diff review before completion is claimed.

## Execution plan

1. Inspect the smallest suitable fixture boundary and create an isolated, runnable direction-alignment fixture with a clear audience, primary task, real content, and working behavior, but without leaking an expected visual answer.
2. Add paired EN/TH prompts for the ambiguous and explicit variants. Reuse existing Review and narrow-repair scenarios as regression controls rather than duplicating them.
3. Run the current v1.1.0 skill in fresh contexts and append raw, scenario-level results to `EVIDENCE-0010`; do not expose desired answers to the evaluated agent.
4. Classify the baseline: appropriate autonomy, unnecessary questioning, unsupported autonomous direction, or inconclusive. Record whether the reported behavior reproduces across independent contexts.
5. If the evidence threshold is not met, retain the eval and evidence without changing the core. If it is met, patch only the minimum workflow/output guidance required for the conditional gate.
6. Rerun the paired scenarios and the relevant Create, Redesign, Review, brand-conflict, and negative-trigger regressions in English and Thai.
7. Run repository validation, inspect the final diff, reconcile WORK/state/evidence, and leave release or publication as a separately authorized action.

## Risks and recovery

- **Over-questioning:** A broad rule could make the agent slow and shift design work back to the user. Protect explicit-direction, Review, and narrow-repair controls.
- **Under-questioning:** A weak rule could let an agent implement a polished but unwanted identity. Require a pre-edit gate only when thesis-level ambiguity is material.
- **Biased evaluation:** A fixture or rubric could reveal the expected answer. Keep product facts observable while withholding desired style, and preserve independent raw runs.
- **Nondeterminism:** One output cannot establish a behavioral pattern. Use repeated runs and preserve agent/model/language context.
- **Recovery:** If a proposed core edit causes regression, keep the fixture and evidence, remove or revise only the unproven core change, and leave v1.1.0 guidance frozen.

## Next executable action

None for this work item. The verified change remains Unreleased; version bump,
release preparation, marketplace update, and publication require separate authority.
