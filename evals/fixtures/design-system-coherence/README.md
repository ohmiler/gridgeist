# Ledger Account design-system coherence fixture

Ledger Account is a fictional multi-page workspace where an individual account
owner manages a public profile, plan, and invoice history. The baseline is
deliberately functional but systemically inconsistent.

## Product facts

- The profile route is index.html and the billing route is billing.html.
- Navigation between both routes, the light/dark theme toggle, profile save
  feedback, invoice filtering, and local invoice preparation feedback are required
  behavior.
- The account name, plan, invoice records, and all visible content must be
  preserved. The fixture data is fictional and labeled as such.
- styles.css intentionally repeats near-identical color, spacing, radius, layout,
  and component values rather than using a coherent token and variant system.
- DESIGN.md is intentionally stale and conflicts with the rendered interface. It is
  inspection evidence for Scenario 19 and must remain unchanged in that task.
- No user research, conversion data, compliance result, or approved replacement
  direction is supplied.

## Run locally

Serve this directory with any static HTTP server and open index.html. Evaluation
runs should redesign a disposable copy so every run starts from the same baseline
and the original stale DESIGN.md can be compared byte for byte.
