import mkdocs_gen_files
from pathlib import Path

index_path = Path("docs/tmp/index.md")
if not index_path.exists():
    with mkdocs_gen_files.open(index_path, "w") as f:
        f.write("# 🧬 Hydrated Templates\n\n")
        f.write("This page was auto-generated during build.\n\n")
        f.write("Use the hydration workflow to populate this folder.\n")
    mkdocs_gen_files.set_edit_path(index_path, "docs/tmp/index.md")
