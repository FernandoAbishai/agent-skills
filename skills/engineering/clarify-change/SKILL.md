---
name: clarify-change
description: Resolve load-bearing decisions for a feature, bug, or behavior change before specification or planning.
disable-model-invocation: true
---

# Clarify a Software Change

Turn `$ARGUMENTS` and the current conversation into decisions strong enough to plan against. Ask only questions whose answers change behavior, scope, architecture, safety, or proof.

Create a decision table covering actors and permissions, trigger and expected behavior, failure and recovery behavior, compatibility, data ownership, operational constraints, rollout, and rollback. Challenge each material assumption with a concrete edge case. Ask the highest-consequence unresolved question first and use repository evidence for lower-risk decisions.

Record feature-specific decisions in the specification, durable domain language in project context, and durable technical choices in an ADR. Do not create ADRs for temporary sequencing choices.

## Output

Produce a Decision Record with target outcome, resolved decisions, rejected alternatives, accepted assumptions, remaining blockers, and repository context updates.

## Completion criterion

No unresolved decision can materially change acceptance behavior, system boundaries, safety, or the verification strategy.

## Communication

Communicate in the user's language while preserving technical identifiers.
