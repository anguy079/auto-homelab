import mkdocs_gen_files
import shutil

# Copy the main index page from the safe templates directory
try:
    shutil.copyfile("docs/templates/index.md", "docs/tmp/index.md")
    mkdocs_gen_files.set_edit_path("docs/tmp/index.md", "docs/templates/index.md")
except FileNotFoundError:
    print("Warning: docs/templates/index.md not found.")
