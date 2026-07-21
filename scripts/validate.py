#!/usr/bin/env python3
"""Validate the promoted Agent Skills catalog without external dependencies."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills" / "engineering"
PLUGIN = ROOT / ".claude-plugin" / "plugin.json"
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail(f"{path.relative_to(ROOT)} has no YAML frontmatter")
    try:
        block = text.split("---\n", 2)[1]
    except IndexError:
        fail(f"{path.relative_to(ROOT)} has malformed YAML frontmatter")
    result: dict[str, str] = {}
    for line in block.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        result[key.strip()] = value.strip().strip('"').strip("'")
    return result


def validate_links(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    for target in LINK_RE.findall(text):
        if target.startswith(("http://", "https://", "#", "mailto:")):
            continue
        target_path = (path.parent / target.split("#", 1)[0]).resolve()
        if not target_path.exists():
            fail(
                f"broken relative link in {path.relative_to(ROOT)}: {target}"
            )


def main() -> None:
    if not SKILLS_ROOT.exists():
        fail("skills/engineering does not exist")

    skill_dirs = sorted(
        path for path in SKILLS_ROOT.iterdir() if path.is_dir() and (path / "SKILL.md").exists()
    )
    if not skill_dirs:
        fail("no promoted skills found")

    names: set[str] = set()
    for directory in skill_dirs:
        skill_file = directory / "SKILL.md"
        frontmatter = parse_frontmatter(skill_file)
        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")

        if not NAME_RE.fullmatch(name):
            fail(f"invalid skill name {name!r} in {skill_file.relative_to(ROOT)}")
        if name != directory.name:
            fail(f"skill name {name!r} does not match directory {directory.name!r}")
        if name in names:
            fail(f"duplicate skill name: {name}")
        if not description:
            fail(f"missing description in {skill_file.relative_to(ROOT)}")
        names.add(name)

        validate_links(skill_file)
        openai_yaml = directory / "agents" / "openai.yaml"
        if not openai_yaml.exists():
            fail(f"missing {openai_yaml.relative_to(ROOT)}")

        for markdown in directory.rglob("*.md"):
            validate_links(markdown)

    if not PLUGIN.exists():
        fail("missing .claude-plugin/plugin.json")
    plugin = json.loads(PLUGIN.read_text(encoding="utf-8"))
    declared = {
        Path(item).name for item in plugin.get("skills", [])
    }
    if names != declared:
        missing = sorted(names - declared)
        stale = sorted(declared - names)
        fail(f"plugin manifest mismatch; missing={missing}, stale={stale}")

    for path in [ROOT / "README.md", SKILLS_ROOT / "README.md"]:
        validate_links(path)

    print(f"Validated {len(names)} promoted skills and plugin metadata.")


if __name__ == "__main__":
    main()
