# Readable Container Implementation Plan

**Goal:** Center and constrain readable content across the English, Thai, and examples pages while preserving full-bleed backgrounds and interactive specimens.

**Architecture:** Define shared gutter and width tokens in `site/styles.css`, then constrain existing top-level regions with `width`, `max-width`, and auto margins. Use page-specific styles only where the Thai guide and examples require different composition. Avoid HTML changes unless selector-based containment proves insufficient.

**Tech Stack:** Static HTML, CSS, JavaScript, GitHub Pages

---

### Task 1: Shared container foundation

**Files:**
- Modify: `site/styles.css`

- [ ] Add `--page-gutter`, `--container-wide`, and `--container-copy` tokens.
- [ ] Replace repeated viewport padding with centered wide-container geometry on the header, hero, content sections, install block, and footer.
- [ ] Keep full-bleed section backgrounds and grid effects intact through pseudo-elements or section-level backgrounds.
- [ ] Preserve the existing 16px mobile gutter at the current 800px breakpoint.

### Task 2: Localized and gallery containment

**Files:**
- Modify: `site/th/thai.css`
- Modify: `site/examples/examples.css`

- [ ] Apply the shared wide width to Thai-only top-level layouts and a tighter readable measure to Thai prose.
- [ ] Constrain gallery hero content, specimen navigation, case studies, and CTA without shrinking the interactive stage below its useful presentation width.
- [ ] Verify page-specific mobile rules continue to override desktop composition correctly.

### Task 3: Verification and delivery

**Files:**
- Verify: `site/index.html`
- Verify: `site/th/index.html`
- Verify: `site/examples/index.html`

- [ ] Run static checks for syntax markers, missing files, and whitespace errors.
- [ ] Render all three pages at desktop and mobile widths and inspect screenshots.
- [ ] Check for horizontal overflow and verify interactive Before/After and copy controls.
- [ ] Review the final diff, commit the implementation, push `main`, and confirm the GitHub Pages workflow.
