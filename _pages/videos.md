---
title: "Videos"
permalink: /videos/
author_profile: true
---

<div class="yt-header">
  <a class="yt-subscribe" href="https://www.youtube.com/@RicardoVGodoy" target="_blank" rel="noopener">
    Visit my YouTube channel
  </a>
</div>

<div class="yt-grid">
  {% assign vids = site.data.videos %}
  {% for v in vids %}
    <a class="yt-card" href="https://www.youtube.com/watch?v={{ v.youtube_id }}" target="_blank" rel="noopener">
      <div class="yt-thumb">
        <img src="{{ v.thumbnail }}" alt="{{ v.title | escape }}">
      </div>
      <div class="yt-title">{{ v.title }}</div>
      <div class="yt-meta">{{ v.date | date: "%d/%m/%Y" }}</div>
    </a>
  {% endfor %}
</div>

<style>
.yt-header{margin:0 0 18px 0;display:flex;justify-content:flex-end}
.yt-subscribe{font-size:.95em;text-decoration:none;border:1px solid rgba(0,0,0,.15);padding:8px 12px;border-radius:10px}
.yt-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px}
.yt-card{text-decoration:none;display:block}
.yt-thumb{position:relative;aspect-ratio:16/9;overflow:hidden;border-radius:12px;background:rgba(0,0,0,.06)}
.yt-thumb img{width:100%;height:100%;object-fit:cover;display:block}
.yt-title{margin-top:10px;font-weight:600;line-height:1.25}
.yt-meta{font-size:.85em;opacity:.75;margin-top:4px}
</style>
