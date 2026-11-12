# Portfolio & Platform Engineering Project Guidelines

This repository contains the professional portfolio, architectural case studies, engineering blog, and interactive CV of Oscar Redondo (Senior Python & Platform Engineer).

## Tech Stack & Architecture
- **Engine:** [Zensical](https://zensical.org/) (native, high-performance static site generator by the Material for MkDocs team) with native Blog support and Mermaid diagrams.
- **Package & Runtime Manager:** [`uv`](https://docs.astral.sh/uv/) with Python 3.13.
- **Styles:** Custom CSS in `docs/stylesheets/extra.css` (KPI cards, project grids, print-optimized media queries).
- **Deployment:** GitHub Pages via `.github/workflows/deploy.yml` on push to `main`.

## Workspace Commands
- **Run bilingual local server (EN + ES):** `python3 serve.py` (serves `/` and `/es/` on port 8000 with auto-rebuild).
- **Run single-language server (EN):** `uv run zensical serve`
- **Run single-language server (ES):** `uv run zensical serve -f mkdocs.es.yml`
- **Build site (both languages):** `uv run zensical build -s && uv run zensical build -s -f mkdocs.es.yml`
- **Check i18n parity:** `python3 .agents/skills/i18n-sync/scripts/sync_i18n.py`

## Content Structure & Multilingual Setup
- `mkdocs.yml`: English configuration (`docs_dir: docs`, `site_dir: site`, URL `/`).
- `mkdocs.es.yml`: Spanish configuration (`docs_dir: docs_es`, `site_dir: site/es`, URL `/es/`).
- `docs/`: English content tree (primary).
- `docs_es/`: Spanish mirror content tree.
- `.agents/skills/i18n-sync/`: Custom skill to keep English and Spanish in 1:1 parity with automatic translation.

## Development Rules
1. Never commit `.venv/` or `site/`.
2. Always maintain 1:1 parity between `docs/` and `docs_es/` using the `i18n-sync` skill.
3. Test dual builds with `uv run zensical build -s && uv run zensical build -s -f mkdocs.es.yml`.
4. Keep Markdown internal links relative to the `.md` file (e.g., `projects/orion-iaas.md`).
5. Never use raw HTML `<a href="*.md">` links: use Markdown links inside `markdown`-enabled blocks (e.g., Material grid cards).
6. Code in case studies must be labelled as simplified/illustrative — never publish proprietary employer code.
7. Enforce LF endings on all files (configured via `.gitattributes`).
