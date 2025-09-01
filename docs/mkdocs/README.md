## 🧪 Getting Started

To hydrate and deploy your docs:

### ✅ Requirements

- [Set GitHub Pages source to GitHub Actions](https://github.com/anguy079/auto-homelab/settings/pages)
- Ensure repo is [public for free hosting](https://github.com/anguy079/auto-homelab)
- Include:
  - [`mkdocs.yml`](/mkdocs.yml)
  - [`requirements.txt`](/requirements.txt)
  - [`hydrate.yml`](/.github/workflows/hydrate.yml)

### 🚀 Trigger Hydration

Click the button below to hydrate and deploy for 24h:

[![Hydrate](https://img.shields.io/badge/Hydrate-24h-blue)](https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml)

> You can override the timer or trigger cleanup manually via the Actions tab.

---

## ⏱️ Live Countdown Recommendation

For a **live countdown that refreshes on page reload**, your best option is:

### ✅ GitHub Pages + JavaScript Timer

- Add a small HTML/JS snippet to your hydrated page:
  ```html
  <div id="countdown"></div>
  <script>
    const endTime = new Date("2025-09-02T03:00:00Z"); // set dynamically
    const countdown = document.getElementById("countdown");
    setInterval(() => {
      const now = new Date();
      const diff = endTime - now;
      const hours = Math.floor(diff / 3600000);
      const minutes = Math.floor((diff % 3600000) / 60000);
      countdown.textContent = `Time remaining: ${hours}h ${minutes}m`;
    }, 60000);
  </script>
  ```

- You can inject this via MkDocs macros or include it in a custom HTML block.

---

## ⏱️ Displaying Timer in Both Hydrated Page & README

### ✅ In Hydrated Page (via MkDocs Macros)

1. Add this to `mkdocs.yml`:
   ```yaml
   extra:
     COUNTDOWN_END: "2025-09-02T03:00:00Z"
   ```

2. In your Markdown file (e.g. `tmp/template-forking.md`):
   ```html
   <div id="countdown"></div>
   <script>
     const endTime = new Date("{{ COUNTDOWN_END }}");
     const countdown = document.getElementById("countdown");
     setInterval(() => {
       const now = new Date();
       const diff = endTime - now;
       const hours = Math.floor(diff / 3600000);
       const minutes = Math.floor((diff % 3600000) / 60000);
       countdown.textContent = `Time remaining: ${hours}h ${minutes}m`;
     }, 60000);
   </script>
   ```

This will render a live countdown on the hydrated page.

---

### ✅ In `README.md` (Static Timestamp + Status Badge)

```markdown
### 🚀 Hydration Status

![Hydration Status](https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml/badge.svg)  
🕒 Hydrated on: **Sept 1, 2025 @ 04:07 PDT**  
⏳ Expires in: **24h** (auto-cleanup scheduled)
```

> You can automate the timestamp update using a GitHub Action that commits the updated `README.md` when hydration is triggered.

---

## 🖱️ README.md Button Integration

You can add buttons to your root `README.md` like:

```markdown
### 🚀 Hydration Actions

[![Hydrate for 24h](https://img.shields.io/badge/Hydrate-24h-blue)](https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml)

[![View Temporary Docs](https://img.shields.io/badge/View-Temporary%20Docs-green)](https://anguy079.github.io/auto-homelab/tmp/template-forking/)

[![Hydrate](https://img.shields.io/badge/Hydrate-24h-blue)](https://github.com/<GH_USERNAME>/<REPO>/actions/workflows/hydrate.yml)
[![View Docs](https://img.shields.io/badge/View-Temporary%20Docs-green)](https://<GH_USERNAME>.github.io/<REPO>/tmp/template-forking/)
[![Override Timer](https://img.shields.io/badge/Override-Timer-orange)](https://github.com/<GH_USERNAME>/<REPO>/actions/workflows/hydrate.yml)
```

```markdown
### 🚀 Hydration Controls

[![Hydrate 24h](https://img.shields.io/badge/Hydrate-24h-blue)](https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml)
[![View Docs](https://img.shields.io/badge/View-Temporary%20Docs-green)](https://anguy079.github.io/auto-homelab/tmp/template-forking/)
[![Override Timer](https://img.shields.io/badge/Override-Timer-orange)](https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml)

![Hydration Status](https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml/badge.svg)
```

> You can also use GitHub’s [workflow_dispatch](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows#workflow_dispatch) to trigger hydration manually.

---

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
  COUNTDOWN_END: "2025-09-02T03:00:00Z"  # used in countdown timer

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
