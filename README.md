# Fernando Abishai Agent Skills

[![skills.sh](https://skills.sh/b/FernandoAbishai/agent-skills)](https://skills.sh/FernandoAbishai/agent-skills)

Evidence-driven software engineering workflows for Codex, Claude Code, Cursor, OpenCode, and compatible coding agents.

> A coding agent may propose freely, but it may only claim success when the relevant system boundary has been exercised and the result recorded.

## Install

```bash
npx skills@latest add FernandoAbishai/agent-skills
```

Standalone invocation:

```text
Claude Code: /fernandoabishai <task>
Codex:       $fernandoabishai <task>
```

Claude Code plugin installation:

```text
/plugin marketplace add FernandoAbishai/agent-skills
/plugin install fa-engineering@fernandoabishai
```

Plugin invocation:

```text
/fa-engineering:fernandoabishai <task>
```

## Evidence Loop

```text
CLARIFY → SPECIFY → SLICE → IMPLEMENT → DEBUG/REVIEW → VERIFY → SHIP
```

## Initial catalog

### User-invoked workflows

- [`fernandoabishai`](skills/engineering/fernandoabishai/SKILL.md) — route a task to the smallest useful workflow.
- [`setup-engineering-context`](skills/engineering/setup-engineering-context/SKILL.md) — discover project commands and architecture facts.
- [`clarify-change`](skills/engineering/clarify-change/SKILL.md) — resolve load-bearing behavior and safety decisions.
- [`write-change-spec`](skills/engineering/write-change-spec/SKILL.md) — create an implementation-neutral specification with acceptance evidence.
- [`plan-delivery`](skills/engineering/plan-delivery/SKILL.md) — break work into vertical, reversible slices.
- [`implement-change`](skills/engineering/implement-change/SKILL.md) — implement one verified slice at a time.

### Model-invoked disciplines

- [`debug-with-evidence`](skills/engineering/debug-with-evidence/SKILL.md) — diagnose through reproduction, competing hypotheses, and discriminating experiments.
- [`review-change`](skills/engineering/review-change/SKILL.md) — review intent, behavior, risk, and design independently.
- [`verify-system`](skills/engineering/verify-system/SKILL.md) — prove the complete runtime story.
- [`ship-with-evidence`](skills/engineering/ship-with-evidence/SKILL.md) — prepare release proof, monitoring, and rollback.

## Positioning

This repository is not a translation or renamed copy of another catalog. It uses the open Agent Skills format and implements original workflow text, terminology, artifacts, safety boundaries, and completion criteria.

The initial release intentionally starts with a coherent engineering lifecycle. Additional skills for architecture, migrations, impact analysis, domain modeling, research, prototypes, issue triage, and conflict resolution will be added after behavioral evaluation.

## License

MIT.
