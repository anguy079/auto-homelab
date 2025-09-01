import yaml
from pathlib import Path

mkdocs_path = Path("mkdocs.yml")

# Load data from the central YAML file
try:
    with open("data/services.yml", "r") as f:
        data = yaml.safe_load(f)
    folder_icons = data.get("folder_icons", {})
    file_icons = data.get("file_icons", {})
except (IOError, yaml.YAMLError) as e:
    print(f"Error reading data/services.yml: {e}")
    folder_icons, file_icons = {}, {}

grouped = {}
for path in sorted(Path("docs/tmp").rglob("*.md")):
    if path.name == "index.md":
        continue
    rel = path.relative_to("docs/tmp")
    parts = rel.parts
    stem = path.stem.replace("-", " ").title()
    file_icon = next((icon for key, icon in file_icons.items() if key in path.stem.lower()), ":file:")
    title = f"{file_icon} {stem}"
    entry = {title: str(rel)}

    if len(parts) == 1:
        grouped.setdefault("_root", []).append(entry)
    else:
        grouped.setdefault(parts[0], []).append(entry)

nav = [{":droplet: Hydration Preview": "index.md"}]
for folder, entries in grouped.items():
    if folder == "_root":
        nav.extend(entries)
    else:
        folder_title = folder_icons.get(folder.lower(), f":folder: {folder.title()}")
        nav.append({folder_title: entries})

try:
    config = yaml.load(mkdocs_path.read_text(), Loader=yaml.FullLoader)
    config["nav"] = nav
    mkdocs_path.write_text(yaml.dump(config, sort_keys=False))
except (IOError, yaml.YAMLError) as e:
    print(f"Error processing mkdocs.yml: {e}")
