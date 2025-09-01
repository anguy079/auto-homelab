from pathlib import Path
import yaml

mkdocs_path = Path("mkdocs.yml")

# Group hydrated files by subfolder
grouped = {}
for path in sorted(Path("docs/tmp").rglob("*.md")):
    if path.name == "index.md":
        continue
    rel = path.relative_to("docs/tmp")
    parts = rel.parts
    title = path.stem.replace("-", " ").title()
    entry = {title: str(rel)}

    if len(parts) == 1:
        grouped.setdefault("_root", []).append(entry)
    else:
        grouped.setdefault(parts[0], []).append(entry)

# Build nav block
nav = [{"Hydration Preview": "index.md"}]
for folder, entries in grouped.items():
    if folder == "_root":
        nav.extend(entries)
    else:
        nav.append({folder.title(): entries})

# Load existing mkdocs.yml
config = yaml.safe_load(mkdocs_path.read_text())

# Replace or insert nav block
config["nav"] = nav

# Write updated mkdocs.yml
mkdocs_path.write_text(yaml.dump(config, sort_keys=False))
