#!/usr/bin/env python3
"""Validate promoted skills, manifests, metadata, and local links."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills" / "engineering"
PLUGIN = ROOT / ".claude-plugin" / "plugin.json"
MARKETPLACE = ROOT / ".claude-plugin" / "marketplace.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_yaml(path: Path) -> dict[str, Any]:
    try:
        value = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        fail(f"invalid YAML in {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)} must contain a YAML mapping")
    return value


def parse_frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} has no YAML frontmatter")
    parts = text.split("---\n", 2)
    if len(parts) != 3:
        fail(f"{path.relative_to(ROOT)} has malformed YAML frontmatter")
    try:
        value = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        fail(f"invalid frontmatter in {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"frontmatter in {path.relative_to(ROOT)} must be a mapping")
    return value


def load_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"invalid JSON in {path.relative_to(ROOT)}: {exc}")
    if not isinstance(value, dict):
        fail(f"{path.relative_to(ROOT)} must contain a JSON object")
    return value


def validate_links(path: Path, allowed_root: Path = ROOT) -> None:
    text = path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        relative = target.split("#", 1)[0]
        if not relative:
            continue
        target_path = (path.parent / relative).resolve()
        if not target_path.is_relative_to(allowed_root.resolve()):
            fail(f"relative link escapes allowed root in {path.relative_to(ROOT)}: {target}")
        if not target_path.exists():
            fail(f"broken relative link in {path.relative_to(ROOT)}: {target}")


def validate_openai_metadata(path: Path, skill_name: str) -> None:
    data = load_yaml(path)
    interface = data.get("interface")
    if not isinstance(interface, dict):
        fail(f"missing interface mapping in {path.relative_to(ROOT)}")
    for key in ("display_name", "short_description", "default_prompt"):
        value = interface.get(key)
        if not isinstance(value, str) or not value.strip():
            fail(f"missing interface.{key} in {path.relative_to(ROOT)}")
    if f"${skill_name}" not in interface["default_prompt"]:
        fail(f"default_prompt must reference ${skill_name} in {path.relative_to(ROOT)}")
    policy = data.get("policy")
    if policy is not None:
        if not isinstance(policy, dict) or not isinstance(policy.get("allow_implicit_invocation"), bool):
            fail(f"policy.allow_implicit_invocation must be boolean in {path.relative_to(ROOT)}")


def main() -> None:
    if not SKILLS_ROOT.exists():
        fail("skills/engineering does not exist")

    skill_dirs = sorted(
        path for path in SKILLS_ROOT.iterdir() if path.is_dir() and (path / "SKILL.md").exists()
    )
    if not skill_dirs:
        fail("no promoted skills found")

    names: set[str] = set()
    paths_by_name: dict[str, Path] = {}
    for directory in skill_dirs:
        skill_file = directory / "SKILL.md"
        frontmatter = parse_frontmatter(skill_file)
        name = frontmatter.get("name")
        description = frontmatter.get("description")

        if not isinstance(name, str) or not NAME_RE.fullmatch(name) or len(name) > 64:
            fail(f"invalid skill name {name!r} in {skill_file.relative_to(ROOT)}")
        if name != directory.name:
            fail(f"skill name {name!r} does not match directory {directory.name!r}")
        if name in names:
            fail(f"duplicate skill name: {name}")
        if not isinstance(description, str) or not description.strip() or len(description) > 1024:
            fail(f"invalid description in {skill_file.relative_to(ROOT)}")
        names.add(name)
        paths_by_name[name] = directory

        validate_links(skill_file, directory)
        openai_yaml = directory / "agents" / "openai.yaml"
        if not openai_yaml.exists():
            fail(f"missing {openai_yaml.relative_to(ROOT)}")
        validate_openai_metadata(openai_yaml, name)

        for markdown in directory.rglob("*.md"):
            validate_links(markdown, directory)

    plugin = load_json(PLUGIN)
    skill_entries = plugin.get("skills")
    if not isinstance(skill_entries, list) or not all(isinstance(item, str) for item in skill_entries):
        fail("plugin.json skills must be a list of paths")
    if len(skill_entries) != len(set(skill_entries)):
        fail("plugin.json contains duplicate skill paths")

    declared_names: set[str] = set()
    for item in skill_entries:
        declared_path = (ROOT / item).resolve()
        if not declared_path.is_relative_to(ROOT.resolve()):
            fail(f"plugin skill path escapes repository: {item}")
        if not declared_path.is_dir() or not (declared_path / "SKILL.md").exists():
            fail(f"plugin skill path does not exist: {item}")
        declared_names.add(declared_path.name)
    if names != declared_names:
        fail(
            f"plugin manifest mismatch; missing={sorted(names - declared_names)}, "
            f"stale={sorted(declared_names - names)}"
        )

    marketplace = load_json(MARKETPLACE)
    plugins = marketplace.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        fail("marketplace.json must declare at least one plugin")
    if not any(isinstance(item, dict) and item.get("name") == plugin.get("name") for item in plugins):
        fail("marketplace.json does not expose the plugin declared by plugin.json")

    for markdown in ROOT.rglob("*.md"):
        if ".git" not in markdown.parts:
            validate_links(markdown)

    print(f"Validated {len(names)} promoted skills, manifests, OpenAI metadata, and links.")


if __name__ == "__main__":
    main()
