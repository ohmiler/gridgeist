<p align="center">
  <img src="skills/gridgeist/assets/gridgeist.svg" alt="Gridgeist agent skill for web interface direction" width="240" />
</p>

# Gridgeist

**English** · [ภาษาไทย](README.th.md) · [Website](https://ohmiler.github.io/gridgeist/) · [Examples](https://ohmiler.github.io/gridgeist/examples/)

Gridgeist is an agent skill for creating, redesigning, and reviewing product-native web interfaces. It adapts structure, typography, imagery, interaction, and product evidence to the established brand, using grids as visible, quiet, or invisible logic. It helps agents move beyond generic AI-generated SaaS patterns while preserving product intent, behavior, responsiveness, and accessibility.

## See the difference

This illustrative Northline logistics comparison is rendered from two full HTML/CSS pages with the same product, copy, data, and viewport.

<table>
  <tr>
    <th width='50%'>Without Gridgeist - generic SaaS</th>
    <th width='50%'>With Gridgeist - product-native system</th>
  </tr>
  <tr>
    <td><img src='docs/assets/northline-before.png' alt='Generic Northline logistics landing page with centered marketing copy, rounded controls, a chart, and interchangeable metric cards' width='100%' /></td>
    <td><img src='docs/assets/northline-after.png' alt='Product-specific Northline logistics website organized around live freight routes, lane status, arrival times, and operational metrics' width='100%' /></td>
  </tr>
</table>

Same content and operating data; a different design system. Gridgeist shifts the visual identity from generic cards to a live freight network built from product evidence. [Open the Before page](https://ohmiler.github.io/gridgeist/readme-showcase/?view=before) or [open the After page](https://ohmiler.github.io/gridgeist/readme-showcase/?view=after).

## 60-second Quickstart

1. Download this repository:

   ```shell
   git clone https://github.com/ohmiler/gridgeist.git
   ```

2. Copy the `skills/gridgeist/` directory into your agent's skills directory. The directory location and skill-discovery behavior vary by agent, so check that product's skills documentation if needed.
3. Start a new agent session in your web project and paste:

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

### Codex

```powershell
git clone https://github.com/ohmiler/gridgeist.git
Copy-Item -Recurse .\gridgeist\skills\gridgeist "$HOME\.agents\skills\gridgeist"
```

Codex should detect the skill automatically. If it does not appear, restart Codex.

### Plugin package

This repository is also packaged as a Codex plugin through [`.codex-plugin/plugin.json`](.codex-plugin/plugin.json). The plugin points to the same `skills/gridgeist/` directory, so direct skill installs and marketplace distribution share one source of truth.

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

Copy the `skills/gridgeist/` directory to the skills directory used by your agent. The agent must support the Agent Skills `SKILL.md` convention. Discovery and invocation behavior can differ between products.

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

```powershell
python -X utf8 "$HOME\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\skills\gridgeist
```

Behavioral evaluation prompts are in [`evals/prompts.md`](evals/prompts.md).

## Contributing

Keep `SKILL.md` concise and place detailed, conditionally loaded guidance in `references/`. For behavior changes, update an evaluation scenario and record what failed before changing the skill. Open an issue or pull request with the motivating prompt and observed output.

## License

[MIT](LICENSE)
