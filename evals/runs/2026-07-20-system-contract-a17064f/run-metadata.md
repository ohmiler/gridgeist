# Run metadata

- Date: 2026-07-20
- Final candidate: `a17064f0b0077aa88274b1d078d765bd711b0407`
- Gridgeist tree: `c30e6c2a359e7d94b9b56adaf14eb124efb519f9`
- Runner: Codex CLI 0.144.6
- Model: `gpt-5.6-sol`
- Session mode: ephemeral; user config and project rules ignored
- Sandbox: `danger-full-access`, explicitly authorized by the user after the
  managed Windows runner downgraded `workspace-write` to `read-only`
- Target: one fresh `C:\tmp` copy per run containing the fictional fixture and
  workspace-local Gridgeist skill; no Git history, repository rules, eval rubric,
  Solodeveling memory, or prior outputs
- Prompt envelope: the published Scenario 19 text plus a target-only access and
  preview-server cleanup instruction
- Canonical stale `DESIGN.md` SHA-256:
  `4b873a2d582d715753e8efd080f1df0788651a04a2feb92a313112c344c8bdb6`

## Counted formal runs

| Run | Session | Source changes | Result |
| --- | --- | --- | --- |
| EN2 | `019f7fa2-a59f-7c43-b617-27b261de0613` | `index.html`, `billing.html`, `styles.css` | Pass |
| EN3 | `019f7faa-d773-7f93-ab92-dfc28ab7cf9c` | `billing.html`, `styles.css` | Pass |
| EN4 | `019f7fc2-ebe3-7f11-82f2-eb8aabfb8e2b` | `styles.css` | Pass |
| TH1 | `019f7f9d-ed0f-7873-98f7-17453e186473` | `styles.css` | Pass |
| TH2 | `019f7fb2-7870-7743-9c7b-542c7d95f142` | `index.html`, `billing.html`, `styles.css` | Pass |
| TH3 | `019f7fb8-f9ab-7992-95eb-33e499f122cc` | `styles.css` | Pass |

Every counted run preserved `DESIGN.md`, created no design document or dependency,
implemented semantic tokens and shared component/state rules, preserved routes and
behavior, and reported rendered multi-width/theme/state verification. Primary
Playwright verification independently opened Profile and Billing at 360 CSS px and
reported zero console errors for every counted target.

EN1 session `019f7f95-ac44-70e1-959b-c2db3f410ccf` passed behaviorally but is
excluded from the count because its log shows reads of two global nonvisual helper
skills outside the target. Its response and manifests remain preserved for audit.

## Evidence layout

- `responses/`: raw final responses
- `prompts/`: exact delivered prompts
- `hashes/`: per-run baseline, post-run, and change manifests
- `renders/`: primary-agent 360 px Profile screenshots
- `guardrails/`: selected raw pre-repair and post-repair smoke responses

Markdown trailing hard-break spaces were normalized after capture; wording and line
order are unchanged.

## Limitations

- Full local filesystem authority was required because the managed Windows sandbox
  could not provide writable isolation. Counted-run logs were audited for explicit
  repository or user-Codex paths and contained none, but this is not an OS-hermetic
  guarantee.
- Screenshot pixels could not be reopened through the local image-view helper
  because the Windows sandbox helper executable was unavailable. Playwright page
  titles, accessibility snapshots, viewport screenshots, and console results were
  captured successfully.
- Forced-colors and reduced-motion behavior was generally code-inspected rather than
  rendered in dedicated OS emulation.
- Model behavior remains nondeterministic; results support planning, not an
  unconditional claim about every future run.
