# Agent-neutral 60-second Quickstart Implementation Plan

**Goal:** Add equivalent English and Thai opening Quickstarts that let a first-time user install and invoke Gridgeist without assuming a specific agent product.

**Approach:** Modify only the two README files. Insert a compact three-step section after each opening description, retain all detailed installation and usage material, then validate structure, language parity, UTF-8 content, Markdown fences, and the repository diff.

**Files:**

- Modify: `README.md`
- Modify: `README.th.md`

---

### Task 1: Add the English Quickstart

- [ ] Insert `## 60-second Quickstart` after the opening description in `README.md`.
- [ ] Include clone, inner-directory copy, session restart, and a review-first English prompt.
- [ ] State that the skills-directory location varies and that `$gridgeist` can be used where explicit invocation is supported.
- [ ] Confirm the existing detailed installation and example-prompt sections remain present.

### Task 2: Add the Thai Quickstart

- [ ] Insert `## เริ่มใช้ใน 60 วินาที` after the opening description in `README.th.md`.
- [ ] Mirror the English steps and caveats in natural Thai.
- [ ] Provide an equivalent review-first Thai prompt.
- [ ] Confirm the existing detailed Thai installation and usage sections remain present.

### Task 3: Validate and publish

- [ ] Verify each README contains exactly one new Quickstart heading and matching three-step structure.
- [ ] Verify required detailed sections, links, code fences, and UTF-8 Thai text remain intact.
- [ ] Run `git diff --check` and inspect the final diff.
- [ ] Commit the README changes as `docs: add agent-neutral quickstart`.
- [ ] Push `main` and verify local and remote commit hashes match.
