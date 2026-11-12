---
name: portfolio-manager
description: >-
  Manage the lifecycle, local preview, validation, and deployment of the
  bilingual portfolio, CV, and blog built with Zensical. Use whenever the user
  wants to run the local dev server, build the static site, validate links/Mermaid diagrams,
  or deploy to GitHub Pages.
---

# Portfolio Manager Skill

Use this skill to inspect, test, validate, and publish the portfolio and blog site built with **Zensical** and managed with **`uv`**.

---

## Prerequisites
Ensure commands are run from the project root:
```bash
cd /Users/oscarredondo/Documents/portfolio-platform
```

---

## Workflows

### 1. Local Development Server
To start the live-reloading dev server for **English** (default at `http://localhost:8000`):
```bash
uv run zensical serve
```

To start the dev server for **Spanish**:
```bash
uv run zensical serve -f mkdocs.es.yml
```

### 2. Parity & i18n Check
Before building, verify that English and Spanish content are in 1:1 synchronization:
```bash
python3 .agents/skills/i18n-sync/scripts/sync_i18n.py
```

### 3. Strict Dual Build Validation
Run before pushing to ensure zero broken links, valid Mermaid diagrams, and strict syntax in both languages:
```bash
uv run zensical build -s && uv run zensical build -s -f mkdocs.es.yml
```
If errors occur:
- Verify that internal markdown links use `.md` suffixes (e.g. `projects/orion-iaas.md`).
- Ensure Mermaid code blocks have matching node identifiers and valid syntax.
- Ensure all authors in `.authors.yml` have an `avatar` field.

### 4. Deploy to GitHub Pages
Deploys automatically via `.github/workflows/deploy.yml` on push to `main`.
To manually build the complete dual static output for inspection:
```bash
uv run zensical build -s && uv run zensical build -s -f mkdocs.es.yml
```
Output will be generated in `./site` (English at `/`, Spanish at `/es/`).
