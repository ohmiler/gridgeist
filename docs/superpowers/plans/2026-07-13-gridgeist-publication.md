# Gridgeist Publication Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a documented, installable, and manually evaluable Gridgeist agent skill to `ohmiler/gridgeist`.

**Architecture:** Human-facing project documentation and evaluation fixtures live at the repository root. The installable artifact remains self-contained in `gridgeist/`, with agent UI metadata and progressively disclosed references.

**Tech Stack:** Markdown, YAML, Git, GitHub CLI, Codex skill validator when Python is available

---

### Task 1: Add repository-level publication files

**Files:**
- Create: `README.md`
- Create: `LICENSE`
- Create: `.gitignore`

- [ ] **Step 1: Record the precondition**

Run `Test-Path README.md; Test-Path LICENSE; Test-Path .gitignore`.
Expected: all three values are `False`.

- [ ] **Step 2: Create the public documentation**

Write a concise README with the purpose, installation methods, example prompts,
layout, limitations, validation, and contribution instructions. Add the standard
MIT license using copyright `2026 Miler`. Ignore OS/editor noise only.

- [ ] **Step 3: Verify documentation structure**

Run searches for the README headings, MIT grant text, and ignored filenames.
Expected: each required section and text fragment is found once.

### Task 2: Normalize installable skill metadata

**Files:**
- Modify: `gridgeist/agents/openai.yaml`

- [ ] **Step 1: Capture the unsupported metadata condition**

Run `rg -n "products:|chatgpt|codex|api|atlas" gridgeist/agents/openai.yaml`.
Expected: matches demonstrate the product policy currently present.

- [ ] **Step 2: Apply documented metadata fields**

Quote all interface strings, keep a single-line default prompt containing
`$gridgeist`, retain `policy.allow_implicit_invocation: true`, and remove the
unsupported `policy.products` list.

- [ ] **Step 3: Verify metadata invariants**

Check that `$gridgeist` and implicit invocation remain, product entries are
absent, and the short description remains between 25 and 64 characters.

### Task 3: Add repeatable behavioral evaluation prompts

**Files:**
- Create: `evals/prompts.md`

- [ ] **Step 1: Record the missing evaluation fixture**

Run `Test-Path evals/prompts.md`.
Expected: `False`.

- [ ] **Step 2: Create the evaluation suite**

Document success criteria and prompts for create, redesign, review, responsive,
accessibility, conflicting direction, product-specific evidence, and a negative
non-web trigger. Include a result table for repeat runs without claiming model
determinism.

- [ ] **Step 3: Verify scenario coverage**

Search the fixture for all eight scenario labels and the result table headings.
Expected: every required scenario is present.

### Task 4: Validate the complete publication artifact

**Files:**
- Verify: `README.md`
- Verify: `LICENSE`
- Verify: `.gitignore`
- Verify: `evals/prompts.md`
- Verify: `gridgeist/SKILL.md`
- Verify: `gridgeist/agents/openai.yaml`
- Verify: `gridgeist/references/*.md`

- [ ] **Step 1: Run the official validator**

Run `python C:\Users\Miler\.codex\skills\.system\skill-creator\scripts\quick_validate.py .\gridgeist`.
Expected: validator success. If no Python runtime exists, record the exact
environment limitation and continue with explicit structural checks.

- [ ] **Step 2: Verify internal links and encoding**

Confirm each relative Markdown link in `gridgeist/SKILL.md` resolves and scan
tracked text files for replacement characters or merge markers.
Expected: no missing targets, replacement characters, or merge markers.

- [ ] **Step 3: Review the complete diff**

Run `git diff --check`, `git diff --stat`, and `git status --short`.
Expected: no whitespace errors; only intended publication files are changed.

### Task 5: Commit and publish

**Files:**
- Commit all files created or modified in Tasks 1-4

- [ ] **Step 1: Commit the publication artifact**

Run `git add .` followed by
`git commit -m "feat: publish Gridgeist agent skill"`.
Expected: one commit containing the skill, README, license, evaluations, and
metadata cleanup.

- [ ] **Step 2: Push main**

Run `git push -u origin main`.
Expected: the remote branch is created and tracks `origin/main`.

- [ ] **Step 3: Verify GitHub state**

Run `gh repo view ohmiler/gridgeist --json defaultBranchRef,url` and
`git status --short --branch`.
Expected: GitHub reports `main` as the default branch and the local tree is
clean and tracking `origin/main`.
