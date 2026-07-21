---
name: verify-system
description: Verify a completed feature or fix across the runtime boundaries required by the real user-visible claim, including negative paths and reproducible evidence.
---

# Verify the System Story

Verification proves the requested behavior, not merely that source code exists or isolated checks pass.

Use [`templates/verification-matrix.md`](templates/verification-matrix.md) for non-trivial verification.

## 1. State the claim precisely

Record:

- actor or caller;
- environment;
- preconditions and test data;
- action or trigger;
- expected observable result;
- requirement IDs;
- critical negative behavior.

A claim such as “checkout works” is too broad. State which actor, payment state, inventory state, side effects, and returned result are being verified.

## 2. Trace the required runtime path

Trace only the boundaries required by the claim, for example:

```text
client action → network contract → application logic → authorization
→ persistence or messaging → external side effect → returned state
→ operational signal
```

Do not require every possible layer when the behavior does not cross it. Do not omit a required boundary because source inspection appears convincing.

## 3. Choose evidence at each boundary

Use the narrowest method that still proves the real behavior:

- browser or client interaction;
- HTTP request and response;
- CLI invocation;
- integration test against real infrastructure or a representative local dependency;
- database or event inspection;
- captured external-service sandbox result;
- logs, metrics, traces, or profiler output;
- screenshot or recording when visual behavior matters.

Use controlled, disposable data. Do not expose secrets or modify production state without explicit authorization.

## 4. Exercise critical negative paths

Select negative paths based on risk, including where applicable:

- unauthorized actor;
- invalid or stale state;
- duplicate request or retry;
- dependency timeout or failure;
- conflict or concurrent update;
- rollback or compensating action;
- malformed input;
- partial success.

A happy-path pass does not prove protections or failure behavior.

## 5. Record results honestly

Map each requirement and negative path to one status:

- **Passed** — executed and matched the expected result;
- **Failed** — executed and did not match;
- **Blocked** — could not run because a named dependency or access is missing;
- **Not run** — intentionally omitted with a stated reason.

Do not convert source inspection, model reasoning, or expected test behavior into a runtime pass.

## 6. Produce the verification report

Include:

- environment and data setup;
- exact claim;
- runtime path;
- commands or procedures;
- evidence artifacts;
- requirement matrix;
- negative-path results;
- failures and evidence gaps;
- verdict and confidence.

The verdict must be scoped to what was actually exercised.

## Completion criterion

The actual user-visible or caller-visible claim—not a proxy—has been exercised through every required boundary, critical negative behavior has been checked according to risk, and the evidence is reproducible by another engineer.

## Communication

Communicate in the user's language while preserving technical identifiers, commands, payloads, errors, and repository terminology.