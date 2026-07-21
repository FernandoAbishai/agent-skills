---
name: ship-with-evidence
description: Prepare a software change for a release decision with named verification, compatibility and migration readiness, observability, rollback, and explicit limitations.
---

# Ship With Evidence

Prepare a release decision. Do not perform the release unless the user separately authorizes the specific push, merge, publish, deployment, migration, or production action.

Use [`templates/release-evidence.md`](templates/release-evidence.md) as the default artifact.

## 1. Gather the release inputs

Collect:

- specification and requirement IDs;
- implementation or slice evidence;
- review findings and their disposition;
- system verification report;
- migration and compatibility plan;
- configuration requirements;
- observability changes;
- rollout and rollback procedures.

Record missing inputs instead of inferring that they exist.

## 2. Confirm scope integrity

Compare the intended release scope with the actual diff, commits, and artifacts.

Check for:

- unrelated changes;
- generated or temporary files;
- debug instrumentation;
- secrets or local configuration;
- partially implemented requirements;
- undocumented operator steps;
- changes that require a different rollout order.

## 3. Assess readiness by evidence

For every material claim, name the supporting command, procedure, artifact, or source.

Review:

- intended behavior and critical negative paths;
- targeted and broader test results;
- runtime verification;
- authorization and data integrity;
- compatibility and version skew;
- schema and data migration readiness;
- performance or capacity evidence;
- configuration and secret dependencies;
- deployment sequencing;
- observability and alerting;
- rollback credibility.

Never say “all tests pass” without naming the commands that ran. Never call a change “safe” without naming the evaluated risk boundary.

## 4. Define monitoring

For each important failure mode, state:

- the signal that would expose it;
- expected healthy behavior;
- inspection or alert mechanism;
- responsible operator where known;
- response or rollback trigger.

A log line that no one will inspect is not an operational signal.

## 5. Define rollback or containment

Document:

- rollback trigger;
- exact procedure;
- compatibility implications;
- data restoration or forward-fix requirements;
- verification after rollback;
- cases where rollback is impossible and containment is required.

Do not describe rollback as “revert the commit” when data, public contracts, or external side effects make that insufficient.

## 6. Produce the Release Evidence Report

Choose one decision:

- **Ready** — required evidence exists and rollback or containment is credible.
- **Ready with accepted risk** — unresolved risks are explicit, owned, and accepted by an authorized decision maker.
- **Not ready** — required proof, compatibility work, monitoring, or rollback is missing.

Scope the decision to the environment and release artifact actually evaluated.

## Authorization boundary

Preparing release evidence does not authorize:

- pushing or merging code;
- publishing packages;
- creating a GitHub release;
- deploying an application;
- changing production configuration or data;
- running migrations.

Perform those actions only when explicitly requested.

## Completion criterion

Evidence supports every readiness claim, known limitations are visible, operators can detect meaningful failure, rollback or containment is executable for accepted risks, and the release decision is separated from authorization to execute it.

## Communication

Communicate in the user's language while preserving technical identifiers, commands, artifact names, errors, and repository terminology.