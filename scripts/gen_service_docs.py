import yaml
from pathlib import Path
from scripts import write_if_missing

# Load data from the central YAML file
with open("data/services.yml", "r") as f:
    data = yaml.safe_load(f)

services = data.get("services", {})
repo_origin = "{{ REPO_ORIGIN }}"
gh_username = "{{ GH_USERNAME }}"
countdown_snippet = "{{ COUNTDOWN_SNIPPET }}"

for name, service_data in services.items():
    path = f"docs/tmp/{name}.md"
    content = f"""# 📦 {service_data['title']}

This guide helps you fork and hydrate `{repo_origin}` using your GitHub account `{gh_username}`.

---

{countdown_snippet}
"""
    try:
        write_if_missing(path, content)
    except IOError as e:
        print(f"Error writing file {path}: {e}")
