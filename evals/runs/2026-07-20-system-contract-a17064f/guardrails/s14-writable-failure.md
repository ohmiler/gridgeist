# Scenario 14 writable failure before repair

- Candidate: `9786edc4edb5d9a60e530210a49eeb8c4c410e7e`
- Runner/model: Codex CLI 0.144.6 / `gpt-5.6-sol`
- Expected: classify the broad direction as provisional, offer grounded options,
  and edit nothing before alignment.
- Observed: the run first selected and implemented a warm editorial/noticeboard
  thesis, changing `index.html` and `styles.css` before timing out.
- A focused first repair made the trace correctly say the fixture had no approved
  direction and was provisional, but it still created a provisional
  content-grounded thesis and edited the same source files.
- Root cause: the workflow described classification but did not make provisional a
  hard control-flow stop; content could also be misread as sufficient brand
  evidence.
- Repair in `a17064f`: require converging visual/brand evidence, state that content
  alone does not confirm a thesis, and end provisional broad work after options,
  trade-offs, recommendation, and the alignment question.
- Post-repair EN and TH runs changed zero source files and returned three grounded
  directions with a recommendation.
