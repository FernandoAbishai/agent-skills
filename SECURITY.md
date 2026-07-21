# Security Policy

## Supported versions

Security fixes are provided for the latest tagged release and the current `main` branch. Older releases may not receive backports.

## Reporting a vulnerability

Do not open a public issue for a vulnerability involving secrets, credentials, authorization bypass, destructive automation, unsafe production behavior, or a skill that causes an agent to exceed the user's authorization.

Preferred reporting methods:

1. Use GitHub private vulnerability reporting for this repository when the **Report a vulnerability** option is available.
2. Otherwise email `mail@triherm.com` with the subject `agent-skills security report`.

Do not include live credentials, access tokens, private keys, proprietary source code, or production customer data. Replace sensitive values with safe reproductions.

Include:

- affected skill and release, version, or commit;
- the unsafe behavior;
- exact reproduction steps using a disposable environment;
- agent and installation method;
- expected safety boundary;
- practical impact;
- suggested mitigation when known.

A report should receive an initial acknowledgement within seven calendar days. Publication and remediation timelines depend on severity and reproducibility.

## Safety model

These skills provide instructions to coding agents. They do not grant permission to:

- push or merge branches;
- deploy applications;
- modify production data;
- rotate or expose secrets;
- run destructive migrations;
- disable security controls;
- contact external users or systems.

The agent must obtain explicit user authorization before performing those actions, regardless of which skill is active.
