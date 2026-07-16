# Direction

**Thesis:** An account-data import workspace for operators, organized around a clear upload–validate–resolve–commit sequence, with restrained product styling and the import ledger itself—file, progress, row status, and recovery actions—as the dominant visual motif.

Preserve the existing CSV contract, validation rules, cancellation semantics, retry behavior, and partial-success behavior. Existing brand typography, palette, geometry, and voice should remain; because no product fixture was provided, the redesign must map the semantic roles below onto existing tokens rather than invent a new brand. Use a quiet grid: alignment should make the workflow legible, not turn it into technical decoration.

# Responsive implementation specification

Use one persistent import surface with three regions:

1. **Import header:** “Import account data,” concise CSV requirements, and a link to the current template or format documentation.
2. **Primary work area:** upload/drop target before selection; after selection, replace it with a file summary and validation/import progress. Do not stack a second generic card beneath it.
3. **Import ledger:** counts and row-level results grouped as `Ready`, `Needs attention`, and `Imported`, followed by a stable action bar.

On desktop (about 1024 px and wider), use a 12-column container: the work area spans 8 columns and a 4-column status rail holds totals, requirements, and recovery actions. Keep the action bar aligned with the work area. On tablet, use a single main column with the compact status summary immediately above the ledger. On mobile, reorder to file/status → next required action → row issues; make actions full-width when necessary, keep touch targets at least 44×44 px, and replace wide tables with row summaries that disclose field-level errors. Never hide failed rows behind horizontal scrolling.

Type roles should be limited to page heading, section heading, body, label, and tabular metadata. Use tabular numerals for counts and progress. Borders indicate stage boundaries and row status; color is supplementary to an icon and text label. Reserve motion for progress and state transitions, and replace it with immediate state changes under reduced-motion preferences.

The stable action bar changes by state but does not jump around: secondary action on the left (`Cancel` or `Choose another file`), primary action on the right (`Validate`, `Import valid rows`, `Retry`, or `Done`). Cancellation during validation or import opens a confirmation dialog that names the consequence, offers `Continue import` as the safe default, and restores focus to the invoking control when closed.

# State and behavior contract

| State | Primary presentation | Available behavior |
|---|---|---|
| Empty | Upload target, `Choose CSV` button, supported format/size requirements, and template link | Drag/drop and keyboard file picker; validation cannot start |
| Loading | Determinate progress when measurable, otherwise a named status such as “Validating rows”; retain filename and counts already known | `Cancel` remains available; prevent duplicate submission; announce meaningful progress without excessive live-region updates |
| Invalid file | File-level error beside the file summary: unsupported type, unreadable file, size limit, missing headers, or incompatible schema | Preserve the error text; offer `Choose another file`; do not show row actions for a file that could not be parsed |
| Row errors | Summary states exact valid/error counts; ledger identifies row number, field, value when safe to display, and a specific correction | Allow issue filtering and CSV error-report download if already supported; preserve valid rows; enable `Import valid rows` only when partial success is permitted |
| Disabled | Disabled controls retain their labels and have adjacent explanatory text, e.g. “Select a CSV to continue” or “No valid rows to import” | Do not rely on tooltip or color; do not make the whole workflow appear inactive when only one action is unavailable |
| Success | Confirmation names the imported count and destination; ledger remains available as evidence | Offer `Done` and the existing destination action; prevent accidental re-import of the same completed job |
| Partial success | Success is explicit but not absolute: “842 imported, 18 need attention”; imported and failed rows remain separately identifiable | Retry only failed rows, without duplicating successful rows; retain or export the error set; `Done` remains available |
| Interrupted | Persistent recovery panel says what stopped, what is known to have completed, and whether status is still being reconciled | `Retry` resumes/replays only where the backend contract guarantees idempotency; otherwise re-check status first. Keep `Cancel` only if the job is still cancellable |
| Cancelled | Neutral terminal message distinguishes “cancelled before import” from “cancelled after N rows”; no success styling | Allow a new file or a safe retry according to existing semantics; never imply rollback unless the product actually provides it |

For retry, carry forward the selected file and validated results when the current system safely supports that; otherwise explain why reselection is required. For partial success, use immutable row/job identifiers or the existing idempotency mechanism so retry cannot create duplicate accounts. Do not promise rollback, resume, or downloadable reports unless those capabilities already exist.

Accessibility requirements: use a labeled file input with the drop target as an enhancement; put file-level errors in the input’s description; link the error summary to affected rows/fields; move focus to the summary after validation fails while preserving a logical return path; use `aria-live="polite"` for stage changes and a progress element for measurable work; keep row status understandable without color; ensure dialogs support Escape, focus containment, and focus restoration. Preserve entered or parsed data after recoverable errors.

# Verification

I verified only that this specification explicitly preserves CSV upload, validation, cancellation, retry, and partial success, and that it covers empty, loading, invalid-file, row-error, disabled, success, interrupted, plus the consequential cancelled and partial-success states. I also checked the proposal against the supplied Gridgeist design-language and review-checklist guidance for transactional workflows, responsive recomposition, recovery, semantic state cues, focus behavior, and truthful reporting.

I did **not** inspect an existing product UI or brand system, edit implementation files, render any viewport, exercise keyboard/touch flows, upload a CSV, run automated checks, or verify backend cancellation/idempotency semantics. Therefore this is a redesign specification, not an implemented or rendered result. The stated desktop, tablet, mobile, accessibility, retry, and interruption behavior remains to be validated against the real interface and import API.
