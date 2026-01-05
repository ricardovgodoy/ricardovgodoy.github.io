---
layout: single
title: "Videos"
permalink: /videos/
author_profile: true
---

<div class="yt-actions">
  <a class="yt-btn" href="https://www.youtube.com/@RicardoVGodoy" target="_blank" rel="noopener">
    Visit my YouTube channel
  </a>
</div>

<div class="yt-grid">
{% assign selected_ids = site.data.videos | map: "id" %}

{% for v in site.data.videos %}
  <div class="yt-card">
    <div class="yt-embed">
      <iframe
        loading="lazy"
        referrerpolicy="strict-origin-when-cross-origin"
        src="https://www.youtube-nocookie.com/embed/{{ v.id | strip }}?rel=0"
        title="{{ v.title | escape }}"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
      </iframe>
    </div>
    <div class="yt-meta">
      <div class="yt-title">{{ v.title }}</div>
      {% if v.date %}<div class="yt-sub">{{ v.date }}</div>{% endif %}
      {% if v.description %}<div class="yt-desc">{{ v.description }}</div>{% endif %}
    </div>
  </div>
{% endfor %}

{% if site.data.playlist_videos %}
  {% for p in site.data.playlist_videos %}
    {% unless selected_ids contains p.id %}
      <div class="yt-card">
        <div class="yt-embed">
          <iframe
            loading="lazy"
            referrerpolicy="strict-origin-when-cross-origin"
            src="https://www.youtube-nocookie.com/embed/{{ p.id | strip }}?rel=0"
            title="{{ p.title | escape }}"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen>
          </iframe>
        </div>
        <div class="yt-meta">
          <div class="yt-title">{{ p.title }}</div>
          {% if p.date %}<div class="yt-sub">{{ p.date }}</div>{% endif %}
        </div>
      </div>
    {% endunless %}
  {% endfor %}
{% endif %}
</div>

<style>
.yt-actions{display:flex;justify-content:center;margin:1rem 0 1.5rem 0;}
.yt-btn{display:inline-block;padding:.55rem .9rem;border-radius:.6rem;text-decoration:none;border:1px solid rgba(127,127,127,.35);}
.yt-btn:hover{opacity:.9}

.yt-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1rem;}
.yt-card{border:1px solid rgba(127,127,127,.25);border-radius:.9rem;overflow:hidden;}
.yt-embed{position:relative;padding-bottom:56.25%;height:0;}
.yt-embed iframe{position:absolute;top:0;left:0;width:100%;height:100%;}
.yt-meta{padding:.75rem .9rem;}
.yt-title{font-weight:700;line-height:1.25;}
.yt-sub{opacity:.8;font-size:.9rem;margin-top:.2rem;}
.yt-desc{margin-top:.55rem;opacity:.9;font-size:.95rem;line-height:1.4;}
</style>
