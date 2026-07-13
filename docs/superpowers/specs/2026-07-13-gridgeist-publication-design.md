# Gridgeist Publication Design

## Goal

Publish Gridgeist as a professional, reusable public agent skill at
`https://github.com/ohmiler/gridgeist`.

## Repository structure

The repository root contains human-facing project material and evaluation
fixtures. The installable skill remains isolated in `gridgeist/`.

```text
gridgeist/
|-- README.md
|-- LICENSE
|-- .gitignore
|-- evals/
|   `-- prompts.md
|-- docs/
|   `-- superpowers/specs/
`-- gridgeist/
    |-- SKILL.md
    |-- agents/openai.yaml
    `-- references/
```

## Metadata

Keep the existing `gridgeist` skill name and trigger description. Normalize
`agents/openai.yaml` to the documented interface fields, quote string values,
retain implicit invocation, and remove unsupported product policy fields.

## Public documentation

Create a concise README covering purpose, installation, example prompts,
repository layout, supported use cases, limitations, validation, and
contribution guidance. Use the MIT License.

## Evaluation

Add a compact prompt suite covering creation, redesign, review, mobile,
accessibility, conflicting visual direction, and cases that should not trigger
the skill. The suite is a repeatable manual behavioral evaluation, not a claim
that model outputs are deterministic.

## Verification and publication

Check YAML and Markdown structure, internal links, UTF-8 content, repository
diff, and Git status. Run the official skill validator if a usable Python
runtime exists; otherwise report that limitation explicitly. Commit the
release-quality files, set the GitHub remote, and push the default `main`
branch.

## Out of scope

- Building a website or documentation portal
- Adding CI that depends on an unspecified Python environment
- Publishing a package to a separate marketplace
- Creating visual assets or screenshots without real output examples
