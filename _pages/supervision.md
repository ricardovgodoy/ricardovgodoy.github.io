---
layout: single
title: "Supervision"
permalink: /supervision/
author_profile: true
---

I supervise and co-supervise students across robotics, physical AI, and human–robot interaction.
Currently, I am the Technical leader of a team of 30-50 members from a big industry-funded project at the Univeristy of São Paulo.

{% assign primary = site.data.supervision.primary | default: empty %}
{% assign co = site.data.supervision.co | default: empty %}

{% assign degree_order = "phd|msc|ug" | split: "|" %}
{% assign degree_labels = "phd:PhD|msc:MSc|ug:Undergraduate" | split: "|" %}

{% capture help_note %}
To add or update students, edit <code>_data/supervision.yml</code>.
{% endcapture %}

<div class="sup-note">{{ help_note }}</div>

## Primary supervision

{% for d in degree_order %}
  {% assign group = primary | where: "degree", d | sort: "year" | reverse %}
  {% if group and group.size > 0 %}
### {% if d == "phd" %}PhD{% elsif d == "msc" %}MSc{% else %}Undergraduate{% endif %}

<div class="sup-table-wrap">
  <table class="sup-table">
    <thead>
      <tr>
        <th>Name</th>
        <th>Research topic</th>
        <th>Affiliation</th>
        <th class="sup-year">Year</th>
      </tr>
    </thead>
    <tbody>
      {% for s in group %}
      <tr>
        <td class="sup-name">{{ s.name }}</td>
        <td class="sup-topic">{{ s.topic }}</td>
        <td class="sup-affil">{{ s.affiliation }}</td>
        <td class="sup-year">{{ s.year }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
  {% endif %}
{% endfor %}

---

## Co-supervision

{% for d in degree_order %}
  {% assign group = co | where: "degree", d | sort: "year" | reverse %}
  {% if group and group.size > 0 %}
### {% if d == "phd" %}PhD{% elsif d == "msc" %}MSc{% else %}Undergraduate{% endif %}

<div class="sup-table-wrap">
  <table class="sup-table">
    <thead>
      <tr>
        <th>Name</th>
        <th>Research topic</th>
        <th>Affiliation</th>
        <th class="sup-year">Year</th>
      </tr>
    </thead>
    <tbody>
      {% for s in group %}
      <tr>
        <td class="sup-name">{{ s.name }}</td>
        <td class="sup-topic">{{ s.topic }}</td>
        <td class="sup-affil">{{ s.affiliation }}</td>
        <td class="sup-year">{{ s.year }}</td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</div>
  {% endif %}
{% endfor %}

<style>
/* Small note */
.sup-note{
  margin: 0.6rem 0 1.2rem 0;
  padding: 0.7rem 0.9rem;
  border: 1px solid rgba(127,127,127,.25);
  border-radius: .75rem;
  opacity: .95;
}

/* Table */
.sup-table-wrap{ overflow-x:auto; margin: .6rem 0 1.2rem 0; }
.sup-table{
  width: 100%;
  border-collapse: collapse;
  border: 1px solid rgba(127,127,127,.25);
  border-radius: .75rem;
  overflow: hidden;
}
.sup-table thead th{
  text-align: left;
  font-weight: 700;
  padding: .7rem .8rem;
  border-bottom: 1px solid rgba(127,127,127,.2);
}
.sup-table td{
  padding: .65rem .8rem;
  vertical-align: top;
  border-top: 1px solid rgba(127,127,127,.15);
}
.sup-year{ white-space: nowrap; width: 5.5rem; }
.sup-name{ font-weight: 600; }
.sup-topic{ min-width: 18rem; }
.sup-affil{ min-width: 14rem; opacity: .95; }
</style>
