---
title: Senior Platform Engineer · Python
description: >-
  Oscar Redondo — Senior Platform Engineer · Python with 10+ years architecting
  infrastructure deployment platforms, custom IaC engines, and large-scale operational AI.
hide:
  - navigation
  - toc
  - feedback
---

<div class="hero" markdown>

<p class="hero__eyebrow">Senior Platform Engineer · Python · Madrid, Spain</p>

# Oscar Redondo { .hero__title }

<p class="hero__lead">
I design and build <strong>infrastructure deployment and provisioning platforms rooted in a custom Infrastructure as Code philosophy</strong> — abstracting the distributed complexity of hybrid cloud across AWS, OpenStack, OpenShift, and bare metal into clean self-service APIs, declarative lifecycle engines, and deterministic automation.
</p>

[:material-sitemap-outline: Explore architecture & projects](projects/index.md){ .md-button .md-button--primary }
[:material-newspaper-variant-outline: Read engineering essays](blog/index.md){ .md-button }
[:material-file-account-outline: View my CV](cv/index.md){ .md-button }

</div>

<div class="kpi-grid">
  <div class="kpi-card">
    <span class="kpi-value">30,000+</span>
    <span class="kpi-label">Machines governed</span>
  </div>
  <div class="kpi-card">
    <span class="kpi-value">40,000+</span>
    <span class="kpi-label">Daily operations</span>
  </div>
  <div class="kpi-card">
    <span class="kpi-value">500+</span>
    <span class="kpi-label">Engineers served</span>
  </div>
  <div class="kpi-card">
    <span class="kpi-value">10+ yrs</span>
    <span class="kpi-label">Platform &amp; Python</span>
  </div>
</div>

## Platform Engineering Philosophy

*Three architectural principles that guide how I design and operate high-scale distributed systems:*

<div class="grid cards" markdown>

-   :material-road-variant:{ .lg .middle } __Pave Golden Paths, not ticket queues__

    ---

    Infrastructure complexity must be resolved in software, not human bureaucracy. Self-service APIs across AWS, OpenStack, OpenShift, and bare metal must ensure the secure, auditable, and compliant path is also the fastest and simplest for engineering teams.

-   :material-file-code-outline:{ .lg .middle } __Custom IaC philosophy & idempotent state__

    ---

    Creating fresh environments is trivial; safely recovering from a failure midway through a 30-step teardown is what truly tests an engine. I design asynchronous YAML engines with DAG wave scheduling and continuous state reconciliation, eliminating the cost and vendor lock-in of commercial suites.

-   :material-shield-check-outline:{ .lg .middle } __Deterministic guardrails for operational AI__

    ---

    LLMs and agentic systems are untrusted components in mission-critical operations. Rather than brittle open-ended prompts, operational agents must be bounded by cyclic state machines (LangGraph), typed read-only tool contracts (MCP), and strict schema verification before emitting diagnoses or taking action.

</div>

## Architecture Essays & Production Lessons

*In-depth technical reflections from a decade of building internal cloud platforms and operating banking infrastructure:*

<div class="grid cards" markdown>

-   :material-cached:{ .lg .middle } __[When Shared Libraries Hit a Wall: Why We Replaced Jenkins with a Custom HA Dispatcher](blog/posts/2026-02-15-leaving-jenkins-at-scale-custom-dispatcher.md)__

    ---

    Why standardizing CI/CD on Jenkins Shared Libraries was necessary first — and how it exposed the state and availability bottlenecks that led to engineering our own Django/Celery HA dispatcher and ephemeral Kubernetes Jobs.

    [:octicons-arrow-right-24: Read architecture essay](blog/posts/2026-02-15-leaving-jenkins-at-scale-custom-dispatcher.md)

-   :material-file-tree-outline:{ .lg .middle } __[Nine Years of Internal Cloud Platforms: Why Declarative YAML Replaced Our Commercial Orchestrator](blog/posts/2026-03-01-declarative-infrastructure-python.md)__

    ---

    How owning the central control plane shifts the build-vs-buy calculus, why we avoided local state files, and why idempotent teardowns are the true test of any infrastructure provisioning engine.

    [:octicons-arrow-right-24: Read architecture essay](blog/posts/2026-03-01-declarative-infrastructure-python.md)

-   :material-radar:{ .lg .middle } __[The PoC Was the Easy Part: Lessons from Building an Agentic CI/CD Diagnostic Engine in Banking](blog/posts/2026-03-10-agentic-cicd-diagnostics-langgraph.md)__

    ---

    Why cyclic stateful graphs in LangGraph outperform linear chains for failure triage, and what actually blocks validated AI prototypes from wide production rollout in a regulated bank.

    [:octicons-arrow-right-24: Read architecture essay](blog/posts/2026-03-10-agentic-cicd-diagnostics-langgraph.md)

</div>

<div style="text-align: right; margin-top: -0.5rem; margin-bottom: 2.5rem;" markdown>

[Explore all engineering essays :octicons-arrow-right-24:](blog/index.md){ .md-button .md-button--primary }

</div>

## Enterprise Platform Systems & Infrastructure

*System topology, architectural trade-offs, and failure modes in high-scale multi-cloud production:*

<div class="grid cards two-col" markdown>

