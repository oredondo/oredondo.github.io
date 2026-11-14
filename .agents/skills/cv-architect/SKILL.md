---
name: cv-architect
description: >-
  Architect, review, and optimize high-impact engineering CVs and resumes for Platform Engineering,
  Infrastructure as Code (IaC), Distributed Systems, and Applied AI roles. Aligns with Google XYZ,
  Harvard Career Services, and r/EngineeringResumes standards, strictly preserving 1:1 bilingual
  parity (docs/cv/ and docs_es/cv/), ATS compliance, and print-to-PDF formatting.
---

# CV Architect Skill

Transform engineering experience into an executive-grade, ATS-optimized marketing document that commands the attention of hyperscalers (Google, AWS, Meta, Apple, Microsoft) and tier-1 software companies.

This skill synthesizes the core principles of **Harvard Career Services**, Reddit's **r/EngineeringResumes**, Gergely Orosz's *The Tech Resume Inside Out*, and **Google's XYZ formula**, customized specifically for Oscar Redondo's platform engineering philosophy: **Custom Infrastructure as Code (IaC), self-service control planes, and deterministic operational AI**.

---

## 1. Core Engineering Resume Principles

### A. The Document Purpose
A senior resume is not an exhaustive autobiography or a list of job duties; it is a **high-impact architectural marketing document**. Every line must prove:
1. **Architectural Ownership:** Conceived, designed, and led systems rather than simply using them.
2. **Technical Mastery:** Python, AsyncIO, custom DSL engines, distributed dispatchers, hybrid persistence tiers, Kubernetes Jobs, and deterministic multi-agent graphs.
3. **Auditable Scale & Impact:** Quantified results (30,000+ nodes, 40,000+ ops/day, 500+ engineers, €6M+ licensing cost avoidance, MTTR from hours to seconds, zero downtime).

### B. Portfolio & Identity Standards
- **Organization & Employer:** Always use **`BBVA Technology`** as the employer company in the Professional Experience section, building systems and infrastructure for **`BBVA`** (Core Banking).
- **Strategic Context (NextGen & Mainframe Migration):** Frame the architecture within BBVA's **NextGen** initiative to offload critical workloads from the legacy **mainframe**, evolving from on-premises datacenters to a fully hybridized private/public cloud.
- **Role Title:** Always use **`Arquitecto y Responsable de Plataforma`** (ES) or **`Architect & Platform Lead`** (EN). Never use "Arquitecto Único" or "Sole Architect/Sole Owner".
- **Regulatory Frameworks:** Ground data and reliability bullets in **DORA (Digital Operational Resilience Act - Regulation EU 2022/2554)** requirements for continuous ICT asset tracking, zero single points of failure (SPOF), and business continuity.
- **Project Descriptions:**
  - *Orion:* Central IaaS platform & control plane (replacing commercial suites), web self-service forms, OpenAPI REST, automated schedulers, 30,000+ machines, 40,000+ daily ops.
  - *Blueprint:* Declarative YAML specification layer interpreted and executed natively by Orion, DAG waves, idempotent teardown, €6M+ licensing cost avoidance vs. Red Hat Automation Platform.
  - *Dispatcher:* Django + Celery HA dispatcher replacing Jenkins master SPOF, runtime variable injection, ephemeral K8s Jobs.
  - *Orion AI:* Validated PoC in LangGraph + ReAct analyzing Orion execution logs in Dispatcher + GitLab diffs under deterministic guardrails.
  - *OmniLecture Studio:* Linux native (Wayland, GTK 3), FFmpeg dictation filtering, Whisper anti-hallucination, Markdown knowledge graphs (no DOCX).
  - *WrenchBuddy:* Early-stage idea under active construction, Django 6 + pgvector RAG + Celery vision OCR.

---

## 2. Google's XYZ Bullet Formula
Every experience bullet point must follow the **XYZ formula**:
> **Accomplished [X] as measured by [Y], by doing [Z]**  
> *(Logró [X] medido por [Y], implementando [Z])*

- ❌ **Weak / Passive:** *"Worked on the Orion platform deploying machines in AWS and OpenStack."*
- ❌ **Generic:** *"Responsible for CI/CD pipelines and automating failure diagnostics."*
- ✅ **Google XYZ Standard:** *"Architected BBVA's central IaaS platform (Orion) governing **30,000+ machines** and **40,000+ daily operations for 500+ engineers**, building a modular driver pattern that unified AWS, OpenStack, OpenShift, and bare-metal under a single OpenAPI control plane."*

---

## 3. Bullet Construction Taxonomy

### The 4-Part Platform Formula
```
[Strong Active Verb] + [System / Architectural Component] + [Mechanism / Technical Implementation] + [Measurable Impact (Scale / Cost / Reliability / DORA)]
```

### Power Verbs by Domain (Never use "Worked on", "Helped", "Responsible for")
- **IaC & Orchestration:** *Architected, Conceived, Engineered, Decoupled, Reconciled, Automated, Standardized.*
- **Scale & Reliability:** *Streamlined, Eliminated (SPOF/lock-in), Scaled, Restored (zero-downtime), Optimized, Governed.*
- **Data & Compliance:** *Engineered (hybrid persistence), Ingested, Indexed, Accelerated, Automated (audit pipelines & DORA compliance).*
- **Applied AI:** *Pioneered, Designed (cyclic state machines), Constrained (deterministic guardrails), Slashed (MTTR).*
- **Leadership & Scale:** *Led (international rollout), Mentored, Established (org-wide standards), Owned (on-call).*

---

## 4. ATS & Technical Standards

### A. Semantic Structure & ATS Parsing
- Use linear Markdown headers (`# Name`, `## Section`, `### Role`).
- Keep contact information on a clean single line with direct clickable links (`[github.com/oredondo](https://github.com/oredondo)`).
- Use standard bullet lists (`- `) for work experience; never enclose job duties inside nested layout tables.
- Keep tables strictly reserved for structured summaries: *Selected Systems*, *Technical Skills*, and *Certifications*.
- Ensure all text is 100% extractable vector Unicode.

### B. Print-to-PDF Guidelines
The web CV is optimized for browser printing via `window.print()` and CSS media queries in `docs/stylesheets/extra.css`:
- Header navigation, buttons, and language switchers must use `.no-print`.
- Print font colors must force `#111827` on white background, even when exported from dark mode.
- Avoid orphaned headings using CSS `break-after: avoid`.

---

## 5. Bilingual Parity Protocol (EN & ES)

Any modification to the CV must maintain **strict 1:1 synchronization**:
- English: `docs/cv/index.md`
- Spanish: `docs_es/cv/index.md`

### Verification Workflow:
1. Update both language versions following the Google XYZ and active verb standards.
2. Run automated validation:
   ```bash
   python3 .agents/skills/cv-architect/scripts/validate_cv.py
   python3 .agents/skills/i18n-sync/scripts/sync_i18n.py
   ```
3. Test dual build with zero warnings:
   ```bash
   uv run zensical build -s && uv run zensical build -s -f mkdocs.es.yml
   ```
