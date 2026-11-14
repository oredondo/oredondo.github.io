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
A senior resume is not an exhaustive autobiography or a list of job duties; it is a **high-impact architectural marketing document**. Every line must earn its place by proving:
1. **Architectural Ownership:** Conceived, designed, and led systems rather than simply maintaining or using them.
2. **Technical Mastery:** Python, AsyncIO, custom DSL engines, distributed dispatchers, hybrid persistence tiers, Kubernetes Jobs, and deterministic multi-agent graphs.
3. **Auditable Scale & Impact:** Quantified results (30k+ nodes, 40k+ ops/day, 500+ engineers, MTTR from hours to seconds, zero downtime).

### B. Google's XYZ Bullet Formula
Every experience bullet point must follow the **XYZ formula**:
> **Accomplished [X] as measured by [Y], by doing [Z]**  
> *(Logró [X] medido por [Y], implementando [Z])*

- ❌ **Weak / Passive:** *"Worked on the Orion platform deploying machines in AWS and OpenStack."*
- ❌ **Generic:** *"Responsible for CI/CD pipelines and automating failure diagnostics."*
- ✅ **Google XYZ Standard:** *"Architected BBVA's central IaaS platform (Orion) governing **30,000+ machines** and **40,000+ daily operations for 500+ engineers**, building a modular driver pattern that unified AWS, OpenStack, OpenShift, and bare-metal under a single OpenAPI control plane."*

---

## 2. Bullet Point Construction Taxonomy

### The 4-Part Platform Formula
```
[Strong Active Verb] + [System / Architectural Component] + [Mechanism / Technical Implementation] + [Measurable Impact (Scale / Latency / Reliability)]
```

### Power Verbs by Domain (Never use "Worked on", "Helped", "Responsible for")
- **IaC & Orchestration:** *Architected, Conceived, Engineered, Decoupled, Reconciled, Automated, Standardized.*
- **Scale & Reliability:** *Streamlined, Eliminated (SPOF/lock-in), Scaled, Restored (zero-downtime), Optimized, Governed.*
- **Data & Compliance:** *Engineered (hybrid persistence), Ingested, Indexed, Accelerated, Automated (audit pipelines).*
- **Applied AI:** *Pioneered, Designed (cyclic state machines), Constrained (deterministic guardrails), Slashed (MTTR).*
- **Leadership & Scale:** *Led (international rollout), Mentored, Established (org-wide standards), Owned (on-call).*

---

## 3. Oscar Redondo's Platform Philosophy Pillars

Whenever reviewing or writing CV content, ground every point in these 4 architectural pillars:

1. **Custom Infrastructure as Code (IaC) vs. Off-The-Shelf Tools:**
   - Highlight **Blueprint**: Not merely using Terraform/Ansible; engineered an asynchronous Python YAML lifecycle engine with DAG wave execution and state reconciliation against Orion, eliminating commercial suites (Red Hat Automation Platform / Ansible Tower).
2. **Universal Driver Abstraction & Zero Configuration Drift:**
   - Modular driver pattern: Target AWS, OpenStack, OpenShift, and bare metal with the exact same codebase by swapping drivers.
   - Centralized Configuration Management: Dynamically injects environment variables at runtime, guaranteeing zero drift between dev, staging, and production.
3. **Replacing Single Points of Failure (SPOFs):**
   - Migrating away from Jenkins bottlenecks to a purpose-built High-Availability Operation Dispatcher (Django + Celery) running ephemeral container tasks via Kubernetes Jobs.
   - Zero-downtime RESTful API bridge between F5 load balancers and OpenStack when the vendor deprecated native drivers.
4. **Deterministic Operational AI:**
   - Orion AI (PoC validada): LangGraph + ReAct + Qwen 131k context under deterministic guardrails (strict Pydantic schemas, read-only MCP contracts) cutting MTTR from hours to seconds.

---

## 4. ATS & Technical Standards

### A. Semantic Structure & ATS Parsing
- Use linear Markdown headers (`# Name`, `## Section`, `### Role`).
- Keep contact information on a clean single line with direct clickable links (`[github.com/oredondo](https://github.com/oredondo)`).
- Use standard bullet lists (`- `) for work experience; never enclose job duties inside nested layout tables.
- Keep tables strictly reserved for structured summaries: *Selected Systems*, *Technical Skills*, and *Certifications*.
- Ensure all text is 100% extractable vector Unicode (no image-based CVs, no canvas rendering).

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
