## Direction

**Thesis:** A human portfolio for creative collaborators, organized as a warm editorial journey in which asymmetric artwork, candid captions, and concrete project evidence reveal both the maker and the work.

Use an invisible alignment system rather than a visible technical grid. Preserve every artwork asset, caption, evidence item, and fictional-work disclosure verbatim unless editorial changes are separately approved. The redesign should feel composed but not systematized: generous image scale, varied pacing, tactile color, and occasional overlap or offset create character, while a stable reading order keeps it usable.

## Responsive implementation blueprint

- Open with one strong artwork at near-editorial scale, paired with a short introduction and one clear route into the work. Avoid a centered hero, technical labels, decorative code, and dashboard-like chrome.
- Turn the project index into a varied sequence rather than repeated cards. Alternate full-bleed artwork, offset image-and-text pairings, narrow caption-led interludes, and evidence-rich case-study entries. Variation should follow the material—not randomize the layout.
- Give each project a narrative: role and context, artwork, caption, process or constraint, and verifiable evidence. Keep evidence adjacent to the claim it supports. Do not invent clients, metrics, outcomes, testimonials, or research.
- Keep fictional work visually first-class, but attach a persistent, plain-language “Fictional / self-initiated project” disclosure beside the project title and repeat it wherever work may be encountered out of context. Do not hide it in a tooltip, footer, or low-contrast metadata.
- Use the existing palette as the source of semantic roles: warm page ground, readable text, quiet supporting text, link/focus color, and restrained separators. Use texture, borders, shadows, or radii only when they reinforce the portfolio’s existing material character.
- Establish distinct type roles for expressive display copy, project headings, readable body text, captions, and metadata. Keep narrative text around 45–75 characters per line. Reserve monospace for genuinely technical evidence, if any.
- Treat captions as content: associate them structurally with their images, preserve credit/context, and keep them readable at every crop. Meaningful artwork receives descriptive alt text; decorative imagery uses empty alt text. Never place essential text only inside an image.
- Motion should support reveal or spatial continuity, not create ambient spectacle. Disable nonessential transforms and parallax under `prefers-reduced-motion`; do not make scrolling, pointer precision, or animation the only way to access a project.
- Use semantic landmarks, real links and buttons, visible focus states, logical heading order, sufficient contrast, keyboard-operable navigation, and touch targets of comfortable size. Preserve a linear DOM order even when desktop composition is asymmetric.

On wide screens, use a flexible editorial scaffold with consistent outer gutters and a few quiet alignment lines; let selected artwork span or escape those lines deliberately. On tablets, reduce overlaps and protect caption-image relationships. On phones, recompose into a clear narrative order—title, disclosure, artwork, caption, evidence—using natural image ratios and no horizontal canvas. Asymmetry can survive through crop, indentation, scale, and pacing without sacrificing reading order.

## Verification

No repository fixture or rendered interface was available, so this response does not claim implementation or visual verification. After implementation, verify representative phone, tablet, laptop, and wide-desktop widths; keyboard traversal and visible focus; disclosure visibility; image crops and captions; text contrast and zoom; reduced motion; slow or failed image loading; long titles and captions; and that every preserved evidence item remains attached to the correct project. The decisive review question is: if the grid and interface chrome disappear, does the portfolio still unmistakably belong to this person?
