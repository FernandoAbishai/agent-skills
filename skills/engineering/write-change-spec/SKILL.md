---
name: write-change-spec
description: Write an implementation-neutral specification from the conversation, issue, decisions, and repository context.
disable-model-invocation: true
---

# Write a Change Specification

Synthesize `$ARGUMENTS`, the conversation, repository context, and resolved decisions into an implementation-neutral specification. Do not restart discovery unless a missing fact makes the specification unsafe or contradictory.

For every requirement, define actor, precondition, trigger, expected result, failure behavior, and acceptance evidence. Use stable IDs such as `R1`, `R2`, and `R3`.

Bound the change with in-scope behavior, explicit non-goals, compatibility, security and privacy constraints, data and migration considerations, operational requirements, rollout, and rollback. Avoid prescribing files, classes, or framework mechanics unless they are requirements.

Create an evidence matrix:

```markdown
| Requirement | Relevant boundary | Evidence | Pass condition |
|---|---|---|---|
```

Write to the configured documentation location or `docs/specs/<name>.md`.

## Completion criterion

A reviewer can judge an implementation right or wrong without relying on the implementer's intentions.

## Communication

Communicate in the user's language while preserving technical identifiers.
