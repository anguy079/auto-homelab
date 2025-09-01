# 🧪 Variable Substitution Test Page

This page displays the values of the dynamic variables populated by the GitHub Actions workflow and the `mkdocs-macros` plugin.

---

### ## Repository Information

| Variable | Value from Macro | Expected Output Example |
| :--- | :--- | :--- |
| **Repo Owner** | `{{ REPO_OWNER }}` | `anguy079` |
| **Repo Name** | `{{ REPO_NAME }}` | `auto-homelab` |
| **Full Repo Name** | `{{ REPO_FULL_NAME }}` | `anguy079/auto-homelab` |
| **Repo URL** | `{{ REPO_URL }}` | `https://github.com/anguy079/auto-homelab` |

---

### ## Build & Commit Information

| Variable | Value from Macro | Expected Output Example |
| :--- | :--- | :--- |
| **Triggered By** | `{{ LAST_UPDATED_BY }}` | `anguy079` |
| **Commit SHA** | `{{ COMMIT_SHA }}` | `e0ed3ea...` |
| **Branch/Ref Name**| `{{ REF_NAME }}` | `main` |

---

### ## Site & Workflow Information

| Variable | Value from Macro | Expected Output Example |
| :--- | :--- | :--- |
| **Workflow Run ID**| `{{ WORKFLOW_RUN }}` | `123456789` |
| **Site URL** | `{{ SITE_URL }}` | `https://anguy079.github.io/auto-homelab/`|

---

### ## Live Countdown Timer Test

<div id="countdown"></div>
<script>
  const endTime = new Date("{{ COUNTDOWN_END }}");
  const countdown = document.getElementById("countdown");
  setInterval(() => {
    const now = new Date();
    const diff = endTime - now;
    const hours = Math.floor(diff / 3600000);
    const minutes = Math.floor((diff % 3600000) / 60000);
    countdown.textContent = `Time remaining: ${hours}h ${minutes}m`;
  }, 60000);
</script>
