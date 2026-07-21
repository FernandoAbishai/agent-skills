---
name: implement-change
description: Implement an approved specification or delivery slices one verified slice at a time.
disable-model-invocation: true
---

# Implement a Planned Change

Implement `$ARGUMENTS` one approved slice at a time.

## Safety boundary

Do not push, merge, deploy, modify production data, rotate secrets, or run destructive migrations unless the user explicitly requested that exact action.

Pin the current slice: outcome, requirements, affected boundary, verification gate, and rollback. Run targeted baseline checks and record pre-existing failures. For behavior changes, establish a failing or baseline signal at the correct public boundary before editing.

Make the minimum coherent change. After each meaningful step, run the narrowest relevant check and maintain an Evidence Packet:

```markdown
| Claim | Command or procedure | Result | Artifact |
|---|---|---|---|
```

Before completion, compare the diff with the slice, remove temporary instrumentation, identify unrelated files, and confirm rollback remains possible. Use `review-change` for non-trivial diffs and `verify-system` when correctness crosses runtime boundaries.

Do not commit unless the user requested it or the active repository workflow explicitly requires it.

## Completion criterion

The observable outcome exists, its verification gate passes, evidence supports the claim, and unrelated work has not leaked into the diff.

## Communication

Communicate in the user's language while preserving technical identifiers.
