---
solodeveling_schema: 1
---

# Risks

| Risk | Impact | Mitigation | Status |
|---|---|---|---|
| Marketplace tracks unreleased `main` | Users may install unstable or cache-colliding content | Pin plugin source to the release tag and bump manifest version | Open |
| Behavioral evals do not yet execute implementation fixtures | Strong reasoning may not generalize to rendered, interactive output | Run independent executable fixtures with browser, interaction, state, and project evidence | Open |
| External user comprehension is unmeasured | Instructions may be clear to the authoring agent but confusing or overbearing in other projects | Collect structured feedback from 3–5 external projects or users before revising the core skill | Open |
| Manual-copy installs have no update metadata | Users may remain on stale skill versions | Make plugin and `npx skills` primary; document manual replacement as fallback | Open |
| Version values drift across release files | Cache or release identity becomes ambiguous | Add automated version-alignment validation | Open |
| Untracked `.agents/skills/` enters public release accidentally | Repository gains an unintended third-party/local bundle | Exclude it from release staging unless separately authorized | Open |
| Showcase HTML and cached assets drift across deployments | Returning browsers may combine different interface revisions | Version changed showcase asset URLs and verify the linked public route after deployment | Controlled |
