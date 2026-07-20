---
solodeveling_schema: 1
---

# EVIDENCE-0019: System-contract behavioral evaluation

- **Work item:** `WORK-0017-system-contract-behavioral-eval`
- **Opened:** 2026-07-20
- **Candidate:** `a17064f0b0077aa88274b1d078d765bd711b0407`
- **Result:** Pass — ready for proportional minor-release planning; no release action authorized.

## Current acceptance matrix

| Boundary | Evidence | Result |
| --- | --- | --- |
| Exact candidate and isolated skill discovery | Ephemeral probe session `019f7f28-7c4f-7781-80c7-19ade9cba289` loaded the workspace-local skill and directly read `references/system-contract.md`; it returned all three token layers. Runner `codex-cli 0.144.6`, model `gpt-5.6-sol`. | Pass |
| English Scenario 19 runs 1–3 | Clean counted sessions EN2 `019f7fa2-a59f-7c43-b617-27b261de0613`, EN3 `019f7faa-d773-7f93-ab92-dfc28ab7cf9c`, and EN4 `019f7fc2-ebe3-7f11-82f2-eb8aabfb8e2b`; raw responses and manifests in [`../../evals/runs/2026-07-20-system-contract-a17064f/`](../../evals/runs/2026-07-20-system-contract-a17064f/). | Pass |
| Thai Scenario 19 runs 1–3 | Sessions TH1 `019f7f9d-ed0f-7873-98f7-17453e186473`, TH2 `019f7fb2-7870-7743-9c7b-542c7d95f142`, and TH3 `019f7fb8-f9ab-7992-95eb-33e499f122cc`; zero outside-path mentions. | Pass |
| Artifact-boundary and source-change inspection | Per-run pre/post SHA-256 manifests show `DESIGN.md` unchanged in every counted run, zero new design documents or dependencies, and implementation changes limited to existing HTML/CSS files. | Pass |
| Rendered fixture behavior and responsive verification | Fresh runners exercised routes, themes, widths, and states. Primary Playwright independently opened Profile and Billing at 360 CSS px with zero console errors for all six counted targets. | Pass |
| Targeted guardrail smoke set | Scenario 12 passed. Scenario 14 and 18 exposed failures, were diagnosed and repaired in `a17064f`, then passed post-repair in EN and TH. Scenario 15 passed; Scenario 13 passed as a state/recovery alignment smoke. | Pass with stated Scenario 13 scope |
| Repository scope and disposable cleanup | Unrelated untracked files were preserved. Tracked evidence was copied before exact target cleanup; all targets were removed except two empty locked directories under `C:\tmp\gridgeist-guardrails-20260720`. | Pass with Windows handle limitation |

## Limitations

- The user explicitly authorized full local filesystem access after the managed
  Windows runner downgraded `workspace-write` to read-only. Counted-run logs contain
  no explicit outside-workspace paths, but the harness is not OS-hermetic.
- A behaviorally passing EN1 was excluded because it read global nonvisual helper
  skills. EN4 replaced it so the counted English set remained three clean sessions.
- The original guardrail validation had used a read-only decision harness and only
  one run per language. A writable Scenario 14 exposed that classification alone
  did not stop implementation. The final candidate makes provisional broad work a
  hard stop and distinguishes content evidence from brand-direction evidence.
- Scenario 13 verifies state/recovery priority at the alignment boundary, not a full
  post-repair import implementation.
- The image-view helper was unavailable because the Windows sandbox helper was
  missing. Playwright captures, snapshots, and console checks succeeded.
- Two empty disposable directories remain locked by released Windows handles; no
  fixture, skill, response, or secret data remains in them.
