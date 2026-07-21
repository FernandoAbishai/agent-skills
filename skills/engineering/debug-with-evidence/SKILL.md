---
name: debug-with-evidence
description: Diagnose bugs, regressions, crashes, intermittent failures, wrong output, or performance problems through a reproducible signal, competing hypotheses, and discriminating experiments.
---

# Debug With Evidence

Debugging is an evidence-reduction process, not a sequence of plausible edits.

Use this loop:

```text
OBSERVE → CAPTURE → REDUCE → COMPETE → DISCRIMINATE → REPAIR → PROVE
```

Use [`templates/evidence-ledger.md`](templates/evidence-ledger.md) for non-trivial investigations.

## 1. Observe the exact symptom

Record expected behavior, actual behavior, environment, trigger, frequency, affected cases, and unaffected cases. Preserve exact error messages, timings, payloads, and timestamps when available.

Separate observations from interpretations. “The request returned stale data” is an observation. “The cache key is wrong” is a hypothesis.

**Complete when:** the symptom can be stated precisely enough that a reproduction can distinguish this bug from nearby failures.

## 2. Capture a red-capable signal

Build the tightest practical reproduction:

1. targeted automated test at the real behavior boundary;
2. HTTP or CLI harness;
3. browser automation asserting DOM, console, or network behavior;
4. captured trace or payload replay;
5. deterministic stress or concurrency loop;
6. benchmark or profiler capture for performance problems;
7. minimal fixture or throwaway harness.

The signal must detect the exact symptom, not merely confirm that the program ran.

Improve the signal until it is as fast, deterministic, and agent-runnable as the environment permits. For intermittent failures, increase the reproduction rate through looping, concurrency, seeded randomness, controlled timing, or fault injection.

When no credible signal can be built, stop and report the access or artifact required. Do not substitute speculation for reproduction.

**Complete when:** one named command or procedure has been executed and can return a meaningful red or green verdict for the reported symptom.

## 3. Reduce the scenario

Remove inputs, callers, configuration, state, and steps one at a time. Re-run the signal after each reduction.

Keep only conditions that are load-bearing for the failure. Record discoveries in the Evidence Ledger.

**Complete when:** removing any remaining condition changes the verdict or the reason for failure.

## 4. Maintain competing hypotheses

For non-trivial failures, keep at least two plausible causal hypotheses until evidence eliminates alternatives.

Each hypothesis must include:

- the proposed cause;
- the observation it explains;
- a falsifiable prediction;
- evidence that would contradict it.

Avoid single-hypothesis anchoring, random patches, and broad “log everything” instrumentation.

**Complete when:** the leading explanations make distinct observable predictions.

## 5. Run a discriminating experiment

Choose the smallest experiment whose possible outcomes separate the active hypotheses. Change one variable at a time.

Prefer direct inspection, a debugger, a query plan, a profiler, or targeted boundary instrumentation over broad logs. Tag temporary instrumentation so it can be removed reliably.

Update the ledger after each experiment. A failed hypothesis is useful evidence and should remain recorded as rejected, not silently disappear.

**Complete when:** one hypothesis is materially better supported and meaningful alternatives have been contradicted or reduced to explicit residual uncertainty.

## 6. Repair the supported cause

Apply the smallest coherent repair supported by the evidence. Do not bundle speculative cleanup into the same repair.

Add regression protection at the narrowest boundary that still reproduces the real defect. Verify that the protection would fail if the defect were reintroduced; a passing but insensitive test is not protection.

## 7. Prove the repair

Run:

- the reduced reproduction;
- the original un-reduced scenario;
- the new regression protection;
- relevant neighboring checks;
- performance measurements when the issue was performance-related.

Remove temporary instrumentation and throwaway artifacts.

## Final report

Return:

- exact symptom;
- reproduction command or procedure;
- supported root cause;
- evidence supporting it;
- meaningful alternatives rejected;
- repair applied;
- regression protection;
- proof commands and results;
- remaining uncertainty.

## Completion criterion

The supported cause explains the observations, meaningful alternatives were discriminated, the original symptom no longer reproduces, and the recorded regression protection reacts to the defect pattern.

## Communication

Communicate in the user's language while preserving technical identifiers, command output, error messages, and repository terminology.