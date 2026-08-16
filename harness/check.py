#!/usr/bin/env python3
"""
Coding Lounge harness — checks a lounge's code or markdown against what
that lounge's checklist expects, without needing a real API key.

Usage:
    python harness/check.py list
    python harness/check.py lounge01
    python harness/check.py lounge01 --file path/to/your_file.py
    python harness/check.py all
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from harness.checks import (  # noqa: E402
    lounge01, lounge02, lounge03, lounge04, lounge05,
    lounge06, lounge07, lounge08, lounge09,
)

LOUNGES = {
    "lounge01": lounge01,
    "lounge02": lounge02,
    "lounge03": lounge03,
    "lounge04": lounge04,
    "lounge05": lounge05,
    "lounge06": lounge06,
    "lounge07": lounge07,
    "lounge08": lounge08,
    "lounge09": lounge09,
}


def run_one(key: str, file_override: str | None = None) -> bool:
    module = LOUNGES[key]
    path = Path(file_override) if file_override else module.DEFAULT_TARGET
    print(f"\n== {key}: {path.relative_to(ROOT) if path.is_absolute() else path} ==")

    if not path.exists():
        print(f"  [FAIL] file not found: {path}")
        return False

    results = module.run(path)
    passed = 0
    for name, ok, detail in results:
        mark = "PASS" if ok else "FAIL"
        line = f"  [{mark}] {name}"
        if detail and not ok:
            line += f" — {detail}"
        print(line)
        passed += int(ok)

    total = len(results)
    print(f"  {passed}/{total} checks passed")
    return passed == total


def main() -> None:
    parser = argparse.ArgumentParser(description="Check Coding Lounge exercises.")
    parser.add_argument("target", help="lounge01..lounge09, 'all', or 'list'")
    parser.add_argument("--file", help="check a specific file instead of the lounge's template")
    args = parser.parse_args()

    if args.target == "list":
        for key in LOUNGES:
            print(key)
        return

    if args.target == "all":
        ok = True
        for key in LOUNGES:
            ok = run_one(key) and ok
        sys.exit(0 if ok else 1)

    if args.target not in LOUNGES:
        print(f"Unknown lounge '{args.target}'. Try: {', '.join(LOUNGES)}, or 'all'.")
        sys.exit(2)

    ok = run_one(args.target, args.file)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
