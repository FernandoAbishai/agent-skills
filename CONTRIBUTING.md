# Contributing

Contributions should improve observable agent behavior, not only add more instructions.

## Before proposing a skill

Describe:

1. the recurring engineering failure mode;
2. why existing skills do not already cover it;
3. the behavior the skill should produce;
4. the artifact or completion criterion that makes the behavior checkable;
5. at least one evaluation scenario.

## Skill requirements

A promoted skill must:

- use a lowercase hyphenated directory name;
- contain a valid `SKILL.md` with YAML frontmatter;
- have a narrow and recognizable responsibility;
- state when it should be invoked;
- include a checkable completion criterion;
- preserve user authorization boundaries;
- keep supporting resources inside the skill directory;
- avoid references that disappear when the skill is installed alone;
- communicate with the user in the user's language while preserving technical identifiers.

## Directory structure

```text
skills/engineering/<skill-name>/
├── SKILL.md
├── agents/openai.yaml
├── references/      # optional
├── templates/       # optional
└── examples/        # optional
```

## Evaluation

Use the same agent, repository, task, and starting state for both runs:

```text
baseline run without the skill
comparison run with the skill
```

Record behavioral differences and failure cases. Do not claim improvement from prompt length, tone, or subjective preference alone.

## Pull request checklist

- [ ] The skill solves one clear failure mode.
- [ ] The description contains accurate invocation triggers.
- [ ] Completion is externally checkable.
- [ ] Resources are co-located and linked correctly.
- [ ] Examples do not contain secrets or private data.
- [ ] Destructive actions require explicit authorization.
- [ ] Plugin manifests are updated for promoted skills.
- [ ] README catalog entries are updated.
