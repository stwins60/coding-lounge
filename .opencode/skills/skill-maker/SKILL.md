---
name: skill-maker
description: "Create and validate reusable OpenCode agent skills. Use when making a SKILL.md, packaging a repeatable workflow, fixing skill discovery, or adding project and global skills."
compatibility: opencode
metadata:
  workflow: customization
  artifact: skill
---

# Skill Maker

## Steps

1. Define one repeatable job and the phrases that should trigger it.
2. Choose a lowercase hyphenated name with at most 64 characters.
3. Create `.opencode/skills/<name>/SKILL.md` for a project skill.
4. Add YAML frontmatter with matching `name` and a specific `description`.
5. Write ordered steps, expected checks, and important guardrails.
6. Keep the main file concise; place large references or scripts beside it.
7. Verify the folder name, frontmatter, description, and referenced paths.
8. Start OpenCode from the project and ask it to use the skill by name.

OpenCode has no `opencode install <skill>` command. Install project skills by placing their folders under `.opencode/skills/` and global skills under `~/.config/opencode/skills/`.