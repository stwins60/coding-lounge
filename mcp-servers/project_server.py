"""Read public Coding Lounge guides through MCP."""

from __future__ import annotations

import os
import re
from pathlib import Path

from mcp.server import MCPServer


LOUNGE_PATTERN = re.compile(r"^lounge-(0[1-9])-[a-z0-9-]+$")
WORKSPACE_ROOT = Path(os.getenv("LOUNGE_ROOT", Path.cwd())).resolve()

mcp = MCPServer("coding-lounge-project")


def _find_lounges() -> dict[int, Path]:
    lounges: dict[int, Path] = {}
    for candidate in WORKSPACE_ROOT.iterdir():
        match = LOUNGE_PATTERN.fullmatch(candidate.name)
        if candidate.is_dir() and match:
            lounges[int(match.group(1))] = candidate
    return lounges


@mcp.tool()
def list_lounges() -> list[str]:
    """List the Coding Lounge exercises available in this workspace."""
    return [
        f"{number}: {folder.name}"
        for number, folder in sorted(_find_lounges().items())
    ]


@mcp.tool()
def read_lounge_guide(lounge: int) -> str:
    """Read a lounge README without opening templates, bugs, or answer keys."""
    if not 1 <= lounge <= 9:
        raise ValueError("Lounge must be a number from 1 through 9.")

    folder = _find_lounges().get(lounge)
    if folder is None:
        raise ValueError(f"Lounge {lounge} was not found.")
    return (folder / "README.md").read_text(encoding="utf-8")


@mcp.tool()
def search_lounge_guides(query: str) -> list[str]:
    """Find public lounge guides containing a word or short phrase."""
    term = query.strip().casefold()
    if len(term) < 2:
        raise ValueError("Search text must contain at least 2 characters.")
    if len(term) > 100:
        raise ValueError("Search text cannot exceed 100 characters.")

    matches: list[str] = []
    for number, folder in sorted(_find_lounges().items()):
        guide = (folder / "README.md").read_text(encoding="utf-8")
        matching_lines = [line.strip() for line in guide.splitlines() if term in line.casefold()]
        for line in matching_lines[:5]:
            matches.append(f"Lounge {number}: {line}")
    return matches


@mcp.tool()
def get_lounge_checklist(lounge: int) -> list[str]:
    """Return the checklist items from one public lounge guide."""
    guide = read_lounge_guide(lounge)
    return [line[6:].strip() for line in guide.splitlines() if line.startswith("- [ ] ")]


if __name__ == "__main__":
    mcp.run()