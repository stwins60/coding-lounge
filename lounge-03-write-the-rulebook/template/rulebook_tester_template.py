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
    if heading not in text:
        return ""

    section = text.split(heading, 1)[1]

    if "\n## " in section:
        section = section.split("\n## ", 1)[0]

    return section.strip()


def count_bullets(text: str, heading: str) -> int:
    """Count lines beginning with '- ' inside one section."""
    section = section_text(text, heading)

    count = 0

    for line in section.splitlines():
        if line.strip().startswith("- "):
            count += 1

    return count


def check_rulebook(text: str) -> list[tuple[str, bool]]:
    results: list[tuple[str, bool]] = []

    for heading in REQUIRED_HEADINGS:
        results.append((f"Has {heading}", heading in text))


    abilities = count_bullets(text, "## What I Can Do")
    results.append(("Has at least 3 abilities", abilities >= 3))


    restrictions = count_bullets(text, "## What I Must Never Do")
    results.append(("Has at least 3 restrictions", restrictions >= 3))


    examples_section = section_text(text, "## Example Conversations")


    example_lines = 0
    for line in examples_section.splitlines():
        stripped = line.strip()
        if stripped.startswith("**You:**"):
            example_lines += 1

    results.append(("Has at least 2 examples", example_lines >= 2))


    results.append(("Has no ___ blanks", "___" not in text))

    return results


def main() -> int:
    if not RULEBOOK_PATH.exists():
        print(f"ERROR: Could not find {RULEBOOK_PATH}")
        return 1

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