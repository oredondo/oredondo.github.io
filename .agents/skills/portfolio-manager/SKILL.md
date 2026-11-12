---
name: portfolio-manager
description: >-
  Manage the lifecycle, local preview, validation, and deployment of the
  portfolio, CV, and blog built with Zensical. Use whenever the user wants to
  run the local dev server, build the static site, validate links/Mermaid diagrams,
  or deploy to GitHub Pages.
---

# Portfolio Manager Skill

Use this skill to inspect, test, validate, and publish the portfolio and blog site built with **Zensical** and managed with **`uv`**.

## Prerequisites
Ensure commands are run from the project root:
```bash
cd /Users/oscarredondo/Documents/portfolio-platform
```

## Workflows

### 1. Local Development Server
To start the live-reloading dev server:
```bash
uv run zensical serve
```
- Available at `http://localhost:8000`.
- Changes to Markdown files, styles, or configuration automatically trigger reload.

### 2. Strict Build Validation
Run before pushing to ensure zero broken links and valid syntax:
```bash
uv run zensical build -s
```
If errors occur:
- Verify that internal markdown links use `.md` suffixes (e.g. `projects/orion-iaas.md`).
- Ensure Mermaid code blocks have matching node identifiers and valid syntax.

### 3. Deploy to GitHub Pages
Deploys automatically via `.github/workflows/deploy.yml` on push to `main`.
To manually build the static output for inspection:
```bash
uv run zensical build -s
```
Output will be generated in `./site`.
