# 🧩 MkDocs Setup & Usage Guide

## 🔧 What MkDocs Can Do

MkDocs is a static site generator built for documentation. It can:

- 💧 Hydrate Markdown files using variables via the `macros` plugin
- 📁 Convert `.md` files into clean HTML pages
- 🚀 Serve docs locally or deploy to GitHub Pages / Cloudflare Pages
- 🔄 Automate file generation, renaming, and relocation via plugins
- 🧼 Support temporary hydration workflows with cleanup logic

---

## 📦 What Is `mkdocs.yml`?

- Central config file for MkDocs
- Must be named `mkdocs.yml` and placed at the **root of your repo**
- Defines:
  - Site name
  - Plugins
  - Variable substitutions (`extra:` block)
  - Source folder (`docs_dir`)
  - Theme and navigation (optional)

### ✅ Example

```yaml
site_name: Auto Homelab Docs
docs_dir: docs/tmp
plugins:
  - search
  - macros
  - mkdocs-copy
extra:
  GH_USERNAME: anguy079
  FORK_NAME: lsio-docker-radarr
  REPO_ORIGIN: linuxserver/docker-radarr
  DELETE_AFTER_DAYS: 1
```

---

## 📁 Path & Directory Behavior

| Config Element     | Default Value       | Function                                                                 |
|--------------------|---------------------|--------------------------------------------------------------------------|
| `mkdocs.yml`       | `/mkdocs.yml`       | Defines site config and variables                                        |
| `docs_dir`         | `docs/`             | Folder MkDocs processes for `.md` files                                  |
| Working Directory  | Current shell path  | Used when running `mkdocs serve` or `mkdocs build`                       |

### 🔧 Override Config Location

```bash
mkdocs serve -f tmp/mkdocs.yml
```

---

## 📦 What Is `requirements.txt`?

A `requirements.txt` file lists all Python packages needed to build your MkDocs site. It’s used in CI/CD pipelines (GitHub Actions, Cloudflare Pages) to install dependencies.

### ✅ Example

```txt
mkdocs
mkdocs-material
mkdocs-macros-plugin
mkdocs-copy
```

### 🔧 Usage in GitHub Actions

```yaml
- name: Install dependencies
  run: pip install -r requirements.txt
```

---

## 🖥️ Install Options (All Free)

### ✅ Linux (Unraid, Ubuntu, Debian)

**Option A: Python Install**
```bash
pip install mkdocs mkdocs-macros-plugin mkdocs-copy
```

**Option B: Docker Container**
```bash
docker run --rm -v $(pwd):/docs -p 8000:8000 squidfunk/mkdocs-material
```

---

### ✅ GitHub Pages

- Free for **public repos**
- Deploys from `gh-pages` branch
- Requires `mkdocs.yml` at repo root

**Deploy Command**
```bash
mkdocs gh-deploy --force
```

---

### ✅ Cloudflare Pages

- Free for all users
- Supports Python-based builds
- [Cloudflare MkDocs Guide](https://developers.cloudflare.com/pages/framework-guides/mkdocs/)

---

## 🔌 Plugins Overview

### 🔧 `mkdocs-copy`

- Copies hydrated `.md` files to custom paths
- Supports renaming and relocation across repos
- **Does not auto-delete copied files** — cleanup logic must target original hydration paths

### 🔧 `mkdocs-gen-files`

- Dynamically generates new `.md` files during build
- Ideal for templating multiple services or onboarding flows

---

## ⚙️ GitHub Actions Workflow: Hydrate + Deploy + Cleanup

```yaml
name: Hydrate & Deploy Docs

on:
  workflow_dispatch:

jobs:
  build-docs:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v3

      - name: Install Dependencies
        run: pip install -r requirements.txt

      - name: Build Hydrated Docs
        run: mkdocs build -f tmp/mkdocs.yml

      - name: Deploy to GitHub Pages
        run: mkdocs gh-deploy --force -f tmp/mkdocs.yml

      - name: Cleanup Hydrated Files (after 1 day)
        run: |
          find docs/tmp -type f -name "*.md" -mtime +${{ vars.DELETE_AFTER_DAYS || 1 }} -exec rm {} \;
```

> 🔐 GitHub Pages requires the repo to be **public** for free hosting

---

## 🧼 Temporary Hydration Workflow

### ✅ Preview Locally

```bash
mkdocs serve -f tmp/mkdocs.yml
# Visit http://localhost:8000/tmp/template-forking/
```

### ✅ Manual Cleanup

```bash
rm docs/tmp/template-forking.md
```

---

## 🖱️ README.md Button Integration

You can add buttons to your root `README.md` like:

```markdown
### 🚀 Hydration Actions

[![Hydrate for 24h](https://img.shields.io/badge/Hydrate-24h-blue)](https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml)

[![View Temporary Docs](https://img.shields.io/badge/View-Temporary%20Docs-green)](https://anguy079.github.io/auto-homelab/tmp/template-forking/)
```

> You can also use GitHub’s [workflow_dispatch](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch) to trigger hydration manually.

---
