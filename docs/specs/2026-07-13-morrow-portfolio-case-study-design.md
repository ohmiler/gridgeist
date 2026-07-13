# Morrow Portfolio Case Study Design

## Purpose

Build Morrow as a standalone fictional creative-developer portfolio and use it as Gridgeist's third public case study. The experiment tests whether the skill can preserve a human, image-led, asymmetric brand instead of turning every interface into the technical visual language used by Tracefield or Ledgerline.

## Product

Morrow presents a fictional creative developer working across code, space, and moving image. The visual thesis is “a field notebook after dark”: an authored record with fragments, process traces, and reflection rather than a polished agency template.

All people, projects, outcomes, and artwork are fictional. The site must state this clearly and must not imply client relationships, exhibitions, or real-world results.

## Information architecture

- Home: a concise statement and three featured projects.
- Work: project index with year, medium, and role.
- Case studies: Tidal Memory, Soft Circuit, and Afterlight.
- Process: sketches, fragments, technical notes, and failed experiments.
- About: working perspective and capabilities without skill clouds or proficiency meters.
- Contact: email and availability.

Each case study includes premise, role, constraints, process, outcome, and reflection:

- Tidal Memory: a generative data sculpture.
- Soft Circuit: an interactive spatial installation.
- Afterlight: an experimental web archive.

## Visual direction

Use a warm charcoal ground, bone text, faded violet, and red-orange sampled from the artwork. Pair an expressive serif voice with a neutral sans-serif information layer. Let generative artwork lead the hierarchy while captions and prose provide context.

Compose with offset blocks, overlap, asymmetric whitespace, and an underlying grid. Use borders and monospace sparingly so the result does not inherit Ledgerline's documentation language. Do not use custom cursors, scroll hijacking, generic card grids, skill clouds, or decorative technical chrome.

## Responsive behavior

- At 1440 px and above, alternate large artwork fields with offset narrative and a lateral project index.
- From 1024 px through 1439 px, reduce overlap while preserving editorial image order.
- From 768 px through 1023 px, use a deliberate two-column rhythm with artwork and narrative alternating sides.
- Below 768 px, recompose each project as artwork, premise, metadata, and reflection in that reading order instead of shrinking the desktop collage.
- At 360 px, prevent document-level overflow and ensure navigation never obscures the work.

## Interaction and accessibility

- Navigate to stable project and section anchors.
- Open and close the mobile menu with Escape and focus return.
- Expose meaningful captions and alternative text for every artwork.
- Use short reveal transitions that respect reduced motion.
- Provide semantic landmarks, logical heading order, visible keyboard focus, readable contrast, and touch targets of at least 44 CSS pixels.

## Artwork strategy

Create a new set of abstract/generative raster artworks specifically for Morrow. Store final assets in `public/artworks/` and record their image-generation prompt plus a usage note. Use the same source artwork in baseline and final so composition, not asset quality, is the variable under comparison.

The assets must not imitate a living artist, use copyrighted characters, or present themselves as documentary photographs of real installations. Label them as fictional study artifacts.

## Technical approach

- Create a standalone public repository at `ohmiler/morrow-portfolio`.
- Use Next.js and TypeScript with static export for GitHub Pages.
- Keep portfolio content and interface state deterministic and local.
- Do not add a CMS, backend, blog, authentication, WebGL, custom cursor, or scroll hijacking in version one.
- Use automated checks plus Playwright at 360, 768, 1024, and 1440 px.

## Experiment record

Preserve the following artifacts in the Morrow repository:

1. `baseline/`: a generic portfolio-template implementation using the same content and artwork.
2. `experiment/prompt.md`: the exact Gridgeist prompt and run metadata.
3. `experiment/rubric.md`: baseline and final scores with concrete evidence.
4. `experiment/artwork-prompt.md`: image-generation prompt and fictional-use disclosure.
5. `public/artworks/`: the shared source artwork.
6. The main application: the final Gridgeist-guided interface.
7. `README.md`: setup, verification, deployment, method, and limitations.

Score baseline and final implementations from 1–5 on six fixed dimensions, for a maximum total of 30:

1. Brand fidelity.
2. Visual authorship.
3. Image-led hierarchy.
4. Case-study clarity.
5. Responsive composition.
6. Accessibility and implementation.

Do not establish a target final score before implementation.

## Verification

- Lint, unit tests, and production build pass.
- Static export works under the GitHub Pages base path.
- Browser tests verify section anchors, project navigation, mobile menu, Escape/focus return, keyboard focus, artwork dimensions, console errors, and horizontal overflow.
- Reduced-motion CSS is present and disables nonessential reveal transitions.
- The deployed site and public source repository are reachable before Gridgeist links the case study.

## Success criteria

- A visitor can identify Morrow's practice and distinguish the three projects without instruction.
- Artwork leads the experience while project premise, role, constraints, process, outcome, and reflection remain findable.
- The final interface has a recognizably different visual language from Tracefield and Ledgerline.
- Mobile composition preserves narrative order without flattening every section into interchangeable cards.
- Another person can reconstruct the experiment from the baseline, exact prompt, rubric, artwork prompt, and verification evidence.

## Limitations

- Morrow, its practitioner, projects, outcomes, and artwork are fictional.
- The raster artwork is AI-generated specifically for the experiment.
- The case study records one model run rather than repeated controlled trials.
- It does not include external usability testing.
- Results remain model-, prompt-, asset-, and repository-context dependent.
