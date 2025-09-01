# Live Files

➡️ [View mkdocs.yml](/mkdocs.yml)  
➡️ [View requirements.txt](/requirements.txt)


# Default Files - Template

<details><summary>📄 mkdocs.yml</summary>

> ⚠️ **Place this file at the root of your repo** — GitHub Actions expects it there by default.

```yaml
site_name: Auto Homelab Docs

# Folder to hydrate from (relative to repo root)
docs_dir: tmp

# Optional: where to output the built site
# site_dir: site  # default is 'site'

# Plugins to enable
plugins:
  - search
  - macros
  - mkdocs-copy  # optional: for relocating hydrated files

# Variables for substitution
extra:
  GH_USERNAME: anguy079
  FORK_NAME: lsio-docker-radarr
  REPO_ORIGIN: linuxserver/docker-radarr
  DELETE_AFTER_DAYS: 1  # used in cleanup logic
  TARGET_FOLDER: services/radarr
  WORKFLOW_FILE: hydrate.yml
  # WORKFLOW_FILE: sync-lsio-docker-radarr.yml  # not in template file

# Optional: theme settings
# theme:
#   name: material
#   palette:
#     primary: blue
#     accent: pink

# Optional: navigation structure
# nav:
#   - Home: index.md
#   - Forking Guide: github/template-forking.md
```

</details>

<details><summary>📄 requirements.txt</summary>

> ⚠️ **Place this file at the root of your repo** — GitHub Actions expects it there by default.

```txt
# Core MkDocs packages
mkdocs
mkdocs-material

# Plugin: Variable substitution
mkdocs-macros-plugin

# Plugin: Copy and relocate hydrated files
mkdocs-copy

# Optional: Generate files dynamically during build
# mkdocs-gen-files

# Optional: Theme extensions (icons, image handling)
# mkdocs-material[recommended,imaging]

# Optional: Markdown extensions (tables, footnotes, etc.)
# pymdown-extensions

# Optional: Syntax highlighting for code blocks
# pygments

# Optional: Spellcheck or linting tools
# mkdocs-spellcheck
```

</details>

---
