---
draft: false
description: >-
  Reflections on nine years of building an internal cloud platform: why owning the central control plane changed our build-vs-buy calculus, and why idempotent teardown is the real test of declarative infrastructure.
slug: declarative-yaml-engine-python
date: 2026-03-01
authors:
  - oredondo
categories:
  - Platform Engineering
  - Python
  - Architecture
tags:
  - IaC
  - Python
  - AsyncIO
  - PlatformEngineering
---

# Nine Years of Internal Cloud Platforms: Why Declarative YAML Replaced Our Commercial Orchestrator

"Never build your own orchestrator" is generally good advice — until you look closely at what your organization already owns and where commercial suites actually spend your engineering budget.

When we evaluated how 500+ engineers should orchestrate full infrastructure environments across our hybrid cloud, the default enterprise option on the table was a commercial suite like **Red Hat Automation Platform (Ansible Tower)**. Instead, we built **Blueprint**: an asynchronous, declarative Python lifecycle engine driven by versioned YAML blueprints.

Here is why that trade-off made sense for us, what we chose *not* to build, and why **teardown** — not creation — is the true test of any infrastructure engine.

<!-- more -->

## 1. Owning the Control Plane Changes the Build-vs-Buy Calculus

Most teams adopt heavy external orchestrators because they have no unified API over their underlying infrastructure.

We were in a different position. Over several years, we had already built **Orion**, our central IaaS platform governing tens of thousands of nodes across AWS, OpenStack, OpenShift, and bare-metal behind a single driver-based REST API. Orion already handled:

- Authentication, RBAC, and compliance policies.
- Provider-specific driver translation.
- Live multi-cloud inventory across PostgreSQL and MongoDB.
- Job tracking and immutable audit trails.

Buying a commercial orchestration suite to sit in front of Orion meant paying per-node licensing fees across tens of thousands of machines just to sequence HTTP calls against an API we already owned — while losing native visibility into Orion's job identifiers when a multi-step deployment failed halfway through.

## 2. Why We Avoided Local State Files

Tools inspired by Terraform often copy its most operationally painful design choice: a separate state file (`tfstate`) that must be stored, locked, and reconciled against reality whenever someone makes an out-of-band change.

Because **Blueprint** was designed specifically for **Orion**, we made a deliberate architectural decision: **no separate state files**.

```mermaid
flowchart LR
    Manifest["Versioned YAML Blueprint<br/>(Desired State in Git)"] --> Engine["Blueprint Async Engine<br/>(DAG & Delta Resolver)"]
    Orion[("Orion Control Plane<br/>(Live Observed State)")] --> Engine
    Engine -->|"Execute only the delta<br/>(Concurrent waves)"| Orion
    Engine --> Report["Structured Audit Report<br/>(Mapped to Orion Job IDs)"]
```

Orion's hybrid database *is* the live source of truth. Before Blueprint executes a wave of operations, it queries Orion directly for the current state of the declared resources and acts only on the delta. There is no state file to corrupt, no stale lock after a crashed CI runner, and no drift between "orchestrator state" and "platform inventory".

## 3. Creation Is Easy; Idempotent Teardown Is the Real Test

Almost any script can provision a greenfield environment when every API returns `200 OK`. Where procedural automation falls apart is **partial failure during teardown**.

Imagine tearing down a 25-resource environment (compute pools, load balancer rules, storage volumes, networks). Step 14 times out because an upstream cloud API is momentarily degraded. What happens when the engineer re-runs the destroy job five minutes later?

- **In procedural playbooks:** Step 1 tries to delete a resource that was already deleted in the first run, fails with `404 Not Found`, and aborts the entire pipeline — forcing an engineer to manually comment out steps or clean up resources by hand.
- **In Blueprint:** Every step in a reverse-dependency teardown queries Orion first. Steps 1 through 13 see that their target resources are already gone, record a clean no-op, and the engine resumes immediately at Step 14.

Making teardown **safe to repeat** turned environment decommissioning from a high-stress manual ticket into a routine self-service operation.

## 4. The Honest Cost of Building In-House

Owning your orchestration engine eliminates commercial licensing and gives you a tight fit with internal compliance, but it is not free:

- **You own the edge cases:** Cycle detection in dependency graphs, partial failure reporting, and schema evolution are now your team's responsibility.
- **Documentation is a first-class engineering deliverable:** A commercial tool comes with public Stack Overflow answers; an internal YAML DSL only succeeds if its error messages, schema validation, and golden-path templates are self-explanatory.

After nine years of evolving this stack, the lesson is straightforward: don't reinvent commodity cloud SDKs — encapsulate them behind drivers. But when the orchestration layer sits directly between your engineers, your auditors, and your core control plane, a lean, well-bounded Python engine can outperform a heavyweight commercial suite in both reliability and cost.

---

*See how Orion and Blueprint fit together in the [Orion IaaS](../../projects/orion-iaas.md) and [Blueprint](../../projects/blueprint.md) case studies.*
