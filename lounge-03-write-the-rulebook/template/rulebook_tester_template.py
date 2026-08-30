"""Lounge 3: build an offline tester for your AGENTS.md rulebook."""

import sys
from pathlib import Path

RULEBOOK_PATH = Path(__file__).with_name("AGENTS.md")
REQUIRED_HEADINGS = [
    "## Who I Am",
    "## What I Can Do",
    "## What I Must Never Do",
    "## Example Conversations",
]


def section_text(text: str, heading: str) -> str:
    """Return the text below one heading and before the next heading."""
    # TODO: split at `heading`, then split again at the next "\n## ".
    return ""


def count_bullets(text: str, heading: str) -> int:
    """Count lines beginning with '- ' inside one section."""
    # TODO: call section_text(), loop through its lines, and count bullets.
    return 0


def check_rulebook(text: str) -> list[tuple[str, bool]]:
    results: list[tuple[str, bool]] = []

    for heading in REQUIRED_HEADINGS:
        # TODO: replace False with a test that finds `heading` in `text`.
        results.append((f"Has {heading}", False))

    # TODO: replace each False with a real test.
    results.append(("Has at least 3 abilities", False))
    results.append(("Has at least 3 restrictions", False))
    results.append(("Has at least 2 examples", False))
    results.append(("Has no ___ blanks", False))
    return results


def main() -> int:
    text = RULEBOOK_PATH.read_text(encoding="utf-8")
    results = check_rulebook(text)

    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        passed += int(ok)

    print(f"{passed}/{len(results)} checks passed")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())