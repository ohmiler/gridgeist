---
solodeveling_schema: 1
---

# WORK-0003: Redesign the bilingual documentation site

- **Status:** Verifying
- **Class:** Standard (audited release)
- **Users:** Developers evaluating, installing, updating, and applying Gridgeist in English or Thai.
- **Problem:** The Docs pages retain a strong visual base but still identify themselves as v1.0, hide cross-site navigation on mobile, under-explain v1.1 brand adaptation, and present commands without the copy behavior used by the main site.

## Goal

Turn the English and Thai Docs pages into a reading-first v1.1 field manual that demonstrates Gridgeist's product-native documentation guidance while preserving established routes, content truth, and brand identity.

## Direction

A field manual for solo builders organized by persistent reading orientation, decision-led editorial structure, and authentic prompts, commands, workflow, and verification evidence in Gridgeist's paper/ink/cobalt identity. The grid remains visible but quieter than the homepage so prose and decisions lead.

## In scope

- Redesign English and Thai Docs together.
- Update version and workflow language to v1.1.
- Add an explicit structural adaptation decision section.
- Improve quickstart, install/update, mode, brief, workflow, verification, and limitations hierarchy without inventing claims.
- Add semantic mobile cross-site navigation and reusable copy interactions.
- Recompose the layout across representative widths and preserve current anchors and routes.
- Commit and push the verified source to `origin/main`, then observe GitHub checks and the published critical route when available.

## Out of scope

- Changing the skill, plugin, release version, evaluation results, or installation commands.
- Rebuilding Examples or Tracefield.
- Adding dependencies, search, analytics, backend features, or claiming accessibility conformance/user research.

## Acceptance criteria

1. EN/TH Docs identify v1.1 and present a clear first-use path for evaluating, installing, and invoking the skill.
2. The information architecture reflects Create/Redesign/Review, visible-to-invisible structural adaptation, the current six-step workflow, and evidence-bounded verification.
3. Codex, Agent Skills, manual, and update paths remain accurate; primary commands are keyboard-accessible and copyable.
4. Existing anchors and routes remain usable, with semantic mobile navigation providing cross-site access.
5. Both languages retain coherent reading hierarchy and no unintended horizontal overflow near 360, 768, 1280, and 1600 px.
6. Details, copy, navigation, keyboard focus, and reduced-motion behavior work without console errors in Chromium.
7. Release validation and diff checks pass; limitations and rollback are recorded.
8. The verified candidate is committed and pushed to `origin/main`; post-push checks and published-route observation are recorded where available.

## Risks and decisions

- **Reading fatigue:** Keep body measure controlled and vary density by task rather than adding decorative panels.
- **Brand over-application:** Use a quieter visible grid than the homepage; commands and decision artifacts carry hierarchy.
- **Bilingual drift:** Change and verify EN/TH in matched slices.
- **Evidence overclaim:** Keep 30/30 labeled as targeted behavioral evaluation only.
- **Release target:** GitHub `origin/main`; Pages deployment is driven by repository workflow.
- **Last known good:** Commit `83583b0` locally; remote baseline will be recorded before push.
- **Rollback:** Revert the Docs redesign commit and push the revert if published navigation, reading, or layout regresses.

## Plan

1. Recompose the shared Docs shell, hero, orientation, and v1.1 content model.
2. Implement matched English and Thai content, navigation, copy affordances, and responsive styles.
3. Run static validation and Chromium checks across representative widths and interactions.
4. Record the acceptance matrix and release candidate, archive the work item, commit, and push.
5. Observe GitHub checks and the public Docs routes; record unavailable production signals as gaps.

## Next action

Reconcile the acceptance matrix, release candidate, evidence, and publication readiness before committing and pushing.
