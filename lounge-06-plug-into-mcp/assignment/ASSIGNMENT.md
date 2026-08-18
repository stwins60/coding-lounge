# Assignment: Virtual Museum Resource Server

Build a mini MCP-style server that stores museum exhibits instead of files.

Create `assignment/museum_server.py` from scratch. Do not edit or copy the
lounge template.

## Resource Design

Each exhibit has a safe ID, title, room name, and short description.

## Requirements

1. List all exhibit IDs and titles.
2. Read one complete exhibit by ID.
3. Add a new exhibit.
4. Move an exhibit to another room.
5. Search descriptions for a word or phrase.
6. Raise a helpful error when an exhibit does not exist.

Start with at least three exhibits and demonstrate every operation in
`__main__`.

## Evidence

```bash
python lounge-06-plug-into-mcp/assignment/museum_server.py
```

- [ ] The initial list contains three exhibits.
- [ ] Adding an exhibit changes the list.
- [ ] Moving an exhibit changes only its room.
- [ ] Search returns matching exhibits without changing them.
- [ ] I can identify which methods would become MCP tools or resources.
