---
title: Curriculum Vitae
description: >-
  CV of Oscar Redondo — Senior Platform Engineer · Python with 10+ years architecting internal developer platforms, distributed automation engines, and applied operational AI.
hide:
  - navigation
  - feedback
---

<div class="cv-actions no-print">
  <button class="md-button md-button--primary" onclick="window.print()">Print / Save as PDF</button>
</div>

# Oscar Redondo

<p class="cv-headline">Senior Platform Engineer · Python — Internal Developer Platforms, Distributed Automation &amp; Applied AI</p>

<p class="cv-contact">
Madrid, Spain ·
<a href="mailto:o.redondo91@gmail.com">o.redondo91@gmail.com</a> ·
<a href="https://linkedin.com/in/oscarredondodjangopython">linkedin.com/in/oscarredondodjangopython</a> ·
<a href="https://github.com/oredondo">github.com/oredondo</a>
</p>

## Career Profile

**Senior Platform Engineer · Python** with **10+ years of experience** architecting high-scale internal developer platforms, distributed automation engines, and operational AI workflows. My core engineering philosophy centers on turning complex multi-cloud infrastructure into clean, self-service developer abstractions — building declarative lifecycle engines, universal driver layers, and deterministic systems that eliminate operational bottlenecks.

As **sole architect and owner of the central IaaS platform suite (Orion & Blueprint)** powering BBVA's Core Banking Infrastructure, I conceived and built the systems governing **tens of thousands of machines** across AWS, OpenStack, OpenShift, and on-premises environments, processing **high-throughput daily operations for 500+ engineers**. I designed the underlying hybrid data and query architecture (PostgreSQL, MongoDB, Redis) to support high-volume operations, automated audit export pipelines, and strict regulatory compliance, while engineering custom asynchronous YAML orchestration engines (`Blueprint`) and High-Availability operation dispatchers that eliminated commercial vendor lock-in.

