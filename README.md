# Oscar Redondo — Python & Platform Engineering Portfolio

Portfolio, architecture case studies, engineering blog and printable CV of
**Oscar Redondo**, Senior Python & Platform Engineer.

**Live site:** <https://oredondo.github.io/>

Built with [Zensical](https://zensical.org/) (the modern successor to Material for MkDocs),
Mermaid diagrams and [`uv`](https://docs.astral.sh/uv/) (Python 3.13).

## Quick start

```bash
# Install uv (once)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Live-reloading dev server (English at http://localhost:8000)
uv run zensical serve

# Live-reloading dev server (Spanish)
uv run zensical serve -f mkdocs.es.yml

# Strict dual build (English & Spanish)
uv run zensical build -s && uv run zensical build -s -f mkdocs.es.yml
```

## Multilingual Architecture (i18n)

- **English (Primary):** configured in `mkdocs.yml`, source in `docs/`, served at `https://oredondo.github.io/`.
- **Spanish:** configured in `mkdocs.es.yml`, source in `docs_es/`, served at `https://oredondo.github.io/es/`.
- **Switcher:** interactive language selector in the header (`extra.alternate`) with full search and navigation translated in each language.

## Project structure

```text
docs/                        # English content (primary)
docs_es/                     # Spanish content (1:1 mirror)
mkdocs.yml                   # English site configuration
mkdocs.es.yml                # Spanish site configuration
overrides/404.html           # Custom 404 page
.github/workflows/deploy.yml # Strict build & deploy to GitHub Pages on main
.agents/skills/              # Antigravity / Gemini CLI skills
  ├── i18n-sync/             # Automated EN <-> ES translation and parity skill
  ├── portfolio-manager/     # Lifecycle and build management
  ├── case-study-author/     # Case study drafting
  └── tech-blog-publisher/   # Blog article publishing
```

## Deployment

- **Automatic:** every push to `main` runs a strict Zensical build and deploys to GitHub Pages
  (`gh-pages` branch) via `peaceiris/actions-gh-pages`. Pull requests run the strict build only.
- **Manual preview / build:** `uv run zensical build -s`

## Agent skills

- `portfolio-manager` — run, build, validate and deploy the site.
- `case-study-author` — scaffold architecture case studies in the house style.
- `tech-blog-publisher` — publish blog posts with correct metadata and excerpts.

## License

- Source code, stylesheets and workflows: [MIT License](LICENSE)
- Written articles, case studies and CV content: [Creative Commons Attribution-NonCommercial 4.0 (CC BY-NC 4.0)](LICENSE)
