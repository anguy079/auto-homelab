from mkdocs_gen_files import new_file
from pathlib import Path

templates = {
    "docs/tmp/index.md": "# 🧬 Hydrated Templates\n\nThis page was auto-generated.\n",
    "docs/mkdocs/README.md": "# 🧪 Getting Started\n\nThis guide explains hydration workflows.\n",
    "docs/mkdocs/mkdocs-overview.md": "# 📦 MkDocs Overview\n\nFeatures, plugins, and setup.\n"
}

for path_str, content in templates.items():
    path = Path(path_str)
    if not path.exists():
        with new_file(path) as f:
            f.write(content)
