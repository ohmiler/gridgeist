# Gridgeist System Contract

Use this reference when Create or Redesign work introduces or changes visual-system
decisions. Apply it proportionally: a narrow repair may need only the affected
tokens, component, and states; a greenfield or multi-surface interface needs a
broader contract.

## Reconcile sources before defining values

Inspect the sources that actually exist:

- explicit user constraints and the selected direction;
- established brand assets and content;
- rendered desktop and mobile behavior;
- CSS variables, theme configuration, utility conventions, and design tokens;
- component libraries, local primitives, variants, and state implementations;
- design documentation, including `DESIGN.md` when present.

Treat disagreement as a finding. Do not silently let an aspirational document
override working product behavior, or let accidental implementation drift erase an
intentional brand rule. Mark meaningful signals as preserve, evolve, or replace and
state the product reason for a replacement.

## Define the smallest complete contract

Record decisions in the project's native implementation format whenever possible.
Use this compact contract in reasoning or handoff when several dimensions change:

| Dimension | Minimum relevant decisions |
|---|---|
| Color and themes | Canvas, surface, text, muted, border, accent, destructive, focus, and applicable status roles; foreground/background pairs; light, dark, forced-color, or user-theme behavior when supported |
| Typography | Display, heading, body, label, metadata, and code roles only when needed; family and fallback, size, weight, line height, tracking, measure, language coverage, and loading behavior |
| Layout and spacing | Container behavior, tracks, gutters, spacing rhythm, section density, alignment anchors, and transformations across viewport or container ranges |
| Shape, surface, and depth | Radius, border, shadow, texture, elevation, and adjacency roles; avoid values that differ without a product or state reason |
| Component grammar | Shared anatomy, variants, sizes or density, state behavior, content limits, composition rules, and narrow-container behavior |
| Media and motion | Crop, aspect ratio, loading and empty behavior, motion causality, duration or easing roles, and reduced-motion treatment |

Do not invent every category for completeness. Omit roles the product does not need,
but cover every dimension changed by the work.

## Use token layers deliberately

- **Foundation tokens** hold raw palette, type, spacing, radius, and motion values.
- **Semantic tokens** express purpose such as canvas, text-muted, border-strong,
  action-primary, focus-ring, success, warning, or destructive.
- **Component tokens or variants** bind semantic roles to a component only when a
  shared component needs a stable exception.

Prefer semantic tokens in implementation. Keep foreground/background pairs and
interaction-state relationships explicit. Reuse an existing scale when it is
coherent; consolidate accidental near-duplicates instead of adding another magic
value. A token file is evidence of intent, not proof that rendered contrast,
hierarchy, or behavior is correct.

## Define component grammar

For each component family affected by the work:

1. Identify its product job and required anatomy.
2. Keep variants task-based, such as primary, secondary, quiet, or destructive,
   rather than naming them after isolated visual treatments.
3. Define only justified sizes or density modes and preserve usable targets.
4. Cover applicable default, hover, focus, active, selected, disabled, loading,
   empty, error, success, and destructive behavior.
5. Keep state cues visible without relying on color alone.
6. Define content stress behavior: long labels, missing media, localization,
   dynamic data, overflow, and narrow or wide containers.
7. Reuse existing primitives and repository conventions unless changing them is an
   explicit, system-level decision.

Do not require a particular component library. A coherent local primitive is better
than importing a dependency solely to make the contract look formal.

## Treat DESIGN.md as optional interoperability

When a `DESIGN.md` file exists:

- inspect its tokens and rationale during discovery;
- trace relevant values into the theme, components, and rendered interface;
- report stale, conflicting, unreachable, or one-off values;
- preserve or update it only within the user's authorized scope.

When it does not exist, do not create one automatically. Create or update a
`DESIGN.md` only when the user requests a portable design-system artifact or the
authorized work explicitly requires durable system documentation. Keep exact values
machine-readable and explain the rationale in prose. Use an existing validator when
available, but do not add a package, CLI, or network dependency without need and
authorization.

The project implementation remains the delivery target. A portable artifact does
not replace rendered, responsive, interaction, or accessibility verification.

## Keep the contract proportional

- **Narrow repair:** preserve the established system; document only the affected
  token, component rule, and states.
- **Single surface:** define the system decisions needed for that page or workflow
  and map them to reusable project tokens and primitives.
- **Multiple surfaces or greenfield:** define the broader contract, show how shared
  components inherit it, and identify any intentional local exceptions.
- **Review:** diagnose drift and recommend the smallest coherent correction; do not
  create or edit an artifact without authorization.
