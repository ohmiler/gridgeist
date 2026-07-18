---
solodeveling_schema: 1
---

# EVIDENCE-0010: Direction-alignment behavior

- **Work item:** `WORK-0008-validate-direction-alignment`
- **Date opened:** 2026-07-18
- **Target:** GridGeist v1.1.0 direction-selection behavior before broad Create or Redesign implementation.
- **Result:** Pass — the v1.1.0 gap reproduced, the minimum conditional gate was implemented, and affected EN/TH behavioral and repository checks passed. Release and publication were not performed.

## Motivating observation

- **Source:** User report from a real GridGeist usage session.
- **Observation:** A broad webpage-adjustment request implicitly triggered GridGeist, after which the agent selected a direction and implemented it without first asking which direction the user wanted.
- **Interpretation:** This may expose a missing collaboration checkpoint when several materially different visual theses are credible.
- **Limit:** The original prompt, target repository, raw agent output, diff, model context, and rendered result were not captured here. This is motivating feedback, not an independently reproduced failure and not sufficient by itself to revise the frozen core.

## Static inspection

- `skills/gridgeist/SKILL.md` currently instructs the agent to derive direction from an established brand and to present options only when brand signals conflict materially or the user requests exploration.
- The workflow moves directly from **Inspect** to **Set a thesis**, with no explicit direction-alignment decision between them.
- `evals/prompts.md` and `evals/prompts.th.md` cover Create, Redesign, Review, conflicting brand direction, and negative frontend triggers, but do not directly test an underspecified broad redesign against an explicit-direction control on the same fixture.
- Existing Scenario 6 supplies a clear established playful brand, so it tests brand preservation rather than whether the agent should consult the user when the desired direction is genuinely underdetermined.
- `.solodeveling/roadmap.md` freezes v1.1.0 core guidance until a severe finding or a pattern reproduced in at least two independent projects provides evidence for revision.

## Reproduction and decision

The gap reproduced on the isolated Commonroom fixture in both English and Thai. The
v1.1.0 agent inspected the product and then selected a warm neighborhood
noticeboard/editorial thesis without asking the user to align on one of several
credible directions. The explicit-direction controls correctly proceeded without a
redundant preference question.

Together with the motivating report from a separate real project, the isolated
reproduction established the required cross-context pattern. The smallest justified
change was therefore applied between **Inspect** and **Set a thesis**. It classifies
direction as user-confirmed, brand-derived, or provisional; asks only for material
thesis-level ambiguity; and treats variations within a coherent user-confirmed
thesis as implementation choices.

## Fixture evidence

- Fixture: [`../../evals/fixtures/direction-alignment/`](../../evals/fixtures/direction-alignment/)
- Behavioral harness: [`../../evals/harnesses/direction-decision/AGENTS.md`](../../evals/harnesses/direction-decision/AGENTS.md)
- `python scripts/validate_release.py` passed after paired scenarios 14 and 15 were added.
- `node --check evals/fixtures/direction-alignment/script.js` passed.
- Playwright rendered the fixture at 360 px and 1280 px with no observed overflow;
  screenshots are preserved as
  [`commonroom-360.png`](../../evals/runs/2026-07-18-v1.1.0-direction-alignment/commonroom-360.png)
  and [`commonroom-1280.png`](../../evals/runs/2026-07-18-v1.1.0-direction-alignment/commonroom-1280.png).
- Observed flow: topic filter reduced three records to one; combining Food with
  Places available produced the visible zero-result state; the details dialog opened;
  reservation closed the dialog and returned focus to its trigger; the live
  confirmation appeared and cleared after four seconds; final console result was
  zero errors and zero warnings.
- During fixture verification, `.workshop { display: grid }` was found to override
  the `hidden` attribute. The confirmed root cause was repaired with an explicit
  `[hidden]` rule and the original reproduction passed afterward.

## Behavioral runs

All recorded runs used Codex CLI 0.144.5 with `gpt-5.6-sol`. Decision-harness runs
used an ephemeral, isolated local skill copy and read-only sandbox so the response
before editing could be compared without leaking the rubric. Baseline source was the
unchanged v1.1.0 skill (`v1.1.0` tag `b3421c69`; SHA-256
`e2e93cda5747432dbaef7070b32094d240a2f0d0a4e27b6e49235f340263b68f`).
Post-change source was the working-tree skill at HEAD `6fe2d98` with SHA-256
`3e6efb82129a82edf504d6a7ef5a24afa2a11c35badc2b78a2f3d9938ed1545e`.

