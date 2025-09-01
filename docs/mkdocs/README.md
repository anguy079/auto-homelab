## mkdocs.yml Template

- explain any requirements such as placing the file at root of repo. link both files using relative paths to _mkdocs.yml and _requirements.txt which are provided default templates.

## 📦 `requirements.txt` Template

> ⚠️ **Place this file at the root of your repo** — GitHub Actions expects it there by default.


---

v1
.github/workflows/hydrate.yml

v2 - modular with timer override. You can trigger this workflow manually and override the timer using the GitHub Actions UI.
.github/workflows/hydrate-modular.yml 
