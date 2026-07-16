# Direction

**Thesis:** An evidence-led import workspace for people moving account data, organized as a clear upload → validate → resolve → commit sequence, with restrained brand expression and the file’s real row-level status as the product-native motif.

Preserve the existing CSV contract, upload action, validation rules, cancellation, retry, and partial-success semantics. This proposal does not invent new parsing rules or redefine when data is committed. Existing brand typography, palette, voice, and controls should be reused; without a fixture, those signals cannot be specified honestly. The grid should remain quiet: it aligns the workflow and row evidence without turning the screen into decorative technical chrome.

# Implementation blueprint

Use one dominant import panel rather than a dashboard of equal cards. Its stable anatomy is:

1. **Orientation:** “Import account data,” a short statement of accepted CSV requirements, and a link to the existing template/help.
2. **Progress rail:** Upload, Validate, Import, Results. It describes progress but does not behave like free navigation when later steps are unavailable.
3. **Working area:** the drop zone before selection; then a persistent file strip showing name, size, and current status. Replacing or removing the file is explicit.
4. **Evidence area:** validation summary followed by the row-error table. Counts—not decoration—carry the hierarchy.
5. **Stable action bar:** contextual primary action on the right and safe secondary action on the left. Cancellation remains reachable while work is active.

The row-error table should contain row number, account identifier or closest safe locator, field, issue, and suggested correction. Never expose sensitive values that the current product masks. Errors must be announced in text and with icons, not color alone. Preserve valid input after validation fails.

## State contract

| State | Main surface | Actions and recovery |
|---|---|---|
| Empty | Labeled CSV drop zone plus **Choose CSV** button; accepted type and size guidance adjacent | Import action disabled with nearby text: “Choose a CSV to continue.” Disabled styling is not the only explanation. |
| Loading | File strip stays visible; determinate progress when measurable, otherwise a labeled status such as “Uploading…” or “Validating 240 rows…” | **Cancel** remains enabled. File replacement and import are disabled to prevent competing operations. Status uses `aria-live`; reduced motion gets a static indicator. |
| Invalid file | Inline error directly below the file strip: unsupported type, unreadable file, oversize file, or missing required columns, using the parser’s real reason | **Choose another file** is primary. Keep **Cancel** available. Do not show a row table when row parsing never began. |
| Row errors | Summary splits “ready” and “needs attention”; error rows appear in a filterable table with an error-only default view | If partial import is allowed, primary action is explicit: **Import 184 valid rows**; secondary action is **Replace CSV**. Explain that 16 rows will not import. If policy forbids partial import, disable import and say exactly what must be fixed. |
| Disabled | A control is disabled only while prerequisites are absent or an operation conflicts; the reason is visible next to it | Do not rely on tooltip-only explanations. Disabled controls remain visually legible and are omitted from misleading progress announcements. |
| Success | Result headline reports exact counts, followed by imported, skipped, and failed groups; no confetti or invented outcome claims | Offer **View imported accounts** as primary and **Import another CSV** as secondary. Preserve a downloadable error report only if that behavior already exists. |
| Partial success | Treat as a first-class result, not generic success: “184 accounts imported; 16 rows need attention” | **Download errors** or equivalent existing recovery action, then **Retry failed rows** if the backend supports retrying only failures. Never rerun successful rows implicitly. |
| Interrupted | Persistent neutral-warning panel: “Import stopped before completion,” with last confirmed counts and whether processing state is known | **Retry import** must state its scope. If idempotency is not guaranteed, require a fresh status check before retry and warn against duplicates. Keep **Cancel/Leave** available. |

Cancellation should be proportional to the phase. Before commit, cancel immediately and return to the selected-file state. During import, use the product’s actual cancellation semantics: if processed rows cannot be rolled back, say so before confirmation and report confirmed results afterward. Never imply cancellation reverses already imported rows unless the system guarantees it.

Retry should retain the selected file and validation evidence when safe. Invalid-file retry means replacement; transient upload or validation retry reuses the same file; partial-success retry targets failed rows only when supported. These distinct labels prevent accidental duplicate imports.

## Responsive and interaction behavior

At desktop widths, use a two-track evidence layout after validation: summary and actions in a narrow track, row evidence in the wide track. Before validation, keep the working area centered at a readable measure rather than filling empty space.

At approximately 768 px, place the summary above the table and keep the action bar sticky only if it does not obscure errors. At approximately 360 px, recompose the table into row disclosure items headed by row number and identifier; do not squeeze columns. Put the primary action full-width after the current status, keep Cancel visually secondary but reachable, and maintain at least touch-sized targets.

Use semantic headings, a labeled file input, real buttons, table markup on wide screens, logical focus order, visible focus, and an error summary that moves focus only after a user-triggered validation attempt. On cancellation dialogs, Escape closes and focus returns to the invoking control. Status announcements should be concise and should not repeat on every progress tick.

# Verification

I verified only that this specification explicitly covers the requested behaviors and states: CSV upload, validation, cancellation, retry, partial success, loading, empty, invalid-file, row-error, disabled, success, and interrupted handling. I also checked the proposal against the Gridgeist state/recovery, responsive, and accessibility review criteria at a design-specification level.

I did **not** inspect or change an implementation, render any viewport, exercise a browser flow, test keyboard or screen-reader behavior, run automated checks, or verify backend cancellation, idempotency, retry, validation, and partial-import semantics. Those remain implementation-dependent gaps; existing brand signals and exact parser copy also remain unverified because no fixture was provided.
