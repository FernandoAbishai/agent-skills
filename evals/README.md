# Behavioral Evaluations

This directory documents reproducible comparisons between baseline agent behavior and behavior with a skill installed.

## Evaluation contract

Keep these variables fixed:

- coding agent and model;
- repository and commit;
- task wording;
- available tools;
- environment and dependencies;
- time or turn budget where applicable.

Change only whether the target skill is available or explicitly invoked.

## Required record

Each evaluation should include:

```text
scenario/
├── README.md           # task, repository state, expected behavioral difference
├── task.md             # exact user prompt
├── rubric.md           # objective pass and failure criteria
├── baseline.md         # observed run without the skill
└── with-skill.md       # observed run with the skill
```

Do not commit secrets, proprietary source code, or fabricated results.

## What counts as improvement

Strong signals include:

- a real reproduction exists before a bug repair;
- unsupported hypotheses are explicitly rejected;
- a plan delivers vertical behavior rather than disconnected layers;
- a review identifies missing runtime proof;
- the final completion statement names executed commands and their results;
- destructive or production actions remain blocked without authorization.

Weak signals include:

- longer output;
- stricter tone;
- more headings;
- more tests without evidence that they detect the target behavior;
- subjective claims that the response “feels more professional.”

## Current status

Evaluation infrastructure is present, but no benchmark results are claimed yet. Results will be added only after they are run and preserved reproducibly.
