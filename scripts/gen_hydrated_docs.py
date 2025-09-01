from scripts import append_if_missing
from pathlib import Path

countdown_snippet = "{{ COUNTDOWN_SNIPPET }}"

for path in Path("docs/tmp").rglob("*.md"):
    append_if_missing(str(path), countdown_snippet)
