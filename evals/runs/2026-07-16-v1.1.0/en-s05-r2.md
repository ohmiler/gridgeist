## Verdict

The interface is visually polished but not interaction-complete: keyboard orientation, status meaning, motion preferences, and modal recovery are all under-specified. Based only on the issues reported—not rendered or code-level observation—the accessibility repair should precede further visual polish.

## Prioritized findings and corrections

1. **High — Modal focus lifecycle**
   - **Location:** Modal open/close flow.
   - **Evidence:** Focus return is reported broken.
   - **Impact:** Keyboard and assistive-technology users can lose their place after closing the modal.
   - **Correction:** Save the invoking element before opening; move focus to the modal heading or first meaningful control; keep Tab and Shift+Tab within the open modal; close on Escape; prevent the background from receiving focus; on close, restore focus to the invoker if it still exists, otherwise to a logical nearby control. Use the project’s established accessible dialog primitive or native `<dialog>` rather than maintaining a partial custom trap.

2. **High — Weak focus visibility**
   - **Location:** All interactive controls, including links, buttons, inputs, tabs, menu items, icon controls, and modal actions.
   - **Evidence:** Focus states are reported as weak.
   - **Impact:** Keyboard users cannot reliably locate the active control.
   - **Correction:** Define one shared `:focus-visible` token: a clearly contrasting 2–3 px outline or ring with separation from the component edge. Do not remove the browser outline unless the replacement is at least as clear. Test it on every surface and state, especially selected, destructive, disabled-adjacent, and dark-theme controls.

   ```css
   :where(a, button, input, select, textarea, [tabindex]):focus-visible {
     outline: 3px solid var(--focus-ring);
     outline-offset: 3px;
   }
   ```

3. **High — Color-only status**
   - **Location:** Badges, indicators, validation, and success/warning/error states.
   - **Evidence:** Status is reported to rely on color alone.
   - **Impact:** Meaning is lost for users with color-vision differences, monochrome displays, or low visual contrast.
   - **Correction:** Pair color with persistent text and a second visual cue such as an icon or shape. Keep the status word in the accessible name; mark a duplicate icon decorative. For dynamic changes, announce only meaningful updates with an appropriate live region—do not make every badge live.

   ```html
   <span class="status status--warning">
     <svg aria-hidden="true"><!-- warning icon --></svg>
     Warning: connection unstable
   </span>
   ```

4. **Medium — Ambient animated grid**
   - **Location:** Page background.
   - **Evidence:** Background grids are reported as animated.
   - **Impact:** Nonessential motion competes with the primary task and can affect motion-sensitive users.
   - **Correction:** Make the grid static by default unless its motion communicates real product state. If motion has a justified role, keep it subtle, pause it when obscured, and remove it under reduced-motion preferences without hiding essential feedback.

   ```css
   @media (prefers-reduced-motion: reduce) {
     .background-grid { animation: none; transform: none; }
   }
   ```

## Replacement direction

Use a quiet structural grid for alignment, not ambient spectacle; preserve the existing polished brand expression; and make semantic state markers and a strong focus ring the product-native motif. The governing rule is simple: every change of state must remain understandable without color, every control must remain locatable without a pointer, and every overlay must return the user to a predictable place.

No files were changed and no rendered verification was performed because no target fixture or source was provided. After implementation, verify keyboard-only open → interact → close → focus-return flows, status comprehension without color, reduced-motion behavior, and representative widths around 360, 768, 1280, and 1600 px.
