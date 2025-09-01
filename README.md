### 🚀 Hydration Actions
🕒 Hydrated on: **Sept 1, 2025 @ 04:28 PDT**  
⏳ Expires in: **23h 32m** (auto-cleanup scheduled)

[![Hydrate for 24h](https://img.shields.io/badge/Hydrate-24h-blue)](https://github.com/anguy079/auto-homelab/actions/workflows/hydrate.yml)

[![View Temporary Docs](https://img.shields.io/badge/View-Temporary%20Docs-green)](https://anguy079.github.io/auto-homelab/tmp/template-forking/)


## 🧩 Step 1: Requirements

**mkdocs.yml**
- located at **root folder** of repo
- named exactly `mkdocs.yml`. 
>variables substitution defined via the `macros` plugin.

### ✅ Example

```yaml
site_name: Auto Homelab Docs
plugins:
  - search
  - macros

extra:
  GH_USERNAME: anguy079
  FORK_NAME: lsio-docker-radarr
  REPO_ORIGIN: linuxserver/docker-radarr
```

These variables are then available in any `.md` file using `{{ GH_USERNAME }}`, etc.

---

## 🧠 Step 2: How MkDocs Knows Which File to Use

- MkDocs doesn’t “target” specific files for substitution — it processes **all Markdown files** in the `docs/` folder by default and converts them into HTML pages. Other file types (images, CSS, JS) are copied as-is into the final build.
- You can customize the folder using docs_dir in mkdocs.yml, but by default it’s docs/.

- So as long as `template-forking.md` lives in `docs/github/`, and uses `{{ VARIABLE }}` syntax, MkDocs will hydrate it automatically when you build or serve the site.

You don’t need to specify the file in `mkdocs.yml` unless you’re using a plugin like `mkdocs-copy` or `mkdocs-gen-files` to relocate or rename the output.

---

## 💧 Step 4: Previewing Hydrated Markdown

Yes — you’ll need to install MkDocs locally to preview or build the hydrated docs.

### ✅ Install MkDocs + Macros Plugin

```bash
pip install mkdocs mkdocs-macros-plugin
```

### ✅ Preview Locally

```bash
mkdocs serve
```

Then visit:  
`http://localhost:8000/github/template-forking/`  
This shows the fully substituted version of your file — perfect for quick reference or copy-paste usage.

---

## 📦 What Do `mkdocs-gen-files` and `mkdocs-copy` Do?

These plugins allow you to **copy, rename, or relocate hydrated files** — useful if you want to move a file from `auto-homelab` into `homelab`, or generate a temporary file.

### 🔧 `mkdocs-copy`

- Copies hydrated `.md` files to custom paths
- Can rename files and move them across repos

```yaml
plugins:
  - macros
  - mkdocs-copy:
      add_per_path:
        - docs/github/template-forking.md: ../homelab/docs/services/radarr/radarr-forking.md
```

### 🔧 `mkdocs-gen-files`

- More advanced: lets you generate new files dynamically during build
- Useful for templating multiple services or onboarding flows

---

## 🖥️ Can You Run This on Unraid?

Yes — if your Unraid server has Python and pip installed, you can run MkDocs and its plugins locally. You’d:

1. SSH into Unraid
2. Install MkDocs:
   ```bash
   pip install mkdocs mkdocs-macros-plugin mkdocs-copy
   ```
3. Navigate to your `auto-homelab` repo
4. Run:
   ```bash
   mkdocs serve  # for preview
   mkdocs build  # for output
   ```

Alternatively, you can run this in a container or VM if you prefer isolating the environment.

---

## 📁 How MkDocs Processes Files

- MkDocs **only processes files inside the `docs/` folder** by default.
- It looks for `.md` files (Markdown) and converts them into HTML pages.
- Other file types (images, CSS, JS) are copied as-is into the final build.
- You can customize the folder using `docs_dir` in `mkdocs.yml`, but by default it’s `docs/`.

### ✅ Example:
```yaml
docs_dir: docs
```

So if your repo has:
```
docs/
├── index.md
├── github/
│   └── template-forking.md
```

MkDocs will process both `.md` files and generate corresponding HTML pages.

---

## 🧠 How `mkdocs serve` Chooses the Working Directory

- When you run `mkdocs serve`, it uses the **current working directory** as the root.
- It looks for a `mkdocs.yml` file in that directory.
- You can override this by specifying a config file:
  ```bash
  mkdocs serve -f path/to/mkdocs.yml
  ```

So if you're in `/mnt/user/repos/auto-homelab/`, and `mkdocs.yml` is there, it will serve that repo.

---

## 🖥️ Is MkDocs Available as a Unraid Community App?

As of now, **MkDocs is not available as a native Unraid Community App**, but you have two options:

### Option A: **Install via Python on Unraid**
If your Unraid server has Python:
```bash
pip install mkdocs mkdocs-macros-plugin mkdocs-copy
```

### Option B: **Run MkDocs in a Docker Container**
You can build or pull a container like:
```bash
docker run --rm -v $(pwd):/docs -p 8000:8000 squidfunk/mkdocs-material
```

This is clean, isolated, and reproducible — perfect for your homelab.

---

## 🚀 Can You Run MkDocs via GitHub Actions or Cloudflare?

### ✅ GitHub Actions: Yes

You can fully automate hydration and deployment using GitHub Actions. Example workflow:

```yaml
name: Build Docs
on:
  push:
    branches: [main]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - run: pip install mkdocs mkdocs-macros-plugin mkdocs-copy
      - run: mkdocs build
      - run: mkdocs gh-deploy --force
```

This builds your docs and deploys them to GitHub Pages. You can also copy hydrated `.md` files into your private repo or trigger a sync.

### ✅ Cloudflare Pages: Yes (with Wrangler)

You can use [Cloudflare Pages](https://developers.cloudflare.com/pages/framework-guides/mkdocs/) to host your MkDocs site. It supports Python-based builds and can hydrate your templates on deploy.

---

## 🧬 Can It Automatically Create Files in Your Repo?

Yes — with plugins like `mkdocs-copy` or `mkdocs-gen-files`, you can:

- Hydrate `.md` files with variables
- Rename and relocate them
- Push them into your private repo via GitHub Actions

You can even set up a workflow that:
- Builds the hydrated file
- Commits it to `homelab`
- Opens a PR for review

---

## ✅ GitHub Pages Requirements

| Requirement                  | Details                                                                 |
|------------------------------|-------------------------------------------------------------------------|
| **Repo Type**                | Works with **public repos** on GitHub Free; **private repos** require GitHub Pro or higher |
| **mkdocs.yml Location**      | Must be at the **root of the repo** — named exactly `mkdocs.yml`       |
| **Source Folder**            | Defaults to `docs/`, but can be changed via `docs_dir:` in `mkdocs.yml` |
| **Branch Setup**             | Pages are served from the `gh-pages` branch (auto-created by `mkdocs gh-deploy`) |
| **Build Output**             | Only the **built site** (HTML, CSS, etc.) is served — not raw `.md` files |
| **Size Limit**               | Max site size: **1 GB**; bandwidth: **100 GB/month**; builds: **10/hour** |

---

## 🌐 Is It Served Publicly?

Yes — by default, GitHub Pages sites are **publicly accessible** on the internet.  
Your site will be available at:

```
https://<USERNAME>.github.io/<REPO_NAME>/
```

However, if you're on GitHub Enterprise Cloud or using private repos with access control, you can restrict visibility to only users with repo access.

---

## 📦 Does It Need to Be Added to the Repo?

Yes — GitHub Pages **must be built from a repo**, and the site content is served from the `gh-pages` branch of that repo. You can’t serve a Pages site without it being tied to a repo.

> 🔧 You don’t need to manually add the built files — `mkdocs gh-deploy` handles that for you.

---

## 🧠 TL;DR for Your Setup

- You can use `auto-homelab` as your public template repo
- MkDocs will hydrate your `.md` files and deploy the HTML to GitHub Pages
- The hydrated content is served publicly, but your dry templates remain private
- You can preview locally or automate deployment via GitHub Actions

