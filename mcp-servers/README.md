# Python MCP Servers for OpenCode

This folder contains three local MCP servers built with the official Python
SDK. They use stdio, stay on this computer, and require no API keys.

| OpenCode name | Tools | Access |
|---|---|---|
| `lounge_project` | List, read, search, and extract checklists from public guides | Read-only |
| `lounge_notes` | List, read, save, append, and search Markdown learning notes | `data/notes/` only |
| `lounge_math` | Arithmetic, percentages, statistics, and temperature conversion | No file or network access |

## Install

From the repository root on Windows PowerShell:

```powershell
py -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe -m pip install -r mcp-servers\requirements.txt
```

The repository's `opencode.json` registers all three servers. Restart OpenCode,
then confirm they connect:

```powershell
opencode mcp list
```

Example prompts:

```text
Use lounge_project to show the available lounges.
Use lounge_notes to save a note named loops.
Use lounge_math to convert 20 Celsius to Fahrenheit.
Use lounge_project to find guides that mention debugging.
Use lounge_notes to search my notes for loops.
Use lounge_math to summarize 4, 8, 15, 16, 23, and 42.
```

## Test

```powershell
.\.venv\Scripts\python.exe mcp-servers\test_servers.py
```

## Install in another OpenCode project

Copy `mcp-servers/` into the project, install its requirements, and copy the
three `mcp` entries from `opencode.json` into that project's config. Change
the Python path to the other project's virtual environment when necessary.

Do not place secrets in `opencode.json`. If a future server needs one, read it
from an environment variable using OpenCode's `{env:VARIABLE_NAME}` syntax.