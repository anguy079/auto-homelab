from pathlib import Path

nav_entries = []

# Scan all .md files in docs/tmp (excluding index.md)
for path in sorted(Path("docs/tmp").rglob("*.md")):
    if path.name == "index.md":
        continue
    title = path.stem.replace("-", " ").title()
    relative_path = str(path.relative_to("docs/tmp"))
    nav_entries.append(f"  - {title}: {relative_path}")

# Always include index.md at the top
nav_block = ["nav:", "  - Hydration Preview: index.md"] + nav_entries

# Write to a file for manual copy-paste into mkdocs.yml
Path("scripts/nav_output.yml").write_text("\n".join(nav_block))
