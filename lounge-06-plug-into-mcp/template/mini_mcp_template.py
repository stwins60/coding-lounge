"""
Lounge 6 — Plug Into MCP (YOUR TURN)
Build a mini MCP server: list resources, read one, write one.
"""


class MiniMCPServer:
    def __init__(self, files: dict[str, str]):
        self._files = files

    def list_resources(self) -> list[str]:
        # TODO: return the names of every file this server knows about
        return ___

    def read_resource(self, name: str) -> str:
        # TODO: return the contents of the file called `name`
        return ___

    def write_resource(self, name: str, content: str) -> None:
        # TODO: store `content` under `name`
        ___

    def delete_resource(self, name: str) -> None:
        # TODO: remove `name` from this server's files
        ___


def summarize(text: str) -> str:
    """A tiny stand-in 'summary': just the first sentence."""
    first_sentence = text.split(".")[0].strip()
    return first_sentence + "." if first_sentence else ""


def agent_reads_and_summarizes(server: MiniMCPServer, filename: str) -> str:
    # TODO (checklist step 3): read the file through the server, then summarize it
    ___


def agent_writes_a_note(server: MiniMCPServer, filename: str, note: str) -> None:
    # TODO (checklist step 4): write `note` to `filename` through the server
    ___


if __name__ == "__main__":
    server = MiniMCPServer({"diary.txt": "Today I learned about MCP. It connects agents to real data."})
    print("Resources:", server.list_resources())
    print("Summary:", agent_reads_and_summarizes(server, "diary.txt"))
    agent_writes_a_note(server, "todo.txt", "Try a real MCP server next lounge.")
    print("New resource list:", server.list_resources())
    # TODO: delete one resource and print the list again.
