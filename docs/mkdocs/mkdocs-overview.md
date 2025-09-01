# 📦 MkDocs Overview

MkDocs is a static site generator built for project documentation. This repo uses it to hydrate, preview, and deploy onboarding templates.

## ✅ Plugin Overview

- `mkdocs-material`: UI theming and layout
- `mkdocs-macros-plugin`: Variable injection (`{{ GH_USERNAME }}`)
- `mkdocs-copy`: Relocates hydrated files
- `mkdocs-gen-files`: Auto-generates Markdown templates

## 🧪 Install Options

- Python: `pip install -r requirements.txt`
- Docker: `docker run --rm -v $PWD:/docs squidfunk/mkdocs-material build`
- GitHub Pages: Deploy via `gh-deploy`
- Cloudflare Pages: Optional for private forks

## 🧼 Cleanup Logic

Hydrated files expire after 24h. Cleanup workflow deletes `docs/tmp/*` and updates hydration status.
