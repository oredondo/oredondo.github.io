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

# Live-reloading dev server at http://localhost:8000
uv run zensical serve

# Strict build (verifies links and syntax)
uv run zensical build -s
```

## Project structure

```text
docs/
├── index.md                 # Landing page: hero, KPIs, featured work, stack, timeline
├── projects/                # Architecture case studies (problem → design → trade-offs → impact)
├── cv/index.md              # CV with print-optimised CSS (Print → Save as PDF)
├── blog/                    # Blog posts, categories, archive
├── about.md                 # Background & engineering principles
├── assets/logo.svg          # Logo & favicon
└── stylesheets/extra.css    # Brand palette, hero, cards, timeline, print styles
overrides/404.html           # Custom 404 page
.github/workflows/deploy.yml # Strict build on PRs, deploy to GitHub Pages on main
.agents/skills/              # Antigravity / Gemini CLI skills for maintaining the site
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
