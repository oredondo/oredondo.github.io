---
title: Case Studies
description: >-
  Architecture case studies on Python platform engineering, declarative
  infrastructure automation and applied agentic AI — from problem to measurable impact.
---

# Case Studies

Code is only one part of a platform. These case studies focus on what matters at
scale: **the problem, the architecture, the trade-offs and the measurable outcome** —
plus a look at the Python design patterns behind each system.

!!! note "About confidentiality"

    The enterprise systems below were built at BBVA. Architecture is described at a
    level that respects confidentiality; code snippets are **simplified, illustrative
    re-implementations** of the patterns used, not proprietary source code.

## Enterprise platform systems

<div class="grid cards" markdown>

-   :material-cloud-cog-outline:{ .lg .middle } __[Orion — Enterprise IaaS Platform](orion-iaas.md)__

    ---

    One self-service API over AWS, OpenStack, OpenShift and bare metal.

    **Scale:** Tens of thousands of nodes · High-throughput ops · 500+ engineers<br>
    **Stack:** Python, Django, DRF, Celery, PostgreSQL, MongoDB, Redis

    [:octicons-arrow-right-24: Read the case study](orion-iaas.md)

-   :material-file-tree-outline:{ .lg .middle } __[Blueprint — Declarative Orchestrator](blueprint.md)__

    ---

    Terraform-style AsyncIO engine driven by versioned YAML blueprints.

    **Impact:** Replaced a commercial automation platform licence<br>
    **Stack:** Python, AsyncIO, YAML + JSON Schema, GitOps

    [:octicons-arrow-right-24: Read the case study](blueprint.md)

</div>

## Applied operational AI

<div class="grid cards" markdown>

-   :material-stethoscope:{ .lg .middle } __[Orion AI — CI/CD Auto-Diagnostics](orion-ai.md)__

    ---

    Multi-agent root-cause triage over logs, diffs and runbooks.

    **Impact:** Initial triage from hours to < 15 seconds<br>
    **Stack:** LangGraph, ReAct, MCP, Qwen (131k context), vector search

    [:octicons-arrow-right-24: Read the case study](orion-ai.md)

-   :material-school-outline:{ .lg .middle } __[OmniLecture — Multimodal AI Suite](omni-lecture.md)__

    ---

    Personal project turning lectures into grounded notes and flashcards.

    **Focus:** Multimodal pipelines & local edge inference<br>
    **Stack:** Python, LangGraph, Whisper (int8 + cloud), OpenCV, OCR

    [:octicons-arrow-right-24: Read the case study](omni-lecture.md)

</div>

## How the systems fit together

```mermaid
flowchart LR
    Dev["Engineers & CI/CD pipelines"] -->|"YAML blueprints"| BP["Blueprint<br/>declarative engine"]
    Dev -->|"REST / portal"| ORION["Orion<br/>IaaS platform API"]
    BP -->|"idempotent operations"| ORION
    ORION --> INFRA["AWS · OpenStack · OpenShift · Bare metal"]
    CI["Jenkins / GitLab failures"] --> AI["Orion AI<br/>diagnostic agents"]
    AI -->|"cited root-cause report"| Dev
```
