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

{{ render_nav_items(nav.items) }}
