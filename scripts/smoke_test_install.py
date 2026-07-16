#!/usr/bin/env python3
"""Exercise Gridgeist's live installation and update paths in temporary homes."""

from __future__ import annotations

import argparse
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
PLUGIN_ID = "gridgeist@gridgeist"
SKILL_NAME = "gridgeist"


class SmokeError(Exception):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SmokeError(message)


def find_command(name: str) -> str:
    path = shutil.which(name)
    require(path is not None, f"Required command is unavailable: {name}")
    return path


def run(
    command: list[str],
    env: dict[str, str],
    timeout: int,
    *,
    capture: bool = True,
) -> subprocess.CompletedProcess[str]:
    print(f"[RUN] {' '.join(command)}", flush=True)
    completed = subprocess.run(
        command,
        cwd=ROOT,
        env=env,
        text=True,
        encoding="utf-8",
        errors="replace",
        stdout=subprocess.PIPE if capture else None,
        stderr=subprocess.PIPE if capture else None,
        timeout=timeout,
        check=False,
    )
    if capture and completed.stdout:
        print(completed.stdout.rstrip())
    if capture and completed.stderr:
        print(completed.stderr.rstrip(), file=sys.stderr)
    require(completed.returncode == 0, f"Command failed with exit code {completed.returncode}: {' '.join(command)}")
    return completed


def json_output(completed: subprocess.CompletedProcess[str], label: str) -> Any:
    try:
        return json.loads(completed.stdout)
    except json.JSONDecodeError as error:
        raise SmokeError(f"{label} did not return valid JSON: {error}") from error


def plugin_version() -> str:
    with (ROOT / ".codex-plugin/plugin.json").open(encoding="utf-8") as handle:
        manifest = json.load(handle)
    version = manifest.get("version")
    require(isinstance(version, str) and version, "Plugin manifest version is missing")
    return version


def require_inside(path: Path, root: Path, label: str) -> None:
    require(path.resolve().is_relative_to(root.resolve()), f"{label} escaped its temporary home: {path}")


def validate_skill_tree(skill_root: Path) -> None:
    skill_file = skill_root / "SKILL.md"
    require(skill_file.is_file(), f"Installed skill is missing {skill_file}")
    content = skill_file.read_text(encoding="utf-8")
    require("name: gridgeist" in content, "Installed SKILL.md has the wrong identity")
    for relative in ("references/design-language.md", "references/review-checklist.md", "agents/openai.yaml"):
        require((skill_root / relative).is_file(), f"Installed skill is missing {relative}")


def validate_plugin_install(result: Any, version: str, codex_home: Path) -> Path:
    require(isinstance(result, dict), "Plugin install output must be an object")
    require(result.get("pluginId") == PLUGIN_ID, "Plugin install returned the wrong plugin ID")
    require(result.get("version") == version, "Plugin install returned the wrong version")
    installed_path = result.get("installedPath")
    require(isinstance(installed_path, str), "Plugin install did not return installedPath")
    plugin_root = Path(installed_path)
    require_inside(plugin_root, codex_home, "Plugin cache")
    validate_skill_tree(plugin_root / "skills/gridgeist")
    with (plugin_root / ".codex-plugin/plugin.json").open(encoding="utf-8") as handle:
        installed_manifest = json.load(handle)
    require(installed_manifest.get("version") == version, "Cached plugin manifest version is incorrect")
    return plugin_root


def validate_plugin_list(result: Any, version: str) -> None:
    require(isinstance(result, dict), "Plugin list output must be an object")
    installed = result.get("installed")
    require(isinstance(installed, list), "Plugin list output is missing installed entries")
    matches = [entry for entry in installed if entry.get("pluginId") == PLUGIN_ID]
    require(len(matches) == 1, "Plugin list must contain exactly one installed Gridgeist entry")
    entry = matches[0]
    require(entry.get("version") == version, "Plugin list returned the wrong Gridgeist version")
    require(entry.get("installed") is True and entry.get("enabled") is True, "Gridgeist is not installed and enabled")


