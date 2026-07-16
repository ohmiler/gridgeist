## Direction

**Thesis:** An account administrator importing customer data moves through a quiet, task-led sequence where the CSV itself becomes a visible import ledger—file, validation, row outcomes, and recovery—expressed with the product’s existing type, color, and control language.

Preserve CSV upload, validation, cancellation, retry, and partial-success behavior. Keep valid rows and the selected file intact when errors occur; never make retry mean “start over.” Because no existing interface or brand fixture was supplied, retain the product’s current tokens and voice rather than inventing a palette, typeface, radius system, or marketing claims. The grid stays quiet: it aligns the workflow but does not become decoration.

## Responsive implementation specification

Use one dominant workspace with three persistent regions:

1. **Context header:** “Import account data,” a concise CSV requirements link, and a step/status label such as “Reviewing 248 rows.”
2. **Import workspace:** the upload target before selection; after selection, a file summary and row ledger become the visual lead. The ledger columns are row number, account identifier, validation result, and recovery action. Filters for All, Ready, and Needs attention show counts and are real buttons or tabs, not decorative pills.
3. **Stable action bar:** the current primary action at the end (“Validate file,” “Import 231 valid rows,” or “Retry 17 rows”), a secondary Cancel action, and explicit consequence copy. Actions should not jump position as validation messages appear.

On desktop (about 1280 px and above), use a 12-track container: context occupies three tracks and the ledger nine, with the action bar aligned to the ledger. At tablet widths (about 768 px), move context above the ledger and keep row filters and actions in a wrapping two-line toolbar. At mobile widths (about 360 px), replace the wide table with a prioritized row list: status and account identifier first, row number and error detail second. Put the primary action in a non-obscuring bottom action region, keep Cancel adjacent, and expose row repair without horizontal scrolling. At every width, long filenames and identifiers wrap or truncate with an accessible full value; dynamic counts must not cause control reordering.

Use existing design tokens for color and geometry. Assign semantic roles for neutral progress, warning, error, success, focus, and disabled states. Pair every color with an icon and text label. Borders explain adjacency between the file summary, filters, and ledger; elevation is reserved for a sticky action region only if needed. Motion is limited to causal progress and row-status changes, and reduced-motion mode swaps transitions for immediate state updates.

### State and behavior model

| State | Interface treatment | Available behavior |
|---|---|---|
| Empty | A labeled file input is dominant, with “Choose CSV” and drag-and-drop as equivalent paths. Show accepted extension/size/required-column guidance before selection. | Select a `.csv`; requirements remain reachable by keyboard and touch. |
| Loading | Keep filename, size, progress text, and a determinate indicator when progress is known; otherwise use restrained indeterminate feedback. Announce phase changes (“Uploading,” “Validating rows”) through a polite live region. | **Cancel** remains enabled. Prevent duplicate submission; do not replace the whole page with a spinner. |
| Invalid file | Show a file-level error beside the file summary, e.g. unsupported type, unreadable encoding, excessive size, or missing required columns. Include specific recovery guidance without asserting a cause the validator cannot know. | **Choose another CSV** is primary; keep the rejected filename visible for context. |
| Row errors | Preserve the parsed file and valid rows. Show total, ready, and error counts; lead each invalid row with its row number, field, plain-language reason, and expected format. Filters retain context. | Allow corrected-file replacement and, if the product already supports inline correction, edit only the failing value. **Import valid rows** must state the exact count and make the excluded count explicit. |
| Disabled | Disable Import when no file exists, validation is running, zero rows are valid, or another import request is pending. Explain the reason next to the control and expose it programmatically; a disabled button alone is insufficient. | Cancel or file replacement remains available whenever safe. Do not use disabled styling for permission denial—show that as a distinct message. |
| Success | Confirm imported, skipped, and failed counts separately. For complete success, say “248 accounts imported.” For partial success, say “231 imported; 17 need attention,” and retain the failed-row ledger. | Offer **View imported accounts** and **Retry 17 rows** (or download an error CSV if that behavior already exists). Never collapse partial success into a generic success banner. |
| Interrupted | Preserve the selected file identity and last confirmed server result. State whether the operation was cancelled, connection was lost, or status is unknown. If commit status is unknown, say so and reconcile before allowing a duplicate import. | **Resume status check** or **Retry** according to backend guarantees; keep **Cancel** only while work is actually cancellable. Retry must be idempotent or use an import job key. |

The default selected-file state sits between Empty and Loading: show file metadata, replacement control, validation summary placeholder, and one clear “Validate file” action. Confirmation is proportional to risk: cancelling before any rows are committed can be immediate; cancelling an active import should explain whether completed rows remain and require confirmation. After any modal confirmation, Escape closes it and focus returns to the invoking control.

### Interaction and accessibility contract

- Use semantic headings, a native labeled file input, real buttons, and a table only when the layout remains tabular; the mobile row list should preserve the same accessible data relationships.
- Move focus to the file-level error heading after invalid submission, and to the results summary after validation/import. Do not move focus for background progress updates.
- Provide visible focus, logical keyboard order, 44 px-equivalent touch targets, non-color status cues, and live-region announcements that are concise enough not to repeat on every row update.
- Preserve privacy: do not preview unnecessary account fields, place raw customer data in telemetry, or expose row details in globally persistent notifications.
- Keep retry scoped to failed/unconfirmed rows and cancellation scoped to the current import job. Server responses—not optimistic animation—determine final counts.

## Verification

This is a read-only redesign specification, not an implemented or rendered interface. I verified the specification against the Gridgeist design-language and review-checklist requirements: it defines one task-led thesis; preserves CSV upload, validation, cancellation, retry, and partial success; covers loading, empty, invalid-file, row-error, disabled, success, and interrupted states; specifies desktop, tablet, and mobile recomposition; and includes keyboard, focus, reduced-motion, recovery, privacy, and non-color status requirements.

I did **not** inspect an existing product UI, source code, brand tokens, validator/API semantics, or backend idempotency guarantees. I did **not** render 360/768/1280/1600 px viewports, exercise pointer/touch/keyboard flows, run automated checks, or verify accessibility, cancellation semantics, retry safety, data integrity, or usability with users. Those remain implementation and product-domain verification gaps.