At the intersection of platform engineering and applied AI, I architected the **Orion AI** validated PoC (LangGraph, ReAct, Qwen 131k context) to automate CI/CD failure diagnostics under deterministic guardrails, and build open-source multimodal and RAG systems in Python ([OmniLecture Studio](https://github.com/oredondo/omnilecture-studio), [WrenchBuddy](https://github.com/oredondo/WrenchBuddy)). Experienced in driving technical architecture across international engineering teams in **Spain, Mexico, and Turkey**, defining organization-wide deployment standards, and mentoring engineers.

## Professional Experience

### Senior Python Developer, DevOps — IaaS Platform Owner
<p class="cv-meta"><strong>BBVA Technology</strong> (Core Banking Infrastructure) · Madrid · 2017 – Present</p>

- **Central IaaS Platform Architecture (Orion):** Conceived, architected, and built from scratch as sole owner BBVA's central IaaS governance, inventory, and deployment platform — governing **tens of thousands of machines** across AWS, OpenStack, OpenShift, and bare-metal for **500+ engineers**. Led all technical decisions end-to-end: OpenAPI REST design, RBAC, async processing, and long-term evolution.
- **Hybrid Data Engineering & Automated Audit Pipelines:** Designed and managed the full persistence architecture across **PostgreSQL, MongoDB, and Redis** — optimizing high-volume queries across tens of thousands of heterogeneous assets and building automated audit export pipelines (CSV reports) consumed directly by internal auditors and compliance teams.
- **Declarative Lifecycle Orchestration (Blueprint):** Conceived and built **Blueprint**, an asynchronous Python orchestration engine driven by versioned YAML blueprints (conceptually analogous to Terraform). Integrated natively with Orion to orchestrate parallel provisioning, full job-level audit traceability, and **idempotent destroy operations** that safely resume partial teardowns — eliminating the need for commercial suites such as Red Hat Automation Platform.
- **Jenkins to Custom HA Operation Dispatcher Migration:** Led the strategic migration away from Jenkins (after first standardizing CI/CD across teams with modular **Jenkins Shared Libraries** in Groovy) by designing a purpose-built **High-Availability Operation Dispatcher** in Django and Celery with an OpenAPI REST interface, custom retry logic, and full execution observability.
- **Universal Driver Pipeline, Runtime Config & Kubernetes Job Engine:** Engineered a universal Django deployment pipeline around a **modular driver pattern** (targeting AWS, OpenStack, OpenShift, and physical servers with the same codebase), a **Centralized Configuration Management System** that dynamically injects environment variables at runtime, and a **Kubernetes Job Execution Engine** that runs infrastructure automations as isolated, ephemeral containers.
- **Zero-Downtime Vendor Interoperability & Shared Services:** Built a custom **F5 / OpenStack RESTful API Bridge** with zero banking downtime after the native vendor integration was deprecated, and owned the environment-agnostic **Ansible codebase** governing internal **GitLab, Artifactory, and Jenkins** platforms.
- **Operational AI (Orion AI — Validated PoC):** Conceived, designed, and developed a validated multi-agent PoC (**LangGraph, ReAct, Qwen 131k LLM**) that concurrently analyzes execution logs, operational runbooks (indexed in Redis for fast RAG retrieval), and GitLab commit diffs under deterministic guardrails to cut CI/CD triage from hours to seconds; prototype validated and prepared pending central AI infrastructure integration guidelines.
- **International Rollout, Production Operations & Mentorship:** Led the technical integration and onboarding of platform workflows across engineering teams in **Mexico and Turkey**, owned on-call incident response at banking scale, and mentored engineers in platform and automation best practices.

<p class="cv-tech"><strong>Tech:</strong> Python, Django, DRF, Celery, AsyncIO, PostgreSQL, MongoDB, Redis, LangChain, LangGraph, ReAct, Model Context Protocol (MCP), Ansible, Kubernetes, OpenShift, AWS, OpenStack, Docker, Podman, Jenkins, GitLab CI, Groovy, F5, Infoblox.</p>

### OpenStack Administrator & Developer
<p class="cv-meta"><strong>Oesia</strong> · Madrid · 2015 – 2017</p>

- **Private Cloud Operations (OpenStack & Ceph):** Administered and maintained a production private cloud infrastructure based on **OpenStack and Ceph distributed storage**, ensuring availability, performance, and reliability for internal engineering teams.
- **Private Cloud Storage Platform (OpenStack Swift):** Architected and developed a self-hosted enterprise cloud storage application (conceptually equivalent to Dropbox) in Python on top of **OpenStack Swift** object storage, enabling secure file storage and sharing without public cloud dependencies.

<p class="cv-tech"><strong>Tech:</strong> OpenStack, Ceph, Swift, Python, Linux.</p>

## Selected Systems & Open-Source Projects

| System | Scope & Architecture |
| :--- | :--- |
| **[Orion — IaaS Platform](../projects/orion-iaas.md)** *(BBVA)* | Central self-service OpenAPI control plane, hybrid PostgreSQL/MongoDB/Redis data tier, and automated compliance pipelines across AWS, OpenStack, OpenShift, and bare metal. |
| **[Blueprint — Declarative Engine](../projects/blueprint.md)** *(BBVA)* | Asynchronous Python YAML orchestrator with DAG wave concurrency, Orion job traceability, and resumable idempotent teardowns. |
| **[HA Dispatcher, Config Mgmt & K8s Jobs](../projects/dispatcher-migration.md)** *(BBVA)* | Migration from Jenkins Shared Libraries to a High-Availability Django/Celery operation dispatcher, runtime variable injection, and ephemeral Kubernetes Job execution. |
| **F5 / OpenStack API Bridge & Core Ansible** *(BBVA)* | Zero-downtime REST API bridge restoring F5 load balancer interoperability with OpenStack; environment-agnostic Ansible automation for GitLab, Artifactory, and Jenkins. |
| **[Orion AI — CI/CD Auto-Diagnostics](../projects/orion-ai.md)** *(BBVA PoC)* | Validated multi-agent LangGraph + ReAct prototype correlating logs, Redis-indexed runbooks, and GitLab diffs under deterministic guardrails. |
| **[OmniLecture Studio](../projects/omni-lecture.md)** *([GitHub](https://github.com/oredondo/omnilecture-studio))* | Native Linux (Wayland/GNOME, GTK 3) screen/audio capture and LangGraph pipeline with dual Whisper (`faster-whisper` `int8` + API) and OpenCV CLAHE + Tesseract OCR. |
| **[WrenchBuddy](../projects/wrenchbuddy.md)** *([GitHub](https://github.com/oredondo/WrenchBuddy))* | Full-stack vehicle lifecycle platform in Django 6, DRF, PostgreSQL (`pgvector` 768-dim RAG), Celery, Redis, S3/MinIO, LangChain Vision OCR, and TypeScript. |

## Technical Skills

| Category | Technologies |
| :--- | :--- |
| **Core Languages & Backend** | Python, AsyncIO, Django, Django REST Framework, FastAPI, Celery, Pydantic, SQL, Groovy, Bash, Go |
| **Platform & Cloud Infrastructure** | AWS, OpenStack, OpenShift, Kubernetes, Docker, Podman, Ceph, Swift, F5 Load Balancers, Infoblox, Linux |
| **IaC & Execution Engines** | Blueprint (custom async YAML DSL), Ansible, Terraform, Pulumi, Helm, ArgoCD, GitOps, Kubernetes Jobs |
| **Data & Messaging** | PostgreSQL (`pgvector`), MongoDB, Redis, RabbitMQ, AWS S3 / MinIO, High-Volume Query & Audit Pipelines |
| **CI/CD & Observability** | GitLab CI, GitHub Actions, Jenkins (Shared Libraries), Prometheus, Grafana, ELK / Splunk, HashiCorp Vault |
| **Applied AI & Agentic Systems** | LangGraph, LangChain, ReAct Agents, Model Context Protocol (MCP), RAG, Vector Databases, Whisper, Ollama, vLLM |

## Education

**B.Sc. Communications Electronic Engineering** (*Grado en Ingeniería Electrónica de Comunicaciones*)
<p class="cv-meta"><strong>Universidad Politécnica de Madrid</strong> · 2009 – 2016</p>

Telecommunications and electronic systems engineering with a strong foundation in software, hardware integration, digital systems design, and network architecture.

## Certifications & Training

| Year | Course | Provider |
| :--- | :--- | :--- |
| 2026 | Complete MCP Developer Guide: Agents, Servers & Tools | Udemy |
| 2026 | Curso Completo: LangChain, LangGraph y Agentes de IA con Python | Udemy |
| 2026 | Curso Completo de Spec-Driven Development (SDD) y Agentes IA | Udemy |
| 2026 | Curso Completo: Bases de Datos Vectoriales para IA Generativa | Udemy |
| 2025 | Developing Secure Software (LFD121) | Linux Foundation |

## Languages

- **Spanish:** Native
- **English:** Professional working proficiency
