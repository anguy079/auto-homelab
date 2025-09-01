from scripts import write_if_missing

# This script no longer creates index.md
write_if_missing("docs/mkdocs/mkdocs-overview.md", "# 📦 MkDocs Overview\n\nFeatures, plugins, and setup.\n")
