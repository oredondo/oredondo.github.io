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
<a href="https://linkedin.com/in/oscarredondodjangopython">linkedin.com/in/oscarredondodjangopython</a> ·
<a href="https://github.com/oredondo">github.com/oredondo</a>
</p>

## Career Profile

**Senior Platform Engineer · Python** with **10+ years of experience** architecting large-scale infrastructure deployment and provisioning platforms, declarative Infrastructure as Code (IaC) engines, and operational AI workflows. My engineering philosophy centers on making distributed infrastructure complexity invisible — engineering clean self-service APIs, asynchronous YAML engines driven by dependency DAGs, universal driver layers, and deterministic systems that eliminate operational bottlenecks and enforce security and auditability by design.

As **sole architect and owner of the central IaaS platform suite (Orion & Blueprint)** powering BBVA's Core Banking Infrastructure, I conceived and built the systems governing **30,000+ machines** across AWS, OpenStack, OpenShift, and bare metal, processing **40,000+ daily operations for 500+ engineers**. I designed the hybrid persistence and querying architecture (PostgreSQL, MongoDB, Redis) to support high-throughput operations and automated compliance audit pipelines. I established a custom Infrastructure as Code philosophy through asynchronous YAML orchestration engines (`Blueprint`), a modular universal driver deployment pipeline, runtime configuration injection, and High-Availability operation dispatchers on Kubernetes Jobs, eliminating proprietary vendor lock-in.

