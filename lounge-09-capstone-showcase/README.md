# Lounge 9 — Capstone Showcase

**Tier:** Capstone · **Uses:** OpenAI API, MCP, Agents, AGENTS.md, SKILLS.md, opencode

One agent, everything you've learned, presented live to the lounge.

## Checklist
- [ ] Pick one idea that needs a skill, a tool, and an MCP-style resource.
- [ ] Write its persona, and a matching `AGENTS.md`/`SKILL.md` if you have time.
- [ ] Build and run the whole thing, start to finish.
- [ ] Test 3 real requests and fix whatever breaks.
- [ ] Present it: what it does, what it uses, and what you're proud of.

`working/showcase_agent.py` combines Lounge 2 (persona), Lounge 5
(tools), and Lounge 6 (mini-MCP resource reads) into one agent — read
it as a map of how the pieces fit together before you build your own.

## Check your work
```bash
python harness/check.py lounge09 --file lounge-09-capstone-showcase/template/showcase_agent_template.py
```

## Debugging challenge
`broken/showcase_agent_broken.py` has 3 bugs, one from each earlier
lounge's bug family: a tool that's silently never registered (Lounge 5
style), a crash from a wrong-case attribute (Lounge 5 style), and a
missing conversation entry (Lounge 8 style). If you've done the earlier
lounges, you've already debugged each of these once.