def smoke_codex(source: str, timeout: int) -> None:
    version = plugin_version()
    codex = find_command("codex")
    with tempfile.TemporaryDirectory(prefix="gridgeist-codex-smoke-") as temporary:
        root = Path(temporary)
        codex_home = root / "codex-home"
        codex_home.mkdir()
        env = os.environ.copy()
        env.update({"CODEX_HOME": str(codex_home), "CI": "1", "NO_COLOR": "1"})

        marketplace = json_output(
            run([codex, "plugin", "marketplace", "add", source, "--json"], env, timeout),
            "Marketplace add",
        )
        require(marketplace.get("marketplaceName") == SKILL_NAME, "Marketplace add returned the wrong name")

        first_install = json_output(
            run([codex, "plugin", "add", PLUGIN_ID, "--json"], env, timeout),
            "Initial plugin install",
        )
        validate_plugin_install(first_install, version, codex_home)
        validate_plugin_list(
            json_output(run([codex, "plugin", "list", "--json"], env, timeout), "Initial plugin list"),
            version,
        )

        upgrade = json_output(
            run([codex, "plugin", "marketplace", "upgrade", SKILL_NAME, "--json"], env, timeout),
            "Marketplace upgrade",
        )
        require(upgrade.get("errors") == [], "Marketplace upgrade reported errors")

        reinstall = json_output(
            run([codex, "plugin", "add", PLUGIN_ID, "--json"], env, timeout),
            "Plugin reinstall",
        )
        validate_plugin_install(reinstall, version, codex_home)
        validate_plugin_list(
            json_output(run([codex, "plugin", "list", "--json"], env, timeout), "Reinstalled plugin list"),
            version,
        )
    print(f"[OK] Codex plugin clean install, refresh, and reinstall passed for v{version}.")


def validate_skills_list(result: Any, expected_root: Path) -> None:
    require(isinstance(result, list), "Universal installer list output must be an array")
    matches = [entry for entry in result if entry.get("name") == SKILL_NAME]
    require(len(matches) == 1, "Universal installer list must contain exactly one Gridgeist entry")
    listed_path = matches[0].get("path")
    require(isinstance(listed_path, str), "Universal installer list is missing the Gridgeist path")
    require(Path(listed_path).resolve() == expected_root.resolve(), "Universal installer listed an unexpected skill path")


def smoke_skills(source: str, timeout: int) -> None:
    if os.name == "nt":
        find_command("npx.cmd")
        command_shell = os.environ.get("COMSPEC", "cmd.exe")
        skills = [find_command(command_shell), "/d", "/s", "/c", "npx.cmd", "--yes", "skills"]
    else:
        skills = [find_command("npx"), "--yes", "skills"]
    with tempfile.TemporaryDirectory(prefix="gridgeist-skills-smoke-") as temporary:
        home = Path(temporary)
        npm_cache = home / "npm-cache"
        env = os.environ.copy()
        env.update(
            {
                "HOME": str(home),
                "USERPROFILE": str(home),
                "npm_config_cache": str(npm_cache),
            }
        )
        run(
            skills + ["add", source, "-g", "-a", "codex", "-s", SKILL_NAME, "-y", "--copy"],
            env,
            timeout,
            capture=False,
        )
        skill_root = home / ".agents/skills/gridgeist"
        require_inside(skill_root, home, "Universal skill install")
        validate_skill_tree(skill_root)
        require((home / ".agents/.skill-lock.json").is_file(), "Universal installer did not create source metadata")
        validate_skills_list(
            json_output(run(skills + ["list", "-g", "-a", "codex", "--json"], env, timeout), "Initial skills list"),
            skill_root,
        )

        run(skills + ["update", SKILL_NAME, "-g", "-y"], env, timeout, capture=False)
        validate_skill_tree(skill_root)
        validate_skills_list(
            json_output(run(skills + ["list", "-g", "-a", "codex", "--json"], env, timeout), "Updated skills list"),
            skill_root,
        )
    print("[OK] Universal installer clean install and update passed.")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--channel", choices=("all", "codex", "skills"), default="all")
    parser.add_argument("--marketplace-source", default="ohmiler/gridgeist")
    parser.add_argument("--skills-source", default="ohmiler/gridgeist")
    parser.add_argument("--timeout", type=int, default=180, help="Per-command timeout in seconds")
    args = parser.parse_args()

    try:
        if args.channel in ("all", "codex"):
            smoke_codex(args.marketplace_source, args.timeout)
        if args.channel in ("all", "skills"):
            smoke_skills(args.skills_source, args.timeout)
    except (OSError, SmokeError, subprocess.TimeoutExpired, json.JSONDecodeError) as error:
        print(f"[FAIL] {error}", file=sys.stderr)
        return 1

    print("[OK] Gridgeist installation smoke tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
