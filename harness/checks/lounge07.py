"""Lounge 7 — Run It With Opencode."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LOUNGE_DIR = ROOT / "lounge-07-run-it-with-opencode"
DEFAULT_TARGET = LOUNGE_DIR / "template" / "AGENTS.md"

REQUIRED_HEADINGS = ["## Who I Am", "## What I Can Do", "## What I Must Never Do", "## Example Conversations"]


def run(path: Path):
    results = []
    text = path.read_text(encoding="utf-8")

    for heading in REQUIRED_HEADINGS:
        ok = heading in text
        results.append((f'Has a "{heading}" section', ok, "" if ok else "heading missing"))

    lowered = text.lower()
    contradiction = "never edit files outside" in lowered and "anywhere in the repo" in lowered
    results.append(
        ("Rules don't contradict each other about file access", not contradiction,
         "one line says never leave the folder, another says edit anywhere" if contradiction else "")
    )

    # Any relative path mentioned in backticks should actually exist on disk.
    referenced_paths = re.findall(r"`(\.\./[^`]+\.(?:md|py))`", text)
    broken_paths = []
    for rel in referenced_paths:
        if not (path.parent / rel).resolve().exists():
            broken_paths.append(rel)
    ok = len(broken_paths) == 0
    results.append(
        ("Every referenced file path actually exists", ok,
         f"broken path(s): {', '.join(broken_paths)}" if not ok else "")
    )

    mission_path = path.parent / "mission.md"
    if mission_path.exists():
        mission_text = mission_path.read_text(encoding="utf-8")
        ok = "___" not in mission_text
        results.append(("mission.md has no leftover blanks", ok, "" if ok else "fill in every ___"))
        steps = re.findall(r"^\d+\.", mission_text, re.MULTILINE)
        ok = len(steps) >= 2
        results.append(("mission.md lists at least 2 numbered steps", ok, f"found {len(steps)}"))
    else:
        results.append(("mission.md exists next to AGENTS.md", False, "file not found"))

    return results
