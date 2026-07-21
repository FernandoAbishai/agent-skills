# Example: Clean Design, Missing Authorization Proof

## Review target

A pull request introduces a well-structured endpoint for exporting workspace audit logs. Unit tests cover filtering and serialization, but the issue requires exports to be restricted to workspace owners.

## Route

`review-change → verify-system`

## Four-lens findings

### Intent

**High confidence, high severity:** the implementation does not demonstrate the owner-only requirement from the issue. The handler delegates to a service without an explicit policy check at the reviewed boundary.

Failure scenario: a workspace administrator or ordinary member can request an export despite the owner-only contract.

Recommendation: enforce the authorization policy at a boundary that cannot be bypassed by alternate callers and add acceptance evidence tied to the issue requirement.

### Behavior

**High confidence, medium severity:** unit tests prove filtering and CSV serialization but do not exercise the authenticated HTTP path or rejected callers.

Missing proof: owner succeeds, administrator fails, member fails, and rejected attempts create no export artifact.

### Risk

**High confidence, high severity:** audit-log exports can contain sensitive user and security activity. A missing role check creates a direct disclosure path.

### Design

**Medium confidence, low severity:** the export service has clear ownership and narrow responsibilities. Keep serialization separate, but place policy enforcement in the shared application boundary rather than only in the HTTP controller.

## Verification matrix

| Caller | Procedure | Expected | Status before correction |
|---|---|---|---|
| Owner | Authenticated export request | `200` and one export artifact | Not run |
| Administrator | Same request | `403`, no artifact | Not run |
| Member | Same request | `403`, no artifact | Not run |
| Unauthenticated caller | Same request | `401`, no artifact | Not run |

## Review verdict

The design is maintainable, but the change is **not ready** because the highest-risk behavioral contract lacks both an evident policy check and runtime proof. A positive design assessment does not override the intent and authorization findings.
