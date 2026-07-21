---
name: plan-delivery
description: Break an approved specification into dependency-aware, vertical, reversible delivery slices.
disable-model-invocation: true
---

# Plan Delivery

Turn `$ARGUMENTS` or an approved specification into vertical, reversible slices. Identify the smallest user-observable path through the system. Prefer one working behavior through every required layer over a horizontal sequence such as database, backend, frontend, then tests.

Each Slice Card must include requirements, observable result, likely change surface, dependencies, verification command or procedure, rollback, and completion gate. A slice that only creates unused infrastructure is invalid unless that infrastructure is the deliverable.

Represent blocking edges explicitly. Front-load learning when uncertainty could invalidate later work. Give migrations, permission changes, and public contracts rollout-aware slices.

## Completion criterion

Every requirement is covered, each slice produces a coherent outcome, dependencies are explicit, and each slice can be verified and reversed to the degree required by its risk.

## Communication

Communicate in the user's language while preserving technical identifiers.
