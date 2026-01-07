---
layout: single
title: "Supervision"
permalink: /supervision/
author_profile: true
---

{% assign sup = site.data.supervision %}
{% assign degree_order = "phd|msc|ug" | split: "|" %}

I supervise and co-supervise students across robotics, physical AI, and human–robot interaction.

## Primary supervision

{% if sup and sup.primary %}
  {% for d in degree_order %}
    {% assign group = sup.primary | where: "degree", d | sort: "year" | reverse %}
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
{% else %}
<p><em>No primary-supervised students listed yet.</em></p>
{% endif %}

---

## Co-supervision

{% if sup and sup.co %}
  {% for d in degree_order %}
    {% assign group = sup.co | where: "degree", d | sort: "year" | reverse %}
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
{% else %}
<p><em>No co-supervised students listed yet.</em></p>
{% endif %}

<style>
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
