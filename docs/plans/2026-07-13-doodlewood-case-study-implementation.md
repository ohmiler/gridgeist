# Doodlewood Case Study Implementation Plan

> Execute this plan inline in a normal Codex session. Do not use Superpowers or subagents. Track each checkbox and verify every checkpoint before committing.

**Goal:** Build and publish Doodlewood, a privacy-preserving playful drawing app that tests whether Gridgeist can reject technical/editorial defaults while retaining safe, accessible interaction.

**Architecture:** Create `ohmiler/doodlewood` as a standalone Next.js static-export repository. Keep a pure immutable stroke/history engine separate from a React Canvas 2D surface, then compare a generic static baseline against the final Gridgeist-guided app. Store the exact prompt, fixed rubric, privacy/safety scope, and four-viewport verification with the code.

**Tech Stack:** Next.js, TypeScript, React, Canvas 2D API, Pointer Events, Vitest, Playwright, code-native SVG/CSS, GitHub Actions, GitHub Pages.

**Fixed rubric:** Score Brand adaptation, Child-centered usability, Drawing interaction quality, Responsive touch composition, Accessibility and safety, and Implementation quality from 1–5 each, for a total of 30.

---

## File map

```text
doodlewood/
├── .github/workflows/pages.yml       Verify, build, deploy static export
├── baseline/
│   ├── index.html                    Generic drawing-app comparison
│   ├── styles.css                    Baseline-only UI styling
│   └── drawing.js                    Same basic drawing features
├── experiment/
│   ├── prompt.md                     Exact Gridgeist invocation and metadata
│   └── rubric.md                     Baseline/final evidence and scores
├── src/app/
│   ├── globals.css                   Playful tokens, layout, responsive tools
│   ├── layout.tsx                    Metadata and privacy-safe document shell
│   └── page.tsx                      Doodlewood composition
├── src/components/
│   ├── ClearDialog.tsx               Confirm/cancel/Escape/focus return
│   ├── ColorSeeds.tsx                Six labeled semantic color controls
│   ├── DoodleCanvas.tsx              Pointer capture, DPR drawing, PNG export
│   ├── ForestDecor.tsx               Accessible-hidden code-native decoration
│   ├── SizeTwigs.tsx                 Three labeled brush-size controls
│   └── ToolActions.tsx               Undo, redo, clear, download actions
├── src/drawing/
│   ├── engine.ts                     Immutable strokes/history operations
│   ├── geometry.ts                   Client-to-logical coordinate scaling
│   └── render.ts                     Canvas render and initial creature prompt
├── src/types/
│   └── drawing.ts                    Point, Stroke, History, Brush types
├── tests/
│   ├── engine.test.ts                History and stroke behavior
│   ├── geometry.test.ts              Coordinate/DPR-independent scaling
│   └── doodlewood.spec.ts            Four-viewport browser checks
├── next.config.ts                    Static export and Pages base path
├── playwright.config.ts              360/768/1024/1440 projects
├── vitest.config.ts                  Unit-test boundary
├── README.md                         Method, privacy, safety, verification, limits
└── LICENSE                           MIT license
```

## Task 1: Create and configure the repository

- [ ] Verify `gh repo view ohmiler/doodlewood` returns repository-not-found. Stop rather than overwrite if it exists.
- [ ] Scaffold `C:\Users\Miler\Downloads\doodlewood` using Next.js TypeScript App Router and create public repository `ohmiler/doodlewood`.
- [ ] Install `vitest`, `jsdom`, `@testing-library/react`, `@testing-library/jest-dom`, `@playwright/test`, and `serve` as development dependencies.
- [ ] Add `test`, `test:e2e`, and `verify` scripts. `verify` runs lint, unit tests, build, then Playwright.
- [ ] Configure static export, unoptimized images, local Turbopack root, and `/doodlewood` base/asset paths only when `GITHUB_ACTIONS === "true"`.
- [ ] Run lint/build, rename branch to `main`, and commit `chore: scaffold Doodlewood app`.

## Task 2: Build and preserve the generic baseline

