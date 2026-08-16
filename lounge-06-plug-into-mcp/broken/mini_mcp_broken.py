"""
Lounge 6 — Plug Into MCP (BROKEN)
Three bugs: one crashes right away, one crashes a little later, and one
never crashes at all — it just quietly gives the wrong answer. Fix them
one at a time. For the last one, read the code instead of just running it.
"""


class MiniMCPServer:
    def __init__(self, files: dict[str, str]):
        self.files = files

    def list_resources(self) -> list[str]:
        return list(self._files.keys())

    def read_resource(self, name: str) -> str:
        self._files[name]

    def write_resource(self, name: str, content: str) -> None:
        self._files[name] = content


def summarize(text: str) -> str:
    first_word = text.split(" ")[0].strip()
    return first_word + "." if first_word else ""


def agent_reads_and_summarizes(server: MiniMCPServer, filename: str) -> str:
    content = server.read_resource(filename)
    return summarize(content)


def agent_writes_a_note(server: MiniMCPServer, filename: str, note: str) -> None:
    server.write_resource(filename, note)


if __name__ == "__main__":
    server = MiniMCPServer({"diary.txt": "Today I learned about MCP. It connects agents to real data."})
    print("Resources:", server.list_resources())
    print("Summary:", agent_reads_and_summarizes(server, "diary.txt"))
    agent_writes_a_note(server, "todo.txt", "Try a real MCP server next lounge.")
    print("New resource list:", server.list_resources())
