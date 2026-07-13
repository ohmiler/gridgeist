# Ledgerline Case Study Implementation Plan

> Execute this plan inline in a normal Codex session. Do not use Superpowers or subagents. Track progress with the checkboxes and verify every checkpoint before committing.

**Goal:** Build and publish Ledgerline, a fictional payment API documentation site that tests whether Gridgeist generalizes from dashboards to dense developer documentation.

**Architecture:** Create `ohmiler/ledgerline` as a standalone Next.js static-export repository. Keep one deterministic content model as the source for the final documentation UI, preserve a separate static generic baseline, and store the exact Gridgeist prompt plus rubric alongside both implementations. Deploy `out/` to GitHub Pages and verify four representative viewport widths.

**Tech Stack:** Next.js, TypeScript, React, CSS Modules/global CSS, Vitest with Testing Library, Playwright, GitHub Actions, GitHub Pages.
**Fixed rubric:** Score Information hierarchy, Product specificity, Navigation and findability, Responsive recomposition, Accessibility, and Implementation quality from 1–5 each, for a total of 30.

---

## File map

```text
ledgerline/
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ .github/workflows/pages.yml        Build, test, and deploy static export
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ baseline/
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ index.html                     Generic documentation baseline
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ styles.css                     Baseline-only styling
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ experiment/
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ prompt.md                      Exact Gridgeist invocation
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ rubric.md                      6 Ãƒâ€” 5 baseline/final evidence table
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ public/
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ favicon.svg                    Code-native Ledgerline mark
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ src/app/
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ globals.css                    Tokens, layout, responsive transformations
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ layout.tsx                     Metadata and document shell
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ page.tsx                       Route composition from documentation data
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ src/components/
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ CodePanel.tsx                  Language switch and copy feedback
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ DocsHeader.tsx                 Brand, environment, mobile TOC control
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ DocsNavigation.tsx             Section navigation and drawer behavior
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ EndpointSection.tsx            Method, path, parameters, examples
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ ParameterList.tsx              Table-to-record responsive parameters
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ src/content/
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ documentation.ts               Typed deterministic Ledgerline content
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ src/lib/
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ clipboard.ts                   Clipboard helper with failure result
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ tests/
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ documentation.test.ts          Content integrity and anchor uniqueness
Ã¢â€â€š   Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ clipboard.test.ts              Copy success/failure behavior
Ã¢â€â€š   Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ ledgerline.spec.ts             Playwright interaction/responsive checks
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ next.config.ts                     Static export and GitHub Pages base path
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ playwright.config.ts               Four viewport projects
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ vitest.config.ts                   Unit/component test environment
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ package.json                       Scripts and dependencies
Ã¢â€Å“Ã¢â€â‚¬Ã¢â€â‚¬ README.md                          Setup, experiment, verification, limits
Ã¢â€â€Ã¢â€â‚¬Ã¢â€â‚¬ LICENSE                            MIT license
```

## Task 1: Create and configure the repository

**Files:**
- Create: the repository root and standard Next.js scaffold
- Create: `next.config.ts`
- Modify: `package.json`

- [ ] Verify `ohmiler/ledgerline` does not already exist:

```powershell
gh repo view ohmiler/ledgerline
```

Expected: repository-not-found response. Stop and inspect rather than overwrite if it exists.

- [ ] Create `C:\Users\Miler\Downloads\ledgerline`, initialize the Next.js TypeScript App Router scaffold, and create the public GitHub repository:

```powershell
npx create-next-app@latest C:\Users\Miler\Downloads\ledgerline --ts --eslint --app --src-dir --import-alias "@/*" --use-npm --yes
gh repo create ohmiler/ledgerline --public --source C:\Users\Miler\Downloads\ledgerline --remote origin
```

Expected: `origin` equals `https://github.com/ohmiler/ledgerline.git`.

- [ ] Install test dependencies:

```powershell
npm install -D vitest jsdom @testing-library/react @testing-library/jest-dom @playwright/test
npx playwright install chromium
```

- [ ] Configure scripts in `package.json`:

