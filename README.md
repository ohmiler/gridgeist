<p align="center">
  <img src="skills/gridgeist/assets/gridgeist.svg" alt="Gridgeist agent skill for web interface direction" width="240" />
</p>

# Gridgeist

**English** · [ภาษาไทย](README.th.md) · [Website](https://ohmiler.github.io/gridgeist/) · [Examples](https://ohmiler.github.io/gridgeist/examples/)

Gridgeist is an agent skill for creating, redesigning, and reviewing product-native web interfaces. It adapts structure, typography, imagery, interaction, and product evidence to the established brand, using grids as visible, quiet, or invisible logic. It helps agents move beyond generic AI-generated SaaS patterns while preserving product intent, behavior, responsiveness, and accessibility.

## See the difference

This illustrative Northline logistics comparison is rendered from two full HTML/CSS pages with the same product, copy, sample operating data, and viewport. The After page and screenshot were refreshed against **Gridgeist v1.1.0**; Northline and all displayed data are fictional.

<table>
  <tr>
    <th width='50%'>Without Gridgeist - generic SaaS</th>
    <th width='50%'>With Gridgeist v1.1.0 - product-native system</th>
  </tr>
  <tr>
    <td><img src='docs/assets/northline-before.png' alt='Generic Northline logistics landing page with centered marketing copy, rounded controls, a chart, and interchangeable metric cards' width='100%' /></td>
    <td><img src='docs/assets/northline-after.png' alt='Gridgeist v1.1.0 Northline concept organized around a dominant live freight topology, sample lane status, arrival times, and an explicit exception state' width='100%' /></td>
  </tr>
</table>

Same content and sample operating data; a different design system. Gridgeist shifts the visual identity from generic cards to a live freight network built from product evidence, while labeling the concept honestly. Both README images are browser captures of the working pages. [Open the Before page](https://ohmiler.github.io/gridgeist/readme-showcase/?view=before) or [open the After page](https://ohmiler.github.io/gridgeist/readme-showcase/?view=after&rev=b4380726).

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

```text
Use $gridgeist to redesign this Next.js course landing page. Preserve all behavior and the blue brand color, but replace the generic SaaS cards with an editorial grid and verify desktop and mobile layouts.
```

```text
Review this dashboard with $gridgeist. Give me a one-line verdict, prioritized findings with evidence, and a coherent replacement direction before editing.
```

```text
Use $gridgeist to create a technical documentation homepage where real API examples and navigation structure carry the visual identity.
```

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
