---
name: fernandoabishai
description: Route a software engineering task through this catalog. Invoke explicitly with a feature, bug, refactor, review, migration, release decision, or large initiative.
disable-model-invocation: true
---

# Fernando Abishai Engineering Router

Route `$ARGUMENTS` through the smallest workflow that can produce trustworthy evidence.

Use [`templates/route-card.md`](templates/route-card.md) when the route is not obvious or spans multiple stages.

## Governing rule

A coding agent may propose freely, but it may only claim success after exercising the relevant system boundary and recording the result.

## Classify the work

Choose the closest class based on the user's actual request and available evidence:

| Class | Typical signals | Default route |
|---|---|---|
| Unknown repository | No verified commands, architecture, or test entry points | `setup-engineering-context` |
| Unclear change | Behavior, scope, constraints, or safety decisions conflict | `clarify-change → write-change-spec → plan-delivery` |
| Defined feature | Outcome is clear but delivery and proof are not | `plan-delivery → implement-change → review-change → verify-system` |
| Bug or regression | Existing behavior is broken, intermittent, slow, or wrong | `debug-with-evidence → implement-change → verify-system` |
| Pull request or branch | The user requests review of existing changes | `review-change`, then `verify-system` when runtime proof is missing |
| Release decision | Implementation exists and readiness must be assessed | `verify-system → ship-with-evidence` |
| Large initiative | The work exceeds one safe implementation session | clarify/specify first; plan only the next independently verifiable slices |

## Route selection rules

1. **Use the smallest useful route.** Do not impose the full lifecycle on a trivial, explicit change.
2. **Begin where uncertainty begins.** Do not repeat clarification when a complete specification already exists.
3. **Prefer evidence over ceremony.** Include a stage only when it resolves a real unknown or produces necessary proof.
4. **Re-route when classification changes.** A feature request that reveals an existing defect may require `debug-with-evidence`.
5. **Separate work from authorization.** Selecting a workflow does not authorize pushes, merges, deployments, production writes, secret rotation, or destructive migrations.

## Start the workflow

State a compact Route Card containing:

- task classification;
- selected route;
- why each included stage is necessary;
- which plausible stages were excluded;
- the success evidence expected at the end;
- any authorization boundary relevant to the task.

Then begin the first skill immediately. Do not stop after recommending a route unless the user asked only for routing advice.

## Completion criterion

Routing is complete when the first selected skill is active, unnecessary stages are excluded, the completion evidence is explicit, and no action authority has been inferred from workflow selection.

## Communication

Communicate in the user's language. Preserve code identifiers, commands, error messages, API names, and repository terminology.