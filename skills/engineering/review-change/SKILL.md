---
name: review-change
description: Review a pull request, branch, commit range, or working diff across intent, behavior, risk, and design.
---

# Review Change

Review through four independent lenses: Intent, Behavior, Risk, and Design.

Pin the base ref or merge base, commit list, diff, originating specification, repository standards, and available evidence. Record missing inputs.

- **Intent:** missing requirements, partial behavior, unauthorized scope, or reinterpretation of the request.
- **Behavior:** whether evidence exercises the relevant boundary, failure paths, and acceptance conditions. Missing runtime evidence is a limitation, not proof of failure.
- **Risk:** authorization, tenant isolation, data integrity, migrations, compatibility, concurrency, idempotency, caching, performance, deployment, rollback, and observability according to the actual change surface.
- **Design:** duplicated policy, leaked boundaries, excessive change surface, unclear ownership, unsupported abstractions, and reduced testability.

Every finding must state lens, severity, confidence, evidence, failure scenario, and recommended correction. Report lenses separately so one cannot mask another.

## Completion criterion

Every finding is tied to evidence and a concrete failure scenario, and review limitations are explicit.

## Communication

Communicate in the user's language while preserving technical identifiers.
