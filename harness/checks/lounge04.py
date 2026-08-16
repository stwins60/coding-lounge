"""Lounge 4 — Teach It a Trick (SKILL.md)."""

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TARGET = ROOT / "lounge-04-teach-it-a-trick" / "template" / "SKILL.md"

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def _frontmatter_fields(text: str) -> dict:
    match = FRONTMATTER_RE.match(text)
    if not match:
        return {}
    fields = {}
    for line in match.group(1).splitlines():
        if ":" in line:
            key, _, value = line.partition(":")
            fields[key.strip()] = value.strip()
    return fields


def run(path: Path):
    results = []
    text = path.read_text(encoding="utf-8")
    fields = _frontmatter_fields(text)

    name_ok = bool(fields.get("name")) and fields.get("name") != "___"
    results.append(("Frontmatter has a real name:", name_ok, "" if name_ok else "name is missing or blank"))

    desc_ok = bool(fields.get("description")) and fields.get("description") != "___"
    results.append(
        ("Frontmatter has a real description:", desc_ok, "" if desc_ok else "description is missing or blank")
    )

    steps_present = "## Steps" in text
    results.append(('Has a "## Steps" section', steps_present, "" if steps_present else "heading missing"))

    step_lines = re.findall(r"^\d+\.\s+(.*)$", text, re.MULTILINE)
    results.append(
        ("Lists at least 2 numbered steps", len(step_lines) >= 2, f"found {len(step_lines)}")
    )

    example_present = "## Example" in text
    results.append(('Has an "## Example" section', example_present, "" if example_present else "heading missing"))

    # Logic check: picking the random result should happen before telling
    # the person the result — order matters even though both lines "work".
    pick_index = next(
        (i for i, s in enumerate(step_lines) if "pick" in s.lower() or "random" in s.lower()), None
    )
    tell_index = next(
        (i for i, s in enumerate(step_lines) if "tell" in s.lower() or "say" in s.lower()), None
    )
    if pick_index is not None and tell_index is not None:
        ok = pick_index < tell_index
        results.append(
            ("Steps are in the right order (pick, then tell)", ok,
             "" if ok else "the result is announced before it's picked")
        )

    return results
