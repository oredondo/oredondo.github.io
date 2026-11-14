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
6. Enterprise case studies (BBVA / Oesia) must use **abstract architecture diagrams and high-level trade-offs only** — never publish proprietary employer code or invented/toy code snippets. Open-source case studies must link directly to the real public GitHub repositories (`omnilecture-studio`, `WrenchBuddy`).
7. Enforce LF endings on all files (configured via `.gitattributes`).
8. Always use **`BBVA Technology`** as the employer company name in the CV / Professional Experience, and **`BBVA`** as the client/target banking organization in the project case studies.
9. Always use **`Arquitecto y Responsable de Plataforma`** (ES) / **`Architect & Platform Lead`** (EN) as role title (never "Arquitecto Único" or "Sole Architect").
10. Flowcharts & Diagrams: Prefer clean 1-line horizontal pipelines (`flowchart LR`) followed by a structured step-by-step table; avoid tall sequence diagrams or cluttered multi-box charts.
11. OmniLecture Studio: Focus on interconnected Markdown (`.md`) knowledge graphs, FFmpeg voice dictation acoustic filtering, and Whisper anti-hallucination guardrails (never mention Word or `.docx`).
12. WrenchBuddy: Explicitly identify as an early-stage idea under active construction (*idea en fase de construcción muy temprana*).
13. Orion vs. Blueprint: **Orion** is the central platform and control plane that replaced commercial suites (such as Red Hat Ansible Automation Platform); **Blueprint** is its declarative YAML specification layer interpreted and executed natively by Orion.
14. Strategic Context (NextGen): Frame the platform evolution within BBVA's **NextGen** cloud initiative (begun in 2017 to offload mission-critical core banking workloads from the legacy mainframe), scaling from initial on-premises datacenters (OpenStack, bare-metal) to a fully hybridized private/public cloud (AWS, OpenShift, OpenStack).