```json
{
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "lint": "eslint",
    "test": "vitest run",
    "test:e2e": "playwright test",
    "verify": "npm run lint && npm run test && npm run build && npm run test:e2e"
  }
}
```

- [ ] Configure static export in `next.config.ts`:

```ts
import type { NextConfig } from "next";

const isProduction = process.env.NODE_ENV === "production";
const nextConfig: NextConfig = {
  output: "export",
  basePath: isProduction ? "/ledgerline" : "",
  assetPrefix: isProduction ? "/ledgerline/" : "",
  images: { unoptimized: true },
};

export default nextConfig;
```

- [ ] Run `npm run lint && npm run build`; expect both commands to exit 0 and create `out/`.
- [ ] Commit:

```powershell
git add .
git commit -m "chore: scaffold Ledgerline documentation"
```

## Task 2: Preserve the generic baseline

**Files:**
- Create: `baseline/index.html`
- Create: `baseline/styles.css`

- [ ] Implement the same Ledgerline content as a deliberately conventional docs template: fixed dark sidebar, unconstrained article, repeated gray panels, generic blue accent, static cURL block, and parameter table. Include Getting Started, Payments, Refunds, Webhooks, Errors, and API Reference links.
- [ ] Keep baseline interactions minimal but valid: anchor links work and HTML is semantic enough to render; do not intentionally introduce accessibility defects.
- [ ] Serve the repository and inspect baseline at 1280 px and 360 px:

```powershell
npx serve . -l 4173
```

Expected: content renders at `/baseline/`; record overflow and navigation weaknesses as evidence rather than silently fixing them into the final direction.

- [ ] Add the initial baseline evidence to `experiment/rubric.md` using the six named dimensions, each scored from 1Ã¢â‚¬â€œ5 with one concrete observation.
- [ ] Commit:

```powershell
git add baseline experiment/rubric.md
git commit -m "test: preserve Ledgerline baseline"
```

## Task 3: Record the exact Gridgeist experiment prompt

**Files:**
- Create: `experiment/prompt.md`

- [ ] Write this prompt verbatim before implementing the final interface:

```text
Use $gridgeist to redesign this working payment API documentation site.
Preserve all Ledgerline content, anchors, endpoint semantics, and the ability to reach the first payment request without instruction.
Make navigation, typography, parameters, request/response code, errors, and payment states carry the visual identity instead of generic documentation cards.
Create a deliberate responsive composition for 360 px, 768 px, 1280 px, and 1600 px; do not simply stack the desktop columns.
Implement working mobile navigation, cURL/JavaScript switching, copy feedback, keyboard focus, reduced motion, and no document-level horizontal overflow.
Treat all payment behavior as fictional illustrative content and do not present it as production payment guidance.
```

- [ ] Record the model, date, Gridgeist tag/commit, repository baseline commit, and command/session surface immediately below the prompt.
- [ ] Invoke the installed local `gridgeist/SKILL.md` against the Ledgerline repository without adding another visual-design skill to the same run.
- [ ] Save the resulting one-sentence direction in the experiment record.
- [ ] Commit:

```powershell
git add experiment/prompt.md
git commit -m "docs: record Gridgeist experiment prompt"
```

## Task 4: Define and test the documentation content model

**Files:**
- Create: `src/content/documentation.ts`
- Create: `tests/documentation.test.ts`
- Create: `vitest.config.ts`

- [ ] Write failing tests that require unique anchors, a create-payment endpoint, both cURL and JavaScript samples, required parameter metadata, success/error responses, and the fictional-product disclaimer.
- [ ] Run `npm test`; expect failure because `documentation.ts` does not exist.
- [ ] Define exported types `NavSection`, `Parameter`, `CodeExamples`, `Endpoint`, and `LedgerlineDocumentation`, then export one immutable `documentation` object. Use consistent example values: `pay_01J9AZ7J6Y3K2E8M4T`, `2500`, `thb`, and `requires_capture`.
- [ ] Include sections and endpoint content specified by the design without claiming real compliance, security, or settlement behavior.
- [ ] Run `npm test`; expect all content integrity tests to pass.
- [ ] Commit:

