from scripts import write_if_missing

# The line for docs/mkdocs/README.md has been removed.
write_if_missing("docs/tmp/index.md", "# 🧬 Hydrated Templates\n\nThis page was auto-generated.\n")
write_if_missing("docs/mkdocs/mkdocs-overview.md", "# 📦 MkDocs Overview\n\nFeatures, plugins, and setup.\n")
