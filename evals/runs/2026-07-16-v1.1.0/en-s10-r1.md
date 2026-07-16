## Direction

**Thesis:** A human portfolio for creative collaborators, paced as an asymmetric editorial sequence in which warm typography, generous artwork, candid captions, and concrete project evidence reveal both the work and the person behind it.

Keep the alignment system quiet. The portfolio should feel composed, not gridded: artwork leads; text supports it; asymmetry creates rhythm without obscuring reading order. Preserve every artwork, caption, proof point, and fictional-work disclosure. Do not convert projects into equal cards or decorate the site with technical labels, mono type, heavy rules, or dashboard chrome.

## Responsive composition

- Open with one unmistakable artwork-led statement: a concise introduction on one side and a large, naturally cropped or uncropped image on the other. Let the artwork cross an internal alignment line while the text remains comfortably readable.
- Treat each project as a narrative `article`, not a reusable card. Alternate a few purposeful compositions: a panoramic artwork followed by context; a tall image beside the story; or a small sequence of process details around one dominant final piece. Variation should follow the material, while project title, role, date, evidence, and disclosure retain a consistent reading hierarchy.
- Keep captions physically and semantically attached to their images with `figure` and `figcaption`. Captions may be quiet, but never hidden on hover or removed on small screens.
- Place project evidence close to the claim it supports: role, constraints, process artifacts, deliverables, and observed outcomes where genuinely known. Avoid fabricated metrics or generalized testimonial language.
- Make fictional-work disclosure persistent, plain-language text beside the project title or introduction—such as “Self-initiated fictional project”—and repeat it where an isolated project image could otherwise be mistaken for client work.
- End with a personal, low-friction contact passage rather than a generic CTA panel. A portrait, studio fragment, sketch, or handwritten detail may carry the human note if it is an authentic existing asset.

Use an invisible 12-track desktop structure and a simpler tablet structure only as alignment logic. On mobile, recompose every project into a deliberate sequence: title and context, artwork, caption, evidence, then disclosure where needed. Do not preserve decorative empty columns, overlap essential text, or require horizontal panning. Full-bleed art can remain expressive while captions and body copy return to a safe inset.

## Visual system

- Retain the established palette and type assets. Give display text an expressive, warm role and use a highly readable companion for body copy; reserve monospace only for real code or technical metadata that already belongs to a project.
- Let original image proportions guide the layout. Define crop behavior per artwork, protect focal points, and offer an uncropped view when cropping would remove evidence or meaning.
- Build hierarchy with scale, position, whitespace, and changes in image density. Use borders only when they clarify a sequence or separate caption from narrative—not as a site-wide aesthetic.
- Keep surfaces tactile but restrained. Any paper texture, shadow, grain, or color wash should support the existing brand and must not reduce text contrast or compete with the art.
- Use motion only to clarify entry, sequencing, or image transitions. Preserve all content and state with `prefers-reduced-motion`; no ambient parallax or cursor-dependent canvas should be required to understand or navigate the work.

## Accessibility guardrails

Use semantic landmarks, a visible skip link, logical heading levels, keyboard-operable navigation, strong focus indicators, descriptive alt text, and empty alt text for purely decorative imagery. Maintain readable line lengths, sufficient color contrast, touch targets of at least 44×44 CSS pixels, and a DOM order that matches the mobile reading order. Any gallery needs explicit previous/next controls, status text, and a non-carousel fallback; the portfolio must remain fully usable without drag gestures, hover, animation, or JavaScript-enhanced effects.

## Implementation and verification status

This is a read-only redesign specification. No target fixture was supplied, so no repository files were changed, no implementation was performed, and no rendered desktop or mobile verification is claimed. Before release, the implemented design should be checked at representative narrow, tablet, desktop, and wide viewports for reading order, image crops, caption association, disclosure visibility, keyboard navigation, focus, contrast, reduced motion, overflow, and gallery fallback behavior.
