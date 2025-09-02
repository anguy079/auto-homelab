import shutil

# This script now just copies the template.
# All other logic is handled by other scripts or plugins.
try:
    shutil.copyfile("docs/templates/index.md", "docs/tmp/index.md")
    print("Successfully copied index.md to docs/tmp/")
except FileNotFoundError:
    print("ERROR: Source file docs/templates/index.md not found.")
    exit(1) # Exit with an error to fail the build
