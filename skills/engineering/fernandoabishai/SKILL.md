---
name: fernandoabishai
description: Route a software engineering task through this catalog. Invoke explicitly with a feature, bug, refactor, review, migration, or large initiative.
disable-model-invocation: true
---

# Fernando Abishai Engineering Router

Route `$ARGUMENTS` through the smallest workflow that can produce trustworthy evidence.

## Governing rule

A coding agent may propose freely, but it may only claim success when the relevant system boundary has been exercised and the result recorded.

## Routes

- Unclear change: `clarify-change` → `write-change-spec` → `plan-delivery`.
- Defined feature: `plan-delivery` → `implement-change` → `review-change` → `verify-system` → `ship-with-evidence`.
- Bug or regression: `debug-with-evidence` → `implement-change` → `review-change` → `verify-system`.
- Pull request: `review-change`; add `verify-system` when runtime proof is missing.
- Release decision: `verify-system` → `ship-with-evidence`.
- Unknown repository: begin with `setup-engineering-context`.

## Routing rules

State the route, reason, and success evidence in one compact block, then begin the first skill immediately. Do not force the entire lifecycle onto a trivial, explicit change. Re-route when evidence changes the classification.

Never push, merge, deploy, alter production data, rotate secrets, or run destructive migrations without explicit authorization.

## Completion criterion

Routing is complete when the first selected skill is active, unnecessary skills are excluded, and the success signal is explicit.

## Communication

Communicate in the user's language. Preserve code identifiers, commands, error messages, API names, and repository terminology.
