from pathlib import Path
from mkdocs_gen_files import new_file

countdown_snippet = """
{{ COUNTDOWN_SNIPPET }}
"""

for path in Path("docs/tmp").rglob("*.md"):
    content = path.read_text()
    if "{{ COUNTDOWN_SNIPPET }}" not in content:
        content += "\n\n" + countdown_snippet
        with new_file(path) as f:
            f.write(content)
