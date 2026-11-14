---
title: "Case Study: Orion IaaS Platform & Driver Pipeline"
description: >-
  High-level architecture of BBVA's central IaaS platform — a Python/Django control plane governing tens of thousands of nodes across AWS, OpenStack, OpenShift, and bare metal.
---

# Orion: Central IaaS Platform & Universal Driver Pipeline

| Dimension | Details |
| :--- | :--- |
| **Role** | Sole Architect & Platform Owner |
| **Organization** | BBVA Technology (Core Banking Infrastructure) · 2017 – Present |
| **Scale** | 30,000+ governed machines · 40,000+ daily operations · 500+ engineers |
| **Stack** | Python, Django, DRF, Celery, PostgreSQL, MongoDB, Redis, AWS, OpenStack, OpenShift, F5, Infoblox |

!!! abstract "Architectural summary"

    Orion is the central control plane for infrastructure governance, auditing, and self-service deployment across BBVA's hybrid cloud. It hides four distinct infrastructure substrates (**AWS, OpenStack, OpenShift, and physical bare-metal**) behind a single OpenAPI-documented REST interface, combining a **universal driver deployment pipeline**, a **hybrid relational/document data tier**, and **automated compliance export pipelines**.

---

## 1. Context & Problem Statement

Operating infrastructure at banking scale across public cloud, private cloud, container clusters, and legacy data centers created three structural bottlenecks:

1. **Siloed provisioning:** Every target environment (AWS, OpenStack, OpenShift, physical hardware) required its own specialized tooling, credentials, and manual ticket handoffs — turning simple provisioning requests into multi-day waits.
2. **Heterogeneous asset auditing:** Regulatory and internal audit teams require continuous, verifiable snapshots of ownership, security baselines, and machine state across tens of thousands of assets whose underlying metadata schemas look nothing alike.
3. **Vendor integration fragility:** Infrastructure platforms depend on upstream vendor integrations (such as F5 load balancers with OpenStack) that can be deprecated mid-lifecycle without warning.

---

## 2. Abstract System Topology

Orion was architected from scratch to make the underlying cloud provider effectively invisible to the 500+ engineers consuming it, while centralizing permissions, product catalogs, remediation workflows, and audit trails.

```mermaid
flowchart TD
    subgraph Consumers["Platform Consumers (500+ Engineers)"]
        Portal["Self-Service Portal & CLI"]
        BP["Blueprint Declarative Engine"]
        Systems["Core Bank Systems & CI/CD"]
    end

    subgraph ControlPlane["Orion Control Plane (Python / Django / DRF)"]
        API["OpenAPI / Swagger REST Gateway"]
        RBAC["Centralized RBAC & Product Catalog"]
        Audit["Automated Audit Export Pipelines (CSV / Reports)"]
        Coord["Async Operation Coordinator (Celery)"]
        API --> RBAC --> Coord
        RBAC --> Audit
    end

    subgraph DataTier["Hybrid Persistence & Messaging Tier"]
        PG[("PostgreSQL<br/>Transactional state, RBAC & immutable audit trail")]
        Mongo[("MongoDB<br/>Polymorphic multi-cloud asset inventory")]
        Redis[("Redis<br/>Hot query cache & Celery broker")]
    end

    subgraph DriverLayer["Universal Driver Deployment Pipeline"]
        AWS_D["AWS Driver"]
        OS_D["OpenStack Driver"]
        F5_B["Custom F5 ↔ OpenStack REST Bridge"]
        OSH_D["OpenShift Driver"]
        BM_D["Bare-Metal / On-Prem Driver"]
    end

    Consumers --> API
    Coord <--> PG & Mongo & Redis
    Audit <-- "High-volume analytical queries" --- PG & Mongo
    Coord --> AWS_D & OS_D & OSH_D & BM_D
    OS_D <--> F5_B
```

---

## 3. Core Architectural Decisions

### A. Hybrid Persistence Tier (PostgreSQL + MongoDB + Redis)
A single database engine could not cleanly serve both strict banking compliance and massive multi-cloud inventory queries:

- **PostgreSQL** stores relational entities requiring transactional integrity: permissions (RBAC), product catalogs, operation state transitions, and immutable audit records.
- **MongoDB** ingests polymorphic asset documents across tens of thousands of machines (where an AWS EC2 instance, an OpenStack VM, an OpenShift namespace, and a physical server have completely different attribute trees) and indexes them for high-volume cross-estate querying.
- **Redis** absorbs hot read paths and backs the asynchronous Celery task queues so HTTP endpoints respond immediately while long-running infrastructure workflows execute in the background.

### B. Universal Driver Deployment Pipeline
Instead of maintaining separate deployment pipelines per cloud provider, the deployment engine is built around an **abstract driver interface**:

- **Single contract, swappable backends:** Every infrastructure flavor (AWS, OpenStack, OpenShift, bare-metal) implements a common lifecycle contract. The core platform dispatches the same normalized payload regardless of target environment.
- **Organization-wide deployment standards:** Beyond the software layer, this pattern established the bank's standard deployment philosophy — enabling application teams to ship artifacts to production autonomously without manual intervention from infrastructure teams.

### C. Zero-Downtime Vendor Deprecation Shield (F5 / OpenStack Bridge)
When the official native integration between **F5 Load Balancers** and **OpenStack** was deprecated upstream, relying directly on vendor plugins would have forced a disruptive migration across production environments. Because Orion's driver layer already isolated downstream calls, I engineered a **custom RESTful API bridge** between F5 and OpenStack and slotted it behind the driver boundary — restoring full automated load-balancing interoperability with **zero banking downtime**.

### D. Automated Compliance & Audit Pipelines
Rather than treating compliance as an ad-hoc manual data gathering exercise before inspections, Orion runs automated export pipelines that aggregate operational state across MongoDB and PostgreSQL into structured reports (CSV pipelines) consumed directly by internal auditors and governance stakeholders.

---

## 4. Architectural Trade-Offs

| Decision | Alternative Considered | Rationale |
| :--- | :--- | :--- |
| **Hybrid PostgreSQL + MongoDB** | Single relational DB with JSONB | Kept strict relational integrity for permissions and audit trails while allowing high-speed indexing across deeply heterogeneous cloud metadata schemas. |
| **In-house Python driver abstraction** | Separate provider-native pipelines per cloud | Unified RBAC, product catalog, and audit trail in one control plane; new infrastructure targets are additive modules. |
| **Custom F5/OpenStack REST bridge** | Full load-balancer platform migration | Preserved operational continuity and delivered zero downtime when the vendor deprecated native integration. |

---

## 5. Operational Impact

- **Self-service at scale:** Enabled **500+ engineers** to provision, govern, and remediate infrastructure autonomously across **tens of thousands of nodes**, reducing provisioning lead times from days of ticket handoffs to minutes.
- **Continuous auditability:** Replaced manual compliance evidence gathering with automated, verifiable audit pipelines consumed directly by governance teams.
- **International adoption:** Rolled out across engineering organizations in **Spain, Mexico, and Turkey**, including cross-team onboarding and targeted platform extensions for regional workflows.

---

[:octicons-arrow-right-24: Next: Blueprint — Declarative lifecycle orchestration built on top of Orion](blueprint.md)