- [ ] Create a conventional white drawing app with rectangular top toolbar, `<input type="color">`, brush-size range input, undo, redo, clear, download, and centered canvas.
- [ ] Use Pointer Events, local history, a faint removable creature prompt, and PNG export so baseline and final compare the same functional requirements.
- [ ] Keep labels, semantic buttons, readable contrast, and clear confirmation; do not intentionally manufacture accessibility failures.
- [ ] Inspect baseline at 360 and 1024 px. Score the six baseline rubric dimensions with concrete evidence and leave final scores unset.
- [ ] Commit `test: preserve Doodlewood baseline`.

## Task 3: Record the exact Gridgeist experiment prompt

- [ ] Before final UI work, save this prompt verbatim to `experiment/prompt.md`:

```text
Use $gridgeist to redesign this working children’s drawing app.
Preserve drawing with mouse, touch, and stylus; six colors; three brush sizes; undo; redo; confirmed clear; PNG download; the removable creature prompt; and the privacy/safety disclosure.
The brand is a warm, playful, slightly irregular “drawing table beneath a tree” for children ages 6–10. Preserve soft shapes, clear language, and code-native forest decoration; do not apply a Swiss, editorial, dashboard, or visible-grid preset.
Keep every control labeled, selected states independent of color, touch targets at least 44 CSS pixels, and normal page scrolling available whenever the pointer is not actively drawing.
Create deliberate compositions for 360 px, 768 px, 1024 px, and 1440 px; do not merely stack a desktop toolbar.
Implement Escape and focus return for clear confirmation, visible keyboard focus, reduced motion, no document-level horizontal overflow, and no network request for drawing or download.
Do not add accounts, analytics, cloud save, social sharing, chat, ads, camera, microphone, personal-data fields, gamified pressure, or fabricated child-safety certification.
```

- [ ] Record date, agent/model, Gridgeist release/commit, baseline commit, and that no other visual-design skill was used.
- [ ] Invoke only `gridgeist/SKILL.md` for final interface direction and save its one-sentence thesis.
- [ ] Commit `docs: record Doodlewood Gridgeist prompt`.

## Task 4: Define stroke types and geometry with TDD

- [ ] Create failing tests for `toLogicalPoint(clientX, clientY, rect, logicalWidth, logicalHeight)` covering origin, center, and non-uniform CSS scaling.
- [ ] Create failing tests for a stroke factory that stores color, logical width, and ordered immutable points.
- [ ] Run unit tests and confirm imports fail before implementation.
- [ ] Define `Point`, `Stroke`, `Brush`, and `History` types. Implement coordinate scaling without device-pixel-ratio in logical values.
- [ ] Run tests and commit `feat: add Doodlewood drawing geometry`.

## Task 5: Implement immutable history engine with TDD

- [ ] Write failing tests for append point, complete stroke, undo, redo, redo invalidation after a new stroke, clear, and retaining only the latest 50 completed strokes.
- [ ] Implement pure functions `startStroke`, `appendPoint`, `completeStroke`, `undo`, `redo`, and `clearHistory`; never mutate input arrays or strokes.
- [ ] Ignore empty strokes and duplicate consecutive points.
- [ ] Run focused tests, then the full unit suite and lint.
- [ ] Commit `feat: add bounded drawing history`.

## Task 6: Implement Canvas rendering and pointer interaction

- [ ] Implement a render function that scales backing-store dimensions by device pixel ratio, draws the warm paper background, optional faint creature prompt, and completed/active strokes in logical coordinates.
- [ ] Implement `DoodleCanvas` with Pointer Events, pointer capture, pressure-safe fixed logical brush widths, and `touch-action: none` only on the canvas.
- [ ] Prevent default scrolling only during an active canvas pointer gesture.
- [ ] Expose canvas name/instructions, drawing status text, and local PNG download. Download must use `canvas.toBlob`/object URL without fetch or network APIs.
- [ ] Re-render after resize using `ResizeObserver` without clearing logical history.
- [ ] Run tests, lint, and build; commit `feat: add local Doodlewood canvas`.

## Task 7: Build safe labeled controls

