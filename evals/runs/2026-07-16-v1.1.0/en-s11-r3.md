# Direction

**Thesis:** A touch-first drawing studio for children aged 6–10, organized around one generous canvas, warm tactile controls, and immediate marks-as-feedback.

Use the fictional name **Scribble Garden**. The canvas—not navigation or decoration—is the dominant surface. Keep the alignment grid invisible and use it only to maintain predictable tool placement. The visual language should feel like sturdy art supplies: warm paper, dark ink, saturated crayon colors, simple shapes, and restrained depth. Avoid technical chrome, gamified rewards, mascot interruptions, and generic card grids.

Preserve these non-negotiable constraints: no account, cloud save, upload, sharing endpoint, camera, analytics, advertising, trackers, or collection of names or other personal data. Drawing state remains in memory for the current session; export creates a file locally on the device. Describe this plainly as “Private on this device.” Do not label the product COPPA-compliant or imply that children tested it.

# Responsive implementation specification

## Core composition

- A 56 px top bar contains the Scribble Garden wordmark, a compact “Private on this device” indicator, and no profile, menu, or account affordance.
- The drawing canvas fills all remaining space above the tool dock. Give it a warm-white paper color, a clear 2 px boundary, and at least 16 px breathing room where the viewport permits.
- The tool dock follows the drawing sequence: **Color → Brush size → Undo → Redo → Clear → Save picture**. Keep every control visible; do not hide core tools behind a hamburger menu.
- All interactive targets are at least 56 × 56 px with 12 px minimum separation. Use short labels beneath icons so meaning never depends on icon recognition.

## Concrete controls

- **Color:** Opens an anchored palette or bottom sheet with 12 large, named swatches: Black, Gray, Red, Orange, Yellow, Green, Teal, Blue, Purple, Pink, Brown, and White. Swatches are 48 px minimum and show selection with both a thick dark ring and a check mark. The closed control displays the current color and its name.
- **Brush size:** Offers four illustrated choices—Tiny 6 px, Small 12 px, Big 22 px, and Giant 36 px. Show each as an actual-width dot or stroke plus text; never rely on a slider that demands fine motor control. Default to Small.
- **Drawing:** Support touch, stylus, and mouse through pointer events. Begin a stroke on pointer down, interpolate smoothly during movement, and commit one complete stroke to history on pointer up or cancel. Prevent page scrolling only while a pointer is actively drawing on the canvas. Preserve sharp output at device pixel ratio while storing coordinates independently of display resolution.
- **Undo / Redo:** Each tap changes exactly one complete stroke or clear action. Disable Undo when history is empty and Redo when there is no reverted action; use reduced contrast plus `disabled`, not color alone. Creating a new stroke after Undo clears the redo stack. Provide `Ctrl/Cmd+Z` and `Ctrl/Cmd+Shift+Z` for keyboard users.
- **Clear:** Opens a simple confirmation sheet: “Clear this picture?” with **Keep drawing** as the safe first action and **Clear picture** as the destructive action. After clearing, show “Picture cleared” with an **Undo** action, so recovery remains possible.
- **Save picture:** Generates a PNG entirely in the browser and invokes the device’s local download/save flow with a neutral filename such as `scribble-garden-2026-07-16.png`. It must not call a server or open a public sharing flow. Announce success as “Picture saved to this device.” If generation fails, keep the drawing intact and show “Couldn’t save the picture. Try again.”

## Visual system

- Palette: paper `#FFF9E8`, ink `#24211D`, toolbar `#FFF2C7`, focus `#165DFF`, destructive `#B42318`, plus the named drawing colors. Check text and control-state contrast before release.
- Typography: use a locally bundled rounded sans or the system sans stack; do not fetch fonts from a third party. Use 24–28 px for the app name, 16–18 px for tool labels, and no tiny metadata.
- Geometry: 16 px radius for the dock and sheets, 12 px for controls, circular swatches, and a single soft shadow only where the dock overlaps the canvas. Borders explain selection and containment.
- Motion: keep tool feedback to a 100–150 ms press response and a brief save confirmation. Under `prefers-reduced-motion`, remove scaling and preserve immediate state changes.

## Responsive behavior

- **360–767 px:** Use a compact top bar, edge-to-edge canvas, and a two-row bottom dock. Put Color and Brush size on the first row; history, Clear, and Save on the second. Respect safe-area insets. Opening a palette uses a bottom sheet no taller than 45% of the viewport, leaving part of the drawing visible.
- **768–1199 px:** Move tools into a 96 px left rail while the canvas occupies the rest of the viewport. Color and size sheets open beside their trigger and remain reachable by touch.
- **1200 px and wider:** Keep the left rail and cap the canvas workspace at a comfortable drawing area rather than stretching controls. Use extra room for canvas, not dashboards, galleries, or promotional content.
- On orientation change or resize, preserve strokes by transforming logical canvas coordinates; never clear or crop the picture silently.

## States and accessibility

- **Empty:** Show a faint, non-exported prompt centered on the canvas: “Draw something!” It disappears on the first stroke.
- **Active:** The selected color and size have persistent visual and text indicators. A live region announces tool changes without announcing every stroke.
- **Disabled:** Undo and Redo remain visible and explain their unavailable state through accessible names.
- **Destructive:** The Clear confirmation traps focus, closes with Escape, and restores focus to Clear.
- **Success/error:** Save feedback is text-based, non-blocking, and announced politely; errors never discard drawing state.
- Use semantic buttons, visible 3 px focus rings, logical tab order matching the visual order, and accessible names such as “Choose color, Blue selected.” Do not use color as the only cue. The drawing surface needs an accessible name and concise instructions, while the controls remain fully keyboard-operable.

## Privacy behavior

- Ship without authentication, network persistence, telemetry, analytics SDKs, advertising SDKs, camera or microphone permissions, social sharing, and third-party font requests.
- Keep strokes and undo history in runtime memory only. Clear them when the page/session closes unless a future, explicitly user-controlled on-device save feature is designed.
- PNG export must contain only rendered pixels: no entered name, device identifier, location, account metadata, analytics identifier, or hidden application state.
- Present factual copy only: “No account,” “Nothing is uploaded,” and “Saved pictures stay on your device.” These are implementation requirements that must be tested before publication, not compliance claims.

# Verification status

This is a read-only design specification; no interface was implemented or rendered. Therefore no viewport, touch flow, keyboard flow, contrast result, screen-reader behavior, local-export behavior, privacy property, or child usability has been verified.

Before release, render at approximately 360, 768, 1280, and 1600 px; exercise touch, stylus, mouse, and keyboard controls; test empty, selected, disabled, clear-confirmation, undo-after-clear, export-success, and export-error states; inspect resize/orientation behavior; confirm reduced motion and focus restoration; and verify through network inspection that drawing, clearing, and PNG export make no requests. Usability with children and any legal or compliance assessment require separate, qualified evidence.
