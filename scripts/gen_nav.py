from pathlib import Path
import yaml

mkdocs_path = Path("mkdocs.yml")

folder_icons = {
    "radarr": ":radarr:{ .radarr-icon }",
    "sonarr": ":sonarr:{ .sonarr-icon }",
    "plex": ":plex:{ .plex-icon }",
    "_root": ":file:"
}

file_icons = {
    "sync": ":link:",
    "fork": ":fork:",
    "onboard": ":rocket:",
    "guide": ":book:"
}

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

config = yaml.safe_load(mkdocs_path.read_text())
config["nav"] = nav
mkdocs_path.write_text(yaml.dump(config, sort_keys=False))
