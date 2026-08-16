# Lounge 7 — Run It With Opencode

**Tier:** Advanced · **Uses:** opencode, AGENTS.md, SKILL.md · **Time:** ~1 hour

Hand a real coding task to opencode and supervise it end to end.

## Checklist
- [ ] Read `working/AGENTS.md` and `working/mission.md` so you know
      what a finished version looks like before filling in the templates.
- [ ] In `template/AGENTS.md`, replace every `___` with real content:
      give your runner agent a name, list at least **3 specific** things
      it can do and **3 things it must never do**, and write one example
      conversation.
- [ ] In `template/mission.md`, invent your own mission (not the
      countdown timer — make something new). Write a clear task with
      at least **3 numbered requirements**.
- [ ] Run the harness to check your `AGENTS.md`:
      `python harness/check.py lounge07 --file lounge-07-run-it-with-opencode/template/AGENTS.md`
- [ ] Launch opencode inside the `template/` folder and point it at your
      `AGENTS.md`. Give it the mission from your `mission.md`.
- [ ] Watch it work in real time. If it drifts off the mission or tries
      to edit a file it shouldn't, pause it and give a correcting
      instruction.
- [ ] When it finishes, open the output file(s) it created and test them.
      Do they actually do what `mission.md` asked?
- [ ] Write a `review.md` next to the template with two sections:
      **What it did well** and **What I would change**. Each section
      needs at least 2 bullet points.
- [ ] Based on your review, improve either your `AGENTS.md` or your
      `mission.md` (or both) and run opencode again. Did the second run
      do better?

## Try it
```bash
cd lounge-07-run-it-with-opencode/template
opencode
```
Then tell opencode to read `mission.md` and build what it describes.

## Check your work
```bash
python harness/check.py lounge07 --file lounge-07-run-it-with-opencode/template/AGENTS.md
```

## Debugging challenge
`broken/AGENTS.md` has **3 bugs**. Read the file carefully — these
bugs only show up when you actually *use* the file, not just by
glancing at it.

1. **Bug 1 — a rule that contradicts itself:** One item in "What I Can
   Do" directly contradicts one item in "What I Must Never Do". A real
   agent following both rules would freeze — it can't do both. Find
   the contradiction and remove the bad rule.
2. **Bug 2 — skill path doesn't exist:** The `AGENTS.md` references a
   skill file using a relative path that doesn't match the real folder
   layout. The file won't be found when opencode tries to use it. Fix
   the path so it points to the actual skill file.
3. **Bug 3 — example gives away too little:** The one example
   conversation has a reply of just "Done!" — that tells the agent
   nothing about *how* to respond, what detail to include, or what
   format to use. Rewrite the reply to be a genuine, useful example
   response.

## Go deeper
- **Harder mission:** Write a second `mission_hard.md` with a more
  ambitious task (a simple Python script, an HTML page with a form,
  etc.). Run opencode on it and compare how confident it is vs. the
  first mission.
- **Scope guard test:** Add a rule to your `AGENTS.md` that explicitly
  forbids touching a specific fake file (e.g. `secrets.txt`). During
  the run, ask opencode to edit that file anyway. Does the rule hold?
- **Mission debrief:** After two runs, write a third section in
  `review.md` called **What I learned about writing good missions**.

## Reflect
Write your answers in `review.md` under a **Reflect** heading:

1. What's the difference between an agent that *tries* to follow a
   mission and one that *understands* it? What in your `AGENTS.md`
   helped it understand?
2. If opencode edits a file you didn't expect it to, whose "fault" is
   that — the agent, the mission, the `AGENTS.md`, or the human? Why?
