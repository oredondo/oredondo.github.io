---
draft: false
description: >-
  Why an enterprise platform team replaced a commercial orchestration suite with a lean, idempotent AsyncIO engine driven by declarative YAML.
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

# Why We Built Our Own Declarative YAML Engine in Python

In enterprise infrastructure, the default answer to orchestration is usually to purchase a commercial platform suite like Red Hat Automation Platform (Ansible Tower) or force an off-the-shelf tool into workflows it was never designed to handle.

Here is why we decided to engineer **Blueprint** — an in-house asynchronous Python orchestration engine — and how it eliminated vendor lock-in while providing true idempotency across tens of thousands of banking infrastructure nodes.

<!-- more -->

## The Trap of Commercial Platforms

Commercial orchestration platforms often suffer from three fatal flaws when applied to custom enterprise architectures:

1. **Restrictive Licensing Models:** License costs scale with managed hosts or operational frequency, penalizing automation growth.
2. **Opaque Execution & Audit Gaps:** When an automated job fails midway through a 50-step sequence, reconstructing the exact state for audit compliance is notoriously painful.
3. **Impedance Mismatch:** Enterprise internal APIs (like our proprietary Orion platform) require tailored retry semantics, dynamic variable injection, and custom rollback policies.

## The Solution: Declarative Asynchronous Blueprints

We conceived **Blueprint** around three design principles:

### 1. Declarative YAML Specifications
Developers should not write procedural execution scripts. They declare the desired end-state of their infrastructure stack in version-controlled YAML files:

```yaml
version: "2.0"
target_environment: "aws-production"

resources:
  - name: "payment-worker-pool"
    type: "compute.instance_group"
    count: 12
    flavor: "m5.xlarge"
    driver: "aws"
    
  - name: "payment-redis-cache"
    type: "cache.cluster"
    engine: "redis"
    depends_on: ["payment-worker-pool"]
```

### 2. Directed Acyclic Graph (DAG) Execution
The Python engine parses the YAML manifest, validates it against a JSON Schema, and constructs an in-memory execution DAG. Independent components are provisioned concurrently using Python's `asyncio.gather()`, while strictly serializing dependencies.

### 3. Idempotent Teardowns
Unlike naive automation scripts that break if an asset is already deleted, Blueprint's destroy operation verifies live state before executing actions, safely resuming interrupted teardowns without manual database manipulation.

## Conclusion

Building your own platform engine is not about reinventing the wheel — it is about knowing when an off-the-shelf product costs more in licenses and operational friction than a clean, 2,000-line asynchronous Python engine that fits your exact organizational topology.

---

*Read the full architecture in the [Blueprint case study](../../projects/blueprint.md).*
