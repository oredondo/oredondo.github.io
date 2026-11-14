---
title: About
description: >-
  About Oscar Redondo — Senior Platform Engineer · Python in Madrid. Engineering philosophy, architectural trajectory, and how to connect.
hide:
  - navigation
---

# About Me

I'm **Oscar Redondo**, a **Senior Platform Engineer · Python** based in Madrid, Spain.

Over the last decade, my work has centered on a single question: **how do you let hundreds of engineers move fast across tens of thousands of heterogeneous servers without losing governance, reliability, or sleep?**

My answer is to treat internal infrastructure as a software product — paving **Golden Paths** through clean APIs, driver abstractions, and declarative engines where security, auditability, and recovery are built in by design rather than enforced through manual tickets.

## Architectural Trajectory

- **From storage and hypervisors up:** I trained in Communications Electronic Engineering at the **Universidad Politécnica de Madrid** and began my career at **Oesia** operating a production **OpenStack and Ceph** private cloud and building a self-hosted cloud storage platform on **OpenStack Swift**. Starting close to storage clusters, hypervisors, and network fabrics shaped how I design higher-level abstractions today.
- **Building a bank's internal cloud platform layer by layer:** Since 2017 at **BBVA Technology**, I have served as sole architect and owner of the central IaaS platform suite (**Orion** & **Blueprint**). Whenever an off-the-shelf tool became a scaling or licensing bottleneck, I engineered a lean Python replacement — migrating from Jenkins to a custom **High-Availability Django/Celery Dispatcher**, decoupling runtime configuration, executing workloads in **Kubernetes Jobs**, bridging **F5 and OpenStack** with zero downtime, and building **Orion AI (PoC)** with LangGraph and ReAct.
- **Open-source engineering:** Outside enterprise environments, I build and maintain open-source AI and backend systems on GitHub — including **[OmniLecture Studio](https://github.com/oredondo/omnilecture-studio)** (a native Linux Wayland/GTK 3 multimodal study suite) and **[WrenchBuddy](https://github.com/oredondo/WrenchBuddy)** (a Django 6, Celery, and `pgvector` RAG vehicle lifecycle platform).

## Engineering Principles

<div class="grid cards" markdown>

-   :material-road-variant:{ .lg .middle } __Pave Golden Paths, not ticket queues__

    ---

    If an engineer needs a 20-page manual or a manual approval ticket to provision standard infrastructure, the abstraction has failed. Self-service APIs should make the compliant path the easiest path.

-   :material-file-code-outline:{ .lg .middle } __Declarative state & idempotent recovery__

    ---

    Creating greenfield resources is easy; recovering from a failure halfway through a 30-step teardown is where systems are tested. Every operation should inspect live state and be safe to re-run.

-   :material-shield-check-outline:{ .lg .middle } __Deterministic guardrails around AI__

    ---

    LLMs and multi-agent graphs are transformative for operational triage only when treated as untrusted components — bounded by typed schemas, read-only tool contracts (MCP), and strict evidence checks.

-   :material-account-group-outline:{ .lg .middle } __End-to-end ownership & international collaboration__

    ---

    Carrying the on-call pager for what you design keeps architectures honest. Sharing that architecture across teams — from mentoring junior engineers to onboarding hubs in Spain, Mexico, and Turkey — is what makes a platform last.

</div>

## Outside of Engineering

When I'm away from the terminal, you'll usually find me riding or wrenching on my motorbike (the real-world inspiration behind [WrenchBuddy](projects/wrenchbuddy.md)), snowboarding, hiking in the mountains, or listening to music.

## Let's Connect

- :fontawesome-brands-linkedin: **LinkedIn:** [linkedin.com/in/oscarredondodjangopython](https://linkedin.com/in/oscarredondodjangopython)
- :fontawesome-brands-github: **GitHub:** [github.com/oredondo](https://github.com/oredondo)
- :material-email-outline: **Email:** [o.redondo91@gmail.com](mailto:o.redondo91@gmail.com)
