# Lounge 7 — Run It With Opencode

**Tier:** Advanced · **Uses:** opencode, AGENTS.md, SKILLS.md

Hand a real coding task to opencode and supervise it end to end.

## Checklist
- [ ] Start a fresh project folder and launch opencode inside it.
- [ ] Point it at your `AGENTS.md` and a skill from Lounge 4.
- [ ] Give it one real task — `mission.md` has a starter one.
- [ ] Watch its steps live and pause it if it drifts off track.
- [ ] Review the finished files: one thing it did well, one thing you'd change.

## Try it
```bash
cd lounge-07-run-it-with-opencode/working
opencode
```
Then tell opencode to read `mission.md` and build what it describes.

## Check your work
```bash
python harness/check.py lounge07 --file lounge-07-run-it-with-opencode/template/AGENTS.md
```

## Debugging challenge
`broken/AGENTS.md` has two rules that flatly contradict each other, and
points at a skill file using a path that doesn't actually exist on
disk. Both are the kind of bug that only shows up once you actually try
to use the file — not by reading it quickly.
