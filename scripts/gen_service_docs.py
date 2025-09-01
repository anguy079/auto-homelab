from scripts import write_if_missing
from pathlib import Path

services = {
    "radarr": {
        "title": "Radarr Forking Guide",
        "repo": "{{ REPO_ORIGIN }}",
        "user": "{{ GH_USERNAME }}",
        "countdown": "{{ COUNTDOWN_SNIPPET }}"
    },
    "sonarr": {
        "title": "Sonarr Forking Guide",
        "repo": "{{ REPO_ORIGIN }}",
        "user": "{{ GH_USERNAME }}",
        "countdown": "{{ COUNTDOWN_SNIPPET }}"
    }
}

for name, data in services.items():
    path = f"docs/tmp/{name}.md"
    content = f"""# 📦 {data['title']}

This guide helps you fork and hydrate `{data['repo']}` using your GitHub account `{data['user']}`.

---

{data['countdown']}
"""
    write_if_missing(path, content)
