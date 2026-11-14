---
title: "Case Study: Orion IaaS Platform & Universal Driver Pipeline"
description: >-
  Architecture of BBVA's central IaaS control plane — a Python/Django platform governing 30,000+ machines across AWS, OpenStack, OpenShift, and bare metal with comprehensive auditability, layered Ansible operations (Ground + User), and API-driven scheduled automation.
---

# Orion: Central IaaS Platform & Universal Driver Pipeline

| Dimension | Details |
| :--- | :--- |
| **Role** | Sole Architect & Platform Owner |
| **Organization** | BBVA Technology (Core Banking Infrastructure) · 2017 – Present |
| **Scale** | 30,000+ governed machines · 40,000+ daily operations · 500+ engineers |
| **Stack** | Python, Django, DRF, Celery, PostgreSQL, MongoDB, Redis, Ansible, AWS, OpenStack, OpenShift, Infoblox |

!!! abstract "Architectural summary"

    Orion is the central control plane for infrastructure governance, comprehensive auditing, and self-service deployment across BBVA's hybrid cloud. It abstracts four technological substrates (**AWS, OpenStack, OpenShift, and physical bare-metal**) behind an OpenAPI-documented REST interface and scheduled **automation schedulers**, combining a **universal driver provisioning pipeline**, **two-layer Ansible configuration (corporate Ground + User workloads)**, a **hybrid persistence tier**, and an **end-to-end machine traceability audit engine**.

---

## 1. The Evolution of Orion: From API-First CMDB & Inventory to a High-Availability Dispatcher

Orion was not built as a static monolithic tool, but as an evolving architectural response to enterprise infrastructure bottlenecks at scale within **BBVA Technology** — governing **30,000+ machines** across **AWS, OpenStack, OpenShift, and bare metal**, processing **40,000+ daily operations** for **500+ engineers**:

