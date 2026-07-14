# Gridgeist Design Language

Use this reference when selecting or explaining a visual direction. Combine influences by purpose, not by collecting fashionable labels.

## Style map

| Influence | Use it for | Signals | Risk |
|---|---|---|---|
| Swiss / International Typographic Style | Clarity and information order | rational grid, sans-serif typography, asymmetric balance, objective hierarchy | sterile imitation without meaningful content |
| Visible grid | Exposing structure as visual identity | thin rules, shared tracks, framed regions, baseline rhythm | outlining everything until the page feels like a spreadsheet |
| Editorial | Giving long pages pace and hierarchy | varied compositions, strong headlines, controlled measures, captions and metadata | sacrificing usability for magazine-like novelty |
| Technical minimalism | Making complex products feel precise | restrained palette, code/data UI, functional motion, quiet surfaces | generic developer-tool monochrome |
| Utilitarian | Prioritizing directness and function | explicit labels, dense controls, clear states, minimal ornament | losing warmth and brand personality |
| Code-native | Making the product itself the artwork | real snippets, commands, tokens, logs, previews | fake code or unreadable decorative syntax |

## Combining styles

Choose one structural influence, one expressive influence, and one product-native motif.

Example:

- Structural: Swiss grid
- Expressive: editorial scale shifts
- Product-native: lesson progress and code previews

This creates a learning platform with a clear system without making it look like a copied developer-tool homepage.

## System heuristics

### Grid

- Use a consistent outer container and gutters across sections.
- Let major edges align across navigation, hero, content, and footer.
- Break the grid only to create deliberate emphasis.
- On small screens, replace wide columns with a simpler hierarchy; do not preserve decorative empty tracks.

### Typography

- Define roles: display, heading, body, label, metadata, code.
- Keep body measure readable, commonly around 45–75 characters.
- Use weight and spacing before inventing more font sizes.
- Use mono sparingly for commands, code, IDs, timestamps, or technical labels.

### Borders and surfaces

- Use borders to explain containment, adjacency, sequence, or interaction.
- Prefer subtle neutral borders that survive both light and dark themes.
- Avoid combining heavy borders, strong shadows, gradients, and large radii on the same component without a product reason.

### Color

- Start with semantic roles, not a collection of hex values.
- Reserve the accent for actions, state, or key emphasis.
- Check contrast in real component states: default, hover, focus, disabled, selected, and error.

### Motion

- Animate change, causality, or spatial relationship.
- Avoid constant ambient motion competing with reading.
- Support `prefers-reduced-motion`.

## Reference use

When a user supplies a reference site:

1. Identify reusable principles: hierarchy, density, grid, type, color, motion, and content strategy.
2. Separate those principles from protected brand assets and distinctive compositions.
3. Translate the principles into the user's content, stack, and visual identity.
4. State what was inspired by the reference without claiming an exact replica.
