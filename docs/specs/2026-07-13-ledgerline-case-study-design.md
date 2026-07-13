# Ledgerline Case Study Design

## Purpose

Build Ledgerline as a standalone payment API documentation site and use it as Gridgeist's second public case study. The experiment tests whether the skill generalizes beyond a developer-observability dashboard to dense documentation, navigation, code samples, and responsive reading flows.

## Product

Ledgerline documents a fictional REST API for developers who need to create payments, inspect their status, issue refunds, and process webhooks. The content must remain internally consistent while clearly identifying all payment data and behavior as illustrative rather than production guidance.

The visual thesis is “an executable ledger.” The interface should feel precise, auditable, and useful. Navigation, typography, rules, code, parameters, responses, and status transitions carry the visual identity instead of generic fintech decoration.

## Information architecture

- Getting Started: API keys, environments, and the first payment.
- Payments: create, retrieve, capture, and cancel.
- Refunds: create and inspect a refund.
- Webhooks: event types, signature verification, and retry behavior.
- Errors: HTTP statuses, the error object, and troubleshooting.
- API Reference: parameters, requests, and responses for each endpoint.

The landing route opens with a working quickstart that leads directly into reference material. Example IDs, amounts, currencies, states, and payloads remain consistent across the documentation.

## Interface direction

Use a light ledger-paper surface, readable sans-serif text, monospace for code and identifiers, and thin rules that reveal document structure. Reserve a ledger-red accent for active state, warnings, and focus. Prefer square geometry and composed document regions over repeated cards.

At wide desktop sizes, use three coordinated regions: navigation on the left, a constrained reading column in the center, and context-matched code on the right.

## Responsive behavior

- At 1280 px and above, show navigation, article, and code simultaneously.
- From 768 px through 1279 px, collapse navigation to a compact rail while retaining a deliberate article/code split.
- Below 768 px, replace persistent navigation with a document header and table-of-contents drawer. Place each code sample beside the step it supports in reading order.
- At 360 px, transform parameter tables into term/value records without losing type, required state, or description.
- Restrict horizontal scrolling to code blocks; the document itself must not overflow.

## Interaction and accessibility

- Open and close the mobile table of contents.
- Switch code examples between cURL and JavaScript.
- Copy code with accessible feedback.
- Navigate through stable section anchors.
- Provide semantic landmarks, logical headings, visible keyboard focus, sufficient contrast, and reduced-motion behavior.

## Technical approach

- Create a standalone public repository at `ohmiler/ledgerline`.
- Use Next.js and TypeScript with static export for GitHub Pages.
- Keep documentation content and UI state deterministic and local.
- Do not add authentication, a backend, live search, documentation versioning, or real payment processing in version one.
- Use automated checks plus Playwright at 360, 768, 1280, and 1600 px.

## Experiment record

Preserve the following artifacts in the Ledgerline repository:

1. `baseline/`: a generic documentation-template implementation built from the same requirements and content.
2. `experiment/prompt.md`: the exact prompt used to invoke Gridgeist.
3. `experiment/rubric.md`: baseline and final scores with evidence.
4. The main application: the final Gridgeist-guided implementation.
5. `README.md`: setup, verification, deployment, experiment method, and limitations.

Score baseline and final implementations on six dimensions worth five points each:

1. Information hierarchy.
2. Product specificity.
3. Navigation and findability.
4. Responsive recomposition.
5. Accessibility.
6. Implementation quality.

Do not establish a target final score before implementation.

## Verification

- Lint and production build pass.
- Static export works under the GitHub Pages base path.
- Automated tests cover content and interaction logic where appropriate.
- Browser tests verify navigation, language switching, copy feedback, anchors, keyboard focus, and horizontal overflow.
- The deployed site and source repository are public and reachable before Gridgeist links the case study.

## Success criteria

- A developer can reach a first successful illustrative payment request from the landing route without instruction.
- A developer can find the create-payment endpoint, understand its required parameters, and inspect success and error responses.
- Navigation and code remain usable at all four representative viewport widths.
- Product evidence dominates the interface; generic documentation chrome does not become the visual idea.
- Another person can reconstruct what was tested from the preserved baseline, prompt, rubric, and verification evidence.

## Limitations

- Ledgerline is fictional and must not be treated as payment-system guidance.
- The case study records one model run rather than a statistically representative evaluation.
- It does not include usability testing with external developers.
- Results remain model-, prompt-, and repository-context dependent.