```mermaid
flowchart TD
    subgraph Origin["1. Origin: API-First CMDB, Inventory & Catalog"]
        direction TB
        CMDB["Orion Control Plane<br/>• Multi-cloud inventory (AWS · OpenStack · OpenShift · Bare-metal)<br/>• Hybrid persistence (PostgreSQL + MongoDB + Redis)<br/>• API-driven REST & scheduled operations<br/>• Comprehensive RBAC audit & machine traceability"]
    end

    subgraph Replacement["2. Strategic Jenkins Replacement"]
        direction LR
        JNK["Legacy Jenkins<br/>❌ No High Availability (Critical SPOF)<br/>❌ Rigid UI unsuited for ops<br/>❌ Highly complex to maintain, scale & extend"] -.->|"Replaced by"| DISP["Integrated HA Dispatcher in Orion<br/>(Django + Celery + Kubernetes Job Workers)<br/>✅ Native High Availability (HA)<br/>✅ REST APIs & scheduled execution<br/>✅ Two-layer Ansible pipeline: Ground + User"]
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
3. **Phase 3 — Evolution into a Purpose-Built HA Dispatcher:** Orion evolved by absorbing the execution plane into a **native High-Availability Operation Dispatcher (Django + Celery + Kubernetes Jobs)**. This migration completely replaced Jenkins for infrastructure workflows, decoupled runtime variables, enabled API-driven and scheduled operations, and structured provisioning into two phases: cloud drivers followed by layered Ansible automation (Ground and User).
4. **Phase 4 — Declarative Extension (Blueprint) & Operational AI (Orion AI):** With the CMDB, the audit engine, and the dispatcher unified under the same architecture, Orion expanded into declarative provisioning with **Blueprint** (asynchronous YAML engine with DAG waves and idempotent teardowns, eliminating suites like Red Hat Automation Platform) and agentic auto-diagnostics with **Orion AI** (LangGraph).

---

## 2. Context & Problem Statement

Operating infrastructure at banking scale across public cloud, private cloud, container clusters, and legacy data centers created three structural bottlenecks:

1. **Siloed provisioning & heterogeneity:** Every target environment (AWS, OpenStack, OpenShift, physical hardware) required its own specialized tooling, credentials, and manual ticket handoffs — turning simple provisioning requests into multi-day waits.
2. **Audit blindness & fragmented traceability:** In a strictly regulated banking environment, infrastructure provisioning requires proof of authorization: who requested the asset, who holds permissions, **what exact software packages are installed on each machine, and every operational event that occurred over its entire lifecycle**. Dispersed provider logs prevented rapid, reliable audit and forensic reporting.
3. **Configuration drift & baseline security vulnerabilities:** Without an enforced operational baseline, application teams provisioned systems inconsistently, resulting in servers lacking mandatory monitoring agents, unpatched operating systems, or non-compliant corporate package repositories.

---

## 3. Abstract System Topology

Orion governs the full infrastructure lifecycle: from REST API calls or scheduled jobs, through cloud provisioning drivers and layered Ansible configurations, down to an immutable forensic audit record.

```mermaid
flowchart TD
    subgraph Consumers["Operation Triggers (API-Driven & Schedulers)"]
        direction TB
        API_Call["REST API / OpenAPI (Self-Service & CI/CD)"]
        Schedulers["Schedulers & Periodic Workflows (Celery Beat)"]
        BP["Blueprint Declarative Engine"]
    end

    subgraph ControlPlane["Orion Control Plane (Python / Django / DRF)"]
        API_GW["OpenAPI / Swagger REST Gateway"]
        RBAC["Centralized RBAC & Permission Control"]
        Coord["HA Dispatcher & Async Coordinator (Celery)"]
        Audit["Comprehensive Audit & Traceability Engine"]
        
        API_GW --> RBAC --> Coord
        Schedulers --> Coord
        RBAC --> Audit
        Coord --> Audit
    end

    subgraph DataTier["Hybrid Persistence & Audit Trail Tier"]
        PG[("PostgreSQL<br/>RBAC, transactional state & immutable history")]
        Mongo[("MongoDB<br/>Polymorphic inventory & installed software state")]
        Redis[("Redis<br/>Query caching & Celery broker")]
    end

    subgraph ProvisioningTier["1. Multi-Cloud Provisioning (Driver Layer)"]
        AWS_D["AWS Driver"]
        OS_D["OpenStack Driver"]
        OSH_D["OpenShift Driver"]
        BM_D["Bare-Metal / On-Prem Driver"]
    end

    subgraph ConfigTier["2. Layered Ansible Configuration Pipeline"]
        direction TB
        Ground["Ground Layer (Mandatory)<br/>• Hardening & baseline bank security<br/>• Monitoring & observability agents<br/>• Approved corporate repositories & core packages"]
        UserOp["User Layer<br/>• Workload & application deployment<br/>• Business logic & middleware configuration"]
        Ground --> UserOp
    end

    Consumers --> API_GW
    Coord <--> PG & Mongo & Redis
    Audit --> PG & Mongo
    Coord --> ProvisioningTier
    ProvisioningTier --> ConfigTier
    ConfigTier -->|"Telemetry, packages & events"| Audit
