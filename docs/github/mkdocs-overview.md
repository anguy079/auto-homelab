# 🧩 MkDocs Setup & Usage Guide

## 🔧 What MkDocs Can Do

MkDocs is a static site generator built for documentation. It can:

- 💧 Hydrate Markdown files using variables
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
extra:
  GH_USERNAME: anguy079
  FORK_NAME: lsio-docker-radarr
  REPO_ORIGIN: linuxserver/docker-radarr
  DELETE_AFTER_DAYS: 7
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

```yaml
plugins:
  - macros
  - mkdocs-copy:
      add_per_path:
        - docs/tmp/template-forking.md: ../homelab/docs/services/radarr/radarr-forking.md
```

### 🔧 `mkdocs-gen-files`

- Dynamically generates new `.md` files during build
- Ideal for templating multiple services or onboarding flows

---

## ⚙️ GitHub Actions Workflow: Hydrate + Deploy + Cleanup

```yaml
name: Hydrate & Deploy Docs

on:
  push:
    branches: [main]

jobs:
  build-docs:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Repo
        uses: actions/checkout@v3

      - name: Install MkDocs & Plugins
        run: |
          pip install mkdocs mkdocs-macros-plugin mkdocs-copy

      - name: Build Hydrated Docs
        run: |
          mkdocs build -f tmp/mkdocs.yml

      - name: Deploy to GitHub Pages
        run: |
          mkdocs gh-deploy --force -f tmp/mkdocs.yml

      - name: Cleanup Hydrated Files (after 7 days)
        run: |
          find docs/tmp -type f -name "*.md" -mtime +${{ vars.DELETE_AFTER_DAYS || 7 }} -exec rm {} \;
```

> 🔐 GitHub Pages requires the repo to be **public** for free hosting

---

## 🧼 Optional: Temporary Hydration Workflow

If you only need to preview or grab commands:

```bash
mkdocs serve -f tmp/mkdocs.yml
# Visit http://localhost:8000/tmp/template-forking/
```

To delete hydrated files manually:
```bash
rm docs/tmp/template-forking.md
```

---

Let me know if you’d like this scaffolded into a reusable onboarding block or synced with your `template-forking.md`. I can also modularize the GitHub Actions workflow with service-specific hydration triggers.


Great questions, Alexander — let’s break each one down precisely so you can architect your homelab workflows with confidence:

---

### 📍 1. Does `mkdocs.yml` Need to Be at Repo Root for GitHub Pages?

**Yes — for GitHub Pages to work with MkDocs**, `mkdocs.yml` must be located at the **root of the repo** and named exactly `mkdocs.yml`.

Even if you run `mkdocs build -f path/to/mkdocs.yml` locally or in CI, GitHub Pages itself doesn’t parse that config — it simply serves the output from the `gh-pages` branch. So the hydration and build process must be done before deployment, and that process expects `mkdocs.yml` at the root unless overridden manually during build.

> ✅ You can override the config path during build (`mkdocs build -f tmp/mkdocs.yml`), but **GitHub Pages won’t respect that unless the build step happens before deploy**.

---

### 💧 2. Can You Hydrate Files Using GitHub Pages or Cloudflare Without Local Install?

**Yes — but only through CI/CD**, not directly via GitHub Pages or Cloudflare.

- **GitHub Pages**: Only serves static files from the `gh-pages` branch. It does **not** run MkDocs or hydrate templates itself.
- **Cloudflare Pages**: Can run MkDocs during build if you configure a Python environment and install dependencies via `requirements.txt`.

So to hydrate `.md` files with variables:

- ✅ Use **GitHub Actions** or **Cloudflare build scripts** to run `mkdocs build`
- ✅ Include `mkdocs.yml`, your plugins, and template `.md` files
- ✅ Output hydrated HTML to `site/` → deploy that folder

> You don’t need to install MkDocs locally if you use CI — but hydration must happen during the build step.

---

### ⚙️ 3. Can You Set GitHub Defaults Like Indentation or Soft Wrap?

**Not natively in GitHub’s web interface**, but you have a few options:

#### ✅ EditorConfig

You can add a `.editorconfig` file to your repo to enforce formatting rules across supported editors:

```ini
# .editorconfig
[*]
indent_style = space
indent_size = 2
end_of_line = lf
charset = utf-8
trim_trailing_whitespace = true
insert_final_newline = true
```

This works with VS Code, JetBrains IDEs, and others — but **not GitHub’s web editor**.

#### ✅ GitHub Web Editor Limitations

- No way to enforce soft wrap or indentation defaults for new files
- Contributors must configure their local editor or use `.editorconfig`

---

Would you like me to scaffold a `requirements.txt`, `.editorconfig`, and GitHub Actions workflow that hydrates your templates and deploys to GitHub Pages or Cloudflare? I can modularize it with service-specific triggers and cleanup logic.
