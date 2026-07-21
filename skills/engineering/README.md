# Engineering Skills Catalog

This directory contains the promoted software-engineering skills distributed by the repository.

## Invocation model

### User-invoked workflows

These skills orchestrate complete stages and should normally be started explicitly.

| Skill | Invoke when |
|---|---|
| [`fernandoabishai`](fernandoabishai/) | You want the router to select the smallest trustworthy workflow. |
| [`setup-engineering-context`](setup-engineering-context/) | The repository is unfamiliar or its commands and boundaries are undocumented. |
| [`clarify-change`](clarify-change/) | Important behavior, scope, constraints, or safety decisions are unresolved. |
| [`write-change-spec`](write-change-spec/) | The requested outcome is understood and needs a verifiable specification. |
| [`plan-delivery`](plan-delivery/) | A defined change must be divided into vertical, reversible increments. |
| [`implement-change`](implement-change/) | A specification or slice plan is ready to implement. |

### Model-invoked disciplines

These skills contain reusable engineering discipline and may be activated by the agent when the task matches.

| Skill | Invoke when |
|---|---|
| [`debug-with-evidence`](debug-with-evidence/) | A bug, regression, crash, wrong result, intermittent failure, or performance problem requires diagnosis. |
| [`review-change`](review-change/) | A branch, pull request, or diff needs independent review across intent, behavior, risk, and design. |
| [`verify-system`](verify-system/) | The implementation exists but complete runtime behavior has not been proven. |
| [`ship-with-evidence`](ship-with-evidence/) | A release decision needs explicit proof, monitoring, and rollback readiness. |

## Composition

The default lifecycle is:

```text
setup-engineering-context
  ↓
clarify-change
  ↓
write-change-spec
  ↓
plan-delivery
  ↓
implement-change
  ↓
review-change
  ↓
verify-system
  ↓
ship-with-evidence
```

This is not a mandatory pipeline. The router should remove stages that do not add evidence.

Examples:

```text
Small, explicit fix
implement-change → review-change → verify-system

Hard bug
debug-with-evidence → implement-change → verify-system

Review only
review-change

Release readiness
verify-system → ship-with-evidence
```

## Shared principles

### Evidence before completion

A tool exit code, changed file, or plausible explanation is not sufficient by itself. Completion requires a result at the boundary relevant to the requested behavior.

### Smallest useful workflow

Do not impose a full ceremony on a trivial task. Use only the skills required to resolve uncertainty and produce proof.

### Reversible progress

Prefer increments that can be verified and reverted independently. A slice should cross the layers necessary to create one observable capability.

### Separate observation from interpretation

Debugging, review, and verification artifacts should distinguish what was observed from what is inferred.

### Explicit authorization

No skill authorizes pushes, merges, deployments, production writes, secret rotation, or destructive migrations.

## Resource convention

Detailed resources live inside the skill that uses them:

```text
<skill>/
├── SKILL.md
├── agents/openai.yaml
├── references/
├── templates/
└── examples/
```

This ensures that installing a single skill also installs its supporting material.