```

---

## 4. Key Architectural Decisions

### A. Comprehensive Platform Auditing: Permissions & Machine Traceability
Orion acts as the **single source of truth for infrastructure auditing** across BBVA:

- **RBAC & Authorization Audit:** Strict role-based access control with complete accountability. Every operation — whether triggered via the REST API or invoked automatically by a **Scheduler** — is tied to a verified identity, role, approval chain, and change ticket.
- **Full Machine Lifecycle Traceability:** Every compute asset retains an immutable lifecycle ledger from initial bootstrap to decommissioning. The platform tracks every playbook executed, configuration change applied, detected failure, and technician interaction.
- **Exhaustive Software & Historical Reporting:** Internal compliance teams and banking regulators can instantaneously export complete reports showing **exactly what software packages are installed on any machine** (versions, security patches, agents) and **every operational event that occurred on that node throughout its existence**.

### B. Universal Multi-Cloud Driver Provisioning Pipeline
Instead of maintaining provider-specific provisioning pipelines:

- **One lifecycle contract, swappable backends:** AWS, OpenStack, OpenShift, and bare-metal targets implement a common abstract lifecycle interface. The control plane dispatches normalized workloads regardless of target infrastructure.
- **Provider decoupling:** Organizational business logic and consumer platforms interact with uniform resource specifications, shielding downstream systems from individual cloud vendor API variations.

### C. Layered Ansible Configuration Pipeline: Ground vs. User Operations
Once raw compute resources are provisioned by cloud drivers, Orion orchestrates operating system configuration via Ansible structured into two sequential and isolated stages:

1. **Ground Layer (Mandatory Banking Baseline):**
    - **Security:** CIS benchmark OS hardening, corporate root and TLS certificates, firewall rules, and privileged access management.
    - **Observability:** Automated installation and configuration of corporate monitoring, metric, and log forwarding agents.
    - **Core Packaging:** Configuration of approved internal repositories and system utility dependencies.
    - *Policy:* No machine progresses to the next phase without a successful Ground verification check.
2. **User Operation Layer:**
    - Execution of user-defined playbooks and roles: deployment of application middleware, databases, microservices, and workload-specific configuration.

### D. API-Driven Operations & Scheduled Automation
Operational interactions with Orion avoid manual consoles and ad-hoc scripts:

- **API-First Architecture:** The complete catalog of operations (creation, remediation, start/stop, scaling, teardown, reports) is fully exposed via OpenAPI/REST, enabling headless execution from developer self-service portals, CI/CD pipelines, and declarative engines like **Blueprint**.
- **Integrated Schedulers:** Orion incorporates an asynchronous scheduler (Celery Beat) for recurring workflows: nightly inventory state reconciliation across physical and cloud estates, automated compliance scans, scheduled credential rotation, and maintenance tasks outside core banking hours.

### E. Hybrid Persistence Tier (PostgreSQL + MongoDB + Redis)
- **PostgreSQL** handles relational models requiring strict ACID transactions: RBAC permissions, operation catalogs, state machines, and the immutable audit log.
- **MongoDB** stores polymorphic documents detailing multi-cloud assets, arbitrary cloud attribute trees, and point-in-time snapshots of installed packages and software components.
- **Redis** provides hot caching for frequent inventory queries and serves as the high-throughput task queue broker for Celery workers.

---

## 5. Architectural Trade-Offs

| Decision | Alternative Considered | Rationale |
| :--- | :--- | :--- |
| **Two-layer Ansible pipeline (Ground + User)** | Monolithic user-managed playbook | Guarantees that 100% of compute instances adhere to corporate security, hardening, and monitoring baselines before user workloads are applied. |
| **Centralized audit engine in Orion** | Traceability delegated to ephemeral pipeline logs | Enables immediate generation of comprehensive audit reports showing complete software inventory and operational history for any machine. |
| **API-first operations & Celery Schedulers** | Manual console triggers or isolated cron scripts | Unifies access control, traceability, and concurrency under a single high-availability dispatcher. |
| **Hybrid PostgreSQL + MongoDB** | Single relational DB with JSONB | Retains strict relational integrity for RBAC and audit logs while providing high-performance indexing across heterogeneous cloud metadata and package inventories. |
| **In-house Python driver abstraction** | Separate cloud-specific tooling stacks | Unifies permissions, operation catalogs, and governance in a vendor-neutral control plane. |

---

## 6. Operational Impact

- **Auditability & complete traceability:** Reduced audit preparation from weeks of manual data compilation to instant queries covering any machine: who authorized it, what is installed, and its full historical event log.
- **Enforced security & observability baseline (Ground):** 100% of the **30,000+ managed machines** run verified corporate security policies and monitoring agents from the moment of provisioning.
- **Self-service at banking scale:** Over **500 engineers** govern infrastructure autonomously, executing **40,000+ daily operations** via REST APIs and scheduled automations.
- **International adoption:** Successfully deployed across multiple international banking divisions (**Spain, Mexico, and Turkey**).

---

[:octicons-arrow-right-24: Next: Blueprint — Declarative Lifecycle Engine](blueprint.md)
