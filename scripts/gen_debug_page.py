import mkdocs_gen_files

with mkdocs_gen_files.open("debug-info.md", "w") as f:
    f.write("# 🕵️ Debug Info\n\n")
    f.write("This page lists the variables available to `mkdocs-macros` during the build.\n\n")
    
    f.write("## `extra` Variables (from mkdocs.yml)\n")
    f.write("```\n")
    f.write("{{ config.extra | tojson(indent=2) }}\n")
    f.write("```\n\n")
    
    f.write("## `env` Variables (from Workflow Environment)\n")
    f.write("```\n")
    f.write("{{ env | tojson(indent=2) }}\n")
    f.write("```\n")
