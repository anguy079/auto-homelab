import yaml
import shutil
from pathlib import Path

def copy_recursive(source_str, dest_str):
    """Recursively copies a directory and its contents."""
    source_path = Path(source_str)
    dest_path = Path(dest_str)
    if not source_path.exists() or not source_path.is_dir():
        print(f"Warning: Source directory for copy task '{source_str}' not found.")
        return
    dest_path.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source_path, dest_path, dirs_exist_ok=True)
    print(f"Copied contents from '{source_str}' to '{dest_str}'.")

def generate_services(data_file_str, dest_str):
    """Generates Markdown files for services."""
    try:
        with open(data_file_str, "r", encoding="utf-8") as f:
            service_data = yaml.safe_load(f)
        services_to_generate = service_data.get("services", {})
        dest_path = Path(dest_str)
        dest_path.mkdir(parents=True, exist_ok=True)
        for name, data in services_to_generate.items():
            file_path = dest_path / f"{name}.md"
            content = f"""# 📦 {data['title']}

This guide helps you fork and hydrate `{{{{ REPO_FULL_NAME }}}}` using your GitHub account `{{{{ REPO_OWNER }}}}`.
"""
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)
        print(f"Generated {len(services_to_generate)} service documents in '{dest_str}'.")
    except FileNotFoundError:
        print(f"Warning: Data file '{data_file_str}' not found. No service docs generated.")
    except Exception as e:
        print(f"An error occurred generating service docs: {e}")

def main():
    """Orchestrates the hydration process based on config.yml."""
    print("--- Starting hydration process ---")
    try:
        with open("config.yml", "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        tasks = config.get("hydration_tasks", [])
        print(f"Found {len(tasks)} hydration tasks in config.yml.")
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f"Error reading or parsing config.yml: {e}")
        return

    for i, task in enumerate(tasks, 1):
        task_type = task.get("type")
        print(f"\n--- Running Task {i}: {task.get('description', task_type)} ---")
        if task_type == "copy_recursive":
            copy_recursive(task.get("source"), task.get("destination"))
        elif task_type == "generate_services":
            generate_services(task.get("data_file"), task.get("destination"))
        else:
            print(f"Warning: Unknown task type '{task_type}'. Skipping.")
    print("\n--- Hydration process complete ---")

if __name__ == "__main__":
    main()
