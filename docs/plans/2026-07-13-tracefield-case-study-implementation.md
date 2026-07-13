# Tracefield Case Study Implementation Plan

**Goal:** Build and publish a standalone observability dashboard that provides reproducible evidence of how Gridgeist changes a generic product interface.

**Architecture:** A statically exported Next.js application reads deterministic typed trace fixtures and derives all filters and summary metrics in the browser. The working surface is split into navigation, trace list, and trace inspector boundaries, with a drawer replacing the inspector on mobile. Experiment artifacts live beside the product code so the baseline, prompt, rubric, and final result remain reviewable.

**Tech Stack:** Next.js, React, TypeScript, CSS, Vitest, Playwright, GitHub Actions, GitHub Pages

---

### Task 1: Repository and build foundation

**Files:**
- Create: `package.json`
- Create: `next.config.ts`
- Create: `src/app/layout.tsx`
- Create: `src/app/page.tsx`
- Create: `.github/workflows/pages.yml`

- [ ] Create public repository `ohmiler/tracefield` and scaffold a TypeScript Next.js App Router project without a component library.
- [ ] Configure `output: "export"`, repository-aware asset paths, trailing slashes, linting, and test scripts.
- [ ] Add a Pages workflow that installs with `npm ci`, runs tests and build, uploads `out/`, and deploys only after checks pass.
- [ ] Run the initial test and production build, then commit the foundation.

### Task 2: Experiment evidence and baseline

**Files:**
- Create: `experiment/brief.md`
- Create: `experiment/gridgeist-prompt.md`
- Create: `experiment/rubric.md`
- Create: `experiment/baseline.html`
- Create: `experiment/baseline.css`

- [ ] Record one shared product brief and deterministic data requirements.
- [ ] Record the exact `$gridgeist` prompt used for the redesign.
- [ ] Define a 1–5 rubric for hierarchy, product specificity, originality, responsive composition, accessibility, and implementation quality.
- [ ] Build a self-contained generic dashboard baseline using a welcome banner and interchangeable metric cards.
- [ ] Commit the experiment record before building the final interface.

### Task 3: Typed trace domain and filtering

**Files:**
- Create: `src/data/traces.ts`
- Create: `src/lib/traces.ts`
- Create: `src/lib/traces.test.ts`

- [ ] Define `Trace`, `Span`, `Service`, and status types plus fixtures covering healthy, slow, and failed requests.
- [ ] Write tests for text search, service/status filters, health metrics, and empty results.
- [ ] Implement pure selectors and metric derivation until the tests pass.
- [ ] Commit the trace domain independently from the UI.

### Task 4: Operational workspace

**Files:**
- Create: `src/components/Sidebar.tsx`
- Create: `src/components/Topbar.tsx`
- Create: `src/components/HealthStrip.tsx`
- Create: `src/components/TraceTable.tsx`
- Create: `src/components/TraceInspector.tsx`
- Create: `src/components/TraceWorkspace.tsx`
- Modify: `src/app/page.tsx`

- [ ] Render navigation, environment and time controls, derived health metrics, and the trace table.
- [ ] Connect search, service, and status filters to the pure selectors.
- [ ] Open the selected trace in an inspector containing request metadata and a proportional span waterfall.
- [ ] Implement deterministic loading, empty, and error views accessible through a development state control.
- [ ] Commit the complete desktop workflow.

### Task 5: Visual system and responsive behavior

**Files:**
- Create: `src/app/globals.css`
- Modify: `src/components/TraceWorkspace.tsx`
- Modify: `src/components/TraceInspector.tsx`

- [ ] Apply the “live incident record” direction with a dark surface, visible structure, restrained typography, and acid green used only for focus and important status.
- [ ] Keep data and workflow evidence visually dominant and avoid dashboard-card mosaics.
- [ ] Recompose below 760px into a trace list with a modal drawer inspector, explicit close control, focus return, and scroll locking.
- [ ] Add visible focus, minimum target sizes, semantic status text, and reduced-motion handling.
- [ ] Commit the responsive visual system.

### Task 6: Verification and publication

**Files:**
- Create: `tests/workspace.spec.ts`
- Create: `playwright.config.ts`
- Create: `README.md`
- Modify: `experiment/rubric.md`

- [ ] Add Playwright checks for filtering, opening a trace, closing the mobile drawer, keyboard focus, and horizontal overflow at desktop and mobile viewports.
- [ ] Run unit tests, Playwright checks, lint, and static export; inspect representative screenshots and console output.
- [ ] Score the baseline and final interface in the rubric with evidence for every score.
- [ ] Document setup, architecture, experiment method, limitations, and deployed URL.
- [ ] Push `main`, enable GitHub Pages through Actions, wait for deployment success, and verify the public URL.
