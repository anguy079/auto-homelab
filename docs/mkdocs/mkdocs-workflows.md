# ⚙️ Hydration & Cleanup Workflows

This repo uses GitHub Actions to automate hydration, deployment, and cleanup.

## ✅ Hydration Workflow

- Triggered manually or via override
- Hydrates docs using `mkdocs build`
- Deploys to GitHub Pages
- Updates `README.md` with countdown and hydration status

## ✅ Cleanup Workflow

- Runs hourly via cron
- Deletes hydrated files in `docs/tmp/` if countdown expired
- Updates hydration status block in `README.md`

## ✅ Deployment

- GitHub Pages: Set source to GitHub Actions
- Optional: Use Cloudflare Pages for private forks
