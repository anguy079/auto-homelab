from pathlib import Path
import mkdocs_gen_files

def write_if_missing(path_str, content):
    path = Path(path_str)
    if not path.exists():
        with mkdocs_gen_files.open(path, "w") as f:
            f.write(content)

def append_if_missing(path_str, snippet, marker="{{ COUNTDOWN_SNIPPET }}"):
    path = Path(path_str)
    if path.exists():
        content = path.read_text()
        if marker not in content:
            content += "\n\n" + snippet
            with mkdocs_gen_files.open(path, "w") as f:
                f.write(content)
