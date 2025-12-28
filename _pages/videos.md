---
title: "Videos"
permalink: /videos/
author_profile: true
---

Short clips of experiments, system demos, and robot setups.

<div class="yt-header">
  <a class="yt-subscribe" href="https://www.youtube.com/@RicardoVGodoy" target="_blank" rel="noopener">
    Visit my YouTube channel
  </a>
</div>

{% if site.data.videos and site.data.videos.size > 0 %}
  <div class="yt-grid">
    {% for v in site.data.videos %}
      <div class="yt-card" data-video-id="{{ v.youtube_id }}">
        <button class="yt-thumb yt-play" type="button" aria-label="Play {{ v.title | escape }}">
          <img src="{{ v.thumbnail }}" alt="{{ v.title | escape }}">
          <span class="yt-play-icon">▶</span>
        </button>
        <div class="yt-title">{{ v.title }}</div>
        <div class="yt-meta">{{ v.date | date: "%d/%m/%Y" }}</div>
      </div>
    {% endfor %}
  </div>
{% else %}
  <p style="opacity:.75;">No videos loaded yet. Run the “Update YouTube videos list” workflow once to generate <code>_data/videos.yml</code>.</p>
{% endif %}

<script>
document.addEventListener("click", function (e) {
  const btn = e.target.closest(".yt-play");
  if (!btn) return;

  const card = btn.closest(".yt-card");
  const id = card.getAttribute("data-video-id");

  const iframe = document.createElement("iframe");
  iframe.src = "https://www.youtube-nocookie.com/embed/" + id + "?autoplay=1";
  iframe.title = "YouTube video player";
  iframe.allow = "accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share";
  iframe.allowFullscreen = true;
  iframe.loading = "lazy";

  const wrap = document.createElement("div");
  wrap.className = "yt-player";
  wrap.appendChild(iframe);

  btn.replaceWith(wrap);
});
</script>

<style>
.yt-header{margin:0 0 18px 0;display:flex;justify-content:center}
.yt-subscribe{font-size:.95em;text-decoration:none;border:1px solid rgba(0,0,0,.15);padding:8px 12px;border-radius:10px}

.yt-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:18px}
.yt-card{display:block}

.yt-thumb{
  position:relative;
  aspect-ratio:16/9;
  overflow:hidden;
  border-radius:12px;
  background:rgba(0,0,0,.06);
  padding:0;
  border:0;
  width:100%;
  cursor:pointer;
}
.yt-thumb img{width:100%;height:100%;object-fit:cover;display:block}

.yt-player{
  position:relative;
  aspect-ratio:16/9;
  overflow:hidden;
  border-radius:12px;
  background:rgba(0,0,0,.06);
}
.yt-player iframe{
  position:absolute;
  inset:0;
  width:100%;
  height:100%;
  border:0;
}

.yt-play-icon{
  position:absolute;
  left:50%;
  top:50%;
  transform:translate(-50%,-50%);
  font-size:42px;
  line-height:1;
  padding:10px 16px;
  border-radius:999px;
  background:rgba(0,0,0,.55);
  color:#fff;
}
.yt-thumb:hover .yt-play-icon{background:rgba(0,0,0,.7)}

.yt-title{margin-top:10px;font-weight:600;line-height:1.25}
.yt-meta{font-size:.85em;opacity:.75;margin-top:4px}
</style>
