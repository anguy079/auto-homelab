import os
import yaml
from datetime import datetime, timezone, timedelta

def main():
    """
    Reads config.yml and GitHub env variables, then dynamically
    configures mkdocs.yml for the build.
    """
    print("--- Configuring mkdocs.yml dynamically ---")

    # --- Load configurations ---
    try:
        with open("config.yml", "r", encoding="utf-8") as f:
            config = yaml.safe_load(f)
        with open("mkdocs.yml", "r", encoding="utf-8") as f:
            mkdocs_config = yaml.load(f, Loader=yaml.FullLoader)
    except (FileNotFoundError, yaml.YAMLError) as e:
        print(f"Error reading YAML files: {e}")
        exit(1)

    # --- Prepare variables ---
    # Start with variables defined in the config file
    final_vars = config.get("variables", {})

    # Define auto-populated variables from the GitHub environment
    # The value from config.yml will be used if it's not blank, otherwise, the GitHub variable is used.
    auto_vars = {
        "REPO_OWNER": os.environ.get("GITHUB_REPOSITORY_OWNER"),
        "REPO_FULL_NAME": os.environ.get("GITHUB_REPOSITORY"),
        "REPO_NAME": os.environ.get("GITHUB_REPOSITORY_NAME"),
        "REPO_URL": f"{os.environ.get('GITHUB_SERVER_URL')}/{os.environ.get('GITHUB_REPOSITORY')}"
    }

    # Merge the dictionaries, giving precedence to non-empty values in config.yml
    for key, value in auto_vars.items():
        if not final_vars.get(key):
            final_vars[key] = value

    # --- Calculate Countdown End Time ---
    hours_str = os.environ.get("INPUT_DELETE_AFTER_HOURS")
    default_hours = config.get("hydration_settings", {}).get("default_hours", 24)
    try:
        # Use user input if provided, otherwise use default from config.yml
        hours = int(hours_str if hours_str else default_hours)
    except (ValueError, TypeError):
        hours = int(default_hours)

    if hours == 0:
        end_time = "2099-12-31T23:59:59Z"
    else:
        end_time_dt = datetime.now(timezone.utc) + timedelta(hours=hours)
        end_time = end_time_dt.isoformat().replace("+00:00", "Z")

    final_vars['COUNTDOWN_END'] = end_time
    
    # --- Update mkdocs.yml in memory ---
    # Set the final site_url
    mkdocs_config['site_url'] = f"https://{final_vars['REPO_OWNER']}.github.io/{final_vars['REPO_NAME']}"
    
    # Inject all variables into the 'extra' block
    if 'extra' not in mkdocs_config or not mkdocs_config['extra']:
        mkdocs_config['extra'] = {}
    mkdocs_config['extra'].update(final_vars)

    # --- Write the new mkdocs.yml ---
    try:
        with open("mkdocs.yml", "w", encoding="utf-8") as f:
            yaml.dump(mkdocs_config, f, sort_keys=False)
        print("Successfully configured mkdocs.yml with dynamic variables.")
    except IOError as e:
        print(f"Error writing to mkdocs.yml: {e}")
        exit(1)

if __name__ == "__main__":
    main()
