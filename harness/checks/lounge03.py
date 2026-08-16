"""Lounge 3 — Write the Rulebook (AGENTS.md)."""

from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TARGET = ROOT / "lounge-03-write-the-rulebook" / "template" / "AGENTS.md"

REQUIRED_HEADINGS = [
    "## Who I Am",
    "## What I Can Do",
    "## What I Must Never Do",
    "## Example Conversations",
]


def run(path: Path):
    results = []
    text = path.read_text(encoding="utf-8")

    for heading in REQUIRED_HEADINGS:
        ok = heading in text
        results.append((f'Has a "{heading}" section', ok, "" if ok else "heading missing"))

    ok = "___" not in text
    results.append(("No leftover blanks (no ___ left)", ok, "" if ok else "fill in every ___"))

    example_count = text.count("**You:**")
    ok = example_count >= 2
    results.append(
        ("At least 2 example conversations", ok, f"found {example_count}" if not ok else "")
    )

    lowered = text.lower()
    contradiction = "pretend to be a real human" in lowered or "pretend to be human" in lowered
    results.append(
        ("Doesn't tell the agent to impersonate a human", not contradiction,
         "found a rule telling it to pretend to be human" if contradiction else "")
    )

    return results
