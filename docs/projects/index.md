---
title: Platform Ecosystem & Case Studies
description: >-
  How ten years of platform engineering fit together — from OpenStack/Ceph storage and Jenkins shared libraries to custom HA dispatchers, driver-based deployment pipelines, Orion, Blueprint, and applied AI.
---

# Platform Ecosystem & Case Studies

Great platforms are rarely designed on a blank whiteboard in a single afternoon. They evolve **layer by layer** as existing tools hit scaling ceilings, vendor integrations get deprecated, and manual governance stops working.

This section maps how the systems I architected over the last decade connect into a single, cohesive engineering trajectory — followed by deep-dive case studies and my public open-source work.

---

## 1. Nine Years of Evolution: From CI/CD Standardization to a Custom IaC & Deployment Platform

At **BBVA Technology** (2017 – Present), what started as standardizing CI/CD pipelines across infrastructure teams grew into a comprehensive infrastructure deployment and governance platform managing **30,000+ machines** across **AWS, OpenStack, OpenShift, and bare metal**, processing **40,000+ daily operations** for **500+ engineers**:

```mermaid
flowchart TB
    subgraph Phase1["1. CI/CD Standardization & Its Limits"]
        JSL["Jenkins Shared Libraries<br/>(Groovy CI/CD standard)"]
        ANS["Ansible Core Services<br/>(GitLab, Artifactory, Jenkins)"]
    end

    subgraph Phase2["2. Decoupling Execution & Configuration"]
        DISP["HA Operation Dispatcher<br/>(Django + Celery REST API)"]
        CFG["Central Config Management<br/>(Runtime variable injection)"]
        K8S["Kubernetes Job Engine<br/>(Ephemeral container execution)"]
    end

    subgraph Phase3["3. Cloud-Agnostic Control Plane"]
        PIPE["Driver Deployment Pipeline<br/>(AWS · OpenStack · OpenShift · Bare-metal)"]
        F5["F5 / OpenStack REST Bridge<br/>(Zero-downtime deprecation fix)"]
        ORION["Orion IaaS Platform<br/>(Central API, RBAC, hybrid DB & audit)"]
    end

    subgraph Phase4["4. Declarative Lifecycle & Applied AI"]
        BP["Blueprint Engine<br/>(Async YAML DAG & idempotent teardown)"]
        AI["Orion AI (Validated PoC)<br/>(LangGraph + ReAct CI/CD diagnostics)"]
    end

    JSL -->|"hit scaling & state limits"| DISP
    ANS --> CFG
    CFG --> DISP
    DISP --> K8S
    DISP --> PIPE
    CFG --> PIPE
    F5 -.->|"restored load-balancing interoperability"| PIPE
    PIPE --> ORION
    ORION --> BP
    ORION --> AI
    DISP --> AI
```

1. **First bottleneck — Pipeline sprawl & Jenkins fragility:** Standardizing on **Jenkins Shared Libraries** unified teams, but exposed Jenkins as a single point of failure under heavy concurrent infrastructure workloads. That directly motivated replacing Jenkins with a purpose-built **High-Availability Operation Dispatcher** in Django and Celery, and later running isolated workloads on a **Kubernetes Job Execution Engine**.
2. **Second bottleneck — Environment drift:** Duplicated Ansible playbooks across dev, staging, and production caused human errors. Building a **Centralized Configuration Management System** decoupled variable resolution from playbook logic, injecting environment parameters dynamically at runtime.
3. **Third bottleneck — Multi-cloud fragmentation & compliance:** Provisioning across AWS, OpenStack, OpenShift, and physical servers required different tools and manual tickets. A **Universal Driver Deployment Pipeline** and **Orion** unified governance, RBAC, inventory, and automated compliance exports behind a single OpenAPI gateway.
4. **Fourth bottleneck — Commercial orchestrator lock-in & slow failure triage:** With Orion as the authoritative source of truth, **Blueprint** brought Terraform-like declarative YAML orchestration and idempotent teardowns without commercial licensing (replacing Red Hat Automation Platform), while **Orion AI (PoC)** explored multi-agent root-cause diagnostics on top of our operational logs and diffs.

---

## 2. Enterprise Architecture Deep-Dives

<div class="grid cards two-col" markdown>

-   :material-cloud-cog-outline:{ .lg .middle } __[Orion — Central IaaS Platform & Driver Pipeline](orion-iaas.md)__

    ---

    Sole architect of the central IaaS and deployment control plane: one OpenAPI interface governing 30,000+ machines across AWS, OpenStack, OpenShift, and bare metal (40,000+ daily ops), backed by a hybrid PostgreSQL + MongoDB + Redis tier and automated compliance audit pipelines.

    [:octicons-arrow-right-24: Architecture & trade-offs](orion-iaas.md)

-   :material-file-tree-outline:{ .lg .middle } __[Blueprint — Declarative Lifecycle Engine](blueprint.md)__

    ---

    Asynchronous Python orchestration engine driven by versioned YAML blueprints. Computes execution DAGs, reconciles against live Orion state, and resumes interrupted teardowns idempotently — eliminating commercial automation licensing.

    [:octicons-arrow-right-24: Architecture & trade-offs](blueprint.md)

