---
solodeveling_schema: 1
---

# WORK-0002: Refresh the main site for Gridgeist v1.1

- **Status:** Done
- **Class:** Standard
- **Users:** Developers and design-minded builders evaluating, installing, or learning Gridgeist in English or Thai.
- **Problem:** The current site has a strong recognizable brand but still presents Gridgeist primarily as a visible Swiss/technical treatment, carries stale evaluation evidence, leads installation with Git clone, removes primary navigation on mobile, and does not fully suppress pointer-led hero motion for reduced-motion users.

## Goal

Make the public site demonstrate the v1.1 product-native, brand-adaptive method while preserving the existing Gridgeist identity and all established routes.

## In scope

- Refresh English and Thai homepage messaging together.
- Preserve the wordmark, paper/ink/cobalt palette, strong editorial type, and visible hero grid as recognizable brand signals.
- Add a clear demonstration that structure may be visible, quiet, invisible, or state-led according to the product.
- Update evaluation evidence to 13 scenarios and 30 fresh targeted bilingual runs with the implementation-fixture limitation stated.
- Make Codex plugin installation the primary path and expose Agent Skills and update commands.
- Restore access to primary routes on mobile.
- Disable pointer-led hero movement when reduced motion is requested or a fine pointer is unavailable.
- Align obvious Gridgeist v1.1 wording drift in English and Thai documentation rails.

## Out of scope

- Changing release version, plugin metadata, skill behavior, or evaluation results.
- Rebuilding Tracefield, Examples, or documentation page layouts.
- Adding dependencies, analytics, accounts, or backend behavior.
- Claiming implementation evaluation, user research, accessibility conformance, or universal design quality.

## Acceptance criteria

1. English and Thai homepages describe Gridgeist as product-native and brand-adaptive without losing the existing identity.
2. The page visibly explains multiple structural modes and labels illustrative specimens honestly.
3. Evaluation evidence reports 13 scenarios and 30 targeted fresh runs and distinguishes behavioral evidence from implementation verification.
4. The primary install surface shows the documented Codex marketplace commands, with Agent Skills and update paths also discoverable and copyable.
5. Docs, examples, install, and key on-page sections remain reachable at mobile widths through a semantic navigation control.
6. Existing comparison and copy interactions continue to work; reduced-motion users do not receive pointer-following hero axes.
7. English and Thai pages have no unintended horizontal overflow and retain coherent hierarchy at approximately 360, 768, 1280, and 1600 px.
8. Relevant validator, keyboard/focus checks, interaction checks, and console checks pass, with remaining visual or user-research gaps recorded.

## Risks and decisions

- **Brand dilution:** Preserve the hero and core tokens; vary structural intensity in later sections instead of replacing the house identity.
- **Evidence overclaim:** Present 30 / 30 as targeted behavioral runs only and explicitly say implementation fixtures were not run.
- **Mobile menu complexity:** Use native `details`/`summary` rather than adding a custom dialog or dependency.
- **Content drift:** Change English and Thai in the same slices and verify both.
- **Rollback:** Revert the website-refresh commit; the skill and v1.1.0 release artifacts are unaffected.

## Plan

1. Update shared header, homepage content, adaptive specimens, evidence, install surface, and shared interaction script.
2. Apply equivalent Thai content and language-specific layout adjustments.
3. Align the documentation quick-reference language with the v1.1 method.
4. Run release validation, HTML/static inspection, and browser verification across representative viewports, navigation, comparison, copy, focus, reduced motion, and console state.
5. Record evidence, move the work item through Verifying to Done, and archive it.

## Outcome

Implemented and locally verified on 2026-07-16. Evidence is recorded in `EVIDENCE-0004-main-site-refresh.md`. Publication remains a separate production action.
