---
title: Curriculum Vitae
description: >-
  CV of Oscar Redondo — Senior Platform Engineer · Python with 10+ years architecting infrastructure deployment platforms, custom IaC engines, and large-scale operational AI.
hide:
  - navigation
  - feedback
---

<div class="cv-actions no-print">
  <button class="md-button md-button--primary" onclick="window.print()">Print / Save as PDF</button>
</div>

# Oscar Redondo

<p class="cv-headline">Senior Platform Engineer · Python — Infrastructure Deployment Platforms, Declarative IaC &amp; Applied AI</p>

<p class="cv-contact">
Madrid, Spain ·
<a href="mailto:o.redondo91@gmail.com">o.redondo91@gmail.com</a> ·
<a href="https://oredondo.github.io/">oredondo.github.io</a> ·
<a href="https://linkedin.com/in/oscarredondodjangopython">linkedin.com/in/oscarredondodjangopython</a> ·
<a href="https://github.com/oredondo">github.com/oredondo</a>
</p>

## Career Profile

**Senior Platform Engineer · Python** with **10+ years of experience** architecting large-scale infrastructure deployment platforms, custom Infrastructure as Code (IaC) engines, and deterministic operational AI. As **architect and platform lead of Orion (and its declarative Blueprint layer)** at **BBVA Technology** — joining in 2017 amidst the strategic **NextGen** transformation to offload critical banking workloads from the legacy mainframe, scaling from on-premises to a fully hybrid cloud — I built **BBVA's** central control plane governing **30,000+ machines** (AWS, OpenStack, OpenShift, and bare metal) and **40,000+ daily operations for 500+ engineers**, eliminating vendor lock-in and single points of failure.

I also drive **operational AI with deterministic guardrails** (**LangGraph, ReAct, RAG**), build personal open-source projects in Python, and lead organization-wide deployment standards across international engineering hubs in **Spain, Mexico, and Turkey**.

## Professional Experience

### Senior Python Developer, DevOps — Architect & Platform Lead
<p class="cv-meta"><strong>BBVA Technology</strong> (BBVA Core Banking Infrastructure) · Madrid · 2017 – Present</p>

- **Central IaaS & Deployment Platform (Orion / NextGen):** Architected **BBVA's** central IaaS control plane under the **NextGen** initiative (evolved from on-premises to hybrid cloud to offload mainframe workloads), governing **30,000+ machines** across AWS, OpenStack, OpenShift, and bare metal with **40,000+ daily operations for 500+ engineers** via OpenAPI REST interfaces, self-service forms, and fine-grained RBAC.
- **Custom IaC Philosophy & YAML Blueprints (Blueprint on Orion):** Conceived **Orion's** declarative orchestration layer using versioned YAML blueprints (**Blueprint**, analogous to Terraform) with concurrent DAG waves, live state reconciliation, and **resumable idempotent teardowns** — replacing commercial per-node suites (Red Hat Automation Platform / Ansible Tower) with **€6M+ in estimated cumulative cost avoidance**.
- **Universal Driver Pipeline & Configuration Management:** Standardized deployment across 4 infrastructure substrates (AWS, OpenStack, OpenShift, bare metal) under one modular Django driver pipeline, paired with a **Centralized Configuration Management System** injecting variables at runtime to guarantee **zero configuration drift** across environments.
- **Jenkins to HA Dispatcher Migration & K8s Jobs:** Eliminated Jenkins as a single point of failure (after initially standardizing CI/CD via Groovy **Jenkins Shared Libraries**) by architecting a **Django + Celery HA Dispatcher** with OpenAPI endpoints, custom retry flows, and isolated **ephemeral Kubernetes Jobs**, ensuring continuous resilience under **DORA** mandates.
- **Hybrid Data Engineering & DORA Audit Pipelines:** Engineered a hybrid persistence tier (**PostgreSQL, MongoDB, Redis**) to query 30,000+ live assets under high concurrency and automate continuous ICT asset and audit compliance pipelines for banking regulators (**DORA**).
- **Zero-Downtime Networking Bridge & Shared Platforms:** Built a custom **F5 / OpenStack RESTful API Bridge** deployed with **zero downtime** after vendor deprecation, and maintained the environment-agnostic **Ansible codebase** governing shared **GitLab, Artifactory, and Jenkins** clusters.
- **Operational AI (Orion AI — Validated PoC):** Conceived and validated a multi-agent prototype (**LangGraph, ReAct, Qwen 131k LLM**) correlating Dispatcher logs, Redis-indexed RAG runbooks, and GitLab diffs under deterministic guardrails to cut incident triage from hours to seconds (prepared pending central AI infrastructure integration guidelines).
- **International Rollout, On-Call & Mentorship:** Led platform onboarding across **Mexico and Turkey** (100+ international engineers), owned banking-scale on-call operations at **99.9%+ availability**, and mentored engineers in automation standards.

