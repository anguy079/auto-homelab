from mkdocs_gen_files import new_file, set_edit_path
from pathlib import Path

index_path = Path("docs/tmp/index.md")
if not index_path.exists():
    with new_file(index_path) as f:
        f.write("# 🧬 Hydrated Templates\n\n")
        f.write("This page was auto-generated during build.\n\n")
        f.write("Use the hydration workflow to populate this folder.\n")
    set_edit_path(index_path, "docs/tmp/index.md")
