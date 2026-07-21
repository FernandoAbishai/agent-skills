# Fernando Abishai Agent Skills

**Evidence-driven software engineering workflows for coding agents.**

A practical catalog for Codex, Claude Code, Cursor, OpenCode, and other Agent Skills-compatible tools. The skills are designed to make agents slow down at the decisions that matter, work in verifiable increments, and distinguish a plausible implementation from a proven one.

> **Governing rule:** an agent may propose freely, but it may only claim success after exercising the relevant system boundary and recording the result.

[Spanish documentation](docs/es/README.md) · [Catalog](skills/engineering/README.md) · [Contributing](CONTRIBUTING.md) · [Security](SECURITY.md)

---

## Why this catalog exists

Coding agents often fail in predictable ways:

- they start editing before understanding the requested behavior;
- they plan horizontal layers instead of complete user-visible slices;
- they anchor on the first plausible debugging theory;
- they treat passing unit tests as proof that the system works;
- they report completion without showing reproducible evidence;
- they mix review concerns until important risks disappear inside generic feedback.

This catalog packages software-engineering discipline into small, composable skills with explicit completion criteria and reusable artifacts.

## The Evidence Loop

```text
CLARIFY → SPECIFY → SLICE → IMPLEMENT → DEBUG / REVIEW → VERIFY → SHIP
```

Each stage produces a concrete artifact:

| Stage | Primary artifact | Question answered |
|---|---|---|
| Clarify | Decision Record | What behavior and constraints are actually intended? |
| Specify | Change Specification | What must be true when the change is complete? |
| Slice | Delivery Plan | What is the smallest reversible increment that proves progress? |
| Implement | Evidence Packet | What changed, and what targeted check reacted? |
| Debug | Evidence Ledger | Which observations support or contradict each hypothesis? |
| Review | Four-Lens Review | Does the change satisfy intent, behavior, risk, and design? |
| Verify | Runtime Proof | Does the complete system path work? |
| Ship | Release Evidence | What supports release, monitoring, and rollback? |

## Installation

### Agent Skills CLI

```bash
npx skills@latest add FernandoAbishai/agent-skills
```

List the available skills without installing:

```bash
npx skills@latest add FernandoAbishai/agent-skills --list
```

Install the complete catalog globally for Codex and Claude Code:

```bash
npx skills@latest add FernandoAbishai/agent-skills \
  --skill '*' \
  --agent codex \
  --agent claude-code \
  --global \
  --yes
```

Standalone invocation:

```text
Claude Code: /fernandoabishai <task>
Codex:       $fernandoabishai <task>
```

### Claude Code plugin

```text
/plugin marketplace add FernandoAbishai/agent-skills
/plugin install fa-engineering@fernandoabishai
```

Plugin invocation is namespaced:

```text
/fa-engineering:fernandoabishai <task>
```

## Catalog

### User-invoked workflows

| Skill | Purpose | Main output |
|---|---|---|
| [`fernandoabishai`](skills/engineering/fernandoabishai/) | Route work to the smallest trustworthy workflow | Route card |
| [`setup-engineering-context`](skills/engineering/setup-engineering-context/) | Discover repository commands, boundaries, and architecture facts | Engineering context |
| [`clarify-change`](skills/engineering/clarify-change/) | Resolve load-bearing product and safety decisions | Decision record |
| [`write-change-spec`](skills/engineering/write-change-spec/) | Define behavior without prescribing implementation | Change specification |
| [`plan-delivery`](skills/engineering/plan-delivery/) | Break work into vertical, reversible increments | Slice plan |
| [`implement-change`](skills/engineering/implement-change/) | Implement one verified slice at a time | Evidence packet |

### Model-invoked disciplines

| Skill | Purpose | Main output |
|---|---|---|
| [`debug-with-evidence`](skills/engineering/debug-with-evidence/) | Diagnose failures with competing hypotheses and discriminating experiments | Evidence ledger |
| [`review-change`](skills/engineering/review-change/) | Review intent, behavior, risk, and design independently | Four-lens review |
| [`verify-system`](skills/engineering/verify-system/) | Prove the complete runtime story through real boundaries | Verification matrix |
| [`ship-with-evidence`](skills/engineering/ship-with-evidence/) | Prepare a release decision with monitoring and rollback | Release evidence report |

See the [engineering catalog](skills/engineering/README.md) for invocation guidance, composition rules, and examples.

## Example workflows

### Feature request

```text
/fernandoabishai Add team invitations with expiring links
```

Expected route:

```text
clarify-change → write-change-spec → plan-delivery → implement-change
→ review-change → verify-system → ship-with-evidence
```

### Hard bug

```text
/fernandoabishai Users occasionally receive another user's cached dashboard
```

Expected route:

```text
debug-with-evidence → implement-change → review-change → verify-system
```

### Pull-request review

```text
/fernandoabishai Review this branch against issue #184
```

Expected route:

```text
review-change → verify-system when runtime evidence is missing
```

## Skill design

Every promoted skill follows four rules:

1. **One recognizable failure mode.** A skill must correct a specific agent behavior.
2. **Checkable completion.** The agent must be able to distinguish done from merely plausible.
3. **Progressive disclosure.** Core steps remain in `SKILL.md`; templates and detailed references live beside the skill and load only when needed.
4. **Action safety.** Skills do not authorize pushing, merging, deploying, modifying production data, rotating secrets, or destructive migrations.

Each skill directory may contain:

```text
skill-name/
├── SKILL.md
├── agents/openai.yaml
├── references/
├── templates/
└── examples/
```

Resources are co-located with the skill so installing one skill does not leave broken references.

## Evaluation standard

A skill is not considered improved because its prose sounds stricter. It must create an observable behavioral difference.

Each evaluation should compare:

```text
same repository + same task + same agent
without skill vs. with skill
```

Useful pass criteria include:

- fewer unsupported completion claims;
- earlier discovery of missing requirements;
- a reproducible bug signal before repair;
- smaller and more reversible implementation increments;
- review findings tied to concrete failure scenarios;
- runtime verification at the boundary named in the specification.

Evaluation fixtures and documented results will be added incrementally rather than fabricated.

## Status

This is an early engineering release. The initial lifecycle is usable, but the catalog is not presented as universally superior to established repositories. Its differentiator is narrower: **evidence, completion criteria, runtime proof, and action safety are first-class concerns.**

Planned additions:

- change-impact analysis;
- safe database and data migrations;
- dependency upgrades;
- architecture and boundary design;
- performance investigation;
- merge-conflict resolution;
- issue triage and delivery tracking;
- behavioral evaluation fixtures.

## Attribution and originality

This repository uses the open Agent Skills format and is informed by established software-engineering practices and the broader public skills ecosystem. The workflows, terminology, artifacts, completion criteria, and supporting resources in this repository are original unless a file explicitly states otherwise.

It is not a translation or a renamed mirror of another catalog.

## License

MIT © 2026 Fernando Abishai. See [LICENSE](LICENSE).