| Phase | Language / scenario | Result | Raw output |
|---|---|---|---|
| v1.1.0 baseline | EN / 14 ambiguous | Fail — selected a thesis without alignment | [`en-s14-isolated-r1.md`](../../evals/runs/2026-07-18-v1.1.0-direction-alignment/en-s14-isolated-r1.md) |
| v1.1.0 baseline | TH / 14 ambiguous | Fail — selected a thesis without alignment | [`th-s14-harness-r1.md`](../../evals/runs/2026-07-18-v1.1.0-direction-alignment/th-s14-harness-r1.md) |
| v1.1.0 baseline | EN / 15 explicit | Pass — proceeded with the supplied direction | [`en-s15-harness-r1.md`](../../evals/runs/2026-07-18-v1.1.0-direction-alignment/en-s15-harness-r1.md) |
| v1.1.0 baseline | TH / 15 explicit | Pass — proceeded with the supplied direction | [`th-s15-harness-r1.md`](../../evals/runs/2026-07-18-v1.1.0-direction-alignment/th-s15-harness-r1.md) |
| Post-change | EN / 14 ambiguous | Pass — offered three grounded options and a recommendation | [`en-s14-r1.md`](../../evals/runs/2026-07-18-direction-alignment-post-change/en-s14-r1.md) |
| Post-change | TH / 14 ambiguous | Pass — offered three grounded options and a recommendation | [`th-s14-r1.md`](../../evals/runs/2026-07-18-direction-alignment-post-change/th-s14-r1.md) |
| Post-change | EN / 15 explicit, first attempt | Fail — over-questioned variants inside the confirmed thesis | [`en-s15-r1.md`](../../evals/runs/2026-07-18-direction-alignment-post-change/en-s15-r1.md) |
| Post-change | EN / 15 explicit, after threshold repair | Pass — classified direction as user-confirmed without another question | [`en-s15-r2.md`](../../evals/runs/2026-07-18-direction-alignment-post-change/en-s15-r2.md) |
| Post-change | TH / 15 explicit | Pass — classified direction as user-confirmed without another question | [`th-s15-r1.md`](../../evals/runs/2026-07-18-direction-alignment-post-change/th-s15-r1.md) |
| Post-change | EN/TH / Review | Pass — reported immediately and labeled replacement direction provisional | [`en-review-r1.md`](../../evals/runs/2026-07-18-direction-alignment-post-change/en-review-r1.md), [`th-review-r1.md`](../../evals/runs/2026-07-18-direction-alignment-post-change/th-review-r1.md) |
| Post-change | EN/TH / narrow frontend | Pass — did not invoke Gridgeist or ask aesthetic questions | [`en-narrow-r1.md`](../../evals/runs/2026-07-18-direction-alignment-post-change/en-narrow-r1.md), [`th-narrow-r1.md`](../../evals/runs/2026-07-18-direction-alignment-post-change/th-narrow-r1.md) |

## Acceptance matrix

| Criterion | Evidence | Result |
|---|---|---|
| 1–3. Paired EN/TH ambiguous and explicit cases on one fixture | Scenarios 14–15, fixture, and raw baseline/post-change runs above | Pass |
| 4. Review and narrow work do not become brainstorming | EN/TH Review and narrow-frontend outputs above | Pass |
| 5. Baseline metadata and raw output preserved | Version, tag, skill hashes, runner/model, prompts, harness, outputs, and limitations recorded here | Pass with repetition limit |
| 6. Core changes require more than the motivating report | Independent Commonroom EN/TH reproduction plus separate user-reported project context | Pass |
| 7. Gate remains conditional and classifies direction | Scoped `skills/gridgeist/SKILL.md` diff and explicit-control repair | Pass |
| 8. Behavioral, structural, repository, and diff checks | EN/TH regressions, browser fixture checks, validator, syntax check, and `git diff --check` | Pass |

## Repository verification

- `python scripts/validate_release.py` — passed: skill, plugin v1.1.0 metadata,
  bilingual docs, and contiguous bilingual evals aligned.
- `node --check evals/fixtures/direction-alignment/script.js` — passed.
- `git diff --check` — passed; only existing line-ending warnings were emitted.
- Scoped diff review confirmed no plugin manifest, marketplace ref, release tag,
  installation path, `design.md`, or `product.md` was added or changed.
- English and Thai Docs received the same one-sentence workflow update. The changelog
  records the behavior under Unreleased; no version bump or publication occurred.

## Limitations

- Model output is nondeterministic. One independent run per language and scenario was
  retained instead of the normal three-run convention to keep this lightweight; the
  explicit English control required and passed one focused rerun after repair.
- A full installed-plugin workspace-write baseline and a full-plugin read-only run
  exceeded 184 and 244 seconds respectively without returning a final response. The
  reproducible decision harness therefore isolated the v1.1.0 core skill and recorded
  behavioral—not implementation—results. The runner itself was confirmed healthy by
  a separate three-word isolation probe.
- Post-change tests validate the pre-edit decision behavior. They do not claim a full
  redesigned Commonroom implementation, usability research, accessibility
  conformance, or performance results.
- Release, marketplace update, Git tag, deployment, and post-release installation
  checks remain outside the user's current authorization.
- Cleanup removed the disposable evaluation copies except `en-s14-r1` and
  `en-s14-readonly-r1`; Windows retained directory handles after their timed-out CLI
  process trees were stopped. These remaining `C:\tmp` copies contain only the
  fictional fixture and can be removed after the session releases the handles.
