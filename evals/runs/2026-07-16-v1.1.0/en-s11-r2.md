# Direction

**Thesis:** A touch-first drawing studio for children aged 6–10, organized around one generous canvas, friendly tool groups, and immediate local feedback from every mark.

The canvas is the visual lead, not a dashboard of cards. Use a warm off-white app background, a clean white drawing sheet, a sturdy rounded sans-serif typeface, and playful color only where it communicates a tool or state. Keep the underlying grid quiet. Controls should feel tactile through clear outlines, pressed states, and small causal animations, while avoiding toy-like decoration that competes with drawing.

Preserve these constraints as product behavior:

- No sign-in, profile, account, upload, sharing, camera, microphone, analytics, advertising, trackers, or personal-data fields.
- Drawing data remains in page memory. It leaves the page only when the child or caregiver explicitly saves a PNG to the device.
- Use bundled assets and system or locally hosted fonts; the drawing flow should make no third-party or telemetry requests.
- A persistent, plain-language note says: **“Your picture stays on this device.”** Do not claim COPPA compliance, safety certification, or research with children.

# Implementation specification

## Composition

Use three task-centered zones:

1. A compact top bar with the product name **Doodle Garden**, the privacy note, and the primary **Save picture** action.
2. The dominant canvas, framed as a sheet of paper with no controls floating over drawable space.
3. A stable tool dock containing **Colors**, **Brush size**, **Undo**, **Redo**, and **Clear**.

Every interactive target should be at least 52×52 px, with at least 8 px between targets. Labels remain visible; do not rely on icons, color, or hover alone. Use a strong focus outline and a pressed state that changes both shape/outline and color.

## Colors

Show eight large swatches in a single named group: Charcoal `#263238`, Blue `#2D7FF9`, Red `#E5484D`, Yellow `#F4C542`, Green `#2EAD66`, Purple `#8B5CF6`, Orange `#F28C28`, and Pink `#EC66A1`.

Each swatch is a real button with an accessible name such as **“Blue color”**. Selection uses a thick outer ring plus a checkmark, not color alone. Charcoal is selected initially. A live preview beside the group shows the current color and brush width together.

## Brush size

Prefer four direct choices over a precision slider:

- **Tiny** — 4 px
- **Small** — 10 px
- **Big** — 20 px
- **Huge** — 36 px

Each button displays a proportionally sized dot and its word label. **Small** is the default. Selection uses the same ring/check treatment as color. On very small screens, the four options may scroll horizontally inside their own labeled region, but the page itself must not scroll sideways.

## Drawing behavior

Use Pointer Events so mouse, pen, and touch share one stroke model. A primary pointer begins a stroke on contact, adds smooth rounded segments while moving, and commits one history entry on release or cancellation. Apply `touch-action: none` only to the canvas so a finger draws there while the rest of the page can still scroll. Ignore additional simultaneous contacts to reduce accidental marks.

Give immediate visual feedback: the mark follows the pointer, and the current tool preview updates as soon as color or size changes. Preserve the canvas bitmap when controls reflow or the viewport resizes. If an unsaved drawing exists, warn before a refresh or navigation would discard it; do not silently persist it or send it anywhere.

## Undo and redo

Undo and redo operate one complete stroke at a time. They are adjacent, labeled buttons with distinct curved-arrow icons. Both begin disabled; the disabled state uses reduced contrast, an unchanged cursor, and `aria-disabled` or the native `disabled` attribute. After undo, redo becomes available. Starting a new stroke after undo clears the redo branch. Support `Ctrl/Cmd+Z` for undo and `Ctrl/Cmd+Shift+Z` for redo without making shortcuts necessary.

Announce changes briefly in a polite status region: **“Last line undone”** or **“Line restored.”** Avoid audio and celebratory motion.

## Clear

**Clear** is visually separated from undo/redo and uses a warning treatment, not the primary-action color. It is disabled on an empty canvas. Activating it opens a focused confirmation sheet:

- Heading: **“Clear the whole picture?”**
- Explanation: **“All the lines will disappear.”**
- Safe action: **Keep drawing**
- Destructive action: **Clear picture**

Escape and **Keep drawing** close the sheet and return focus to Clear. Confirming clear removes the artwork, closes the sheet, and shows **“Picture cleared — Undo”**; Clear itself is recorded as one reversible history action. This provides recovery without making the child interpret a complex dialog.

## Local export

**Save picture** is the only emphasized action outside the canvas. It is disabled while the canvas is empty and accompanied by **“Draw something first”** when relevant. On activation:

1. Render the current canvas to a PNG locally with `canvas.toBlob()`.
2. Create a temporary object URL and trigger a browser download named `my-drawing-YYYY-MM-DD-HHMM.png`.
3. Revoke the object URL after the download begins.
4. Show **“Download started”** in the status region.

There is no server call, upload fallback, share button, or gallery. If PNG creation fails, keep the drawing intact and show **“Couldn’t save the picture. Try again.”** with a **Try again** button. On browsers that open the image instead of downloading it, provide platform-neutral guidance: **“Use your browser’s save option to keep this picture on this device.”**

## Responsive behavior

- **Wide, 1024 px and above:** Center the canvas as the largest region. Put color and brush controls in a left rail; place history and Clear in a compact right rail. Keep both rails secondary and align them to the canvas edge.
- **Medium, 600–1023 px:** Move tools into a two-row dock below the canvas: color and size first, then history/Clear. Keep Save in the top bar. The canvas uses the available width and height without being covered by the dock.
- **Small, 360–599 px:** Recompose to a short header, maximum-height canvas, and bottom tool dock. Show the selected color and size in the collapsed dock; tapping **Colors** or **Brush** opens a bottom sheet with 52 px targets. Keep Undo, Redo, and Clear directly available. Respect safe-area insets and never place controls over the drawing.
- **Landscape on short screens:** Use compact left and right tool strips around the canvas, reducing labels only where an accessible name and persistent tooltip remain. Do not shrink touch targets.

## State and accessibility contract

Specify and implement empty, drawing, selected, pressed, focus-visible, disabled, clear-confirmation, cleared/recoverable, export-in-progress, export-success, and export-error states. Use semantic buttons and grouped labels, logical keyboard order, visible focus, and live-region feedback. Essential state changes must remain immediate under `prefers-reduced-motion`; any optional press or sheet transition should reduce to a simple opacity change. Test UI text at 200% zoom and ensure color names and action labels survive localization without covering the canvas.

# Verification

No repository fixture, implementation, or rendered interface was provided, so nothing has been implemented or visually verified. Before calling the redesign complete, render at approximately 360, 768, 1280, and 1600 px and exercise touch, pen, mouse, and keyboard flows for drawing, every color and size, undo/redo branching, clear/cancel/undo-clear, successful export, failed export, rotation, zoom, and reduced motion. Also inspect network activity to confirm that drawing and export create no requests. These checks would establish technical behavior only; they would not constitute COPPA compliance, a privacy audit, accessibility certification, or evidence from children.