```powershell
git add src/content/documentation.ts tests/documentation.test.ts vitest.config.ts
git commit -m "feat: define Ledgerline documentation content"
```

## Task 5: Build the accessible document shell

**Files:**
- Create: `src/components/DocsHeader.tsx`
- Create: `src/components/DocsNavigation.tsx`
- Modify: `src/app/layout.tsx`
- Modify: `src/app/page.tsx`
- Modify: `src/app/globals.css`

- [ ] Add a component test that opens the mobile table of contents, exposes navigation with an accessible label, closes it on Escape, restores focus to the trigger, and closes after an anchor is chosen.
- [ ] Run `npm test`; expect the new test to fail before components exist.
- [ ] Implement the header and navigation with a button using `aria-expanded`/`aria-controls`, a labeled `nav`, Escape handling, focus restoration, and a backdrop that does not trap desktop interaction.
- [ ] Compose `page.tsx` with semantic `header`, `nav`, `main`, `article`, and `aside` landmarks. Render the disclaimer and quickstart before reference sections.
- [ ] Define CSS tokens and wide-screen three-region grid. Constrain the reading column to approximately 68 characters and reserve red for active/warning/focus roles.
- [ ] Run unit tests and lint; expect both to pass.
- [ ] Commit:

```powershell
git add src/app src/components/DocsHeader.tsx src/components/DocsNavigation.tsx tests
git commit -m "feat: add responsive documentation shell"
```

## Task 6: Implement endpoints, parameters, and code interaction

**Files:**
- Create: `src/components/EndpointSection.tsx`
- Create: `src/components/ParameterList.tsx`
- Create: `src/components/CodePanel.tsx`
- Create: `src/lib/clipboard.ts`
- Create: `tests/clipboard.test.ts`
- Modify: `src/app/page.tsx`
- Modify: `src/app/globals.css`

- [ ] Write failing tests for `copyText`: return `{ ok: true }` when `navigator.clipboard.writeText` resolves and `{ ok: false }` when unavailable or rejected.
- [ ] Run the focused test; expect failure because the helper is missing.
- [ ] Implement `copyText(text)` without throwing to the component boundary.
- [ ] Implement endpoint sections with method/path headings, stable anchors, descriptions, parameter data, success response, and error response.
- [ ] Implement `CodePanel` as a client component with cURL/JavaScript tabs, an accessible selected state, copy button, and polite live-region feedback that clears after two seconds.
- [ ] Implement parameter markup as a table at wide widths and CSS-driven term/value records at 360 px while preserving every field.
- [ ] Run unit tests, lint, and build; expect all to pass.
- [ ] Commit:

```powershell
git add src/components src/lib src/app tests
git commit -m "feat: add executable API reference"
```

## Task 7: Complete responsive recomposition and visual refinement

**Files:**
- Modify: `src/app/globals.css`
- Create: `public/favicon.svg`

- [ ] At 1280 px and 1600 px, verify three coordinated regions, constrained prose, sticky navigation/code only where viewport height permits, and no repeated-card visual system.
- [ ] At 768 px, convert the left navigation to a compact rail and preserve an intentional article/code split.
- [ ] At 360 px, show document header plus TOC drawer, move code into article reading order, transform parameter tables to records, and restrict overflow to `pre` elements.
- [ ] Add `:focus-visible`, `prefers-reduced-motion`, high-contrast selection, and touch targets of at least 44 CSS pixels for mobile controls.
- [ ] Create a simple code-native SVG mark from ledger rules and an `L`; do not use generated raster branding.
- [ ] Run `npm run lint && npm test && npm run build`; expect all to pass.
- [ ] Commit:

```powershell
git add src/app/globals.css public/favicon.svg
git commit -m "style: refine Ledgerline across viewports"
```

## Task 8: Add browser verification

**Files:**
- Create: `playwright.config.ts`
- Create: `tests/ledgerline.spec.ts`
- Create: `scripts/run-preview.mjs` only if Playwright webServer cannot reliably start the static export directly

