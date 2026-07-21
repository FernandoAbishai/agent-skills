---
name: setup-engineering-context
description: Configure the current repository for engineering work by discovering commands, architecture, domain context, and delivery conventions.
disable-model-invocation: true
---

# Set Up Engineering Context

Inspect before writing. Discover build, test, lint, format, typecheck, development, migration, and deployment commands; workspace layout; architecture documents; issue tracking; and contribution conventions.

Use this source order: explicit user instruction, repository documentation and CI, executable configuration, observed convention, then labeled inference.

First produce a compact in-conversation context report covering:

- project purpose, architecture map, domain language, and trust boundaries;
- exact commands, prerequisites, scope, and verification status;
- durable decisions and ADR links;
- issue workflow and status meanings;
- unresolved uncertainty.

Persist context under `docs/agent/` only when the user requests it, the repository already uses that convention, or the task explicitly establishes durable onboarding documentation. When persistence is justified, use:

- `PROJECT.md`;
- `COMMANDS.md`;
- `DECISIONS.md`;
- `ISSUE-TRACKER.md`.

Do not add repository files merely because this skill was invoked.

Verify the cheapest safe commands. Mark each as verified, discovered but not run, unavailable, or already failing. Never report a command as verified merely because it appears in configuration.

## Completion criterion

Another agent can locate or reproduce the project context, run the correct checks, and identify unresolved uncertainty without repeating unnecessary repository discovery.

## Communication

Communicate in the user's language while preserving technical identifiers.
