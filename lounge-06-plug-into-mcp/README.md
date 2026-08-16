# Lounge 6 — Plug Into MCP

**Tier:** Advanced · **Uses:** MCP, Agents

Connect your agent to an MCP server and let it reach beyond the chat
window.

This lounge uses a **mini MCP** — a pretend server, in plain Python,
that copies the real shape of the Model Context Protocol (list what's
available → read a resource → write a resource) without needing a
network connection or any extra installs. Once this clicks, the real
`mcp` Python SDK works the exact same way, just over JSON-RPC instead
of a Python object.

## Checklist
- [ ] Connect to the mini MCP server (or the class demo server).
- [ ] List the resources it hands your agent.
- [ ] Ask your agent to read a file through MCP and summarize it.
- [ ] Ask your agent to create or edit a file through MCP.
- [ ] Explain in one sentence what MCP let it do that it couldn't before.

## Check your work
```bash
python harness/check.py lounge06 --file lounge-06-plug-into-mcp/template/mini_mcp_template.py
```

## Debugging challenge
`broken/mini_mcp_broken.py` has 3 bugs: a crash, a function that
forgets to hand back its answer, and one that runs fine but returns the
*wrong* answer — the hardest kind to catch, since nothing errors at
all. Read the code, don't just trust that it ran.
