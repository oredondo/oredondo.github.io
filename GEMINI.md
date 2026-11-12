# Portfolio & Platform Engineering Project Guidelines

This repository contains the professional portfolio, architectural case studies, engineering blog, and interactive CV of Oscar Redondo (Senior Python & Platform Engineer).

## Tech Stack & Architecture
- **Engine:** [Zensical](https://zensical.org/) (native, high-performance static site generator by the Material for MkDocs team) with native Blog support and Mermaid diagrams.
- **Package & Runtime Manager:** [`uv`](https://docs.astral.sh/uv/) with Python 3.13.
- **Styles:** Custom CSS in `docs/stylesheets/extra.css` (KPI cards, project grids, print-optimized media queries).
- **Deployment:** GitHub Pages via `.github/workflows/deploy.yml` on push to `main`.

## Workspace Commands
- **Run local server:** `uv run zensical serve`
- **Build site:** `uv run zensical build`
- **Strict link & syntax check:** `uv run zensical build -s`
- **Legacy / MkDocs build:** `uv run mkdocs build --strict`

## Content Structure
- `docs/index.md`: Main landing page with hero, key metrics (30k+ nodes, 40k ops/day), and flagship case studies.
- `docs/projects/`: Detailed architectural case studies with Mermaid diagrams and business impact metrics.
- `docs/cv/index.md`: Complete curriculum vitae with one-click PDF printing.
- `docs/blog/posts/`: Technical blog articles formatted with `YYYY-MM-DD-<slug>.md`.
- `docs/blog/.authors.yml`: Author definitions for the blog.
- `overrides/`: Theme overrides (custom 404 page).
- `docs/assets/logo.svg`: Logo and favicon.
- `.agents/skills/`: Custom Antigravity / Gemini CLI skills for managing the portfolio, authoring case studies, and publishing blog posts.

## Development Rules
1. Never commit `.venv/` or `site/`.
2. Always test builds with `uv run zensical build -s` before finalizing changes.
3. Keep Markdown internal links relative to the `.md` file (e.g., `projects/orion-iaas.md`).
4. Never use raw HTML `<a href="*.md">` links: use Markdown links inside `markdown`-enabled blocks (e.g., Material grid cards).
5. Code in case studies must be labelled as simplified/illustrative — never publish proprietary employer code.
6. Enforce LF endings on all files (configured via `.gitattributes`).
