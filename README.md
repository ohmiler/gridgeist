<p align="center">
  <img src="skills/gridgeist/assets/gridgeist.svg" alt="Gridgeist agent skill for web interface direction" width="240" />
</p>

# Gridgeist

**English** · [ภาษาไทย](README.th.md) · [Website](https://ohmiler.github.io/gridgeist/) · [Examples](https://ohmiler.github.io/gridgeist/examples/)

Gridgeist is an agent skill for creating, redesigning, and reviewing product-native web interfaces. It adapts structure, typography, imagery, interaction, and product evidence to the established brand, using grids as visible, quiet, or invisible logic. It helps agents move beyond generic AI-generated SaaS patterns while preserving product intent, behavior, responsiveness, and accessibility.

## See the difference

This illustrative Northline logistics comparison is rendered from two full HTML/CSS pages with the same product, copy, sample operating data, and viewport. The After page and screenshot were rebuilt with the **Gridgeist v1.2.0** system workflow; Northline and all displayed data are fictional.

<table>
  <tr>
    <th width='50%'>Without Gridgeist - generic SaaS</th>
    <th width='50%'>With Gridgeist v1.2.0 - product-native system</th>
  </tr>
  <tr>
    <td><img src='docs/assets/northline-before.png' alt='Generic Northline logistics landing page with centered marketing copy, rounded controls, a chart, and interchangeable metric cards' width='100%' /></td>
    <td><img src='docs/assets/northline-after.png' alt='Gridgeist v1.2.0 Northline concept organized as one operational system with live freight topology, semantic lane states, arrival times, and an explicit priority exception' width='100%' /></td>
  </tr>
</table>

Same content and sample operating data; a different design system. Gridgeist turns the topology, route table, exception, actions, and metrics into one connected operational surface built from product evidence, while labeling the concept honestly. Both README images are browser captures of the working pages. [Open the Before page](https://ohmiler.github.io/gridgeist/readme-showcase/?view=before) or [open the v1.2.0 After page](https://ohmiler.github.io/gridgeist/readme-showcase/?view=after&rev=ab77ceb6).

## What v1.2.0 changes

Gridgeist now treats visual decisions as one system, not a sequence of isolated styling choices.

| Area | v1.2.0 behavior |
| --- | --- |
| System contract | Defines color, typography, layout, spacing, shape, components, states, media, and motion as one compact direction before implementation. |
| Semantic roles | Connects foundation tokens to semantic roles and component decisions, so contrast and state relationships remain intentional. |
| Component grammar | Gives related controls and content shared anatomy, variants, density, states, and content-stress rules instead of styling each instance separately. |
| Direction safety | When the visual thesis is still broad, offers distinct directions and waits for alignment before committing tokens or editing the interface. |
| Skill coordination | Names one direction owner when multiple UI skills are active, preventing competing visual systems. |
| Verification | Checks representative widths, overflow, focus, interaction states, themes, and reduced motion—and limits claims to observed evidence. |

In practice, the result is more coherent, less generic, and easier to extend without losing the product's identity. The v1.2.0 release was exercised through three English and three Thai system-contract scenarios, independent responsive browser checks, and repaired guardrail tests.

## 60-second Quickstart

1. Install Gridgeist through the primary channel for your agent.

   For Codex, add the Git marketplace and install the plugin:

   ```powershell
   codex plugin marketplace add ohmiler/gridgeist
   codex plugin add gridgeist@gridgeist
   ```

   For Claude Code, Cursor, Gemini CLI, GitHub Copilot, OpenCode, and other compatible agents, use the universal installer:

   ```powershell
   npx skills add ohmiler/gridgeist -g
   ```

   **Manual fallback:** If neither installer is available, continue to [Manual installation](#manual-installation).
2. Start a new agent session in your web project and paste:

   ```text
   Use the Gridgeist skill to review this interface without editing it yet. Give me a one-line verdict, prioritized findings with evidence, and one coherent redesign direction. Preserve the product's behavior and brand.
   ```

Agents that support explicit skill invocation can use `$gridgeist` in the prompt. Continue to [Installation](#installation) for product-specific details and more examples.

## Use cases

- Create a distinctive landing page, dashboard, documentation site, portfolio, or learning platform.
- Redesign an existing interface without breaking its behavior or brand.
- Review a draft and prioritize hierarchy, composition, responsiveness, accessibility, and implementation quality.
- Adapt technical, editorial, image-led, playful, utilitarian, or visible-grid direction without erasing the brand.

## Installation

### Codex plugin

This repository is packaged as a Codex plugin through [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json). The plugin points to the same `skills/gridgeist/` directory used by the other channels, so all installations share one source of truth.

Add the Gridgeist marketplace, then install the plugin:

```powershell
codex plugin marketplace add ohmiler/gridgeist
codex plugin add gridgeist@gridgeist
```

Start a new Codex session after installation so the bundled skill is discovered.

### Universal installer

For Claude Code, Cursor, Gemini CLI, GitHub Copilot, OpenCode, and other compatible agents, install Gridgeist with the [open agent skills CLI](https://github.com/vercel-labs/skills):

```powershell
npx skills add ohmiler/gridgeist -g
```

The installer discovers `skills/gridgeist/` and prompts you to choose the target agents. To select one directly, pass its agent name; for example:

```powershell
npx skills add ohmiler/gridgeist -g -a claude-code
```

### Manual installation

Use manual copying only when the plugin and universal installer are unavailable:

```powershell
git clone https://github.com/ohmiler/gridgeist.git
Copy-Item -Recurse .\gridgeist\skills\gridgeist "$HOME\.agents\skills\gridgeist"
```

For a different agent, copy `skills/gridgeist/` to that product's skills directory. The agent must support the Agent Skills `SKILL.md` convention. Discovery and invocation behavior can differ between products. Start a new agent session after copying the directory.

## Updating

Gridgeist releases do not update silently. Use the command for the channel that installed the skill, then start a new agent session.

### Codex plugin

Refresh the Git-backed marketplace snapshot, then reinstall the plugin version exposed by that release:

```powershell
codex plugin marketplace upgrade gridgeist
codex plugin add gridgeist@gridgeist
```

Confirm the installed version with `codex plugin list`. If the current session still uses older instructions, start a new thread or restart the Codex app.

### Universal installer

Update a global Gridgeist installation:

```powershell
npx skills update gridgeist -g -y
```

For a project-scoped installation, use `npx skills update gridgeist -p -y` instead.

### Git clone or manual copy

Run `git pull --ff-only` in an existing clone, then reinstall from `skills/gridgeist/`. Manual copies do not retain source or version metadata, so replace the complete skill directory from a tagged release. Prefer the Codex plugin or universal installer when future updates matter.

## Example prompts

Invoke Gridgeist directly with `$gridgeist` and include four essentials:

1. The product and its audience.
2. The mode: create, redesign, or review.
3. What must be preserved, such as behavior, brand color, or content.
4. What must be verified, such as desktop, mobile, keyboard, and accessibility.

```text
Use $gridgeist to redesign this Next.js course landing page. Preserve all behavior and the blue brand color, but replace the generic SaaS cards with an editorial grid and verify desktop and mobile layouts.
```

```text
Review this dashboard with $gridgeist. Give me a one-line verdict, prioritized findings with evidence, and a coherent replacement direction before editing.
```

```text
Use $gridgeist to create a technical documentation homepage where real API examples and navigation structure carry the visual identity.
```

### Brief for a closer match

For a more precise result, provide these details when they are relevant:

- **Product and audience** — what the product does and who uses it.
- **Primary task** — the most important thing the user must accomplish.
- **Direction** — the intended character, such as warm editorial, precise
  technical, or playful tactile.
- **Authentic material** — product UI, data, prose, imagery, artwork, code, or a
  workflow that should carry visual weight.
- **Preserved constraints** — brand signals, content, routes, behavior, components,
  privacy, or platform requirements that must not change.
- **Exclusions** — visual language or behavior that would be wrong for the product.
- **Flows and states** — the important default, loading, empty, error, success,
  disabled, and destructive paths.
- **Verification** — representative viewports, keyboard, touch, focus, overflow,
  reduced motion, and primary flows to exercise.

When the direction is already clear, state it and let Gridgeist proceed without
another aesthetic questionnaire. When several materially different directions are
still credible, ask Gridgeist to inspect first, offer two or three grounded options
with trade-offs and a recommendation, and wait for alignment before editing.

Copy and adapt this template:

```text
Use $gridgeist to [create / redesign / review] [page or product surface].

Product and audience:
[What it does and who uses it]

Primary task:
[The most important user outcome]

Direction:
[A confirmed direction, or: Inspect first, propose two or three grounded
directions with trade-offs and a recommendation, and do not edit until I choose.]

Authentic material that should lead:
[Product UI / data / prose / imagery / artwork / code / workflow]

Preserve:
[Brand, content, routes, behavior, components, and constraints]

Avoid:
[Visual language or behavior that would be wrong]

Important flows and states:
[Primary flow and applicable default/loading/empty/error/success/disabled states]

Verify:
[Viewports, keyboard, touch, focus, overflow, reduced motion, and primary flow]

Inspect the repository and rendered interface before taking action.
```

Describe outcomes and genuine constraints rather than prescribing a CSS recipe.
Unless they are established brand requirements, leave font sizes, spacing, radii,
shadows, and column counts for Gridgeist to derive as one coherent system.

If a project already contains a `DESIGN.md`, theme, token set, or component
library, Gridgeist inspects it alongside the implementation and rendered interface
instead of assuming the sources agree. `DESIGN.md` is optional interoperability,
not a dependency: Gridgeist should not create or update one unless you request a
portable design-system artifact or explicitly include durable system documentation
in the work.

Gridgeist also allows implicit invocation when the agent recognizes a matching web-interface task.

## Working with companion skills

Gridgeist works best as the sole owner of product and visual direction, with optional companion skills supplying context, technical review, or rendered evidence. The lightest recommended workflow for most projects is:

```text
Gridgeist -> Playwright
```

Gridgeist defines the interface thesis, hierarchy, system, and implementation direction. Playwright then checks the rendered result across representative viewports and interactions; it can also provide repeatable [visual comparisons](https://playwright.dev/docs/test-snapshots).

| Situation | Recommended workflow | Division of responsibility |
| --- | --- | --- |
| Most web projects | `Gridgeist -> Playwright` | Design and implementation, then rendered verification |
| Figma is the source of truth | `Figma -> Gridgeist -> Playwright` | Extract components, variables, and layout context; adapt them to the product and codebase; verify the result. See the [Figma MCP server](https://developers.figma.com/docs/figma-mcp-server/). |
| React or Next.js | `Gridgeist -> Vercel React Best Practices -> Playwright` | Own the interface direction; review framework performance; verify behavior. See [Vercel Agent Skills](https://github.com/vercel-labs/agent-skills). |
| Pre-release quality audit | `Gridgeist -> Web Quality Audit -> Playwright` | Review hierarchy and brand fit; audit accessibility, performance, SEO, and web quality; confirm the live result. See [Web Quality Skills](https://github.com/addyosmani/web-quality-skills). |
| Original imagery is required | `Gridgeist -> image generation -> Gridgeist -> Playwright` | Establish the thesis before generating assets, compose with the selected assets, then verify the interface. |

Treat these as optional workflows, not dependencies. Add only the companion that answers a real need, and keep another broad frontend-design or art-direction skill out of the same design phase; competing visual priors can weaken a coherent result. Companion skill names and availability vary between agents.

Example:

```text
Use $gridgeist to redesign this interface while preserving its behavior and brand.
After implementation, use Playwright to verify representative desktop and mobile
viewports, keyboard interaction, overflow, and the primary user flow.
```

## Repository layout

```text
.codex-plugin/
  plugin.json          Codex plugin manifest
skills/gridgeist/      Installable skill
  SKILL.md             Trigger conditions and core workflow
  agents/openai.yaml   Agent-facing interface metadata
  references/          Design language and review checklist
evals/prompts.md       Repeatable manual behavior checks
docs/                  Design and implementation records
```

## Case studies

[Tracefield](https://ohmiler.github.io/tracefield/) applies Gridgeist to a working developer-observability dashboard. Its [repository](https://github.com/ohmiler/tracefield) preserves the generic baseline, exact prompt, evaluation rubric, tested trace domain, and responsive final interface.

[Ledgerline](https://ohmiler.github.io/ledgerline/) tests the same skill on dense payment API documentation. Its [repository](https://github.com/ohmiler/ledgerline) preserves a conventional baseline, exact prompt, six-part rubric, deterministic API content, four viewport checks, and the responsive final interface.

[Morrow](https://ohmiler.github.io/morrow-portfolio/) stress-tests brand adaptation with a fictional image-led creative portfolio. Its [repository](https://github.com/ohmiler/morrow-portfolio) preserves shared AI-generated artwork, a conventional baseline, exact prompts, a six-part rubric, four viewport checks, and a final interface deliberately unlike the technical case studies.

[Doodlewood](https://ohmiler.github.io/doodlewood/) tests playful interaction design with a fictional, privacy-preserving children's drawing studio. Its [repository](https://github.com/ohmiler/doodlewood) preserves the generic baseline, exact prompt, six-part rubric, local drawing engine, four viewport checks, and explicit limits around child safety and real-user evidence.

Together, the four self-produced case studies cover data-heavy, content-heavy, image-led, and playful interactive surfaces. Further validation should now prioritize independent users, agents, and projects rather than adding another first-party visual category.

## Limitations

- Output quality depends on the agent inspecting the actual repository and rendered interface.
- Automated checks do not replace visual inspection at representative viewport sizes.
- The suggested defaults are starting points, not a mandatory preset for every brand.
- Model outputs are not deterministic. Re-run evaluations when the skill or target agent changes.

## Validation

Validate the installable skill structure:

```powershell
python -X utf8 "$HOME\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\skills\gridgeist
```

Check release metadata and bilingual documentation without external dependencies:

```powershell
python -X utf8 .\scripts\validate_release.py
```

Exercise clean installation and updates through the live Codex marketplace and universal installer. This check requires Codex, Node.js, npm, Git, and network access; it uses temporary homes and does not modify your existing installations.

```powershell
python -X utf8 .\scripts\smoke_test_install.py
```

Behavioral evaluation prompts are in [`evals/prompts.md`](evals/prompts.md).

## Contributing

Keep `SKILL.md` concise and place detailed, conditionally loaded guidance in `references/`. For behavior changes, update an evaluation scenario and record what failed before changing the skill. Open an issue or pull request with the motivating prompt and observed output.

## License

[MIT](LICENSE)
