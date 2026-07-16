Verdict: The surface may look polished, but the interaction system is not yet dependable for keyboard, low-vision, color-vision, or motion-sensitive users. The issues described affect core accessibility, not finishing polish.

### Prioritized findings

1. **Critical — Interactive controls, throughout**
   - **Evidence:** The supplied review notes weak focus states; no rendered fixture was available to inspect.
   - **Impact:** Keyboard users can lose their position or be unable to identify the active control.
   - **Smallest coherent correction:** Define one shared `:focus-visible` treatment for links, buttons, inputs, custom controls, and modal actions. Use a high-contrast 2–3 px outline with separation from the component, and do not remove the native outline unless this replacement is present. Ensure it remains visible in high-contrast/forced-colors modes and against every surface.

2. **High — Status indicators, wherever state is communicated**
   - **Evidence:** Status is described as color-only.
   - **Impact:** Success, warning, error, selected, and inactive states may be indistinguishable to users who cannot perceive the color difference.
   - **Smallest coherent correction:** Pair color with persistent text and, where useful, a distinct icon or shape. Give icons accessible names only when the adjacent text does not already provide one. Announce asynchronous status changes through an appropriately scoped `aria-live` region; do not announce static decoration.

3. **High — Modal open/close flow**
   - **Evidence:** Focus return is described as broken.
   - **Impact:** Closing the modal can strand keyboard or screen-reader users elsewhere in the document and disrupt the primary task.
   - **Smallest coherent correction:** Capture the invoking element before opening; move focus to the modal’s first meaningful target or heading; contain Tab and Shift+Tab inside it; support Escape unless the action must be blocking; make the background inert; and on close restore focus to the invoker if it still exists. If it was removed, focus the nearest logical workflow target. Prefer the project’s established accessible dialog primitive or native `<dialog>` rather than bespoke focus-trap code.

4. **Medium — Animated background grid**
   - **Evidence:** The background grid is described as animated rather than task-causal.
   - **Impact:** Ambient movement competes with content and may cause discomfort or distraction.
   - **Smallest coherent correction:** Make the grid static by default unless its motion communicates real system behavior. At minimum, disable animation under `@media (prefers-reduced-motion: reduce)` without removing essential feedback. Keep reduced-motion state changes immediate and legible.

### Replacement direction

Use a quiet structural grid rather than a moving visual effect: a task-first interface for the existing audience, organized around the current workflow, preserving the polished brand expression while making focus, status, and modal transitions explicit product-native signals. The grid should support alignment; status labels and focus treatment should carry interaction clarity; motion should be reserved for causal feedback.

Implement these as shared tokens and primitives, not page-level patches: `--focus-ring`, `--focus-offset`, semantic status foreground/background/border tokens, a reduced-motion rule, and one dialog component with a documented focus lifecycle. Inventory default, hover, focus, active, selected, disabled, loading, error, success, and destructive states while applying the change.

Acceptance checks:

- Every interactive element has a clearly visible keyboard focus indicator in all themes and surfaces.
- Status remains understandable in grayscale and with color removed.
- The modal opens from keyboard, contains focus, closes with Escape where appropriate, and returns focus to its trigger or a defined fallback.
- Background motion stops when reduced motion is requested; no essential state is lost.
- The primary flow works at representative mobile and desktop widths, at 200% zoom, and with keyboard-only navigation.

No files, rendered viewports, themes, or interaction flows were available in this request, so these are findings and an implementation specification based on the reported behavior—not an implemented or verified fix.
