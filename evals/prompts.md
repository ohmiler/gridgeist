# Gridgeist Behavioral Evaluations

Run these prompts in fresh agent sessions with the skill installed. Evaluate behavior and evidence, not exact wording. Model output is not deterministic.

## Evaluation protocol

1. Record the agent, model, language, exact installed skill commit or release, fixture commit, and any other active skills.
2. Use no other visual-design skill in the same run. Keep each run independent and do not expose prior findings or intended fixes.
3. Run each scenario three times per language and model before treating a pattern as stable.
4. Supply a runnable fixture when a scenario requests implementation or inspection. If no fixture is available, mark the implementation result **Not run** rather than passing a plan.
5. Separate behavioral reasoning from implementation verification. An implementation passes only when the agent renders representative widths, exercises relevant flows and states, runs project checks, and reports evidence.
6. Preserve the raw response or artifact link and record one row per scenario and run. Judge claims against observed evidence, not confidence of wording.

## Shared success criteria

- Selects the correct Create, Redesign, or Review mode.
- Establishes a product-specific visual thesis rather than applying a preset.
- Adapts structure, grid visibility, type, imagery, shape, motion, and product evidence to the brand.
- Preserves behavior and brand constraints when redesigning.
- Inventories important interaction states and recovery paths.
- Treats responsiveness, accessibility, and verification as part of the result.
- Avoids generic SaaS decoration without banning components categorically.
- Labels sample or fictional evidence and does not fabricate outcomes, research, safety, or compliance.

## Scenario 1: Create

> Use $gridgeist to create a landing page for a browser-based SQL learning environment. Make the lessons, schema, query editor, and results feel like the product rather than decorating the page with generic feature cards.

Pass when the agent states a visual thesis, makes authentic product UI dominant, and produces a complete responsive implementation in the supplied fixture. A plan alone does not pass an implementation run.

## Scenario 2: Redesign

> Redesign this working Next.js course page with $gridgeist. Preserve routes, interactions, content, and the blue brand color. Replace its repetitive rounded cards with an editorial information hierarchy.

Pass when the agent inventories existing behavior, preserves constraints, and changes composition as a system rather than merely removing border radii.

## Scenario 3: Review

> Review this dashboard with $gridgeist but do not edit it. Give a one-line verdict, prioritized findings with evidence, and one coherent replacement direction.

Pass when the response stays review-only, prioritizes systemic causes, and ties subjective judgments to usability, consistency, brand, or accessibility.

## Scenario 4: Responsive behavior

> Use $gridgeist to improve this dense desktop documentation layout for 360 px, 768 px, 1280 px, and 1600 px viewports. Do not simply stack every column.

Pass when the agent recomposes navigation, reading order, density, code, and controls intentionally at each width.

## Scenario 5: Accessibility

> The interface looks polished but has weak focus states, color-only status, animated background grids, and a modal with broken focus return. Review and fix it with $gridgeist.

Pass when the agent addresses keyboard order, visible focus, semantics, contrast, reduced motion, modal escape behavior, and focus return while retaining the visual system.

## Scenario 6: Conflicting direction

> Use $gridgeist for a playful children's drawing app whose established brand uses soft shapes, warm illustration, and irregular composition. Keep the brand.

Pass when the agent adapts or rejects Swiss/technical defaults, preserves the brand, and uses only relevant structural principles.

## Scenario 7: Product-specific evidence

> Create a developer observability homepage with $gridgeist. Avoid fake code, fabricated metrics, and interchangeable claims.

Pass when the agent asks for or uses authentic traces, logs, commands, states, screenshots, or clearly labeled sample data as the visual material.

## Scenario 8: Negative non-web trigger

> Diagnose why this Node.js API returns HTTP 500 when refreshing an OAuth token.

Pass when Gridgeist is not invoked solely because the project happens to use a web technology.

## Scenario 9: Dense documentation evidence

> Use $gridgeist to redesign payment API documentation with a quickstart, endpoint parameters, cURL and JavaScript examples, errors, and mobile navigation. Preserve the content and anchors, and verify 360 px, 768 px, 1280 px, and 1600 px without merely stacking the desktop layout.

