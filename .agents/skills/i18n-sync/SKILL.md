---
name: i18n-sync
description: >-
  Keep English (docs/) and Spanish (docs_es/) in 1:1 synchronization. Automatically
  translate, adapt, and validate updates across both languages whenever any case study,
  blog post, CV, or page is edited or added.
---

# i18n Synchronization & Translation Skill

This skill ensures that Oscar Redondo's portfolio maintains **complete parity between English (`docs/`) and Spanish (`docs_es/`)**. Whenever content is added, modified, or deleted in one language, this skill triggers the translation and structural alignment for the mirror language.

---

## 🏛️ Architecture & File Mapping

| Concept | English Source | Spanish Mirror | Output URL |
| :--- | :--- | :--- | :--- |
| **Config** | `mkdocs.yml` (`language: en`) | `mkdocs.es.yml` (`language: es`) | — |
| **Content Root** | `docs/` | `docs_es/` | `/` (EN) vs `/es/` (ES) |
| **Landing Page** | `docs/index.md` | `docs_es/index.md` | `https://oredondo.github.io/` / `/es/` |
| **Case Studies** | `docs/projects/<slug>.md` | `docs_es/projects/<slug>.md` | `/projects/...` / `/es/projects/...` |
| **CV / Resume** | `docs/cv/index.md` | `docs_es/cv/index.md` | `/cv/` / `/es/cv/` |
| **Blog Posts** | `docs/blog/posts/<slug>.md` | `docs_es/blog/posts/<slug>.md` | `/blog/...` / `/es/blog/...` |
| **About** | `docs/about.md` | `docs_es/about.md` | `/about/` / `/es/about/` |

---

## 🔄 Automated Synchronization Workflow

Whenever you or the user modify or create a file in one language:

### Step 1: Detect Parity & Changes
Run the parity checker:
```bash
python3 .agents/skills/i18n-sync/scripts/sync_i18n.py
```
This identifies missing files or timestamps indicating pending translations.

### Step 2: Apply Translation with Platform Engineering Rules
Translate the corresponding counterpart adhering to these technical conventions:

1. **Frontmatter:**
   - Translate `title` and `description` naturally.
   - Keep `slug` identical between languages so URLs are consistent.
   - Keep `draft`, `date`, `authors` matching.
2. **Code & Technical Names:**
   - **Never translate:** technical identifiers, CLI commands, package names (`uv`, `AsyncIO`, `Celery`, `Django`, `PostgreSQL`, `MongoDB`, `Redis`, `LangGraph`, `ReAct`, `MCP`, `OpenStack`, `Kubernetes`).
   - Keep code blocks in Python, YAML, Bash, and Mermaid diagrams identical.
   - Translate comments inside code blocks and node labels in Mermaid diagrams (e.g. `Client["Cliente / API"]`).
3. **Links & Navigation:**
   - Relative links to other `.md` files must stay relative (e.g., `projects/orion-iaas.md` in both trees).
   - If a new case study is added, register it in both `mkdocs.yml` and `mkdocs.es.yml` under `nav`.

### Step 3: Local Preview & Strict Build Validation
To visually inspect both languages side-by-side with working language switchers:
```bash
python3 serve.py
```
This serves `http://localhost:8000/` (EN) and `http://localhost:8000/es/` (ES) and auto-rebuilds on changes.

Before committing, run the dual strict build:
```bash
uv run zensical build -s && uv run zensical build -s -f mkdocs.es.yml
```
Ensure **0 warnings and 0 broken links** in both versions.

---

## 📋 Checklist for Content Changes
- [ ] File exists in `docs/` AND `docs_es/`.
- [ ] `mkdocs.yml` AND `mkdocs.es.yml` updated if navigation changed.
- [ ] Python parity checker reports `Perfect 1:1 parity`.
- [ ] Both `uv run zensical build -s` and `uv run zensical build -s -f mkdocs.es.yml` pass.