<p class="cv-tech"><strong>Tech:</strong> Python, Django, DRF, Celery, AsyncIO, PostgreSQL, MongoDB, Redis, LangChain, LangGraph, ReAct, Model Context Protocol (MCP), Ansible, Kubernetes, OpenShift, AWS, OpenStack, Docker, Podman, Jenkins, GitLab CI, Groovy, F5, Infoblox.</p>

### OpenStack Administrator & Developer
<p class="cv-meta"><strong>Oesia</strong> · Madrid · 2015 – 2017</p>

- **Private Cloud Operations (OpenStack & Ceph):** Administered and maintained a production private cloud infrastructure based on **OpenStack and Ceph distributed storage**, ensuring 99.9% availability, performance, and reliability for internal engineering teams.
- **Private Cloud Storage Platform (OpenStack Swift):** Architected and developed a self-hosted enterprise cloud storage application (conceptually equivalent to Dropbox) in Python on top of **OpenStack Swift** object storage, enabling secure file storage and sharing for 200+ users across 50+ TB clusters without public cloud dependencies.

<p class="cv-tech"><strong>Tech:</strong> OpenStack, Ceph, Swift, Python, Linux.</p>

## Selected Systems & Personal Open-Source Projects

| System | Scope & Architecture |
| :--- | :--- |
| **[Orion — IaaS Platform](../projects/orion-iaas.md)** *(BBVA)* | Central self-service OpenAPI control plane, hybrid PostgreSQL/MongoDB/Redis data tier, and automated compliance pipelines across 30,000+ machines in AWS, OpenStack, OpenShift, and bare metal (40,000+ daily ops). |
| **[Blueprint — Declarative Layer on Orion](../projects/blueprint.md)** *(BBVA)* | Declarative YAML definition layer interpreted and executed natively by Orion with DAG wave concurrency, Job ID traceability, and resumable idempotent teardowns (eliminating Red Hat Automation Platform). |
| **[HA Dispatcher, Config Mgmt & K8s Jobs](../projects/dispatcher-migration.md)** *(BBVA)* | Migration from Jenkins Shared Libraries to a High-Availability Django/Celery operation dispatcher, runtime variable injection, and ephemeral Kubernetes Job execution. |
| **F5 / OpenStack API Bridge & Core Ansible** *(BBVA)* | Zero-downtime REST API bridge restoring F5 load balancer interoperability with OpenStack; environment-agnostic Ansible automation for GitLab, Artifactory, and Jenkins. |
| **[Orion AI — CI/CD Auto-Diagnostics](../projects/orion-ai.md)** *(BBVA PoC)* | Validated multi-agent LangGraph + ReAct prototype correlating pipeline logs, Redis-indexed runbooks, and GitLab diffs under deterministic guardrails. |
| **[OmniLecture Studio](../projects/omni-lecture.md)** *([GitHub](https://github.com/oredondo/omnilecture-studio))* | Native Linux suite (Wayland, GTK 3) with FFmpeg acoustic filtering (`afftdn`, `silenceremove`), Whisper anti-hallucination transcription, and interconnected Markdown knowledge graphs. |
| **[WrenchBuddy](../projects/wrenchbuddy.md)** *([GitHub](https://github.com/oredondo/WrenchBuddy))* | Early-stage idea under initial construction for vehicle lifecycle in Django 6, DRF, PostgreSQL (`pgvector` 768-dim RAG), Celery, Redis, S3/MinIO, Vision OCR, and TypeScript. |

## Technical Skills

| Category | Technologies |
| :--- | :--- |
| **Core Languages & Backend** | Python, AsyncIO, Django, Django REST Framework, FastAPI, OpenAPI / Swagger, Celery, Pydantic, SQL, Groovy, Bash, Go |
| **Platform & Cloud Infrastructure** | AWS, OpenStack, OpenShift, Kubernetes, Docker, Podman, Ceph, Swift, F5 Load Balancers, Infoblox, Linux |
| **IaC & Execution Engines** | Orion / Blueprint (custom declarative YAML layer), JSON Schema, Ansible, Terraform, Pulumi, Helm, ArgoCD, GitOps, Kubernetes Jobs |
| **Data & Messaging** | PostgreSQL (`pgvector`), MongoDB, Redis, RabbitMQ, AWS S3 / MinIO, High-Volume Query & Audit Pipelines |
| **CI/CD & Observability** | GitLab CI, GitHub Actions, Jenkins (Shared Libraries), Prometheus, Grafana, ELK / Splunk, HashiCorp Vault |
| **Applied AI & Agentic Systems** | LangGraph, LangChain, ReAct Agents, Model Context Protocol (MCP), RAG, Vector Databases, Whisper, FFmpeg, Ollama, vLLM |

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
