# Lounge 6 — Plug Into MCP

**Tier:** Advanced · **Uses:** MCP, Agents · **Time:** ~1 hour

Connect your agent to an MCP server and let it reach beyond the chat
window.

This lounge uses a **mini MCP** — a pretend server, in plain Python,
that copies the real shape of the Model Context Protocol (list what's
available → read a resource → write a resource) without needing a
network connection or any extra installs. Once this clicks, the real
`mcp` Python SDK works the exact same way, just over JSON-RPC instead
of a Python object.

## Checklist
- [ ] Read `working/mini_mcp.py` from top to bottom and make sure you
      understand every method before opening the template.
- [ ] Implement `list_resources` so it returns the names of every file
      stored in `self._files`.
- [ ] Implement `read_resource` so it returns the contents of the file
      with the given name.
- [ ] Implement `write_resource` so it stores `content` under `name`,
      creating or replacing the entry.
- [ ] Implement `agent_reads_and_summarizes` so it reads the file
      through the server, then returns a summary.
- [ ] Implement `agent_writes_a_note` so it writes a note through the
      server.
- [ ] Run the harness:
      `python harness/check.py lounge06 --file lounge-06-plug-into-mcp/template/mini_mcp_template.py`
- [ ] Run the script directly and confirm the printed output matches
      what you expect: the right resource list, the right summary, and
      the new file appears in the second list.
- [ ] Add a **fourth method** `delete_resource(name)` that removes the
      entry for `name` from `self._files`. Test it in `__main__`.
- [ ] In one sentence written in a comment at the bottom of your file,
      explain what MCP lets an agent do that it *couldn't* do from
      memory alone.

## Check your work
```bash
python harness/check.py lounge06 --file lounge-06-plug-into-mcp/template/mini_mcp_template.py
```

## Debugging challenge
`broken/mini_mcp_broken.py` has **3 bugs**. Read the *entire* file
before touching anything.

1. **Bug 1 — crash right at the start:** `list_resources` references
   an attribute name that doesn't match what `__init__` actually sets.
   Python will raise `AttributeError` the moment `list_resources` is
   called. Find the mismatch and fix it.
2. **Bug 2 — crash a little later:** `read_resource` never returns
   anything — the `return` keyword is missing. The caller gets `None`
   and the code that uses the result crashes. Add the missing `return`.
3. **Bug 3 — silent wrong answer:** `summarize` has been changed to
   return only the **first word** instead of the first sentence. It
   never crashes, but the summary is obviously wrong when you read it.
   Restore the correct logic.

Fix them one at a time. After each fix, re-run and confirm progress.

## Go deeper
- **List + read loop:** Write a helper function `dump_all(server)` that
  calls `list_resources` and then `read_resource` for each name and
  prints them all. Test it with a server that has 3 files.
- **Real summarizer:** Replace the `summarize` stub with one that
  returns the first sentence **and** the total word count in brackets,
  e.g. `"Today I learned about MCP. [8 words]"`.
- **Error handling:** What happens if you call `read_resource` with a
  name that doesn't exist? Add a check that raises a helpful error
  message instead of a confusing `KeyError`.

## Reflect
Write your answers in an `mcp-notes.md` file next to your template:

1. A real MCP server might store files on a remote computer. What would
   your agent need to change to use *that* server instead of your mini
   one? (Think about what stays the same and what changes.)
2. Why is "list resources first, then read" a good pattern rather than
   just guessing a file name?
