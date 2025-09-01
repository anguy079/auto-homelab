This guide will walk you through:

- 🔧 Setting up MkDocs with Macros for variable substitution  
- 📁 Hydrating specific files or folders  
- 🚀 Previewing or copying hydrated files into your private repo  
- 🧼 Optional cleanup for temporary usage  
- 🧬 Future automation with GitHub Actions or CLI scripts  

---

## 🧩 Step 1: Create Your Public Template Repo (`auto-homelab`)

Structure it like this:

```
auto-homelab/
├── mkdocs.yml
├── docs/
│   ├── github/
│   │   └── template-forking.md
│   └── services/
│       └── radarr/
│           └── sync-guide.md
```

All `.md` files should use variables like `{{ GH_USERNAME }}`, `{{ FORK_NAME }}`, etc.

---

## 🧠 Step 2: Define Variables in `mkdocs.yml`

```yaml
site_name: Auto Homelab Docs
plugins:
  - search
  - macros

extra:
  GH_USERNAME: anguy079
  FORK_NAME: lsio-docker-radarr
  REPO_ORIGIN: linuxserver/docker-radarr
  TARGET_FOLDER: services/radarr
  WORKFLOW_FILE: sync-lsio-docker-radarr.yml
```

You can later swap these values for other services like Sonarr, etc.

---

## 💧 Step 3: Use Variables in Markdown

In `docs/github/template-forking.md`:

```markdown
Go to https://github.com/{{ GH_USERNAME }}/{{ FORK_NAME }}/settings  
Click **Leave fork network**  
Then run:
```bash
git clone https://github.com/{{ GH_USERNAME }}/{{ FORK_NAME }}.git && \
cd {{ FORK_NAME }} && \
git remote add upstream https://github.com/{{ REPO_ORIGIN }}.git && \
git remote -v
```

---

## 🔍 Step 4: Preview Hydrated Docs (No Save)

Run locally:

```bash
mkdocs serve
```

To view the hydrated file with all variables substituted: [click here](http://localhost:8000/github/template-forking/)
> — perfect for quick reference.

---

## 📦 Step 5: Copy Hydrated Files into `homelab` (Optional)

Install [`mkdocs-gen-files`](https://github.com/timvink/mkdocs-gen-files) or [`mkdocs-copy`](https://github.com/chikamichi/mkdocs-copy) to copy hydrated files.

Example config in `mkdocs.yml`:

```yaml
plugins:
  - macros
  - mkdocs-copy:
      add_per_path:
        - docs/github/template-forking.md: ../homelab/docs/services/radarr/radarr-forking.md
```

This will:
- Hydrate `template-forking.md`
- Rename it to `radarr-forking.md`
- Place it in your private repo under `docs/services/radarr/`

---

## 🧼 Step 6: Temporary Usage + Cleanup

If you just want to grab commands and discard the file:

```bash
mkdocs build
cat site/github/template-forking/index.html  # or open in browser
rm site/github/template-forking/index.html   # cleanup
```

Or copy to `/tmp` and delete after use.

---

## 🧬 Step 7: Automate with GitHub Actions (Optional)

You can set up a GitHub Action in `auto-homelab` to:

- Build hydrated docs
- Push them to a branch in `homelab`
- Trigger a PR or sync script

---

## 🧠 Final Thoughts

This setup gives you:

- 🔐 Privacy-safe templates with no personal info
- 🧬 Reproducible onboarding and sync guides
- 🚀 Fast hydration for CLI or contributor use
- 🧼 Optional cleanup or automation
