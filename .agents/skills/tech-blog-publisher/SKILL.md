---
name: tech-blog-publisher
description: >-
  Create, format, and publish bilingual technical deep-dives, architecture essays, and
  post-mortems in the engineering blog (English & Spanish). Use whenever the user wants
  to write a new blog post or edit existing articles.
---

# Tech Blog Publisher Skill

Use this skill to publish thoughtful, production-grade technical articles across both English (`docs/blog/posts/`) and Spanish (`docs_es/blog/posts/`).

---

## File Naming & Slug Convention
Create articles following the ISO date pattern in both trees:
- English: `docs/blog/posts/YYYY-MM-DD-<slug>.md`
- Spanish: `docs_es/blog/posts/YYYY-MM-DD-<slug>.md`

Keep the **slug identical** in both files so URLs match.

---

## Standard Post Frontmatter

```markdown
---
draft: false
date: YYYY-MM-DD
slug: my-article-slug
description: >-
  Concise 1-2 sentence synopsis for SEO and social preview cards.
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

## 1. The Engineering Problem
...
```

---

## Writing Principles
1. **The Excerpt Marker:** Always insert `<!-- more -->` after the introductory paragraph. This controls what appears on the blog index and RSS feed.
2. **Explicit Slug & Description:** Always include `slug:` and `description:` in frontmatter for clean URLs and SEO.
3. **Code Blocks with Syntax Highlighting:** Always specify language (`python`, `yaml`, `bash`, `groovy`, `dockerfile`).
4. **Architecture Visualizations:** Use Mermaid diagrams wherever describing multi-step systems, state machines, or distributed data flows.
5. **Dogfooding & Real-World Anchors:** Connect abstract theory back to real-world operational challenges (e.g., MTTR, idempotency, API versioning).
6. **Cross-Links to Case Studies:** Include a footer note linking to the corresponding architectural case study (e.g. `[Blueprint case study](../../projects/blueprint.md)`).
7. **Bilingual 1:1 Parity:** Every post in English must have its Spanish mirror in `docs_es/blog/posts/` with translated text and Mermaid labels, keeping code blocks, tags and slugs aligned.
8. **Local Preview:** Test both language versions with `python3 serve.py` to inspect `/blog/` and `/es/blog/`.
9. **Validation:** Run `uv run zensical build -s && uv run zensical build -s -f mkdocs.es.yml` to verify build.
