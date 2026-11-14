---
title: Platform Ecosystem & Engineering Projects
description: >-
  Executive bird's-eye view and complete catalog of deployment control planes, declarative IaC engines, infrastructure subsystems, and open-source work.
---

# Platform Ecosystem & Engineering Projects

Over the past decade, I have architected and evolved platform systems, infrastructure-as-code (IaC) engines, multi-cloud control planes, and applied artificial intelligence applications.

---

### Bird's-Eye View of the Ecosystem

The engineering systems documented across this portal center around three core pillars:

1. **Enterprise Banking Platforms (BBVA):** Built to govern **30,000+ machines** and **40,000+ daily operations**. Highlights include **Orion** (an IaaS control plane that evolved from an API-first CMDB into a high-availability dispatcher replacing Jenkins), **Blueprint** (a declarative YAML engine executing DAG waves with idempotent teardowns), and operational AI initiatives like **Orion AI** (LangGraph).
2. **Critical Infrastructure & Network Subsystems:** Engineering components designed to ensure business continuity against technical obsolescence (such as the **custom F5/OpenStack REST bridge** delivered with *zero downtime* when vendor drivers were deprecated), **dynamic configuration management** services, and private cloud storage on **OpenStack Swift and Ceph**.
3. **Open-Source Systems & Applied AI on GitHub:** Public projects showcasing low-level multimedia pipeline engineering in **FFmpeg** (10 FPS stillimage H.264 compression saving 70% disk space, hardware PTS clock sync, and spectral filtering in **OmniLecture Studio**), dual-engine Whisper transcription, and contextual RAG architectures with **PostgreSQL (`pgvector`) and Django 6** in **WrenchBuddy**.

<div class="grid cards" markdown>

