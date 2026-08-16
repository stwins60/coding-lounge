"""Behavior checks for the local MCP servers."""

from __future__ import annotations

import asyncio
import tempfile
from pathlib import Path

from mcp.server import MCPServer

import math_server
import notes_server
import project_server


async def _tool_names(server: MCPServer) -> set[str]:
    tools = await server.list_tools()
    return {tool.name for tool in tools}


def main() -> None:
    assert asyncio.run(_tool_names(project_server.mcp)) == {
        "get_lounge_checklist",
        "list_lounges",
        "read_lounge_guide",
        "search_lounge_guides",
    }
    assert len(project_server.list_lounges()) == 9
    assert "First Contact" in project_server.read_lounge_guide(1)
    assert project_server.search_lounge_guides("personality")
    assert project_server.get_lounge_checklist(1)

    with tempfile.TemporaryDirectory() as directory:
        notes_server.NOTES_ROOT = Path(directory)
        assert notes_server.save_note("loops", "A loop repeats work.") == "Saved loops.md."
        assert notes_server.append_note("loops", "Use for to repeat a known number of times.") == "Updated loops.md."
        assert notes_server.list_notes() == ["loops"]
        assert "Use for" in notes_server.read_note("loops")
        assert notes_server.search_notes("repeat") == ["loops"]

    assert asyncio.run(_tool_names(notes_server.mcp)) == {
        "append_note",
        "list_notes",
        "read_note",
        "save_note",
        "search_notes",
    }
    assert asyncio.run(_tool_names(math_server.mcp)) == {
        "calculate",
        "calculate_percentage",
        "convert_temperature",
        "summarize_numbers",
    }
    assert math_server.calculate(3, "add", 4) == "7"
    assert math_server.convert_temperature(0, "celsius", "fahrenheit") == 32
    assert math_server.calculate_percentage(1, 4) == 25
    assert math_server.summarize_numbers([1, 2, 3, 4])["median"] == 2.5
    print("All MCP server checks passed.")


if __name__ == "__main__":
    main()