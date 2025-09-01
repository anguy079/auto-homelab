Go to https://github.com/{{ GH_USERNAME }}/{{ FORK_NAME }}/settings  
Click **Leave fork network**  
Then run:
```bash
git clone https://github.com/{{ GH_USERNAME }}/{{ FORK_NAME }}.git && \
cd {{ FORK_NAME }} && \
git remote add upstream https://github.com/{{ REPO_ORIGIN }}.git && \
git remote -v
```

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