-   :material-cloud-cog-outline:{ .lg .middle } __[Orion — Central IaaS Platform & Driver Pipeline](projects/orion-iaas.md)__

    ---

    Sole architect of BBVA's central IaaS and deployment control plane: a single OpenAPI interface governing 30,000+ machines across AWS, OpenStack, OpenShift, and bare metal (40,000+ daily ops), backed by PostgreSQL, MongoDB, Redis, and automated compliance pipelines.

    <span class="tech-tag">Python</span><span class="tech-tag">Django REST</span><span class="tech-tag">Celery</span><span class="tech-tag">PostgreSQL</span><span class="tech-tag">MongoDB</span><span class="tech-tag">Redis</span>

    [:octicons-arrow-right-24: Read architecture case study](projects/orion-iaas.md)

-   :material-file-tree-outline:{ .lg .middle } __[Blueprint — Declarative Lifecycle Engine](projects/blueprint.md)__

    ---

    Asynchronous Python engine driven by versioned YAML blueprints (Terraform-like). Orchestrates parallel DAG waves against Orion, produces full audit traces, and supports idempotent teardowns — eliminating commercial platform suites.

    <span class="tech-tag">Python</span><span class="tech-tag">AsyncIO</span><span class="tech-tag">DAG Scheduling</span><span class="tech-tag">Declarative YAML</span><span class="tech-tag">GitOps</span>

    [:octicons-arrow-right-24: Read architecture case study](projects/blueprint.md)

-   :material-cached:{ .lg .middle } __[Leaving Jenkins Behind — HA Dispatcher & K8s Execution](projects/dispatcher-migration.md)__

    ---

    How we evolved from Jenkins toward a High-Availability Operation Dispatcher (Django + Celery), dynamic runtime configuration injection, and ephemeral execution in Kubernetes Jobs.

    <span class="tech-tag">Django</span><span class="tech-tag">Celery</span><span class="tech-tag">Kubernetes Jobs</span><span class="tech-tag">Ansible</span><span class="tech-tag">OpenAPI</span>

    [:octicons-arrow-right-24: Read architecture case study](projects/dispatcher-migration.md)

-   :material-radar:{ .lg .middle } __[Orion AI — CI/CD Auto-Diagnostics (Validated PoC)](projects/orion-ai.md)__

    ---

    Validated multi-agent prototype using LangGraph and ReAct loops to correlate execution logs, Redis-indexed runbooks, and GitLab diffs under deterministic guardrails — plus a candid look at enterprise rollout constraints.

    <span class="tech-tag">LangGraph</span><span class="tech-tag">ReAct</span><span class="tech-tag">MCP</span><span class="tech-tag">Qwen 131k</span><span class="tech-tag">Deterministic Guardrails</span>

    [:octicons-arrow-right-24: Read architecture case study](projects/orion-ai.md)

</div>

<div style="text-align: right; margin-top: -0.5rem; margin-bottom: 2.5rem;" markdown>

[View full platform architecture &amp; subsystems :octicons-arrow-right-24:](projects/index.md){ .md-button }

</div>

## Open-Source Systems on GitHub

<div class="grid cards two-col" markdown>

-   :material-waveform:{ .lg .middle } __[OmniLecture Studio — Linux Multimodal AI Suite](projects/omni-lecture.md)__

    ---

    Native Linux (Wayland/GNOME, GTK 3) suite with an optimized FFmpeg multimedia pipeline (tuned H.264 10 FPS stillimage encoding cutting file size by 70%, hardware PTS clock sync, and afftdn spectral filtering) paired with dual Whisper transcription, 16×16 slide diffing, and LangGraph workflows.

    <span class="tech-tag">Python</span><span class="tech-tag">FFmpeg</span><span class="tech-tag">GTK 3 / Wayland</span><span class="tech-tag">LangGraph</span><span class="tech-tag">Whisper int8</span><span class="tech-tag">OpenCV / OCR</span>

    [:octicons-arrow-right-24: Case study](projects/omni-lecture.md) · [:fontawesome-brands-github: Source on GitHub](https://github.com/oredondo/omnilecture-studio)

-   :material-wrench-outline:{ .lg .middle } __[WrenchBuddy — AI Vehicle Lifecycle & pgvector RAG](projects/wrenchbuddy.md)__

    ---

    Full-stack platform built with Django 6, DRF, PostgreSQL (`pgvector` 768-dim RAG), Celery, Redis, S3/MinIO, LangChain Vision invoice OCR, ReportLab PDF export, and a TypeScript frontend.

    <span class="tech-tag">Django 6 / DRF</span><span class="tech-tag">PostgreSQL pgvector</span><span class="tech-tag">Celery &amp; Redis</span><span class="tech-tag">LangChain RAG</span><span class="tech-tag">TypeScript</span>

    [:octicons-arrow-right-24: Case study](projects/wrenchbuddy.md) · [:fontawesome-brands-github: Backend](https://github.com/oredondo/WrenchBuddy) · [:fontawesome-brands-github: Frontend](https://github.com/oredondo/WrenchBuddy-frontend)

</div>

<div class="cta-banner" markdown>

### Technical Discussion & Collaboration

Open to discussions on infrastructure deployment architecture, custom declarative IaC engines, distributed Python systems, and production-grade operational AI.

[:material-linkedin: Connect on LinkedIn](https://linkedin.com/in/oscarredondodjangopython){ .md-button .md-button--primary }
[:fontawesome-brands-github: GitHub (@oredondo)](https://github.com/oredondo){ .md-button }
[:material-email-outline: o.redondo91@gmail.com](mailto:o.redondo91@gmail.com){ .md-button }

</div>
