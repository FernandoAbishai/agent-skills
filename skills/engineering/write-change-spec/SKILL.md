---
name: write-change-spec
description: Write an implementation-neutral specification from the conversation, issue, decision records, and verified repository context.
disable-model-invocation: true
---

# Write a Change Specification

Convert resolved intent into a document that can judge an implementation independently of the implementer's intentions.

Use [`templates/change-specification.md`](templates/change-specification.md) as the default artifact.

## Inputs

Synthesize:

- the user's request and current conversation;
- issue, PRD, or request text;
- decisions from `clarify-change`;
- verified repository constraints from `setup-engineering-context`;
- existing public contracts and compatibility requirements.

Do not restart discovery unless a missing fact makes the specification contradictory, unsafe, or impossible to evaluate.

## 1. Define the problem and outcome

State the current behavior and requested user-visible outcome without prescribing implementation mechanics.

Avoid vague verbs such as “support,” “improve,” or “handle” unless followed by observable behavior.

## 2. Write behavioral requirements

Assign stable identifiers such as `R1`, `R2`, and `R3`.

For every requirement define:

- actor or caller;
- precondition;
- trigger;
- expected observable result;
- failure or rejection behavior;
- authorization rule;
- acceptance evidence;
- relevant system boundary.

## 3. Define negative behavior

Specify what must not happen:

- unauthorized access;
- duplicate side effects;
- stale or inconsistent state;
- incompatible contract changes;
- data loss;
- silent failure;
- misleading success responses.

Phrase negative behavior as a positive protection or explicit error contract where possible.

## 4. Bound the change

Record:

- in-scope behavior;
- non-goals;
- compatibility constraints;
- security and privacy constraints;
- data and migration considerations;
- performance or capacity requirements;
- observability expectations;
- rollout and rollback requirements.

Do not prescribe files, classes, frameworks, or internal module structure unless those are actual constraints.

## 5. Build the evidence matrix

```markdown
| Requirement | Relevant boundary | Evidence method | Pass condition |
|---|---|---|---|
```

The evidence method must be capable of detecting an incorrect implementation. “Tests pass” is insufficient unless the exact tests and behavior they prove are named.

## 6. Check for specification defects

Before completion, challenge the specification for:

- conflicting requirements;
- unowned open questions;
- hidden implementation assumptions;
- requirements without evidence;
- evidence that observes the wrong boundary;
- unspecified failure behavior;
- accidental scope expansion.

## Output location

Write to the repository's configured documentation location. If no convention exists, use `docs/specs/<descriptive-name>.md`.

Do not overwrite an existing specification silently.

## Completion criterion

A reviewer can determine whether an implementation is correct, incomplete, unsafe, or out of scope using the specification and recorded evidence alone.

## Communication

Communicate in the user's language while preserving technical identifiers, contract names, command output, and repository terminology.
