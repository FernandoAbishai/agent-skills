# Example: Expiring Team Invitations

## Request

Add team invitations that expire after 72 hours. Only workspace administrators may create invitations, and accepting an invitation must not create duplicate memberships.

## Route

`clarify-change → write-change-spec → plan-delivery → implement-change → review-change → verify-system`

## Decision record excerpt

| Decision | Resolution | Evidence impact |
|---|---|---|
| Who may invite? | Workspace administrators only | Verify authorized and unauthorized callers |
| Expiration clock | Server-generated UTC timestamp, 72 hours after creation | Exercise boundary immediately before and after expiry |
| Repeated acceptance | Return the existing membership without duplicating it | Inspect membership count and response contract |
| Revoked invitation | Reject with a stable error code | Verify no membership side effect |

## Specification excerpt

| Requirement | Relevant boundary | Evidence method | Pass condition |
|---|---|---|---|
| R1: an administrator creates an invitation | HTTP authorization and persistence | Integration request plus stored invitation inspection | `201`, one invitation, expiry approximately 72 hours ahead |
| R2: a non-administrator cannot create one | HTTP authorization | Integration request as member | `403`, no invitation stored |
| R3: a valid invitation creates one membership | API, transaction, persistence | Accept request plus membership query | one membership and accepted state |
| R4: repeated acceptance is idempotent | API and persistence | Submit the same token twice | stable success response and one membership |
| R5: expired or revoked invitations are rejected | API and persistence | Controlled clock or fixture | stable rejection and no membership |

## Delivery slices

1. **Create an authorized invitation.** Add the persistence model and administrator-only creation path. Verify R1 and R2.
2. **Accept a valid invitation once.** Add transactional membership creation. Verify R3.
3. **Protect retries and invalid states.** Add idempotency, expiry, and revocation behavior. Verify R4 and R5.

## Evidence packet excerpt

| Claim | Command or procedure | Result | Artifact |
|---|---|---|---|
| Members cannot invite | `pytest tests/invitations/test_create.py -k member_forbidden` | Passed | test output |
| Acceptance creates one membership | `pytest tests/invitations/test_accept.py -k creates_membership` | Passed | test output |
| Retry remains idempotent | Submit the fixture token twice, then query memberships | Passed: membership count remained `1` | captured response and query |

## Verification verdict

**Passed for the disposable integration environment.** The administrator, unauthorized caller, valid acceptance, repeated acceptance, expired token, and revoked token paths were exercised. Deployment readiness and production migration behavior remain outside this example.
