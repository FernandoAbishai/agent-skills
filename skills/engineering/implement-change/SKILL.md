---
name: implement-change
description: Implement an approved specification or delivery plan one coherent, verified slice at a time while preserving authorization and rollback boundaries.
disable-model-invocation: true
---

# Implement a Planned Change

Implement the user's approved specification or delivery plan one approved slice at a time. Do not optimize for the number of files changed or for reaching a final answer quickly; optimize for short feedback distance between a behavior claim and evidence.

Use [`templates/evidence-packet.md`](templates/evidence-packet.md) for each non-trivial slice.

## Safety boundary

Do not push, merge, deploy, modify production data, rotate secrets, contact external users, or run destructive migrations unless the user explicitly requested that exact action.

A specification, plan, ticket, or skill invocation does not itself authorize those actions.

## 1. Pin the active slice

Before editing, state:

- the observable outcome;
- requirement IDs covered;
- the behavior boundary;
- expected change surface;
- targeted verification;
- rollback or containment strategy.

Work on one slice only. If implementation reveals that the slice is invalid or too broad, stop and revise the plan rather than silently expanding scope.

## 2. Establish a baseline

Run the narrowest relevant existing checks before editing. Record pre-existing failures separately.

For behavior changes, establish one of:

- a failing test that detects the missing or broken behavior;
- a baseline test demonstrating current behavior;
- an executable HTTP, CLI, browser, or integration probe;
- a benchmark or measurement for performance work.

The signal must observe the real boundary named by the slice. A shallow test that cannot detect the requested behavior is not a useful baseline.

## 3. Implement the minimum coherent change

Make only the changes required for the active slice.

Prefer existing conventions and interfaces. Add abstractions only when they reduce current complexity or create a boundary required by the specification. Do not add speculative hooks, generic frameworks, or unrelated cleanup.

After each meaningful change, run the narrowest check capable of reacting to it.

## 4. Maintain an Evidence Packet

Record:

```markdown
| Claim | Command or procedure | Result | Artifact or output |
|---|---|---|---|
```

A claim must not be stronger than its evidence. For example, a unit test may prove domain logic but not browser behavior, persistence, authorization, or deployment readiness.

## 5. Inspect the complete slice diff

Before declaring the slice complete:

- compare the diff against the Slice Card or specification;
- identify unrelated or accidental files;
- remove temporary instrumentation and throwaway artifacts;
- confirm secrets and generated credentials are absent;
- check error and negative paths;
- confirm rollback or containment remains credible;
- verify that no later slice is required for this slice's stated outcome.

## 6. Run completion checks

Run:

1. the targeted verification for the active slice;
2. relevant neighboring checks;
3. type checking, linting, or static analysis used by the repository;
4. broader tests only when the slice can affect them.

Use `review-change` for non-trivial diffs. Use `verify-system` when the behavior crosses runtime boundaries or when targeted checks do not prove the complete user path.

Do not commit unless the user requested it or the active repository workflow explicitly requires it.

## Final report

Return:

- slice completed;
- files and behavior changed;
- exact commands executed;
- results and artifacts;
- pre-existing failures;
- remaining risks or evidence gaps;
- whether review or full-system verification is still required.

## Completion criterion

The slice's observable outcome exists, the targeted verification reacts and passes, the evidence supports every completion claim, rollback remains credible, and unrelated work has not leaked into the diff.

## Communication

Communicate in the user's language while preserving technical identifiers, commands, test names, errors, and repository terminology.
