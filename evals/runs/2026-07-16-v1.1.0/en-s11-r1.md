# Direction

**Thesis:** A touch-first drawing studio for children aged 6–10, organized around one generous canvas, warm tactile controls, and the child’s own marks as the dominant visual material.

Call the fictional app **Scribble Patch**. The structure should be quiet and nearly invisible: a compact tool shelf surrounds the canvas, but the artwork always carries the most visual weight. Use a warm off-white workspace, deep ink text, and a palette of saturated crayon-like colors. Softly squared controls and a subtle paper texture can make the tool feel playful without turning every element into a card.

Preserve these non-negotiable constraints:

- No account, sign-in, profile, name prompt, upload, sharing, camera, analytics, advertising, or personal-data collection.
- The app works entirely in the browser on the current device. A drawing remains in memory during the session unless the child explicitly exports it.
- Export is local only. Do not imply cloud backup or recovery after the tab closes.
- Do not claim COPPA compliance, child testing, accessibility, safety, or research findings without corresponding evidence.

# Responsive implementation blueprint

## Core composition

The canvas fills the center of the screen and begins blank, with the friendly prompt “Draw anything!” shown outside the drawable area. A top bar contains the Scribble Patch wordmark, undo, redo, and a clearly labeled **Save picture** button. A bottom tool shelf contains color and brush size. **Clear** sits apart at the far end because it is destructive.

Use a restrained token system:

- Color: `paper`, `ink`, `tool-surface`, `focus`, `danger`, plus named drawing colors. Text and control states must not rely on color alone.
- Spacing: 4, 8, 12, 16, 24, and 32 px.
- Touch targets: at least 48 × 48 px; make primary tools 56 × 56 px where space allows, with at least 8 px between targets.
- Shape: 14 px corners for tool groups, 10 px for controls, and a thin shadow only where it helps distinguish the canvas from the workspace.
- Type: a friendly rounded display face for the short wordmark and headings; a highly legible sans serif for every control label. Keep labels at 16 px or larger.

## Color

Show ten 48 px circular swatches: black, brown, red, orange, yellow, green, blue, purple, pink, and white. Give every swatch an accessible name such as “Blue”; expose that name to assistive technology and in a small tooltip for mouse users. The selected color gets both a thick ink outline and a check mark, so selection never depends on color alone. White receives a checker or contrasting ring so it remains visible.

Place the current color first in the group with the label **Color**. Avoid a complex color picker in the primary flow; the fixed palette is quicker to scan and less likely to cover the canvas.

## Brush size

Offer four choices labeled **Tiny**, **Small**, **Big**, and **Huge**, represented by progressively larger dots. Each is a 56 px button with its text available to screen readers and in a visible label beneath or beside the dot. The selected size uses a strong outline plus a check mark. Start on **Small**, approximately 8 CSS px, with the other sizes around 3, 18, and 34 px. Scale strokes in canvas coordinates so changing viewport density does not unexpectedly change the saved result.

## Drawing

Support finger, stylus, and mouse through pointer events. Set `touch-action: none` only on the drawable canvas so page controls can still scroll normally. Draw a short dot on tap and a continuous, round-capped stroke on drag. Capture the active pointer so a stroke does not break when the finger briefly leaves the canvas.

Keep color and size fixed for the duration of each stroke. Ignore a second simultaneous pointer rather than producing accidental marks. Give the canvas a visible focus outline and a concise accessible label such as “Drawing canvas.” Because freehand canvas drawing is inherently pointer-led, all toolbar actions must still be keyboard operable; do not claim that this alone makes the drawing experience fully accessible.

## Undo and redo

Use separate 56 px buttons with both icons and the visible labels **Undo** and **Redo**. One press changes one complete stroke or one clear action. Disable Undo when history is empty and Redo when there is nothing to restore; disabled controls remain visible and explain their state through native semantics, reduced contrast, and an unchanged layout.

After an undo, making a new stroke clears the redo branch. Keep a bounded in-memory history—for example, the latest 50 actions—and do not send or persist it anywhere.

