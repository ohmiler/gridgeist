#!/usr/bin/env python3
"""Validate Gridgeist skill structure and release metadata without dependencies."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SEMVER = re.compile(r"^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?(?:\+[0-9A-Za-z.-]+)?$")


class ValidationError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValidationError(message)


def read_text(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8")


def read_json(path: str) -> dict:
    with (ROOT / path).open(encoding="utf-8") as handle:
        value = json.load(handle)
    require(isinstance(value, dict), f"{path} must contain a JSON object")
    return value


def validate_skill() -> None:
    skill_path = ROOT / "skills/gridgeist/SKILL.md"
    content = skill_path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---", content, re.DOTALL)
    require(match is not None, "SKILL.md must start with YAML frontmatter")

    fields: dict[str, str] = {}
    for line in match.group(1).splitlines():
        if not line.strip():
            continue
        key, separator, value = line.partition(":")
        require(bool(separator), f"Invalid SKILL.md frontmatter line: {line}")
        fields[key.strip()] = value.strip()

    require(set(fields) == {"name", "description"}, "SKILL.md frontmatter must contain only name and description")
    require(fields["name"] == "gridgeist", "SKILL.md name must be gridgeist")
    require(bool(fields["description"]), "SKILL.md description must not be empty")

    for relative in re.findall(r"\]\((references/[^)]+)\)", content):
        require((skill_path.parent / relative).is_file(), f"Missing SKILL.md reference: {relative}")

    agent_yaml = read_text("skills/gridgeist/agents/openai.yaml")
    short_match = re.search(r"^\s*short_description:\s*(?P<quote>[\x22'])(.+)(?P=quote)\s*$", agent_yaml, re.MULTILINE)
    prompt_match = re.search(r"^\s*default_prompt:\s*(?P<quote>[\x22'])(.+)(?P=quote)\s*$", agent_yaml, re.MULTILINE)
    require(short_match is not None, "agents/openai.yaml needs a quoted short_description")
    require(25 <= len(short_match.group(2)) <= 64, "short_description must be 25-64 characters")
    require(prompt_match is not None and "$gridgeist" in prompt_match.group(2), "default_prompt must mention $gridgeist")
    require("allow_implicit_invocation: true" in agent_yaml, "Gridgeist must preserve implicit invocation policy")


def validate_plugin(expected_version: str | None) -> str:
    manifest = read_json(".codex-plugin/plugin.json")
    for key in ("name", "version", "description", "author", "interface", "skills"):
        require(key in manifest, f"plugin.json is missing {key}")

    require(manifest["name"] == "gridgeist", "plugin name must be gridgeist")
    version = manifest["version"]
    require(isinstance(version, str) and SEMVER.fullmatch(version) is not None, "plugin version must be strict semver")
    require(manifest["skills"] == "./skills/", "plugin skills path must remain ./skills/")
    require(manifest["author"].get("name"), "plugin author.name is required")

    interface = manifest["interface"]
    for key in ("displayName", "shortDescription", "longDescription", "developerName", "category", "websiteURL"):
        require(interface.get(key), f"plugin interface is missing {key}")
    prompts = interface.get("defaultPrompt", [])
    require(isinstance(prompts, list) and 1 <= len(prompts) <= 3, "plugin defaultPrompt must contain 1-3 prompts")
    require(all(isinstance(item, str) and len(item) <= 128 for item in prompts), "plugin prompts must be strings no longer than 128 characters")

    marketplace = read_json(".agents/plugins/marketplace.json")
    entries = [item for item in marketplace.get("plugins", []) if item.get("name") == "gridgeist"]
    require(len(entries) == 1, "marketplace must contain exactly one gridgeist entry")
    entry = entries[0]
    source = entry.get("source", {})
    require(source.get("source") == "url", "marketplace must install Gridgeist from a Git URL")
    require(source.get("url") == "https://github.com/ohmiler/gridgeist.git", "marketplace Git URL is unexpected")
    require(source.get("ref") == f"v{version}", "marketplace ref must match plugin version")
    require(entry.get("policy", {}).get("installation") == "AVAILABLE", "marketplace installation policy must be AVAILABLE")
    require(entry.get("policy", {}).get("authentication") == "ON_INSTALL", "marketplace authentication policy must be ON_INSTALL")
    require(entry.get("category"), "marketplace category is required")

    if expected_version is not None:
        require(version == expected_version, f"tag version {expected_version} does not match plugin version {version}")

    changelog = read_text("CHANGELOG.md")
    require(f"## [{version}]" in changelog, f"CHANGELOG.md needs a {version} release section")
    require(f"[{version}]: https://github.com/ohmiler/gridgeist/compare/" in changelog, f"CHANGELOG.md needs a {version} comparison link")
    return version


def validate_docs_and_evals() -> None:
    update_fragments = (
        "codex plugin marketplace upgrade gridgeist",
        "codex plugin add gridgeist@gridgeist",
        "npx skills update gridgeist -g -y",
    )
    for path in ("README.md", "README.th.md", "site/docs/index.html", "site/th/docs/index.html"):
        content = read_text(path)
        for fragment in update_fragments:
            require(fragment in content, f"{path} is missing update command: {fragment}")

    english = [int(value) for value in re.findall(r"^## Scenario (\d+):", read_text("evals/prompts.md"), re.MULTILINE)]
    thai = [int(value) for value in re.findall(r"^## สถานการณ์ (\d+):", read_text("evals/prompts.th.md"), re.MULTILINE)]
    require(english == thai, "English and Thai eval scenario numbers must match")
    require(english == list(range(1, max(english) + 1)), "Eval scenario numbers must be contiguous")


def validate_installation_paths() -> None:
    for path in ("README.md", "README.th.md"):
        content = read_text(path)
        positions = [
            content.find("codex plugin marketplace add ohmiler/gridgeist"),
            content.find("npx skills add ohmiler/gridgeist -g"),
            content.find("Copy-Item -Recurse"),
        ]
        require(all(position >= 0 for position in positions), f"{path} is missing a documented installation path")
        require(positions == sorted(positions), f"{path} must order Codex, universal, then manual installation")

    require("Manual fallback" in read_text("README.md"), "README.md Quickstart must label manual installation as fallback")

    workflow = read_text(".github/workflows/validate.yml")
    for fragment in (
        "smoke-install:",
        "npm install --global @openai/codex",
        "python scripts/smoke_test_install.py",
    ):
        require(fragment in workflow, f"validate workflow is missing install smoke wiring: {fragment}")
    require((ROOT / "scripts/smoke_test_install.py").is_file(), "install smoke test script is missing")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release-version", help="Expected version when validating a v* Git tag")
    args = parser.parse_args()

    try:
        validate_skill()
        version = validate_plugin(args.release_version)
        validate_docs_and_evals()
        validate_installation_paths()
    except (OSError, json.JSONDecodeError, ValidationError) as error:
        print(f"[FAIL] {error}", file=sys.stderr)
        return 1

    print(f"[OK] Gridgeist v{version} skill, release metadata, docs, and evals are aligned.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
