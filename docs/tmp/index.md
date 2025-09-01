# 🧬 Hydrated Templates

Below are the currently hydrated templates:

{% for file in files if file.is_page and not file.is_index %}
- [{{ file.title }}]({{ file.url }})
{% endfor %}

---

<div id="countdown"></div>
<script>
  const endTime = new Date("{{ COUNTDOWN_END }}");
  const countdown = document.getElementById("countdown");
  setInterval(() => {
    const now = new Date();
    const diff = endTime - now;
    const hours = Math.floor(diff / 3600000);
    const minutes = Math.floor((diff % 3600000) / 60000);
    countdown.textContent = `Global hydration expires in: ${hours}h ${minutes}m`;
  }, 60000);
</script>
