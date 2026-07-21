---
name: plan-delivery
description: Break an approved specification into dependency-aware, vertical, reversible delivery slices with explicit verification and rollback.
disable-model-invocation: true
---

# Plan Delivery

Transform the user's request or an approved specification into the smallest sequence of independently useful, independently verifiable increments.

Use [`templates/vertical-slice-card.md`](templates/vertical-slice-card.md) for each slice.

## 1. Identify the first complete behavior path

Trace the minimum path required to produce one observable outcome:

```text
entry point → application behavior → state or side effect → observable result
```

Prefer one working behavior through every required layer over horizontal stages such as “database,” then “backend,” then “frontend,” then “tests.”

A horizontal step is acceptable only when the infrastructure itself is the deliverable or when a prerequisite cannot be safely combined with behavior. State why.

## 2. Map requirements to slices

Every requirement in the specification must be covered by at least one slice. Avoid duplicated ownership that would make completion ambiguous.

Each slice must name:

- the user-observable or caller-observable outcome;
- requirement IDs covered;
- likely change surface;
- behavior boundary;
- dependencies and blocking edges;
- targeted verification command or procedure;
- rollback or reversibility strategy;
- completion gate.

## 3. Order by learning and risk

Front-load a slice when it answers an uncertainty that could invalidate later work.

Give special treatment to:

- schema and data migrations;
- permission and authorization changes;
- public API or event contracts;
- cache invalidation;
- asynchronous side effects;
- compatibility across rolling deployments;
- performance-sensitive paths.

Do not hide a risky migration inside an otherwise ordinary feature slice.

## 4. Keep slices coherent

A valid slice should be small enough to reason about but complete enough to prove a real capability.

Reject slices that:

- only create unused abstractions;
- add speculative extension points;
- cannot be verified until several later slices exist;
- combine unrelated user outcomes;
- require an all-at-once release without explaining why;
- have no credible rollback or containment strategy.

## 5. Check delivery coverage

Before finalizing the plan, verify:

- every requirement and critical negative path is covered;
- every slice has a named success signal;
- dependencies form an acyclic and understandable order;
- the first slice produces meaningful learning or capability;
- the final slice does not contain all integration and verification work;
- rollout and rollback match the risk.

## Output

Return:

1. a one-paragraph delivery strategy;
2. the ordered Slice Cards;
3. a requirement-to-slice coverage table;
4. the critical path;
5. risks that may require re-planning.

## Completion criterion

Every requirement is covered, each slice produces a coherent observable outcome, dependencies are explicit, targeted verification exists, and each slice can be reversed or contained to the degree required by its risk.

## Communication

Communicate in the user's language while preserving technical identifiers, commands, contract names, and repository terminology.
