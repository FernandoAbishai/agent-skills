# Changelog

All notable changes to this repository will be documented here.

The format follows Keep a Changelog principles, and releases use semantic versioning where practical.

## [Unreleased]

## [0.2.0] - 2026-07-21

### Added

- OpenAI interface metadata for all promoted skills, including explicit default prompts and invocation policies.
- Completed feature, debugging, and review examples under `examples/`.
- JSON schema declarations for Claude Code plugin and marketplace manifests.
- Concrete private security reporting instructions and supported-version guidance.

### Changed

- Replaced shared `$ARGUMENTS` dependencies with portable references to the user request and conversation.
- Made persistent `docs/agent/` context files opt-in instead of automatic.
- Strengthened catalog validation with real YAML parsing, specification limits, OpenAI metadata checks, manifest path checks, marketplace checks, and repository-wide relative-link validation.
- Pinned validation dependencies and the public Agent Skills CLI version in CI.
- Bumped the Claude Code plugin to `0.2.0`.
- Clarified that Spanish documentation is an overview and installation entry point rather than a complete translation of every skill.

## [0.1.0] - 2026-07-21

### Added

- Initial evidence-driven engineering lifecycle.
- Agent Skills CLI support.
- Claude Code plugin manifests.
- Ten launch skills covering context setup, clarification, specification, planning, implementation, debugging, review, verification, and release evidence.
- Professional repository documentation and bilingual entry points.
- Co-located templates for routing, clarification, specification, slicing, implementation, debugging, review, verification, and release readiness.
- Contribution and security policies.
- Engineering catalog documentation.
