# Security Policy

## Reporting a vulnerability

Do not open a public issue for a vulnerability involving secrets, credentials, authorization bypass, destructive automation, or unsafe production behavior.

Use GitHub's private vulnerability reporting when available, or contact the repository owner through the public contact methods on the FernandoAbishai GitHub profile.

Include:

- affected skill and version or commit;
- the unsafe behavior;
- exact reproduction steps;
- agent and installation method;
- expected safety boundary;
- practical impact.

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
