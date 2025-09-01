from pathlib import Path
from mkdocs_gen_files import new_file

def write_if_missing(path_str, content):
    path = Path(path_str)
    if not path.exists():
        with new_file(path) as f:
            f.write(content)

def append_if_missing(path_str, snippet, marker="{{ COUNTDOWN_SNIPPET }}"):
    path = Path(path_str)
    if path.exists():
        content = path.read_text()
        if marker not in content:
            content += "\n\n" + snippet
            with new_file(path) as f:
                f.write(content)
