# 🧬 MkDocs Variables

This repo uses variables in `mkdocs.yml` to inject dynamic content into Markdown files.

## ✅ Defining Variables

```yaml
extra:
  GH_USERNAME: anguy079
  REPO_ORIGIN: linuxserver/docker-radarr
  COUNTDOWN_END: "2025-09-02T03:00:00Z"
```

---

## ✅ Using Variables in Markdown

```markdown
Forked from `{{ REPO_ORIGIN }}`  
Maintained by `{{ GH_USERNAME }}`
```

## 🧼 Privacy Hygiene

Avoid hardcoding usernames or repo names. Use variables to keep forks clean and audit-friendly.

---
