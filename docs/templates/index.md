# 🧬 Hydrated Templates

Below is the directory of currently hydrated templates:

---

{% macro render_nav_items(items) %}
<ul>
  {% for item in items %}
    <li>
      {% if item.url %}
        <a href="{{ item.url | url }}">{{ item.title }}</a>
      {% else %}
        <strong>{{ item.title }}</strong>
      {% endif %}
      {% if item.children %}
        {{ render_nav_items(item.children) }}
      {% endif %}
    </li>
  {% endfor %}
</ul>
{% endmacro %}

{{ render_nav_items(navigation) }}

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
