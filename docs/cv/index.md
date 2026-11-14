---
title: Curriculum Vitae
description: >-
  CV of Oscar Redondo — Senior Python & Platform Engineer with 10+ years building
  internal developer platforms, automation engines and agentic AI systems.
hide:
  - navigation
  - feedback
---

<div class="cv-actions no-print">
  <button class="md-button md-button--primary" onclick="window.print()">Print / Save as PDF</button>
</div>

# Oscar Redondo

<p class="cv-headline">Senior Python &amp; Platform Engineer · DevOps &amp; Automation · Applied AI</p>

<p class="cv-contact">
Madrid, Spain ·
<a href="mailto:o.redondo91@gmail.com">o.redondo91@gmail.com</a> ·
<a href="https://linkedin.com/in/oscarredondodjangopython">linkedin.com/in/oscarredondodjangopython</a> ·
<a href="https://github.com/oredondo">github.com/oredondo</a>
</p>

## Profile

Senior Python & Platform Engineer with **10+ years of experience** architecting
high-scale internal platforms, distributed automation engines and production-grade
agentic workflows.

As **sole architect and owner of the central IaaS platform suite (Orion & Blueprint) powering BBVA's Core Banking Infrastructure**,
I conceived and built the systems governing **tens of thousands of machines** across AWS, OpenStack,
OpenShift and on-premises environments, processing **high-throughput daily operations for 500+
engineers**. I designed the underlying data architecture (PostgreSQL, MongoDB, Redis) for
high-throughput operations, large audit exports and strict regulatory compliance, and
built asynchronous YAML engines that eliminated enterprise vendor lock-in.

At the intersection of platform engineering and applied AI, I build agentic systems
grounded in rigorous engineering: **Orion AI** (LangGraph / ReAct) automates CI/CD
root-cause diagnostics under deterministic guardrails, cutting triage time from hours
to seconds. Experienced in driving architecture across international teams in Mexico and
Turkey, defining deployment standards and mentoring engineers.

## Key achievements

- Designed and own the platform behind **high-throughput daily infrastructure operations** on **tens of thousands of machines** across hybrid cloud for **500+ engineers**.
- Replaced a **commercial automation platform licence** with Blueprint, an in-house declarative AsyncIO engine.
- Reduced provisioning lead time **from days to minutes** through zero-ticket self-service.
- Delivered **100% audit compliance** with automated governance export pipelines.
- Built an agentic diagnostic PoC that produces cited root-cause reports in **under 15 seconds** with **94%+ accuracy** in validation.

## Professional experience

### Senior Python Developer, DevOps — IaaS Platform Owner
<p class="cv-meta"><strong>BBVA Technology</strong> (Core Banking Infrastructure) · Madrid · 2017 – Present</p>

- **Core IaaS Platform Architecture:** Architected and owned BBVA's central IaaS automation platform suite (Orion & Blueprint), governing **tens of thousands of nodes** across hybrid clouds (AWS, OpenStack, OpenShift) for **500+ engineers**, by implementing an abstract Python driver layer and Celery distributed task execution fabric.
- **Self-Service Delivery Velocity:** Accelerated infrastructure provisioning lead time **from several days to minutes** with zero manual ticketing, by designing self-service REST APIs in Django REST Framework backed by an asynchronous event-driven state engine.
- **Commercial Tool Elimination:** Eliminated enterprise commercial licensing overhead across hundreds of servers, by conceiving and implementing **Blueprint** — an in-house declarative YAML orchestration engine utilizing Python's `graphlib.TopologicalSorter` and `asyncio.TaskGroup`.
- **Regulatory Audit Compliance:** Achieved **100% regulatory audit compliance** across continuous banking inspections, by engineering a hybrid persistence architecture combining immutable PostgreSQL audit logs with MongoDB polymorphic asset state indexing.
- **Operational AI & MTTR Reduction:** Reduced CI/CD incident triage time **from hours to under 15 seconds** with **94%+ validation accuracy**, by architecting **Orion AI** — a cyclic multi-agent LangGraph system with ReAct feedback loops and deterministic citation guardrails.
- **Global Technical Enablement:** Standardized platform adoption across international engineering hubs in **Spain, Mexico, and Turkey**, by conducting cross-regional architecture onboarding, establishing common deployment standards, and implementing localized extensions.
- **Production Resilience:** Maintained **99.9%+ platform availability during high-throughput daily operations**, by architecting Redis distributed caching, worker queue isolation per provider, and leading on-call incident response for mission-critical core banking pipelines.

<p class="cv-tech"><strong>Tech:</strong> Python, Django, DRF, Celery, AsyncIO, MongoDB, PostgreSQL, Redis, LangChain, LangGraph, ReAct, Model Context Protocol (MCP), Ansible, Jenkins, GitLab CI, AWS, OpenStack, OpenShift, Kubernetes, Docker, Podman, Groovy, Infoblox, F5.</p>

### OpenStack Administrator & Developer
<p class="cv-meta"><strong>Oesia</strong> · Madrid · 2015 – 2017</p>

- **Private Cloud Storage:** Delivered an enterprise private cloud storage platform serving internal development teams, by engineering a secure file-sharing service in Python on top of **OpenStack Swift** object storage.
- **Infrastructure Reliability:** Guaranteed high availability and data redundancy across multi-tenant environments, by administering production **OpenStack and Ceph** distributed storage clusters, handling automated monitoring, provisioning, and maintenance.

<p class="cv-tech"><strong>Tech:</strong> OpenStack, Ceph, Swift, Python, Linux.</p>

## Technical skills

| Category | Technologies |
| :--- | :--- |
| **Core Architecture & Languages** | Python (expert), AsyncIO, Celery, Django, Django REST Framework, Groovy, Bash, SQL |
| **Applied AI & Agentic Systems** | LangGraph, LangChain, ReAct loops, Model Context Protocol (MCP), Vector Databases, RAG, Whisper |
| **Platform & Cloud Infrastructure** | AWS, OpenStack, OpenShift, Kubernetes, Docker, Podman, Ceph, F5, Infoblox |
| **Declarative IaC & Automation** | Blueprint (custom async YAML engine), GitOps, Ansible, Terraform concepts |
| **Data & Message Brokers** | PostgreSQL, MongoDB, Redis, RabbitMQ / Celery worker queues |
| **CI/CD & Delivery** | GitLab CI, Jenkins (shared Groovy libraries), custom HA operation dispatchers |

## Education

**B.Sc. Communications Electronic Engineering** (*Grado en Ingeniería Electrónica de Comunicaciones*)
<p class="cv-meta"><strong>Universidad Politécnica de Madrid</strong> · 2009 – 2016</p>

Telecommunications and electronic systems engineering with foundations in software,
hardware integration, digital systems design and network architecture.

## Certifications & training

| Year | Course | Provider |
| :--- | :--- | :--- |
| 2026 | Complete MCP Developer Guide: Agents, Servers & Tools | Udemy |
| 2026 | Curso Completo: LangChain, LangGraph y Agentes de IA con Python | Udemy |
| 2026 | Curso Completo de Spec-Driven Development (SDD) y Agentes IA | Udemy |
| 2026 | Curso Completo: Bases de Datos Vectoriales para IA Generativa | Udemy |
| 2025 | Developing Secure Software (LFD121) | Linux Foundation |
