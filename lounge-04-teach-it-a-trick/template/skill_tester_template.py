"""Lounge 4: build an offline tester for your SKILL.md file."""

import sys
from pathlib import Path

SKILL_PATH = Path(__file__).with_name("SKILL.md")


def count_numbered_steps(text: str) -> int:
    """Count lines that begin with a number followed by a period."""
    # TODO: inspect each stripped line and count 1., 2., 3., and so on.
    return 0


def check_skill(text: str) -> list[tuple[str, bool]]:
    # TODO: replace each False with a real string or counting test.
    return [
        ("Starts with frontmatter", False),
        ("Frontmatter has a name", False),
        ("Frontmatter has a description", False),
        ("Has a Steps section", False),
        ("Has at least 4 numbered steps", False),
        ("Has an Example section", False),
        ("Has no ___ blanks", False),
    ]


def main() -> int:
    text = SKILL_PATH.read_text(encoding="utf-8")
    results = check_skill(text)

    passed = 0
    for name, ok in results:
        print(f"{'PASS' if ok else 'FAIL'}: {name}")
        passed += int(ok)

    print(f"{passed}/{len(results)} checks passed")
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main())