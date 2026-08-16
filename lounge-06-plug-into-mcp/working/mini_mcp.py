"""
Lounge 6 — Plug Into MCP (mini version)
Real MCP servers talk JSON-RPC and can live on another machine. This
mini version keeps the exact same shape (list resources -> read a
resource -> write a resource) so you can learn the idea first.
"""


class MiniMCPServer:
    """A pretend MCP server that knows about a handful of files."""

    def __init__(self, files: dict[str, str]):
        self._files = files  # {"notes.txt": "file contents..."}

    def list_resources(self) -> list[str]:
        return list(self._files.keys())

    def read_resource(self, name: str) -> str:
        return self._files[name]

    def write_resource(self, name: str, content: str) -> None:
        self._files[name] = content


def summarize(text: str) -> str:
    """A tiny stand-in 'summary': just the first sentence."""
    first_sentence = text.split(".")[0].strip()
    return first_sentence + "." if first_sentence else ""


def agent_reads_and_summarizes(server: MiniMCPServer, filename: str) -> str:
    """Checklist step 3: agent reads a file through MCP and summarizes it."""
    content = server.read_resource(filename)
    return summarize(content)


def agent_writes_a_note(server: MiniMCPServer, filename: str, note: str) -> None:
    """Checklist step 4: agent creates/edits a file through MCP."""
    server.write_resource(filename, note)


if __name__ == "__main__":
    server = MiniMCPServer({"diary.txt": "Today I learned about MCP. It connects agents to real data."})
    print("Resources:", server.list_resources())
    print("Summary:", agent_reads_and_summarizes(server, "diary.txt"))
    agent_writes_a_note(server, "todo.txt", "Try a real MCP server next lounge.")
    print("New resource list:", server.list_resources())
