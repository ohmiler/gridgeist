---
name: gridgeist
description: Use when creating, redesigning, or reviewing web interfaces that need product-specific structure, clear hierarchy, responsive composition, accessible interaction, or relief from generic AI-generated SaaS aesthetics. Adapt grid, typography, imagery, motion, and product evidence to the established brand—including technical, editorial, image-led, warm, playful, and utilitarian directions—across React, Next.js, Tailwind CSS, HTML/CSS, landing pages, dashboards, documentation, portfolios, and interactive tools.
---

# Gridgeist

## Overview

Craft distinctive, product-native interfaces from audience, content, behavior, and brand intent. Use grid as structural logic; make it visible only when it serves the product.

## Select a mode

| Intent and authorization | Mode | Start with |
|---|---|---|
| Build an interface without an existing design | Create | Audience, primary task, content, and evidence |
| Change an existing interface with permission to edit | Redesign | Preserved behavior, brand signals, and state inventory |
| Diagnose without changing files | Review | Prioritized findings grounded in rendered evidence |

Let user authorization determine whether files change. Derive direction from an established brand; present options only when brand signals conflict materially or the user requests exploration.

## Workflow

1. **Inspect** — Understand the audience, primary tasks, brand signals, content, product evidence, routes, components, tokens, and rendered desktop/mobile UI. Inventory important interaction states and constraints. Do not invent customers, metrics, outcomes, research, or compliance.
2. **Set a thesis** — Write one governing sentence combining audience, primary task, structural logic, brand expression, and a product-native motif. Read [design-language.md](references/design-language.md) before choosing the direction, especially for image-led, warm, playful, or otherwise nontechnical brands.
3. **Define the system** — Establish container and tracks, type roles, spacing rhythm, semantic color, shape and surface roles, image behavior, motion, and responsive transformations. Decide whether the grid should be visible, quiet, or invisible. Prefer reusable tokens over one-off values.
4. **Compose** — Build hierarchy before detail. Make one area dominant, align related content, vary sections within shared logic, and let the most authentic material—product UI, data, prose, imagery, artwork, code, or the primary tool—carry visual weight.
5. **Implement** — Preserve required behavior and states. Follow repository conventions, semantic HTML, keyboard and touch behavior, and existing primitives. Recompose mobile layouts rather than shrinking desktop. Avoid dependencies for simple CSS effects.
6. **Verify** — Use [review-checklist.md](references/review-checklist.md). Render representative widths and exercise primary flows, states, focus behavior, reduced motion, overflow, and dynamic content. Fix clarity and hierarchy before polish. Report what was observed separately from what remains inferred or untested.

For interactive products, inventory at least default, loading, empty, error, success, disabled, and destructive states when applicable. Preserve privacy, safety, data, and platform constraints as product behavior, not optional polish.

## Anti-slop contract

- Use one thesis and one coherent system.
- Preserve or deliberately evolve the brand instead of importing a house aesthetic.
- Build hierarchy through scale, position, density, rhythm, and contrast.
- Give grid visibility, borders, radii, shadows, gradients, and motion defined roles.
- Prefer authentic product evidence; label sample or fictional material and never fabricate proof.
- Give sections or workflows distinct compositions within shared structural logic.

Repeated rounded cards, centered hero copy, gradient blobs, excessive pills, uniform sections, arbitrary icon boxes, generic claims, and technical chrome on nontechnical brands are diagnostic signals, not automatic violations. Replace weak structure with a stronger product-specific idea.

## Decision reference

| Dimension | Decide from |
|---|---|
| Structure | Information order, task flow, shared alignments, and the brand's degree of regularity |
| Type | Brand voice, reading needs, and role hierarchy; reserve mono for genuinely technical content |
| Visual lead | Product UI, data, prose, imagery, artwork, code, or a primary interactive surface |
| Shape and surface | Brand geometry, containment, adjacency, state, and interaction—not fashion |
| Color | Existing brand palette and semantic roles; do not assume neutral plus one accent |
| Motion | Causality, feedback, spatial change, and tone, with reduced-motion support |
| Responsive | Priority, order, density, input method, and content behavior at each range |

## Output contract

For Create or Redesign, provide **Direction** with the thesis and preserved constraints, complete responsive **Implementation**, and **Verification** evidence naming observed viewports, flows, states, and remaining gaps. For Review, make no edits and provide a one-line **Verdict**, prioritized findings with location, evidence, impact, and the smallest coherent correction, plus one replacement **Direction**. Never claim verification without observation.

## Common mistakes

| Mistake | Correction |
|---|---|
| Treating Gridgeist as a visible-grid preset | Use grid as underlying logic and expose it only when the brand benefits |
| Copying a reference literally | Extract principles and preserve the user's identity and content |
| Styling before understanding behavior | Inventory tasks, constraints, and states before composing |
| Making minimalism empty | Add useful evidence and controlled density |
| Improving the default state only | Design loading, empty, error, success, disabled, and destructive paths |
| Stacking desktop UI on mobile | Redesign order, density, navigation, media, and interaction |
| Reporting subjective taste alone | Tie findings to comprehension, usability, consistency, brand, or accessibility |
| Reporting automated checks as user evidence | Separate technical verification from usability, safety, and research claims |

## Contrasting examples

> Redesign dense API documentation with a visible information grid, precise code states, and verified mobile navigation.

> Redesign a warm image-led portfolio with an invisible alignment system, expressive type, artwork-led pacing, and accessible project narratives.
