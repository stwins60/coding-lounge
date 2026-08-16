# OpenCode Skill Pack

These reusable skills are discovered automatically when OpenCode starts in
this repository. Each skill lives at `.opencode/skills/<name>/SKILL.md`, which
is the current official project-local layout.

## Included skills

| Skill | Use it for |
|---|---|
| `coding-lounge-guide` | Coaching a learner through the nine lounges |
| `debug-coach` | Finding one bug at a time without revealing the answer |
| `grill-me` | Challenging a project plan, stack, security, and best practices |
| `explain-code` | Explaining code and concepts clearly |
| `python-checker` | Checking Python syntax, tests, and behavior |
| `test-writer` | Adding focused automated tests |
| `project-planner` | Turning an idea into small buildable steps |
| `code-reviewer` | Finding defects, risks, and missing tests |
| `safe-refactor` | Improving structure while preserving behavior |
| `readme-writer` | Writing verified setup and usage documentation |
| `git-guide` | Using Git carefully without losing work |
| `skill-maker` | Creating and validating more OpenCode skills |

## Install OpenCode

OpenCode does not have an `opencode install` subcommand. On Windows, install
the OpenCode application with one of these package-manager commands:

```powershell
npm install -g opencode-ai
# or
choco install opencode
# or
scoop install opencode
```

Confirm the installation:

```powershell
opencode --version
```

## Install these skills

No extra command is needed in this repository. Start OpenCode from the repo
root and it discovers `.opencode/skills/*/SKILL.md` automatically:

```powershell
cd path\to\coding-lounge
opencode
```

To install one skill in another project, copy its whole folder into that
project's `.opencode/skills/` directory. For example:

```powershell
Copy-Item -Recurse .opencode\skills\debug-coach C:\path\to\other-project\.opencode\skills\
```

To install skills globally for the current user:

```powershell
$target = Join-Path $HOME '.config\opencode\skills'
New-Item -ItemType Directory -Force $target
Copy-Item -Recurse .opencode\skills\debug-coach $target
```

OpenCode also supports `.agents/skills/` and `.claude/skills/` compatible
locations. Restart OpenCode after adding a skill, then ask it to use the skill
by name, such as: `Use debug-coach to help me understand this error.`

## Troubleshooting

- Spell `SKILL.md` in uppercase.
- Make the frontmatter `name` exactly match its folder name.
- Use lowercase letters, numbers, and single hyphens in names.
- Give every skill a specific `description` so OpenCode can discover it.
- Check skill permissions in `opencode.json` if a valid skill stays hidden.