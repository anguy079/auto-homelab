# 🔌 MkDocs Plugin Overview

This repo uses several MkDocs plugins to automate hydration, inject variables, and generate contributor-friendly documentation. All plugins are listed in `requirements.txt` and loaded via `mkdocs.yml`.

---

## ✅ Core Plugins

| Plugin                  | Purpose                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| `mkdocs-material`       | UI theming, layout, icons, and sidebar styling                          |
| `mkdocs-macros-plugin`  | Injects variables like `{{ GH_USERNAME }}` into Markdown                |
| `mkdocs-gen-files`      | Auto-generates `.md` files during build (e.g. index, service docs)      |
| `mkdocs-copy`           | Moves hydrated files into `docs/tmp/` for isolation and cleanup         |

---

## 🧪 Optional Enhancements

If you use `mkdocs-material[recommended,imaging]`, you also get:

| Plugin Feature          | Benefit                                                                 |
|-------------------------|-------------------------------------------------------------------------|
| Admonitions             | Callouts like `!!! note` or `!!! warning`                               |
| Tabs                    | Organize content into horizontal tabs                                   |
| Emojis & Icons          | Use `:rocket:` or `:radarr:` in nav titles                              |
| Diagrams                | Render `mermaid` or `plantuml` diagrams                                 |
| Image Zoom              | Click-to-zoom on images                                                  |

---

## 🧼 Fork-Safe Setup

All plugins are installed via:

```bash
pip install -r requirements.txt
```

> Forks can override or disable plugins by editing `mkdocs.yml`. Just comment out any plugin block you don’t need.

---

## 🧠 Contributor Notes

- Avoid hardcoding plugin behavior — use variables and macros where possible
- Keep hydrated files in `docs/tmp/` to avoid polluting static docs
- Use `mkdocs-gen-files` to scaffold missing files during build
- Use `mkdocs-copy` to isolate hydrated content for cleanup

---

## 📚 Related Docs

- [MkDocs Setup & Plugin Overview](mkdocs-overview.md)
- [Variable Usage in mkdocs.yml](mkdocs-variables.md)
- [Hydration & Cleanup Workflows](mkdocs-workflows.md)

---
