from pathlib import Path
import yaml

mkdocs_path = Path("mkdocs.yml")

# Icon map for known services
folder_icons = {
    "radarr": ":radarr:",
    "sonarr": ":sonarr:",
    "plex": ":plex:",
    "_root": ":file:"
}

# Icon map for common file types
file_icons = {
    "sync": ":link:",
    "fork": ":fork:",
    "onboard": ":rocket:",
    "guide": ":book:"
}

# Group hydrated files by subfolder
grouped = {}
for path in sorted(Path("docs/tmp").rglob("*.md")):
    if path.name == "index.md":
        continue
    rel = path.relative_to("docs/tmp")
    parts = rel.parts
    stem = path.stem.replace("-", " ").title()

    # Determine file icon
    file_icon = next((icon for key, icon in file_icons.items() if key in path.stem.lower()), ":file:")
    title = f"{file_icon} {stem}"
    entry = {title: str(rel)}

    # Group by folder
    if len(parts) == 1:
        grouped.setdefault("_root", []).append(entry)
    else:
        grouped.setdefault(parts[0], []).append(entry)

# Build nav block
nav = [{":droplet: Hydration Preview": "index.md"}]
for folder, entries in grouped.items():
    if folder == "_root":
        nav.extend(entries)
    else:
        folder_icon = folder_icons.get(folder.lower(), ":folder:")
        folder_title = f"{folder_icon} {folder.title()}"
        nav.append({folder_title: entries})

# Load existing mkdocs.yml
config = yaml.safe_load(mkdocs_path.read_text())
config["nav"] = nav
mkdocs_path.write_text(yaml.dump(config, sort_keys=False))
