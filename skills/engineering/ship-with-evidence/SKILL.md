---
name: ship-with-evidence
description: Prepare a software change for release with named verification, migration readiness, observability, rollback, and explicit limitations.
---

# Ship With Evidence

Gather the specification, review report, verification results, migration plan, observability changes, and rollback procedure. Record missing evidence.

Check intended behavior and failure paths, targeted and broader test results, compatibility and migration readiness, authorization and data integrity, removal of temporary instrumentation, configuration requirements, rollout ownership, monitoring, rollback, and unrelated diff changes.

Create a Release Proof containing change summary, requirements covered, named evidence, known limitations, migration and compatibility, rollout, observability, rollback, operator actions, and final readiness.

Never say “all tests pass” without naming the commands that ran. Never call a change “safe” without naming the evaluated risk boundary.

Preparing release evidence does not authorize push, merge, deploy, publish, or production mutation. Perform those only when explicitly requested.

## Completion criterion

Evidence supports the stated claims, operators can detect failure, rollback is executable for accepted risks, and missing checks are visible to the decision maker.

## Communication

Communicate in the user's language while preserving technical identifiers.