- [ ] Configure projects named `mobile-360`, `tablet-768`, `desktop-1280`, and `wide-1600` with matching viewport widths.
- [ ] Configure `webServer` to run the production export locally and set `baseURL` to the served `/ledgerline/` route.
- [ ] Write tests that assert: quickstart and disclaimer visible; create-payment anchor reachable; language switch changes sample; copy produces accessible feedback; mobile TOC opens/closes; focus is visible via keyboard; `document.documentElement.scrollWidth <= window.innerWidth` at every project width.
- [ ] Run `npm run test:e2e`; inspect screenshots and console errors for every failed assertion.
- [ ] Fix root causes in application code, rerun the focused failing project, then rerun the full suite.
- [ ] Run `npm run verify`; expect lint, unit tests, production build, and all browser projects to pass.
- [ ] Commit:

```powershell
git add playwright.config.ts tests scripts src
git commit -m "test: verify Ledgerline interactions and layout"
```

## Task 9: Score and document the experiment

**Files:**
- Modify: `experiment/rubric.md`
- Create: `README.md`
- Create: `LICENSE`

- [ ] Score the final implementation from rendered evidence without changing the baseline score. For each of six dimensions, record baseline score, final score, concrete evidence, and the maximum of five.
- [ ] Add totals out of 30 and state that this is one model run, not a controlled statistical claim.
- [ ] Write README sections: purpose, live demo, install/run, exact experiment method, repository map, verification commands, rubric summary, fictional API warning, limitations, and Gridgeist/commit links.
- [ ] Add the MIT license matching the Gridgeist repository's ownership naming.
- [ ] Verify every local README link resolves and every command matches `package.json`.
- [ ] Commit:

```powershell
git add README.md LICENSE experiment
git commit -m "docs: publish Ledgerline experiment record"
```

## Task 10: Deploy and publish the case study

**Files:**
- Create: `.github/workflows/pages.yml`
- Modify: `README.md`

- [ ] Add a Pages workflow that checks out main, sets up Node with npm cache, runs `npm ci`, `npm run lint`, `npm test`, `npm run build`, uploads `out/`, and deploys with `actions/deploy-pages`.
- [ ] Give only required permissions: `contents: read`, `pages: write`, and `id-token: write`; set the `github-pages` environment.
- [ ] Push main and enable GitHub Pages with GitHub Actions as the build source.
- [ ] Watch the workflow to completion; do not report success while it is queued or running.
- [ ] Verify `https://ohmiler.github.io/ledgerline/` returns 200 and contains the quickstart, disclaimer, and create-payment reference.
- [ ] Add the confirmed live URL to README, commit, push, and verify the follow-up workflow.
- [ ] Tag a pre-case-study milestone only after all checks pass:

```powershell
git tag -a v0.1.0 -m "Ledgerline v0.1.0"
git push origin main v0.1.0
```

## Task 11: Link Ledgerline from Gridgeist

**Files in `C:\Users\Miler\Downloads\gridgeist`:**
- Modify: `README.md`
- Modify: `README.th.md`
- Modify: `evals/prompts.md`
- Modify: `evals/prompts.th.md`

- [ ] Add Ledgerline as the second case study only after its production deployment and evidence are reachable.
- [ ] Add one English and one Thai evaluation scenario targeting dense documentation responsive behavior, linking the scenario to Ledgerline evidence without hard-coding a required score.
- [ ] Run Gridgeist skill structure validation, local link checks, and production URL checks.
- [ ] Commit and push:

```powershell
git add README.md README.th.md evals/prompts.md evals/prompts.th.md
git commit -m "docs: add Ledgerline documentation case study"
git push origin main
```

## Final acceptance checklist

- [ ] Ledgerline public repository, baseline, exact prompt, rubric, and limitations are readable.
- [ ] `npm run verify` passes from a clean clone.
- [ ] GitHub Pages deployment succeeds and production returns 200.
- [ ] Four viewport projects pass without document-level overflow.
- [ ] Keyboard, copy, language switch, anchors, and mobile navigation work.
- [ ] Baseline and final use the same requirements and content.
- [ ] Gridgeist links Ledgerline only after evidence is independently reachable.
