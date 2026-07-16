## Direction

**Thesis:** A human portfolio for creative collaborators, paced as a warm editorial journey on an invisible alignment system, with asymmetric artwork, candid captions, and concrete project evidence carrying the experience.

Preserve the artwork at meaningful scale, its captions and context, every existing piece of project evidence, and the fictional-work disclosure. Keep that disclosure adjacent to the relevant work and written plainly; do not bury it in a footer or soften it into ambiguous metadata. Do not invent clients, metrics, outcomes, or testimonials.

The redesign should feel composed rather than gridded. Use a quiet underlying structure for readable margins and recurring alignments, then vary image scale, crop, and placement to create rhythm. Let one strong artwork lead the opening instead of centered hero copy. Follow with a short personal introduction and a selective project index that acts as navigation, not a set of repeated cards.

Each project should become its own narrative sequence: a dominant image, title and role, concise context, preserved evidence, captioned supporting artwork, and an explicit outcome or fictional-work label where applicable. Alternate image/text relationships and pacing between projects while retaining shared type, spacing, and caption rules. This keeps the work distinct without turning the page into an inaccessible freeform canvas.

Use warm editorial typography: an expressive display face for a few high-emphasis moments and a highly readable text face for narratives and captions. Retain the established palette and material character; derive any paper texture, soft shadow, or irregular edge from the existing artwork rather than adding generic decoration. Avoid monospaced labels, heavy technical borders, dashboard chrome, uniform tiles, and ornamental grid lines.

## Responsive implementation specification

- On wide screens, use purposeful asymmetry with a stable reading column and generous image fields; allow selected artwork to cross an alignment line only when it improves emphasis.
- On tablets, reduce overlap and crop complexity while preserving the relationship between each artwork, caption, and project narrative.
- On phones, recompose every project into a clear semantic order: title and disclosure, lead artwork, caption, context, evidence, supporting media, then next-project link. Do not merely shrink the desktop arrangement.
- Implement artwork as semantic `figure`/`figcaption` pairs. Provide useful alternative text for meaningful images and empty alt text for purely decorative imagery.
- Keep navigation, links, and any media controls keyboard-operable with visible focus, adequate target sizes, and sufficient contrast. Never encode project status or fictional status by color alone.
- Limit motion to causal transitions such as revealing project context or advancing a gallery. Respect `prefers-reduced-motion`, preserve content without animation, and avoid parallax that competes with reading.
- Use normal document flow as the accessibility backbone. Asymmetry may be visual, but reading order, zoom behavior, and screen-reader order must remain coherent.

## Verification

This is a read-only design direction, not an implemented redesign. No repository fixture, rendered viewport, interaction flow, focus state, responsive breakpoint, or assistive-technology behavior was available to inspect, so none is claimed as verified. After implementation, verify representative desktop, tablet, and phone widths; artwork/caption association; preservation of every evidence item; prominence of fictional-work disclosures; keyboard order and focus visibility; text zoom and reflow; image loading/failure behavior; contrast; and reduced-motion behavior.
