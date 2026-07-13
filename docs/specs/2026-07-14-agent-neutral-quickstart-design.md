# Agent-neutral 60-second Quickstart

## Goal

Help a first-time user install and invoke Gridgeist in about 60 seconds without assuming a specific agent product.

## Placement

Add a prominent `60-second Quickstart` section immediately after the opening description in both `README.md` and `README.th.md`. Keep the existing installation and usage sections as detailed reference material.

## Content

Both languages use the same three-step structure:

1. Download or clone this repository.
2. Copy the inner `gridgeist/` directory into the agent's skills directory, noting that its location varies by product.
3. Start a new agent session and paste a review-first example prompt.

The English prompt refers to “the Gridgeist skill” instead of relying only on `$gridgeist`. The Thai version follows the same product-neutral wording. A short note explains that agents supporting explicit skill invocation may also use `$gridgeist`.

## Boundaries

- Do not claim compatibility with agents that have not been tested.
- Do not add an installer script or product-specific commands to the Quickstart.
- Do not remove the existing Codex, plugin, compatible-agent, or detailed prompt guidance.
- Do not duplicate all installation details inside the Quickstart.

## Success criteria

- A reader can identify the skill directory, installation action, session restart, and first prompt without leaving the opening section.
- English and Thai instructions have equivalent meaning and ordering.
- All Markdown links and code fences remain valid.
- `git diff --check` passes and both files remain valid UTF-8.
