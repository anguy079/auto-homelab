import mkdocs_gen_files

with mkdocs_gen_files.open("debug-info.md", "w") as f:
    f.write("# 🕵️ Debug Info\n\n")
    f.write("This page lists the variables available to `mkdocs-macros` during the build.\n\n")
    
    f.write("## `extra` Variables (from mkdocs.yml)\n\n")
    f.write("```yaml\n")
    f.write("{% for key, value in config.extra.items() %}")
    f.write(f"{{ key }}: {{ value }}\n")
    f.write("{% endfor %}")
    f.write("```\n\n")
    
    f.write("## `env` Variables (from Workflow Environment)\n\n")
    f.write("```yaml\n")
    f.write("{% for key, value in env.items() %}")
    f.write(f"{{ key }}: {{ value }}\n")
    f.write("{% endfor %}")
    f.write("```\n")
