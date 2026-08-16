"""Store small learning notes in a confined data directory through MCP."""

from __future__ import annotations

import os
import re
from pathlib import Path

from mcp.server import MCPServer


NOTE_NAME_PATTERN = re.compile(r"^[a-z0-9][a-z0-9_-]{0,49}$")
MAX_NOTE_LENGTH = 20_000
NOTES_ROOT = Path(
    os.getenv("LOUNGE_NOTES_DIR", Path(__file__).parent / "data" / "notes")
).resolve()

mcp = MCPServer("coding-lounge-notes")


def _note_path(name: str) -> Path:
    if not NOTE_NAME_PATTERN.fullmatch(name):
        raise ValueError(
            "Note names must use lowercase letters, numbers, hyphens, or underscores."
        )
    return NOTES_ROOT / f"{name}.md"


@mcp.tool()
def list_notes() -> list[str]:
    """List saved learning-note names."""
    if not NOTES_ROOT.exists():
        return []
    return sorted(path.stem for path in NOTES_ROOT.glob("*.md") if path.is_file())


@mcp.tool()
def read_note(name: str) -> str:
    """Read one learning note by its safe name."""
    path = _note_path(name)
    if not path.is_file():
        raise ValueError(f"Note '{name}' does not exist.")
    return path.read_text(encoding="utf-8")


@mcp.tool()
def save_note(name: str, content: str) -> str:
    """Create or replace one Markdown learning note."""
    if not content.strip():
        raise ValueError("Note content cannot be empty.")
    if len(content) > MAX_NOTE_LENGTH:
        raise ValueError(f"Note content cannot exceed {MAX_NOTE_LENGTH} characters.")

    path = _note_path(name)
    NOTES_ROOT.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")
    return f"Saved {path.name}."


@mcp.tool()
def append_note(name: str, content: str) -> str:
    """Add text to an existing learning note without replacing it."""
    if not content.strip():
        raise ValueError("Appended content cannot be empty.")

    path = _note_path(name)
    if not path.is_file():
        raise ValueError(f"Note '{name}' does not exist.")
    existing = path.read_text(encoding="utf-8")
    separator = "" if existing.endswith("\n") else "\n"
    updated = f"{existing}{separator}{content}"
    if len(updated) > MAX_NOTE_LENGTH:
        raise ValueError(f"Note content cannot exceed {MAX_NOTE_LENGTH} characters.")
    path.write_text(updated, encoding="utf-8")
    return f"Updated {path.name}."


@mcp.tool()
def search_notes(query: str) -> list[str]:
    """Find saved notes containing a word or short phrase."""
    term = query.strip().casefold()
    if len(term) < 2:
        raise ValueError("Search text must contain at least 2 characters.")
    if len(term) > 100:
        raise ValueError("Search text cannot exceed 100 characters.")
    if not NOTES_ROOT.exists():
        return []

    matches: list[str] = []
    for path in sorted(NOTES_ROOT.glob("*.md")):
        if path.is_file() and term in path.read_text(encoding="utf-8").casefold():
            matches.append(path.stem)
    return matches


if __name__ == "__main__":
    mcp.run()