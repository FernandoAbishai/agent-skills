---
name: debug-with-evidence
description: Diagnose bugs, regressions, crashes, intermittent failures, wrong output, or performance problems through reproduction, competing hypotheses, and discriminating experiments.
---

# Debug With Evidence

Use the falsifiable loop:

`OBSERVE → CAPTURE → REDUCE → COMPETE → DISCRIMINATE → REPAIR → PROVE`

Record expected and actual behavior, environment, trigger, frequency, affected cases, and unaffected cases. Separate observations from interpretations.

Build the tightest practical reproduction: targeted test, HTTP or CLI harness, browser automation, trace replay, deterministic stress loop, benchmark, or minimal fixture. It must detect the exact symptom.

Reduce the scenario one condition at a time. Maintain an Evidence Ledger:

```markdown
| Observation | Source | Confidence | Supports | Contradicts |
|---|---|---:|---|---|
```

For non-trivial failures, maintain at least two causal hypotheses. Each must predict an observable result. Run the smallest experiment whose outcomes separate the hypotheses. Avoid random patches, broad logging, and single-hypothesis anchoring.

Apply the smallest repair supported by the evidence. Add regression protection at the real behavior boundary. Re-run the reduced reproduction, original scenario, regression check, and relevant neighboring checks. Remove temporary instrumentation.

## Completion criterion

The supported cause explains the observations, meaningful alternatives were discriminated, and the original symptom no longer reproduces.

## Communication

Communicate in the user's language while preserving technical identifiers.
