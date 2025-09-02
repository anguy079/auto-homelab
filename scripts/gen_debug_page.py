import mkdocs_gen_files

with mkdocs_gen_files.open("debug-info.md", "w") as f:
    f.write("# 🕵️ Debug Info\n\n")
    f.write("This page lists the final variables available to pages during the build.\n\n")
    
    f.write("## `extra` Variables (from mkdocs.yml)\n\n")
    f.write("These are the variables you can use in your Markdown files like `{{ REPO_OWNER }}`.\n\n")
    f.write("```yaml\n")
    # This loop correctly writes the Jinja2 syntax to the file
    f.write("{% for key, value in config.extra.items() %}")
    f.write("{{ key }}: {{ value }}\n")
    f.write("{% endfor %}")
    f.write("```\n")
