---
name: tech-blog-publisher
description: >-
  Create, format, and publish technical deep-dives, architecture essays, and
  post-mortems in the engineering blog. Use whenever the user wants to write a
  new blog post or edit existing articles.
---

# Tech Blog Publisher Skill

Use this skill to publish thoughtful, production-grade technical articles in `docs/blog/posts/`.

## File Naming Convention
Create articles following the ISO date pattern:
`docs/blog/posts/YYYY-MM-DD-<slug>.md`

## Standard Post Frontmatter
```markdown
---
draft: false
date: YYYY-MM-DD
authors:
  - oredondo
categories:
  - Platform Engineering
  - Applied AI
  - Architecture
tags:
  - Python
  - LangGraph
  - DevOps
  - Kubernetes
---

# Title of the Article

Brief hook paragraph introducing the technical problem, why it matters, and what readers will take away.

<!-- more -->

## Section 1: The Problem
...
```

## Writing Principles
1. **The Excerpt Marker:** Always insert `<!-- more -->` after the introductory paragraph. This controls what appears on the blog index and RSS feed.
2. **Code Blocks with Syntax Highlighting:** Always specify language (`python`, `yaml`, `bash`, `groovy`, `dockerfile`).
3. **Architecture Visualizations:** Use Mermaid diagrams wherever describing multi-step systems or distributed data flows.
4. **Dogfooding & Real-World Anchors:** Connect abstract theory back to real-world operational challenges (e.g., MTTR, idempotency, API versioning).
5. **Authors:** Default to `oredondo` (configured in `docs/blog/.authors.yml`).
