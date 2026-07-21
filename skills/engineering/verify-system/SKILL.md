---
name: verify-system
description: Verify a completed feature or fix across the full runtime story, including client, API, authorization, persistence, side effects, and negative paths as applicable.
---

# Verify the System Story

State the exact user-visible claim, actor, environment, preconditions, and expected result. Trace only the boundaries required by that claim: client action, network contract, application logic, authorization, persistence or messaging, external side effects, returned state, and operational signals.

Use controlled data and capture commands, requests, responses, screenshots, queries, or logs needed to prove each boundary. Exercise the highest-risk negative path: unauthorized actor, invalid state, duplicate request, external failure, or rollback scenario as applicable.

Map results to requirement IDs and distinguish passed, failed, not run, and blocked checks. Source inspection is not runtime verification.

## Output

Produce a System Verification Report containing environment, claim, path, evidence artifacts, negative-path result, requirement matrix, limitations, and verdict.

## Completion criterion

The actual user-visible claim—not a proxy—has been exercised through every required boundary and the evidence is reproducible.

## Communication

Communicate in the user's language while preserving technical identifiers.
