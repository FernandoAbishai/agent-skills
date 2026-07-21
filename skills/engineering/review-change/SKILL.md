---
name: review-change
description: Review a pull request, branch, commit range, or working diff independently across intent, behavior, risk, and design.
---

# Review Change

Review the change through four independent lenses so a strong result in one area cannot hide failure in another.

Use [`templates/four-lens-review.md`](templates/four-lens-review.md) for non-trivial reviews.

## 1. Pin the review target

Resolve and record:

- base ref or merge base;
- head ref;
- commit list;
- complete diff or changed-file list;
- originating issue, specification, or requested behavior;
- repository standards and architectural decisions;
- available test, runtime, and deployment evidence.

If the fixed point is ambiguous, ask or state the assumption explicitly. Do not review an unknown range as though it were complete.

## 2. Review Intent

Determine whether the change solves what was requested.

Look for:

- missing or partial requirements;
- behavior that contradicts the specification;
- unauthorized scope or speculative additions;
- accidental reinterpretation of user intent;
- requirements implemented only for the happy path;
- non-goals that leaked into the diff.

Cite the requirement, issue, or decision source for each intent finding.

## 3. Review Behavior

Determine whether available evidence proves the implementation's behavior.

Check:

- acceptance conditions;
- failure and negative paths;
- state transitions and side effects;
- authorization boundaries;
- test sensitivity to the target behavior;
- runtime paths not exercised by tests;
- mismatch between claimed and observed boundaries.

Missing runtime evidence is a review limitation or release risk, not automatic proof that the code is wrong.

## 4. Review Risk

Select risks based on the actual change surface, including where relevant:

- authentication and authorization;
- tenant or account isolation;
- data integrity and migrations;
- compatibility and version skew;
- concurrency, retries, and idempotency;
- caching and invalidation;
- performance and resource use;
- asynchronous events and duplicate side effects;
- deployment sequencing;
- rollback and observability.

Describe a concrete failure scenario rather than naming a generic category.

## 5. Review Design

Assess whether the change makes future work easier or harder.

Look for:

- duplicated policy or business rules;
- ownership split across unrelated modules;
- leaked implementation details;
- broad change surface for one conceptual change;
- abstraction without current leverage;
- hidden coupling;
- reduced testability;
- names that conceal domain meaning.

Design findings are judgment calls. Label confidence and avoid presenting preferences as correctness defects.

## Finding contract

Every finding must include:

- lens;
- severity;
- confidence;
- file, hunk, or behavioral evidence;
- concrete failure or maintenance scenario;
- recommended correction.

Skip observations already enforced reliably by automated tooling unless the tool result itself is failing or misleading.

## Output

Report the four lenses separately. End with:

- finding counts per lens and severity;
- highest-risk finding in each lens;
- evidence limitations;
- verification still required.

Do not collapse the lenses into one overall grade.

## Completion criterion

The complete intended diff was reviewed, every finding is tied to evidence and a concrete scenario, uncertain judgments are labeled, and missing inputs or runtime proof are explicit.

## Communication

Communicate in the user's language while preserving technical identifiers, code excerpts, command output, and repository terminology.