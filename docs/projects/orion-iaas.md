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

## 1. The Evolution of Orion: From API-First CMDB & Inventory to a High-Availability Dispatcher

Orion was not built as a static monolithic tool, but as an evolving architectural response to enterprise infrastructure bottlenecks at scale within **BBVA Technology** — governing **30,000+ machines** across **AWS, OpenStack, OpenShift, and bare metal**, processing **40,000+ daily operations** for **500+ engineers**:

```mermaid
flowchart TD
    subgraph Origin["1. Origin: API-First CMDB, Inventory & Catalog"]
        direction TB
        CMDB["Orion Control Plane<br/>• Multi-cloud inventory (AWS · OpenStack · OpenShift · Bare-metal)<br/>• Hybrid persistence (PostgreSQL + MongoDB + Redis)<br/>• REST operation catalog (OpenAPI / RBAC)<br/>• Automated compliance audit pipelines"]
    end

    subgraph Replacement["2. Strategic Jenkins Replacement"]
        direction LR
        JNK["Legacy Jenkins<br/>❌ No High Availability (Critical SPOF)<br/>❌ Rigid UI unsuited for ops<br/>❌ Highly complex to maintain, scale & extend"] -.->|"Replaced by"| DISP["Integrated HA Dispatcher in Orion<br/>(Django + Celery + Kubernetes Job Workers)<br/>✅ Native High Availability (HA)<br/>✅ Operation-centric UI & REST APIs<br/>✅ Seamless integration of new banking features"]
    end

    subgraph Expansion["3. Declarative IaC & Applied AI"]
        direction LR
        BP["Blueprint<br/>(Declarative YAML engine, DAG waves & idempotent teardowns)"]
        AI["Orion AI (Validated PoC)<br/>(Multi-agent CI/CD diagnostics with LangGraph)"]
    end

    CMDB -->|"Evolved by integrating"| DISP
    DISP --> BP & AI
```

1. **Phase 1 — The Origin: Multi-Cloud CMDB, Inventory & API-First Catalog:** Orion originated as a centralized control plane to inventory and govern heterogeneous assets across AWS, OpenStack, OpenShift, and bare metal, combining a hybrid database tier (PostgreSQL, MongoDB, Redis), RBAC, and automated compliance audit pipelines directly consumed by bank auditors.
2. **Phase 2 — The Jenkins Bottleneck:** Initially, operation catalog execution relied on Jenkins. However, Jenkins lacked native High Availability (posing a critical single point of failure for the bank), its UI was tailored for software compilation logs rather than infrastructure state machines, and it was notoriously complex to operate, scale, and integrate with new bank functionalities and core systems.
3. **Phase 3 — Evolution into a Purpose-Built HA Dispatcher:** Orion evolved by absorbing the execution plane into a **native High-Availability Operation Dispatcher (Django + Celery + Kubernetes Jobs)**. This migration completely replaced Jenkins for infrastructure workflows, decoupled variables at runtime (preventing configuration drift), and delivered an API-first architecture with isolated ephemeral container execution.
4. **Phase 4 — Declarative Extension (Blueprint) & Operational AI (Orion AI):** With the CMDB and dispatcher united under the same architecture, Orion expanded into declarative provisioning with **Blueprint** (asynchronous YAML engine with DAG waves and idempotent teardowns, eliminating suites like Red Hat Automation Platform) and agentic auto-diagnostics with **Orion AI** (LangGraph).

---

## 2. Context & Problem Statement

Operating infrastructure at banking scale across public cloud, private cloud, container clusters, and legacy data centers created three structural bottlenecks:

1. **Siloed provisioning:** Every target environment (AWS, OpenStack, OpenShift, physical hardware) required its own specialized tooling, credentials, and manual ticket handoffs — turning simple provisioning requests into multi-day waits.
2. **Heterogeneous asset auditing:** Regulatory and internal audit teams require continuous, verifiable snapshots of ownership, security baselines, and machine state across tens of thousands of assets whose underlying metadata schemas look nothing alike.
3. **Vendor integration fragility:** Infrastructure platforms depend on upstream vendor integrations (such as F5 load balancers with OpenStack) that can be deprecated mid-lifecycle without warning.

---

## 3. Abstract System Topology

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

## 4. Core Architectural Decisions

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

## 5. Architectural Trade-Offs

| Decision | Alternative Considered | Rationale |
| :--- | :--- | :--- |
| **Hybrid PostgreSQL + MongoDB** | Single relational DB with JSONB | Kept strict relational integrity for permissions and audit trails while allowing high-speed indexing across deeply heterogeneous cloud metadata schemas. |
| **In-house Python driver abstraction** | Separate provider-native pipelines per cloud | Unified RBAC, product catalog, and audit trail in one control plane; new infrastructure targets are additive modules. |
| **Custom F5/OpenStack REST bridge** | Full load-balancer platform migration | Preserved operational continuity and delivered zero downtime when the vendor deprecated native integration. |

---

## 6. Operational Impact

- **Self-service at scale:** Enabled **500+ engineers** to provision, govern, and remediate infrastructure autonomously across **tens of thousands of nodes**, reducing provisioning lead times from days of ticket handoffs to minutes.
- **Continuous auditability:** Replaced manual compliance evidence gathering with automated, verifiable audit pipelines consumed directly by governance teams.
- **International adoption:** Rolled out across engineering organizations in **Spain, Mexico, and Turkey**, including cross-team onboarding and targeted platform extensions for regional workflows.

---

[:octicons-arrow-right-24: Next: Blueprint — Declarative lifecycle orchestration built on top of Orion](blueprint.md)