-   :material-cached:{ .lg .middle } __[Leaving Jenkins — HA Dispatcher & K8s Execution](dispatcher-migration.md)__

    ---

    How we migrated away from centralized Jenkins bottlenecks to a purpose-built High-Availability Operation Dispatcher (Django + Celery), dynamic runtime configuration injection, and ephemeral Kubernetes Job execution.

    [:octicons-arrow-right-24: Architecture & trade-offs](dispatcher-migration.md)

-   :material-radar:{ .lg .middle } __[Orion AI — Agentic CI/CD Diagnostics (Validated PoC)](orion-ai.md)__

    ---

    Multi-agent LangGraph + ReAct diagnostic prototype that correlates pipeline logs, Redis-indexed runbooks, and GitLab diffs under deterministic guardrails — plus a candid look at enterprise rollout constraints.

    [:octicons-arrow-right-24: Architecture & rollout lessons](orion-ai.md)

</div>

---

## 3. Core Platform Subsystems & Earlier Infrastructure Work

Beyond the four flagship deep-dives above, these subsystems formed critical building blocks of the platform stack:

<div class="grid cards two-col" markdown>

-   :material-swap-horizontal-bold:{ .lg .middle } __F5 / OpenStack REST API Bridge (BBVA)__

    ---

    **Problem:** The native F5 Load Balancer integration with OpenStack was officially deprecated, threatening automated traffic balancing across banking environments.
    
    **Solution:** Engineered a custom RESTful API bridge in Python that restored full interoperability between F5 appliances and OpenStack networking. Delivered with **zero downtime**, avoiding a disruptive platform migration.

-   :material-tune-variant:{ .lg .middle } __Centralized Configuration Management System (BBVA)__

    ---

    **Problem:** Environment-specific variables hardcoded inside Ansible playbooks led to repository duplication and configuration drift across dev, staging, and production.
    
    **Solution:** Built a centralized configuration service that decouples variable management from playbook logic, dynamically resolving and injecting target-environment variables at deploy time.

-   :material-dharmachakra:{ .lg .middle } __Kubernetes Job Execution Engine (BBVA)__

    ---

    **Problem:** Running heavy automation and static validation workflows on long-lived worker nodes caused resource contention and environment drift.
    
    **Solution:** Extended the deployment pipeline to execute any infrastructure operation as an isolated, ephemeral **Kubernetes Job**, injecting environment variables at runtime and streaming telemetry back to central monitoring.

-   :material-server-security:{ .lg .middle } __Ansible Shared Services Governance (BBVA)__

    ---

    **Scope:** Owned and maintained the environment-agnostic Ansible codebase provisioning and configuring BBVA's core developer platforms — including **GitLab, Artifactory, and Jenkins** clusters — consuming variables automatically from the Configuration Management System.

-   :material-source-branch:{ .lg .middle } __Jenkins Shared Libraries Framework (BBVA)__

    ---

    **Scope:** Authored modular Groovy shared libraries and reusable pipeline templates that standardized CI/CD across multiple infrastructure teams, cutting pipeline duplication and establishing the operational baseline later superseded by the custom HA Dispatcher.

-   :material-harddisk:{ .lg .middle } __Private Cloud Storage Platform on OpenStack Swift (Oesia · 2015–2017)__

    ---

    **Scope:** Administered a production private cloud on **OpenStack and Ceph** distributed storage, and developed an enterprise self-hosted file storage and sharing application (Dropbox-equivalent) in Python on top of **OpenStack Swift** object storage.

</div>

---

## 4. Open-Source Projects & Personal R&D

Public systems built outside enterprise constraints — with complete source code available on GitHub:

<div class="grid cards two-col" markdown>

-   :material-waveform:{ .lg .middle } __[OmniLecture Studio — Linux Multimodal AI Suite](omni-lecture.md)__

    ---

    Native Linux (Wayland/GNOME, GTK 3) screen/audio recorder with an optimized FFmpeg multimedia pipeline (tuned H.264 10 FPS stillimage encoding cutting file size by 70%, hardware PTS clock sync, and afftdn spectral filtering) paired with LangGraph workflows. Combines dual-engine Whisper (`faster-whisper` CPU `int8` + cloud API), OpenCV CLAHE + Tesseract slide/handwriting OCR, and anti-hallucination guardrails to generate Markdown notes, `.docx` documents, and Anki decks.

    [:octicons-arrow-right-24: Case study](omni-lecture.md) · [:fontawesome-brands-github: GitHub repo](https://github.com/oredondo/omnilecture-studio)

-   :material-wrench-outline:{ .lg .middle } __[WrenchBuddy — AI Vehicle Lifecycle & RAG Platform](wrenchbuddy.md)__

    ---

    Full-stack vehicle maintenance and telemetry platform built with **Django 6, DRF, PostgreSQL (`pgvector`), Celery, Redis, and LangChain** (plus a TypeScript frontend). Uses Vision/OCR to parse workshop invoices and 768-dim vector RAG over technical manuals to power a context-aware mechanical assistant.

    [:octicons-arrow-right-24: Case study](wrenchbuddy.md) · [:fontawesome-brands-github: Backend](https://github.com/oredondo/WrenchBuddy) · [:fontawesome-brands-github: Frontend](https://github.com/oredondo/WrenchBuddy-frontend)

</div>
