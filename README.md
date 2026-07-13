# Gridgeist

**English** · [ภาษาไทย](README.th.md) · [Website](https://ohmiler.github.io/gridgeist/) · [Examples](https://ohmiler.github.io/gridgeist/examples/)

Gridgeist is an agent skill for creating, redesigning, and reviewing web interfaces with a strong grid, precise typography, technical minimalism, and editorial discipline. It helps agents move beyond generic AI-generated SaaS patterns while preserving product intent, behavior, responsiveness, and accessibility.

## Use cases

- Create a distinctive landing page, dashboard, documentation site, portfolio, or learning platform.
- Redesign an existing interface without breaking its behavior or brand.
- Review a draft and prioritize hierarchy, composition, responsiveness, accessibility, and implementation quality.

## Installation

### Codex

```powershell
git clone https://github.com/ohmiler/gridgeist.git
Copy-Item -Recurse .\gridgeist\gridgeist "$HOME\.agents\skills\gridgeist"
```

Restart Codex after installation so it discovers the skill.

### Other compatible agents

Copy the inner `gridgeist/` directory to the skills directory used by your agent. The agent must support the Agent Skills `SKILL.md` convention. Discovery and invocation behavior can differ between products.

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
gridgeist/             Installable skill
  SKILL.md             Trigger conditions and core workflow
  agents/openai.yaml   Agent-facing interface metadata
  references/          Design language and review checklist
evals/prompts.md       Repeatable manual behavior checks
docs/                  Design and implementation records
```

## Limitations

- Output quality depends on the agent inspecting the actual repository and rendered interface.
- Automated checks do not replace visual inspection at representative viewport sizes.
- The suggested defaults are starting points, not a mandatory preset for every brand.
- Model outputs are not deterministic. Re-run evaluations when the skill or target agent changes.

## Validation

```powershell
python "$HOME\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\gridgeist
```

Behavioral evaluation prompts are in [`evals/prompts.md`](evals/prompts.md).

## Contributing

Keep `SKILL.md` concise and place detailed, conditionally loaded guidance in `references/`. For behavior changes, update an evaluation scenario and record what failed before changing the skill. Open an issue or pull request with the motivating prompt and observed output.

## License

[MIT](LICENSE)
