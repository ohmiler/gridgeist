# Gridgeist Design Language

Use this reference before selecting or explaining a visual direction. Build from the product and brand rather than collecting fashionable labels.

## Direction model

Choose one structural influence, one expressive influence, and one product-native motif.

- **Structural influence** defines order: rational grid, editorial sequence, task flow, spatial canvas, or another coherent logic.
- **Expressive influence** defines tone: precise, warm, restrained, playful, tactile, image-led, or another brand-supported quality.
- **Product-native motif** makes the result specific: traces, lesson progress, artwork, route status, drawing tools, documents, or another authentic artifact.

Write the thesis as: **audience + primary task + structural logic + brand expression + product-native motif**.

Examples:

- “An operational workspace for SREs built on aligned trace relationships, compressed hierarchy, and live latency states.”
- “A human portfolio for creative collaborators paced by asymmetric artwork, warm editorial type, and candid project evidence.”
- “A touch-first drawing studio for children organized around the canvas, friendly tool groups, and immediate local feedback.”

## Product-surface adaptation

| Surface | Let this lead | Structural treatment | Avoid |
|---|---|---|---|
| Data or technical product | Real data, state, relationships, commands, product UI | Explicit tracks, dense alignment, quiet rules, precise labels | Fake metrics, decorative code, interchangeable dashboard cards |
| Content or documentation | Reading order, navigation, examples, metadata | Controlled measure, editorial pacing, persistent orientation | Squeezed columns, repetitive content boxes, ornamental complexity |
| Image-led portfolio or brand | Artwork, crop, scale, caption, narrative | Invisible or quiet grid, purposeful asymmetry, varied pacing | Technical chrome, equal project cards, art used as thumbnails only |
| Playful or canvas-based tool | Primary canvas, direct manipulation, touch controls, feedback | Task-centered zones, friendly grouping, flexible geometry | Importing a technical grid, shrinking the main tool, tiny controls |
| Transactional form or workflow | Progress, input, validation, confirmation, recovery | Clear sequence, stable control placement, explicit state changes | Styling only the happy path, hidden errors, disruptive reflow |

This table guides decisions; it is not a set of templates. A product may combine surfaces, but one should dominate each viewport or workflow stage.

## Brand adaptation gate

Before importing any visual influence:

1. Inventory existing voice, typography, palette, imagery, geometry, motion, and recognizable assets.
2. Mark each signal as **preserve**, **evolve**, or **replace**, with a product reason for any replacement.
3. Decide whether structure should be **visible**, **quiet**, or **invisible**.
4. Test recognizability: if borders, mono type, and technical labels disappear, does the direction still belong to this product?
5. Reject the direction if it gains Gridgeist mannerisms while losing the established brand.

When no brand exists, derive expression from audience, task, content, and product character rather than defaulting to technical minimalism.

## System heuristics

### Grid and composition

- Use consistent outer relationships and gutters across the interface.
- Align major edges when alignment improves reading or task flow.
- Break regularity only to create deliberate emphasis, narrative pace, or direct manipulation space.
- On small screens, replace wide structures with a simpler priority order; do not preserve decorative empty tracks.

### Typography

- Define roles for display, heading, body, label, metadata, and code only when needed.
- Keep body measure readable, commonly around 45–75 characters.
- Use weight, spacing, family, and contrast before inventing many sizes.
- Use mono for commands, code, IDs, timestamps, or technical labels—not as automatic Gridgeist branding.

### Imagery and product material

- Give authentic material enough scale and context to carry hierarchy.
- Define crop, aspect ratio, caption, loading, empty, and small-screen behavior.
- Preserve meaningful artwork and brand assets; mark decorative imagery appropriately.
- Label sample or fictional content and avoid implying real customers, outcomes, or research.

### Borders, shape, and surfaces

- Use borders to explain containment, adjacency, sequence, or interaction.
- Derive radius, shadow, texture, and surface contrast from brand and function.
- Avoid combining heavy borders, strong shadows, gradients, and large radii without a product reason.

### Color and motion

- Start with brand and semantic roles rather than a preset palette.
- Check default, hover, focus, disabled, selected, success, warning, and error states.
- Animate feedback, causality, or spatial relationship; avoid ambient motion competing with the primary task.
- Support `prefers-reduced-motion` without hiding essential state changes.

## Reference use

When a user supplies a reference site:

1. Identify reusable principles: hierarchy, density, grid visibility, type, imagery, color, motion, and content strategy.
2. Separate principles from protected brand assets and distinctive compositions.
3. Translate the principles into the user's content, behavior, stack, and identity.
4. State what was inspired by the reference without claiming an exact replica.