At the intersection of infrastructure engineering and applied AI, I conceived and validated **Orion AI** (LangGraph, ReAct, Qwen 131k context) to automate root-cause CI/CD failure diagnostics under deterministic guardrails, and build open-source multimodal and RAG systems in Python ([OmniLecture Studio](https://github.com/oredondo/omnilecture-studio), [WrenchBuddy](https://github.com/oredondo/WrenchBuddy)). Experienced in driving technical architecture across international engineering hubs in **Spain, Mexico, and Turkey**, defining organization-wide deployment standards, and mentoring engineers.

## Professional Experience

### Senior Python Developer, DevOps — IaaS & Deployment Platform Owner
<p class="cv-meta"><strong>BBVA Technology</strong> (Core Banking Infrastructure) · Madrid · 2017 – Present</p>

- **Central IaaS & Deployment Platform Architecture (Orion):** Sole owner and lead architect of BBVA's central IaaS governance, inventory, and deployment control plane — governing **30,000+ machines** across AWS, OpenStack, OpenShift, and bare metal with **40,000+ daily operations for 500+ engineers**. Led all technical decisions end-to-end: OpenAPI/Swagger REST interface, self-service developer model, fine-grained RBAC, and distributed asynchronous processing, abstracting physical and multi-cloud complexity for development teams.
- **Custom IaC Philosophy & Declarative Orchestration (Blueprint):** Conceived and engineered **Blueprint**, an asynchronous Python orchestration engine driven by versioned YAML blueprints (conceptually analogous to Terraform). Engineered to execute parallel provisioning via wave-based DAG dependency analysis, reconcile against live Orion state, and provide **idempotent teardown operations** that safely resume interrupted destructions across hundreds of environments without rework — eliminating 100% of commercial licensing costs (Red Hat Automation Platform / Ansible Tower).
- **Universal Driver Pipeline & Centralized Configuration Management:** Architected a universal Django deployment pipeline around a **modular driver pattern**, unifying 4 distinct infrastructure substrates (AWS, OpenStack, OpenShift, and bare metal) under the same codebase. Built a **Centralized Configuration Management System** that decouples variables from automation playbooks, dynamically injecting them at runtime to ensure **zero configuration drift (*zero drift*)** across development, staging, and production environments.
- **Jenkins to Custom HA Dispatcher Migration & K8s Job Execution:** Led the strategic replacement of Jenkins as a single point of failure (after first standardizing CI/CD across teams using modular **Jenkins Shared Libraries** in Groovy) by designing a purpose-built **High-Availability Operation Dispatcher** in Django and Celery with OpenAPI REST endpoints, custom retry flows, and a **Kubernetes Job Execution Engine** that runs each automation as an isolated, observable, and ephemeral container.
- **Hybrid Data Engineering & Automated Compliance Audit Pipelines:** Designed and managed the hybrid persistence tier across **PostgreSQL, MongoDB, and Redis** for real-time inventory governance, optimizing high-volume concurrent queries across **30,000+ assets** and building automated data export pipelines (CSV audit reports) consumed directly by banking compliance officers and internal auditors.
- **Zero-Downtime Networking Bridge & Shared Platform Services:** Built a custom **F5 / OpenStack RESTful API Bridge** delivered with **zero banking downtime** following the official deprecation of the native vendor integration, and maintained the environment-agnostic **Ansible automation codebase** governing critical shared platforms (**GitLab, Artifactory, and Jenkins**).
- **Operational AI (Orion AI — Validated PoC):** Conceived, designed, and developed a validated multi-agent PoC (**LangGraph, ReAct, Qwen 131k LLM**) that concurrently analyzes execution logs, operational runbooks (indexed in Redis for fast RAG retrieval), and GitLab commit diffs under deterministic guardrails to cut CI/CD triage from hours to seconds; prototype validated and prepared pending central AI infrastructure integration guidelines.
- **International Rollout, Production Operations & Mentorship:** Led the technical onboarding and platform integration across engineering hubs in **Mexico and Turkey** (scaling adoption to 100+ global engineers), owned on-call incident response at banking scale with 99.9%+ availability, and mentored engineers in automation and platform engineering standards.

<p class="cv-tech"><strong>Tech:</strong> Python, Django, DRF, Celery, AsyncIO, PostgreSQL, MongoDB, Redis, LangChain, LangGraph, ReAct, Model Context Protocol (MCP), Ansible, Kubernetes, OpenShift, AWS, OpenStack, Docker, Podman, Jenkins, GitLab CI, Groovy, F5, Infoblox.</p>

### OpenStack Administrator & Developer
<p class="cv-meta"><strong>Oesia</strong> · Madrid · 2015 – 2017</p>

- **Private Cloud Operations (OpenStack & Ceph):** Administered and maintained a production private cloud infrastructure based on **OpenStack and Ceph distributed storage**, ensuring 99.9% availability, performance, and reliability for internal engineering teams.
- **Private Cloud Storage Platform (OpenStack Swift):** Architected and developed a self-hosted enterprise cloud storage application (conceptually equivalent to Dropbox) in Python on top of **OpenStack Swift** object storage, enabling secure file storage and sharing for 200+ users across 50+ TB clusters without public cloud dependencies.

<p class="cv-tech"><strong>Tech:</strong> OpenStack, Ceph, Swift, Python, Linux.</p>

## Selected Systems & Open-Source Projects

| System | Scope & Architecture |
| :--- | :--- |
| **[Orion — IaaS Platform](../projects/orion-iaas.md)** *(BBVA)* | Central self-service OpenAPI control plane, hybrid PostgreSQL/MongoDB/Redis data tier, and automated compliance pipelines across 30,000+ machines in AWS, OpenStack, OpenShift, and bare metal (40,000+ daily ops). |
| **[Blueprint — Declarative Engine](../projects/blueprint.md)** *(BBVA)* | Asynchronous Python YAML orchestrator with DAG wave concurrency, Orion job traceability, and resumable idempotent teardowns (custom IaC philosophy eliminating Red Hat Automation Platform). |
| **[HA Dispatcher, Config Mgmt & K8s Jobs](../projects/dispatcher-migration.md)** *(BBVA)* | Migration from Jenkins Shared Libraries to a High-Availability Django/Celery operation dispatcher, runtime variable injection, and ephemeral Kubernetes Job execution. |
| **F5 / OpenStack API Bridge & Core Ansible** *(BBVA)* | Zero-downtime REST API bridge restoring F5 load balancer interoperability with OpenStack; environment-agnostic Ansible automation for GitLab, Artifactory, and Jenkins. |
| **[Orion AI — CI/CD Auto-Diagnostics](../projects/orion-ai.md)** *(BBVA PoC)* | Validated multi-agent LangGraph + ReAct prototype correlating pipeline logs, Redis-indexed runbooks, and GitLab diffs under deterministic guardrails. |
| **[OmniLecture Studio](../projects/omni-lecture.md)** *([GitHub](https://github.com/oredondo/omnilecture-studio))* | Native Linux suite (Wayland, GTK 3) with an optimized FFmpeg multimedia pipeline (H.264 stillimage, afftdn audio filtering, PTS sync), LangGraph workflows, dual Whisper (int8 + API), and OpenCV CLAHE + Tesseract OCR. |
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
