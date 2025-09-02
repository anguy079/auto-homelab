[![Hydrate 24h](https://img.shields.io/badge/Hydrate-24h-blue)](/.github/workflows/hydrate.yml)
[![View Docs](https://img.shields.io/badge/View-Temporary%20Docs-green)](https://anguy079.github.io/auto-homelab/)
[![Override Timer](https://img.shields.io/badge/Override-Timer-orange)](/.github/workflows/hydrate.yml)
![Hydration Status](https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml/badge.svg)

🕒 Hydrated on: **Sep 02, 2025 @ 04:52 UTC**
⏳ Expires in: **24h 0m** (auto-cleanup scheduled)

---

**v2**

<p align="center">

  <a href="/.github/workflows/hydrate.yml" title="Build and publish the documentation site for 24 hours">
    <img src="https://img.shields.io/badge/Deploy-Docs-blue?style=for-the-badge" alt="Deploy Docs">
  </a>

  <a href="https://anguy079.github.io/auto-homelab/" title="Open the current live documentation site">
    <img src="https://img.shields.io/badge/View-Docs-green?style=for-the-badge" alt="View Docs">
  </a>

  <a href="/.github/workflows/hydrate.yml" title="Rebuild and reset the documentation site timer">
    <img src="https://img.shields.io/badge/Redeploy-orange?style=for-the-badge" alt="Redeploy">
  </a>

  <a href="https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml" title="Current deployment status of the documentation site">
    <img src="https://img.shields.io/github/actions/workflow/status/anguy079/auto-homelab/hydrate.yml?label=Site%20Status&logo=github&style=for-the-badge" alt="Site Status">
  </a>

</p>

---

# 🧪 Auto Homelab Templates

This repo provides modular, privacy-safe templates for onboarding, hydration, and deployment using MkDocs and GitHub Actions.

## 🧪 Getting Started

To hydrate and deploy your docs:

### ✅ Requirements

- [Set GitHub Pages source to GitHub Actions](https://github.com/anguy079/auto-homelab/settings/pages)
- Ensure repo is [public for free hosting](https://github.com/anguy079/auto-homelab)
- Include:
  - [`mkdocs.yml`](./mkdocs.yml)
  - [`requirements.txt`](./requirements.txt)
  - [`hydrate.yml`](./.github/workflows/hydrate.yml)

---

### 🚀 Trigger Hydration

Click the button below to hydrate and deploy for 24h:

[![Hydrate](https://img.shields.io/badge/Hydrate-24h-blue)](https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml)

> You can override the timer or trigger cleanup manually via the Actions tab.

---

### ⏱️ Displaying Countdown in Hydrated Pages

Add this to any `.md` file:

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

## 📚 Additional Docs

- [MkDocs Setup & Plugin Overview](docs/mkdocs/mkdocs-overview.md)
- [Variable Usage in mkdocs.yml](docs/mkdocs/mkdocs-variables.md)
- [Hydration & Cleanup Workflows](docs/mkdocs/mkdocs-workflows.md)

---

<details><summary>📂 Repository Structure & File Purpose</summary>

auto-homelab/
├── [.github/](.github "GitHub-specific configuration")  
│   └── [workflows/](.github/workflows "CI/CD automation workflows")  
│       ├── [cleanup.yml](.github/workflows/cleanup.yml "Scheduled cleanup of hydrated docs")  
│       └── [hydrate.yml](.github/workflows/hydrate.yml "Builds & deploys docs for 24h preview")  
├── [docs/](docs "Documentation source files")  
│   ├── [github-template-forking.md](docs/github-template-forking.md "Guide for forking & onboarding")  
│   ├── [mkdocs-overview.md](docs/mkdocs-overview.md "MkDocs setup & usage overview")  
│   ├── [mkdocs-plugins.md](docs/mkdocs-plugins.md "Plugin list & configuration notes")  
│   ├── [mkdocs-variables.md](docs/mkdocs-variables.md "Variable usage in mkdocs.yml")  
│   ├── [mkdocs-workflows.md](docs/mkdocs-workflows.md "Hydration & cleanup workflow details")  
│   ├── [sync-guide.md](docs/sync-guide.md "Repo sync & update instructions")  
│   └── [index.md](docs/index.md "Docs landing page")  
├── [services/](services "Service-specific docs/configs")  
│   └── [radarr/](services/radarr "Radarr service documentation")  
├── [stylesheets/](stylesheets "Custom CSS for MkDocs theme")  
│   └── [extra.css](stylesheets/extra.css "Overrides & visual tweaks")  
├── [tmp/](tmp "Temporary build artifacts (ignored in CI)")  
├── [overrides/](overrides "MkDocs theme overrides")  
│   └── [.icons/](overrides/.icons "Custom SVG icons for services")  
│       ├── [plex.svg](overrides/.icons/plex.svg "Plex service icon")  
│       ├── [radarr.svg](overrides/.icons/radarr.svg "Radarr service icon")  
│       └── [sonarr.svg](overrides/.icons/sonarr.svg "Sonarr service icon")  
├── [scripts/](scripts "Python automation scripts")  
│   ├── [__init__.py](scripts/__init__.py "Marks scripts as a package")  
│   ├── [gen_docs.py](scripts/gen_docs.py "Generates base documentation")  
│   ├── [gen_hydrated_docs.py](scripts/gen_hydrated_docs.py "Generates hydrated (preview) docs")  
│   ├── [gen_index.py](scripts/gen_index.py "Builds index.md dynamically")  
│   ├── [gen_nav.py](scripts/gen_nav.py "Generates navigation structure")  
│   └── [gen_service_docs.py](scripts/gen_service_docs.py "Creates service-specific docs")  
├── [README.md](README.md "Project overview & usage instructions")  
├── [mkdocs.yml](mkdocs.yml "MkDocs configuration file")  
└── [requirements.txt](requirements.txt "Pinned Python dependencies for reproducibility")

</details>

---

<details><summary>📂 Repository Structure & File Purpose</summary>

<!-- REPO-TREE:START -->
<!-- REPO-TREE:END -->

</details>

---
