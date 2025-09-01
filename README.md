[![Hydrate 24h](https://img.shields.io/badge/Hydrate-24h-blue)](/.github/workflows/hydrate.yml)
[![View Docs](https://img.shields.io/badge/View-Temporary%20Docs-green)](https://anguy079.github.io/auto-homelab/)
[![Override Timer](https://img.shields.io/badge/Override-Timer-orange)](/.github/workflows/hydrate.yml)
![Hydration Status](https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml/badge.svg)

🕒 Hydrated on: **Sept 1 @ 04:28 PDT**  
⏳ Expires in: **24h 0m** (auto-cleanup scheduled)

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