- [ ] Implement six visible color seed buttons with label, swatch, `aria-pressed`, and a non-color selected mark.
- [ ] Implement three brush-size twig buttons with label and visible line sample.
- [ ] Implement undo/redo disabled states, clear trigger, and download action with text labels and at least 44 px hit areas.
- [ ] Implement a semantic clear dialog: initial focus on cancel, Escape cancel, confirm clear, no background action while open, and focus return to the trigger.
- [ ] Add an always-visible privacy note stating drawings stay in the browser and downloads are local.
- [ ] Run tests, lint, and build; commit `feat: add safe Doodlewood tools`.

## Task 8: Apply playful responsive composition

- [ ] Create code-native SVG/CSS leaves, branches, seeds, and forest marks with `aria-hidden="true"` and no raster illustration dependency.
- [ ] At 1024/1440 px, center canvas between left color seeds and right action tools without dashboard cards or a visible grid.
- [ ] At 768 px, place canvas above a large bottom tool area while preserving labels and selection state.
- [ ] At 360 px, use two tool rows with overflow confined to toolbars, 44 px controls, and no document-level overflow.
- [ ] Use rounded readable sans typography, warm paper/forest colors, irregular shapes, visible focus, and reduced-motion-safe decorative movement.
- [ ] Run unit tests, lint, and build; commit `style: grow the Doodlewood visual system`.

## Task 9: Add browser verification

- [ ] Configure Playwright projects `mobile-360`, `tablet-768`, `compact-1024`, and `desktop-1440` on an isolated port.
- [ ] Draw with synthetic pointer events and verify canvas pixels or drawing-status/stroke count change.
- [ ] Test six colors and three sizes expose semantic selected state; test undo/redo changes stroke count.
- [ ] Test clear dialog cancel, Escape, confirm, and focus return.
- [ ] Test download event produces a `.png` filename without page network requests.
- [ ] Emulate reduced motion and verify essential controls/canvas remain usable.
- [ ] Assert zero console errors and document/body `scrollWidth <= innerWidth` at every viewport.
- [ ] Capture full-page screenshots as ignored artifacts and run `npm run verify`.
- [ ] Commit `test: verify Doodlewood drawing flows`.

## Task 10: Score, document, and deploy

- [ ] Complete final rubric from rendered/test evidence without changing baseline scores or setting a target retroactively.
- [ ] Write README with live URL, experiment method, privacy/safety scope, repository map, verification, limitations, exact prompt/rubric/Gridgeist links, and the explicit statement “This experiment is not a COPPA certification or child-product safety assessment.”
- [ ] Add MIT license and ignore test artifacts.
- [ ] Add least-privilege Pages workflow using current official action majors. Run `npm ci`, lint, unit tests, and build before deployment.
- [ ] Push main, enable Pages with `build_type=workflow`, set homepage, and watch deployment to completion.
- [ ] Verify production HTML/assets return 200, the canvas hydrates, drawing/download remain local, and disclosure is visible.
- [ ] Tag the verified production commit as annotated `v0.1.0` and push the tag.

## Task 11: Link the final case-study coverage from Gridgeist

- [ ] In Gridgeist, add Doodlewood to `README.md` and `README.th.md` only after evidence is public.
- [ ] Add English/Thai evaluation scenarios for playful brand preservation, child-centered controls, pointer interaction, privacy, and rejection of technical presets. Link evidence without requiring Doodlewood’s style or score.
- [ ] Add a concise case-study coverage summary explaining that the four self-produced surfaces now cover data-heavy, content-heavy, image-led, and playful interaction work.
- [ ] Verify public links, skill frontmatter, UTF-8 Thai text, scenario counts, and clean diff.
- [ ] Commit `docs: complete Gridgeist case-study coverage` and push main.

## Final acceptance checklist

- [ ] Public baseline, exact prompt, rubric, privacy/safety statement, code, and tests are reachable.
- [ ] Mouse, simulated touch/pointer, tools, history, clear confirmation, and PNG download work.
- [ ] No account, network storage, analytics, personal-data input, or upload exists.
- [ ] `npm run verify` passes from the final commit at 360, 768, 1024, and 1440 px.
- [ ] Production and tag point to the same clean commit.
- [ ] Gridgeist documents four complementary case-study surfaces and transitions next work to external feedback.
