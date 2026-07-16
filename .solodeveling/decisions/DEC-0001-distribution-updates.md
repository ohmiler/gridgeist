---
solodeveling_schema: 1
---

# DEC-0001: Distribution and updates

- **Status:** Accepted
- **Decision:** Use the Codex Git marketplace as the primary Codex distribution channel, `npx skills` as the cross-agent channel, and manual copying only as a fallback.
- **Rationale:** Both primary channels retain source metadata and expose explicit update commands; manual copies cannot update reliably.
- **Consequences:** Every release must bump `.codex-plugin/plugin.json`, pin the marketplace entry to the release tag, publish bilingual update commands, and test reinstall behavior.
