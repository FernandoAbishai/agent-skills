---
name: setup-engineering-context
description: Configure the current repository for engineering work by discovering commands, architecture, domain context, and delivery conventions.
disable-model-invocation: true
---

# Set Up Engineering Context

Inspect before writing. Discover build, test, lint, format, typecheck, development, migration, and deployment commands; workspace layout; architecture documents; issue tracking; and contribution conventions.

Use this source order: explicit user instruction, repository documentation and CI, executable configuration, observed convention, then labeled inference.

Create or update a compact context set under `docs/agent/`:

- `PROJECT.md`: purpose, architecture map, domain language, trust boundaries.
- `COMMANDS.md`: exact commands, prerequisites, scope, and verification status.
- `DECISIONS.md`: durable decisions and ADR links.
- `ISSUE-TRACKER.md`: issue workflow and status meanings.

Verify the cheapest safe commands. Mark each as verified, discovered but not run, unavailable, or already failing. Never report a command as verified merely because it appears in configuration.

## Completion criterion

Another agent can locate the project context, run the correct checks, and identify unresolved uncertainty without repeating repository discovery.

## Communication

Communicate in the user's language while preserving technical identifiers.
