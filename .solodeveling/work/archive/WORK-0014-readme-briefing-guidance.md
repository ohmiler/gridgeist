---
solodeveling_schema: 1
---

# WORK-0014: Add README briefing guidance

- **Status:** Complete
- **Class:** Standard bilingual documentation change
- **Opened:** 2026-07-19

## Goal

Help users brief Gridgeist for results that match their intent without requiring
them to prescribe implementation-level CSS decisions.

## Scope

- Expand the English and Thai README usage sections with equivalent guidance.
- Preserve the existing four-item minimum brief and Create, Redesign, and Review
  examples.
- Add a detailed briefing checklist, explicit-versus-uncertain direction guidance,
  a copyable prompt template, and advice on what to leave for Gridgeist to derive.
- Do not change the installable skill, plugin version, evaluation scenarios,
  production site, installation instructions, or release state.

## Acceptance

1. Both READMEs retain the same minimum four briefing inputs.
2. Both READMEs explain product/audience, primary task, direction, authentic
   material, preserved constraints, exclusions, flows/states, and verification.
3. Both READMEs distinguish a confirmed direction from a materially ambiguous one
   and tell the agent not to edit before alignment in the latter case.
4. Both READMEs provide an equivalent copyable prompt template and explain that
   users need not prescribe fonts, spacing, radii, shadows, or column counts unless
   those are genuine constraints.
5. Repository validation and scoped diff checks pass, with unrelated user files
   preserved.

## Plan

1. Add matched briefing guidance after the existing prompt examples in each README.
2. Inspect the rendered Markdown structure and bilingual intent for parity.
3. Run repository validation and diff checks.
4. Record evidence, reconcile state, and archive the completed work item.

## Recovery

Revert only the new briefing-guidance sections in `README.md` and `README.th.md`,
plus this work's Solodeveling memory entries. No release or production rollback is
required.

## Lifecycle

The user requested the README update directly; scope and acceptance were clear from
the existing usage guidance and the immediately preceding briefing discussion. The
work therefore passed through captured, shaped, and ready during inspection and
entered active before implementation edits.

## Execution record

- Added the four minimum briefing inputs to the English usage section while
  preserving the existing English examples and the established Thai minimum list.
- Added equivalent EN/TH detailed checklists, direction-alignment guidance,
  copyable prompt templates, and outcome-over-CSS advice.
- Kept the installable skill, plugin metadata, evaluations, production site,
  installation guidance, and release state unchanged.
- Verification passed; see `EVIDENCE-0016-readme-briefing-guidance.md`.
