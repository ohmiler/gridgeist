---
solodeveling_schema: 1
---

# Risks

| Risk | Impact | Mitigation | Status |
|---|---|---|---|
| Marketplace tracks unreleased `main` | Users may install unstable or cache-colliding content | Pin plugin source to the release tag and bump manifest version | Open |
| Behavioral evals are aggregate and single-run | Apparent improvements may be nondeterministic | Run independent scenario-level evaluations and preserve artifacts | Open |
| Manual-copy installs have no update metadata | Users may remain on stale skill versions | Make plugin and `npx skills` primary; document manual replacement as fallback | Open |
| Version values drift across release files | Cache or release identity becomes ambiguous | Add automated version-alignment validation | Open |
| Untracked `.agents/skills/` enters public release accidentally | Repository gains an unintended third-party/local bundle | Exclude it from release staging unless separately authorized | Open |
