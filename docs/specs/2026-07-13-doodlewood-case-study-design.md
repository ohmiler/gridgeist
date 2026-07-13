# Doodlewood Case Study Design

## Purpose

Build Doodlewood as a standalone playful drawing web app for children ages 6–10 and use it as Gridgeist's fourth and final self-produced case study. The experiment tests whether the skill can reject its technical/editorial defaults, preserve a warm irregular brand, and still deliver safe, understandable touch interaction.

## Product

Doodlewood is a fictional “living sketchbook” where lines can become forest creatures. The visual thesis is “a drawing table beneath a tree”: warm, friendly, slightly irregular, and immediately usable without resembling an adult design tool.

The application is one page. A child can:

1. See the drawing surface and a short invitation immediately.
2. Select one of six labeled colors.
3. Select a small, medium, or large brush.
4. Draw with mouse, touch, or stylus.
5. Undo or redo a stroke.
6. Clear the drawing after confirmation.
7. Download the result as a PNG.

The canvas begins with a faint, removable creature prompt. The prompt belongs to the local drawing state and can be cleared or drawn over.

## Privacy and safety scope

- Do not create accounts, cloud storage, social sharing, chat, analytics, advertising, camera access, microphone access, or data uploads.
- Do not request a name, age, email address, school, location, or any other personal information.
- Keep drawing state in the browser. The image leaves the browser only through a user-initiated local PNG download.
- Require confirmation before clearing the drawing and restore focus to the clear trigger after cancel or confirmation.
- State explicitly that the experiment is not a COPPA certification, child-product safety certification, or substitute for usability testing with children and guardians.

## Visual direction

Use a warm green-cream paper ground with leaf green, sunlight yellow, fruit orange, flower pink, water blue, and berry violet. Use rounded, readable sans-serif typography without monospace. Create code-native SVG/CSS leaves, seeds, branches, and small forest marks rather than generated raster illustration.

Controls may be soft and slightly irregular, but every control needs a text label, clear selected state, and predictable hit area. Do not use a visible grid, dashboard cards, tables, technical chrome, or icon-only color controls.

## Responsive composition

- At 1024 px and above, center the drawing surface between color tools on the left and action tools on the right.
- From 768 px through 1023 px, place the canvas above a large bottom tool area.
- Below 768 px, let the canvas use the remaining width and recompose controls into two touch-friendly rows. Horizontal scrolling may exist inside a toolbar only.
- At 360 px, keep interactive targets at least 44 CSS pixels and prevent document-level horizontal overflow.
- Prevent page scrolling only while an active pointer draws on the canvas; do not block normal document scrolling globally.

## Interaction architecture

Use the Pointer Events API for mouse, touch, and stylus. Keep the stroke/history engine independent from React so coordinate conversion, history limits, undo, redo, and clear behavior can be unit tested.

Represent a stroke as an immutable record containing a color, logical width, and ordered points. Convert client coordinates to logical canvas coordinates using the canvas bounding rectangle. Render at device pixel ratio while keeping logical stroke values stable. Limit history to the 50 most recent completed strokes.

Undo moves one stroke from the completed stack to the redo stack. Starting a new stroke after undo clears the redo stack. Clear removes the prompt and all strokes only after confirmation. Download exports the current high-resolution canvas as PNG without a network request.

## Accessibility

- Give the canvas a programmatic name and concise instructions.
- Give every color, brush size, and action a visible text label.
- Expose selected color and size with semantic state plus shape/text, not color alone.
- Support visible keyboard focus and logical tab order for all controls.
- Implement a semantic confirmation dialog with Escape, cancel, confirm, initial focus, and focus return.
- Respect reduced motion for decorative leaves and feedback.
- Keep controls at least 44 CSS pixels on touch layouts and maintain readable contrast.

The drawing gesture itself is pointer-based; keyboard users can operate every tool and safety action but version one does not provide keyboard-authored strokes. Document this limitation.

## Technical approach

- Create a standalone public repository at `ohmiler/doodlewood`.
- Use Next.js, TypeScript, React, and the Canvas 2D API.
- Use static export for GitHub Pages.
- Keep all application state local and deterministic.
- Use code-native SVG/CSS decoration; do not add an illustration library or raster-generation dependency.
- Do not add a backend, authentication, storage service, analytics, WebGL, or collaboration in version one.

## Experiment record

Preserve:

1. `baseline/`: a generic drawing toolbar using the same features and initial prompt.
2. `experiment/prompt.md`: the exact Gridgeist invocation and run metadata.
3. `experiment/rubric.md`: baseline and final scores with evidence.
4. The main application: the final Gridgeist-guided implementation.
5. `README.md`: setup, verification, privacy, safety scope, method, and limitations.

Score baseline and final from 1–5 on six fixed dimensions, for a maximum total of 30:

1. Brand adaptation.
2. Child-centered usability.
3. Drawing interaction quality.
4. Responsive touch composition.
5. Accessibility and safety.
6. Implementation quality.

Do not establish a target final score before implementation.

## Verification

Unit tests cover stroke creation, coordinate scaling, undo, redo, redo invalidation, clear, and the 50-stroke history limit.

Playwright projects at 360, 768, 1024, and 1440 px cover:

- Pointer drawing.
- Color and brush-size selection.
- Undo and redo.
- Clear confirmation, Escape, and focus return.
- PNG download initiation.
- Keyboard focus and selected-state semantics.
- Reduced-motion behavior.
- Console errors and document-level horizontal overflow.

Automated Pointer Events and simulated viewports do not replace testing on physical touch devices or usability testing with children.

## Success criteria

- A first-time user can draw, change color/size, undo, clear safely, and download without instruction.
- The interface feels playful and age-appropriate without hiding control meaning.
- The final visual language materially differs from Tracefield, Ledgerline, and Morrow.
- Mouse, simulated touch/pointer, and representative responsive layouts work without document overflow.
- Another person can reconstruct the experiment from the baseline, exact prompt, rubric, tests, privacy statement, and source.

## Limitations

- Doodlewood is a fictional product and records one model run.
- No children, guardians, educators, or accessibility specialists participate in the evaluation.
- The experiment is not COPPA certification or a child-product safety assessment.
- Keyboard users cannot author strokes in version one, although all tools and safety actions remain keyboard operable.
- Automated browser tests do not prove behavior on every physical touch/stylus device.
- PNG download behavior may vary by browser and device policy.