-   :material-server-network:{ .lg .middle } __Enterprise Platforms & Control Plane__

    ---

    Deployment control planes, declarative IaC engines, and monolithic CI/CD replacements designed to govern 30,000+ machines and 40,000 daily ops without single points of failure (SPOF).

    [:octicons-arrow-down-24: View corporate case studies](#enterprise-architecture-deep-dives)

-   :material-lan-connect:{ .lg .middle } __Network & Infrastructure Subsystems__

    ---

    Custom REST bridges shielding against vendor deprecation (F5 / OpenStack) with zero downtime, dynamic runtime config injection, and private cloud storage on OpenStack Swift / Ceph.

    [:octicons-arrow-down-24: View subsystems](#core-platform-subsystems)

-   :material-robot-industrial:{ .lg .middle } __Open-Source, FFmpeg & Applied AI__

    ---

    Native Linux/GTK development with optimized FFmpeg multimedia pipelines (H.264 stillimage, PTS sync), Whisper transcription, and RAG architectures with PostgreSQL, `pgvector`, and LangChain.

    [:octicons-arrow-down-24: View open-source projects](#open-source-projects)

</div>

---

## 1. Enterprise Architecture Deep-Dives {: #enterprise-architecture-deep-dives }

<div class="grid cards two-col" markdown>

-   :material-cloud-cog-outline:{ .lg .middle } __[Orion — Central IaaS Platform & Driver Pipeline](orion-iaas.md)__

    ---

    Sole architect of the central IaaS and deployment control plane: one OpenAPI interface governing 30,000+ machines across AWS, OpenStack, OpenShift, and bare metal (40,000+ daily ops), backed by a hybrid PostgreSQL + MongoDB + Redis tier and automated compliance audit pipelines.

    <span class="tech-tag">Python</span><span class="tech-tag">Django REST</span><span class="tech-tag">Celery</span><span class="tech-tag">PostgreSQL</span><span class="tech-tag">MongoDB</span><span class="tech-tag">Redis</span>

    [:octicons-arrow-right-24: Architecture & trade-offs](orion-iaas.md)

-   :material-file-tree-outline:{ .lg .middle } __[Blueprint — Declarative Lifecycle Engine](blueprint.md)__

    ---

    Asynchronous Python orchestration engine driven by versioned YAML blueprints. Computes execution DAGs, reconciles against live Orion state, and resumes interrupted teardowns idempotently — eliminating commercial automation licensing.

    <span class="tech-tag">Python</span><span class="tech-tag">AsyncIO</span><span class="tech-tag">DAG Scheduling</span><span class="tech-tag">Declarative YAML</span><span class="tech-tag">GitOps</span>

    [:octicons-arrow-right-24: Architecture & trade-offs](blueprint.md)

-   :material-cached:{ .lg .middle } __[Leaving Jenkins — HA Dispatcher & K8s Execution](dispatcher-migration.md)__

    ---

    How we migrated away from centralized Jenkins bottlenecks to a purpose-built High-Availability Operation Dispatcher (Django + Celery), dynamic runtime configuration injection, and ephemeral Kubernetes Job execution.

    <span class="tech-tag">Django</span><span class="tech-tag">Celery</span><span class="tech-tag">Kubernetes Jobs</span><span class="tech-tag">Ansible</span><span class="tech-tag">OpenAPI</span>

    [:octicons-arrow-right-24: Architecture & trade-offs](dispatcher-migration.md)

-   :material-radar:{ .lg .middle } __[Orion AI — Agentic CI/CD Diagnostics (Validated PoC)](orion-ai.md)__

    ---

    Multi-agent LangGraph + ReAct diagnostic prototype that correlates pipeline logs, Redis-indexed runbooks, and GitLab diffs under deterministic guardrails — plus a candid look at enterprise rollout constraints.

    <span class="tech-tag">LangGraph</span><span class="tech-tag">ReAct</span><span class="tech-tag">MCP</span><span class="tech-tag">Qwen 131k</span><span class="tech-tag">Deterministic Guardrails</span>

    [:octicons-arrow-right-24: Architecture & rollout lessons](orion-ai.md)

</div>

---

## 2. Core Platform Subsystems & Infrastructure Automation {: #core-platform-subsystems }

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

## 3. Open-Source Projects & Personal R&D {: #open-source-projects }

Public systems built outside enterprise constraints — with complete source code available on GitHub:

<div class="grid cards two-col" markdown>

-   :material-waveform:{ .lg .middle } __[OmniLecture Studio — Linux Multimodal AI Suite](omni-lecture.md)__

    ---

    Native Linux (Wayland/GNOME, GTK 3) screen/audio recorder with an optimized FFmpeg multimedia pipeline (tuned H.264 10 FPS stillimage encoding cutting file size by 70%, hardware PTS clock sync, and afftdn spectral filtering) paired with LangGraph workflows. Combines dual-engine Whisper (`faster-whisper` CPU `int8` + cloud API), OpenCV CLAHE + Tesseract slide/handwriting OCR, and anti-hallucination guardrails to generate Markdown notes, `.docx` documents, and Anki decks.

    <span class="tech-tag">Python 3.12</span><span class="tech-tag">GTK 3 / PyGObject</span><span class="tech-tag">FFmpeg</span><span class="tech-tag">faster-whisper</span><span class="tech-tag">LangGraph</span><span class="tech-tag">OpenCV</span>

    [:octicons-arrow-right-24: Case study](omni-lecture.md) · [:fontawesome-brands-github: GitHub repo](https://github.com/oredondo/omnilecture-studio)

-   :material-wrench-outline:{ .lg .middle } __[WrenchBuddy — AI Vehicle Lifecycle & RAG Platform](wrenchbuddy.md)__

    ---

    Full-stack vehicle maintenance and telemetry platform built with **Django 6, DRF, PostgreSQL (`pgvector`), Celery, Redis, and LangChain** (plus a TypeScript frontend). Uses Vision/OCR to parse workshop invoices and 768-dim vector RAG over technical manuals to power a context-aware mechanical assistant.

    <span class="tech-tag">Django 6</span><span class="tech-tag">PostgreSQL / pgvector</span><span class="tech-tag">LangChain</span><span class="tech-tag">Celery / Redis</span><span class="tech-tag">TypeScript</span>

    [:octicons-arrow-right-24: Case study](wrenchbuddy.md) · [:fontawesome-brands-github: Backend](https://github.com/oredondo/WrenchBuddy) · [:fontawesome-brands-github: Frontend](https://github.com/oredondo/WrenchBuddy-frontend)

</div>