## Clear

Label the action **Clear** and pair it with a simple eraser or trash icon, using a restrained danger color. On activation, open a bottom sheet on touch devices or a centered dialog on larger screens:

> Clear the whole picture?

Actions are **Keep drawing** (primary focus) and **Clear picture** (destructive). Escape and tapping the backdrop cancel; closing restores focus to Clear. Clearing creates one undoable history action, and a brief message says “Picture cleared — Undo.” If the canvas is already empty, disable Clear.

## Local export

The primary action is **Save picture**. Activating it opens a compact local-export sheet with:

- A preview thumbnail generated on-device.
- Format: **PNG** selected by default; optionally **JPG** with a plain note that it removes transparency.
- Background: **Paper** or **Transparent** for PNG.
- A primary **Save to this device** button and **Keep drawing** to cancel.

Generate the file entirely in the browser using the canvas API. Use a neutral filename such as `scribble-patch.png`; do not ask for the child’s name. Prefer the browser’s native save picker when available, otherwise trigger a normal local download. Revoke temporary object URLs immediately after use. Show “Saved to your device” only after the browser confirms or initiates the save; show “Couldn’t save. Try again.” if generation fails. Never show share, upload, gallery-sync, or camera actions.

## Responsive behavior

- **Wide, 1024 px and above:** top actions remain in one row; a 112 px left shelf holds color and brush controls; the canvas occupies the remaining height and width. Clear stays visually separated at the shelf bottom.
- **Medium, 600–1023 px:** colors become a two-row shelf below the canvas; brush size, undo, and redo stay in a stable top row. The canvas remains the largest region rather than being squeezed by side chrome.
- **Small, below 600 px:** use a compact top bar with Undo, Redo, and Save picture; the canvas fills the space between bars. A bottom shelf has two large tabs, **Color** and **Brush**, opening a single-row horizontally scrollable tray with visible edge fade. Clear remains a labeled button beside those tabs, not hidden in a menu. Account for safe-area insets and allow the surrounding page—not the canvas—to scroll when needed.
- **Landscape phone:** collapse the wordmark, move the tool shelf to the short edge, and preserve a usable canvas rather than retaining the portrait stack.

At every size, keep the canvas aspect flexible, prevent toolbar overlap, and preserve at least 48 px targets at 200% zoom. Do not reduce controls merely to keep every swatch visible at once.

## States and feedback

- **Empty:** blank canvas; Undo, Redo, and Clear disabled; “Draw anything!” nearby.
- **Drawing:** active swatch and brush remain visibly selected; the stroke follows the pointer without ambient animation.
- **Undo/redo:** controls update immediately and an unobtrusive status region announces “Undid stroke” or “Redid stroke.”
- **Clear confirmation:** focus is trapped within the dialog; cancellation preserves the drawing.
- **Exporting:** Save picture shows a short progress state and is disabled against duplicate activation.
- **Export success:** announce “Saved to your device” without implying cloud storage.
- **Export error:** preserve the drawing and offer **Try again**.
- **Reduced motion:** replace tray slides and status transitions with immediate state changes.

Use semantic buttons, visible `:focus-visible` rings, sufficient text and control contrast, and a polite live region for action feedback. Icons always accompany labels rather than replacing them.

# Verification

This is a design specification only: no repository fixture was supplied, no files were implemented, and no interface was rendered or exercised. Consequently, no viewport, pointer flow, keyboard flow, export behavior, performance, accessibility, privacy behavior, or child usability has been verified.

Implementation should later be inspected at approximately 360, 768, 1280, and 1600 px, plus a landscape phone. Exercise finger, stylus, mouse, and keyboard toolbar operation; drawing continuity; multi-touch rejection; history branching; empty and disabled states; clear cancellation and recovery; PNG/JPG export success and failure; focus restoration; 200% zoom; high contrast; and reduced motion. Confirm through network inspection that drawing, history, and export generate no requests. Any usability conclusions require appropriately conducted research; they must not be inferred from this specification.