Pass when the agent gives navigation, reading order, code, parameters, and states a product-specific system; preserves semantics and evidence; and verifies interaction, focus, and overflow. Compare the reasoning process with the public [Ledgerline case study](https://github.com/ohmiler/ledgerline), but do not require its visual style or score.

## Scenario 10: Image-led brand adaptation

> Use $gridgeist to redesign a creative developer portfolio whose brand is warm, image-led, asymmetric, and human. Preserve its artwork, captions, project evidence, and fictional-work disclosure. Do not turn it into a Swiss technical interface, repeated project cards, or an inaccessible experimental canvas.

Pass when the agent derives structure from the existing brand; gives projects distinct but coherent compositions; preserves premise, role, constraints, process, outcome, and reflection; and verifies image behavior, keyboard access, reduced motion, and mobile narrative order. Compare the reasoning process with the public [Morrow case study](https://github.com/ohmiler/morrow-portfolio), but do not require its palette, layout, or score.

## Scenario 11: Playful, privacy-preserving interaction

> Use $gridgeist to redesign a fictional drawing app for children aged 6–10. Make color, brush size, drawing, undo/redo, clearing, and local export concrete and touch-friendly. Preserve privacy: no account, upload, camera, analytics, or personal-data collection. Do not claim COPPA compliance or evidence from children unless that evidence exists.

Pass when the agent adapts the product brand without importing a generic technical grid; keeps the canvas primary across mobile, tablet, and desktop; handles pointer coordinates, history bounds, destructive confirmation, focus restoration, and local download; and explicitly separates automated checks from child usability or safety validation. Compare the reasoning process with the public [Doodlewood case study](https://github.com/ohmiler/doodlewood), but do not require its forest theme, layout, or score.

## Scenario 12: Negative frontend implementation trigger

> Fix the existing Save button click handler so it submits once and preserves the current UI. Do not redesign the page.

Pass when Gridgeist is not invoked implicitly solely because the task changes frontend code.

## Scenario 13: State-complete workflow

> Use $gridgeist to redesign an account-data import flow. Preserve CSV upload, validation, cancellation, retry, and partial-success behavior. Cover loading, empty, invalid-file, row-error, disabled, success, and interrupted states, then report what you actually verified.

Pass when the agent inventories the state model before styling, preserves valid input and recovery, gives each state a coherent hierarchy, verifies relevant keyboard and responsive behavior in a fixture, and separates observed checks from untested assumptions.

## Scenario 14: Underspecified broad redesign

Fixture: [`fixtures/direction-alignment/`](fixtures/direction-alignment/)

> Use $gridgeist to redesign the Commonroom workshop directory. Make it distinctive and easier to use while preserving its content and behavior. Inspect the fixture before taking action.

Pass when the agent inspects the product facts and rendered baseline, recognizes that several materially different visual theses remain credible, offers two or three evidence-grounded directions with trade-offs and a recommendation, and does not edit the fixture before the user aligns on a direction. Fail when it chooses and implements an unsupported visual thesis, asks generic preference questions without inspecting, or shifts design work back to the user without a recommendation.

## Scenario 15: Explicit-direction control

Fixture: [`fixtures/direction-alignment/`](fixtures/direction-alignment/)

> Use $gridgeist to redesign the Commonroom workshop directory as a warm editorial neighborhood guide. Let workshop descriptions and hosts lead, keep dates, availability, and access details easy to scan, use a quiet or invisible grid, and avoid technical-dashboard styling. Preserve all content and behavior, inspect the fixture, implement the redesign responsively, and report what you verify.

Pass when the agent identifies the direction as user-confirmed, states an evidence-backed thesis, and proceeds without redundant aesthetic questions. An implementation pass additionally requires preserved filtering, dialog, reservation, focus return, responsive behavior, and explicit verification evidence from a disposable fixture copy.

## Scenario 16: Internationalization and user preferences

> Use $gridgeist to redesign a bilingual public-service appointment flow for English and Arabic. Long translations break navigation, dates and numbers are hard-coded, the RTL layout uses physical left/right positioning, and selected states disappear in forced-colors mode. Preserve the workflow and verify both language directions without claiming compliance.

Pass when the agent preserves the task while addressing document and in-content language and direction, logical order and properties, locale-aware formatting, translation expansion, keyboard focus, and non-color state cues in forced colors. It must separate observed checks from untested usability or compliance claims.

## Scenario 17: Interaction and performance integrity

> Use $gridgeist to refine this media-rich project board. Cards can only be dragged, compact controls are difficult to target, a sticky toolbar obscures keyboard focus, hero images shift the layout as they load, and filtering feels slow. Preserve URL state and the existing brand, verify representative widths, and report only performance evidence actually measured.

Pass when the agent preserves the product system while providing a non-drag path, usable target sizing or spacing, unobscured focus, stable URL state, reserved media geometry, and measured interaction and layout-stability evidence. It must not present a local or lab check as field Core Web Vitals data.

## Scenario 18: Companion-skill ownership

> Use $gridgeist and a broad frontend-design skill to redesign this working product interface. Preserve its brand and behavior, and begin editing immediately.

Pass when the agent recognizes that both skills claim overlapping art-direction decisions, recommends one direction owner before editing (Gridgeist by default for product-native, brand-adaptive work), and does not silently blend house defaults. It may use non-conflicting context, asset, audit, or verification capabilities after ownership is clear. Fail when it runs two visual theses in parallel, invents a hard dependency, or refuses useful non-design companions categorically.

## Historical aggregate log

| Date | Agent/model | Skill commit | Scenarios passed | Notes |
|---|---|---|---:|---|
| 2026-07-16 | 15 fresh Codex subagents / current model | 316e0b1 / plugin 1.1.0 | 5 / 5 behavioral | Three independent English runs each for scenarios 5, 10, 11, 12, and 13. Implementation: 0 / 5 run because no executable fixtures were supplied. |
| 2026-07-15 | Codex CLI 0.144.4 / default model | fcc620e / plugin 1.0.1 | 9 / 11 | Read-only behavioral run; fixtures for scenarios 2–5; scenarios 10 and 11 failed; rendered implementation was not verified. |

## Scenario-level run log

Use **Pass**, **Fail**, or **Not run**. Add one row per independent run and link the raw response, fixture, screenshots, or artifact when available.

| Date | Language | Agent/model | Skill commit | Fixture commit | Run | Scenario | Result | Evidence or failure note |
|---|---|---|---|---|---:|---:|---|---|
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 1 | 5 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s05-r1.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 2 | 5 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s05-r2.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 3 | 5 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s05-r3.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 1 | 10 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s10-r1.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 2 | 10 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s10-r2.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 3 | 10 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s10-r3.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 1 | 11 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s11-r1.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 2 | 11 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s11-r2.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 3 | 11 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s11-r3.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 1 | 12 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s12-r1.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 2 | 12 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s12-r2.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 3 | 12 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s12-r3.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 1 | 13 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s13-r1.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 2 | 13 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s13-r2.md) |
| 2026-07-16 | English | Fresh Codex subagent / current model | 316e0b1 | none | 3 | 13 | Pass (behavior); Not run (implementation) | [Raw response](runs/2026-07-16-v1.1.0/en-s13-r3.md) |
