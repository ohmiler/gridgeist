---
name: gridgeist
description: Use when creating, redesigning, or reviewing web interfaces that need a strong grid, precise typography, technical minimalism, Swiss or editorial influence, visible borders, or relief from generic AI-generated SaaS aesthetics. Applies to React, Next.js, Tailwind CSS, HTML/CSS, landing pages, dashboards, documentation, portfolios, and learning platforms.
---

# Gridgeist

## Overview

Craft distinctive interfaces from content and product intent. Make grid, type, spacing, borders, and product UI the visual language; decoration supports the system.

## Select a mode

| Intent | Mode | Start with |
|---|---|---|
| Build a new interface | Create | Content hierarchy and visual thesis |
| Restyle working UI | Redesign | Behavior preservation and pattern inventory |
| Improve a draft | Review | Prioritized diagnosis before edits |

If direction materially affects brand identity, present 2–3 concise options for approval. Otherwise proceed.

## Workflow

1. **Inspect** — Understand product, audience, content, routes, components, tokens, and rendered desktop/mobile UI. Preserve intentional brand and behavior.
2. **Set a thesis** — Write one governing sentence, such as: “A precise learning workspace built on an editorial grid, quiet rules, dense product evidence, and one blue accent.” Read [design-language.md](references/design-language.md) when selecting influences.
3. **Define the system** — Establish container, columns, spacing rhythm, type roles, colors, radius, borders, shadows, and responsive transformations. Prefer reusable tokens over one-off values.
4. **Compose** — Build hierarchy before detail. Align related content, use visible rules to clarify structure, vary section composition, and make one area dominant. Let real code, data, lessons, screenshots, or workflows carry visual weight.
5. **Implement** — Follow repository conventions, semantic HTML, keyboard behavior, and existing primitives. Recompose mobile layouts rather than shrinking desktop. Avoid dependencies for simple CSS effects.
6. **Refine** — Use [review-checklist.md](references/review-checklist.md). Fix issues in this order: clarity, hierarchy, alignment, type/color, interaction/responsiveness, accessibility, implementation quality. Reinspect the rendered result.

## Anti-slop contract

- Use one thesis and one coherent system.
- Build hierarchy through scale, position, density, and contrast.
- Give borders, radii, shadows, gradients, and motion defined roles.
- Prefer product-specific copy and evidence over interchangeable decoration.
- Give sections distinct compositions within the shared grid.

Repeated rounded cards, centered hero copy, gradient blobs, excessive pills, uniform sections, arbitrary icon boxes, and generic claims are diagnostic signals, not automatic violations. Replace weak structure with a stronger product-specific idea.

## Quick reference

| Element | Starting point |
|---|---|
| Grid | 12 wide-screen columns; simpler purposeful tracks below |
| Type | Sans hierarchy; mono only for technical metadata |
| Spacing | Small token scale with controlled dense/airy contrast |
| Borders | Quiet 1px rules that organize rather than outline everything |
| Shape | Restrained, consistent radii; square corners are valid |
| Color | Neutral base with one controlled accent family |
| Motion | Short functional transitions with reduced-motion support |
| Visuals | Authentic product UI, code, data, diagrams, or imagery |

Adapt these defaults to the brand; do not turn them into a preset.

## Output contract

For creation/redesign, provide: **Direction**, complete responsive **Implementation**, and **Review** evidence. For review-only tasks, provide: one-line **Verdict**, prioritized findings with evidence, and a coherent replacement **Direction**.

## Common mistakes

| Mistake | Correction |
|---|---|
| Copying a reference literally | Extract principles and preserve the user's brand |
| Drawing lines around everything | Use rules to reveal hierarchy and alignment |
| Calling any sparse page Swiss | Require rational grid, type hierarchy, and information order |
| Making minimalism empty | Add useful product evidence and controlled density |
| Styling before understanding content | Establish information hierarchy first |
| Stacking desktop UI on mobile | Redesign order, density, navigation, and interaction |
| Reporting subjective taste alone | Tie findings to usability, consistency, brand, or accessibility |

## Example

> Use Gridgeist to redesign this Next.js course landing page. Keep its functionality and blue brand color, replace the generic SaaS cards with a visible editorial grid, and verify desktop and mobile behavior.
