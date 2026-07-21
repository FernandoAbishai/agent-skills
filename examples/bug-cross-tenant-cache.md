# Example: Cross-Tenant Dashboard Cache

## Symptom

A user occasionally receives dashboard totals belonging to another workspace after switching organizations in the same browser session.

## Route

`debug-with-evidence → implement-change → review-change → verify-system`

## Reproduction

```text
1. Authenticate one browser session with access to workspace A and workspace B.
2. Request the dashboard for A and record the response.
3. Switch to B without clearing the client or server cache.
4. Request the dashboard repeatedly with controlled concurrency.
5. Fail when the returned workspace identifier or totals differ from B.
```

## Competing hypotheses

| Hypothesis | Prediction | Discriminating experiment | Result |
|---|---|---|---|
| Cache key omits workspace ID | A and B resolve to the same cache entry | Log the normalized key for both requests | Supported: keys were identical |
| Client retains the prior response | Network response is correct while rendered data is stale | Compare network payload with DOM state | Rejected: network payload was already wrong |
| Authorization lookup uses stale session state | Requests bypass the selected workspace before cache access | Disable cache and repeat | Rejected: uncached responses were correct |

## Repair

Include the authorized workspace identifier and dashboard version in the server cache key. Reject cache writes when the selected workspace does not match the authorization context.

## Regression protection

The integration test warms workspace A, switches to B in the same authenticated session, then alternates requests concurrently. It asserts the workspace identifier, totals, cache key partition, and absence of cross-tenant values.

## Proof

| Procedure | Expected | Actual | Status |
|---|---|---|---|
| Reduced cache-key reproduction before repair | Cross-tenant value appears | Reproduced in 8 of 20 loops | Failed as expected |
| Same reproduction after repair | Every response belongs to selected workspace | 200 of 200 correct | Passed |
| Uncached requests | Correct tenant values | Correct | Passed |
| Unauthorized workspace request | Rejected without cache read | `403`, no cache hit | Passed |

## Remaining uncertainty

The local representative cache was exercised. Production topology, eviction behavior, and multi-region propagation require release-environment verification.
