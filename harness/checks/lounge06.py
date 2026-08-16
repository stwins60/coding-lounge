"""Lounge 6 — Plug Into MCP (mini version, no network needed)."""

from pathlib import Path

from harness.util import import_module_from_path

ROOT = Path(__file__).resolve().parents[2]
DEFAULT_TARGET = ROOT / "lounge-06-plug-into-mcp" / "template" / "mini_mcp_template.py"


def run(path: Path):
    results = []

    try:
        module = import_module_from_path("lounge06_target", path)
    except Exception as e:  # noqa: BLE001
        results.append(("File imports without errors", False, f"{type(e).__name__}: {e}"))
        return results
    results.append(("File imports without errors", True, ""))

    ServerClass = getattr(module, "MiniMCPServer", None)
    if ServerClass is None:
        results.append(("Defines MiniMCPServer", False, "class not found"))
        return results
    results.append(("Defines MiniMCPServer", True, ""))

    try:
        server = ServerClass({"diary.txt": "Today I learned about MCP. It connects agents to real data."})
        names = server.list_resources()
        ok = "diary.txt" in names
        results.append(("list_resources() reports known files", ok, f"got {names!r}" if not ok else ""))
    except Exception as e:  # noqa: BLE001
        results.append(("list_resources() reports known files", False, f"{type(e).__name__}: {e}"))
        return results

    try:
        content = server.read_resource("diary.txt")
        ok = isinstance(content, str) and "MCP" in content
        results.append(("read_resource() returns the real file text", ok, f"got {content!r}" if not ok else ""))
    except Exception as e:  # noqa: BLE001
        results.append(("read_resource() returns the real file text", False, f"{type(e).__name__}: {e}"))

    summarize = getattr(module, "agent_reads_and_summarizes", None)
    if summarize is not None:
        try:
            summary = summarize(server, "diary.txt")
            ok = isinstance(summary, str) and summary.strip().startswith("Today I learned about MCP")
            results.append(
                ("agent_reads_and_summarizes() returns the first sentence", ok,
                 f"got {summary!r}" if not ok else "")
            )
        except Exception as e:  # noqa: BLE001
            results.append(("agent_reads_and_summarizes() returns the first sentence", False, f"{type(e).__name__}: {e}"))
    else:
        results.append(("Defines agent_reads_and_summarizes(server, filename)", False, "function not found"))

    write_note = getattr(module, "agent_writes_a_note", None)
    if write_note is not None:
        try:
            write_note(server, "todo.txt", "Try a real MCP server next lounge.")
            ok = "todo.txt" in server.list_resources() and server.read_resource("todo.txt") == "Try a real MCP server next lounge."
            results.append(("agent_writes_a_note() actually creates the file", ok, "" if ok else "todo.txt missing or wrong content"))
        except Exception as e:  # noqa: BLE001
            results.append(("agent_writes_a_note() actually creates the file", False, f"{type(e).__name__}: {e}"))
    else:
        results.append(("Defines agent_writes_a_note(server, filename, note)", False, "function not found"))

    return results
