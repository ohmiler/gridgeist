---
solodeveling_schema: 1
---

# WORK-0016: Strengthen the Gridgeist design-system contract

- **Status:** Complete
- **Class:** Tracked Standard capability expansion
- **Opened:** 2026-07-20
- **Authority:** The user explicitly authorized implementing the previously reviewed
  colors, typography, layout, component-system, and optional DESIGN.md improvements.

## Goal

Make Gridgeist produce more coherent, reusable interface systems without turning it
into a fixed visual preset or imposing persistent design artifacts on narrow work.

## Decisions

- Keep `SKILL.md` concise and place detailed system guidance in one directly linked
  reference.
- Treat existing brand assets, tokens, themes, component libraries, and DESIGN.md
  files as evidence to inspect, not as automatically correct or mutually consistent.
- Define a compact system contract before composition when Create or Redesign work
  needs new or changed system decisions.
- Make DESIGN.md interoperability optional: consume it when present and create or
  update it only when the user requests a portable artifact or the authorized work
  explicitly requires durable system documentation.
- Preserve framework and repository conventions; do not require shadcn/ui, a token
  format, a new dependency, or fixed palette, type, radius, spacing, or component
  values.

## Acceptance

1. The core workflow inspects existing system sources and explicitly covers color,
   typography, layout, component grammar, states, and responsive behavior while
   remaining concise.
2. A conditional reference explains the system contract, source reconciliation,
   semantic tokens, component anatomy/variants/states, responsive rules, and
   optional DESIGN.md artifact policy.
3. The review checklist separately evaluates color/theming coherence and component
   system coherence, not only contrast or implementation style.
4. English and Thai evaluation guidance measure color and component-system
   coherence, with one new contiguous paired scenario backed by a runnable fixture.
5. English and Thai READMEs describe optional DESIGN.md intake/output without
   presenting it as a dependency or proof of quality.
6. The Unreleased changelog describes the behavior change without claiming a
   release or unrun behavioral result.
7. Skill validation, repository validation, bilingual scenario alignment, Markdown
   integrity, and diff-scope checks pass; unrelated user files remain untouched.

## Risks and mitigations

- **Instruction bloat:** Keep the core change compact and route details through one
  reference.
- **Over-formalizing small repairs:** Apply the contract proportionally and do not
  require a new artifact for narrow work.
- **Brand erasure through token presets:** Derive decisions from the product and
  existing brand; include no house token values.
- **Unstable external format:** Describe DESIGN.md as optional interoperability and
  avoid a package or CLI dependency.
- **Behavioral overclaim:** Add the eval contract but record it as not independently
  run until fresh-agent evaluation exists.

## Plan

1. Persist the active work contract and inspect bilingual insertion points.
2. Update the core skill and add the conditional system-contract reference.
3. Extend review, README, changelog, and paired evaluation guidance.
4. Inspect the complete diff and run focused plus repository validation.
5. Reconcile work, evidence, and state; archive only after every acceptance item is
   supported or explicitly left unverified.

## Next action

Run paired fresh-agent Scenario 19 evaluations from disposable fixture copies before
using this capability expansion as evidence for a future minor release.

## Execution record

- Updated the core Inspect, Define the system, decision, output, and common-mistake
  guidance while routing conditional detail through one new reference.
- Added proportional color, typography, layout, token, component-grammar, state,
  media, motion, responsive, and optional DESIGN.md guidance without adding a
  dependency or preset.
- Added separate review sections for color/theming and component-system coherence.
- Added aligned English and Thai Scenario 19 guidance plus a runnable two-route
  fixture with theme, profile-save, invoice-filter, and local status behavior.
- Added aligned English and Thai README guidance and Unreleased changelog entries.
- Browser verification exposed and then confirmed the repair of a 360 px fixture
  overflow; final profile and billing widths matched the viewport and console output
  was clean.
- Cumulative verification and limitations are recorded in
  `EVIDENCE-0018-design-system-contract.md`.
