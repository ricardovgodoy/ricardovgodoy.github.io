---
layout: single
title: "Videos"
permalink: /videos/
author_profile: true
---

Here are videos from my YouTube channel.

<div class="yt-actions">
  <a class="yt-btn" href="https://www.youtube.com/@RicardoVGodoy" target="_blank" rel="noopener">
    Visit my YouTube channel
  </a>
</div>

## Selected Videos

<div class="yt-grid">
{% for v in site.data.videos %}
  <div class="yt-card">
    <div class="yt-embed">
      <iframe
        loading="lazy"
        src="https://www.youtube.com/embed/{{ v.id }}"
        title="{{ v.title | escape }}"
        frameborder="0"
        allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
        allowfullscreen>
      </iframe>
    </div>
    <div class="yt-meta">
      <div class="yt-title">{{ v.title }}</div>
      {% if v.date %}
      <div class="yt-sub">{{ v.date }}</div>
      {% endif %}
      {% if v.description %}
      <div class="yt-desc">{{ v.description }}</div>
      {% endif %}
    </div>
  </div>
{% endfor %}
</div>

---

## Public Playlist

<div id="playlistStatus" class="yt-status">Loading playlist…</div>
<div id="playlistGrid" class="yt-grid"></div>

<style>
/* Buttons */
.yt-actions{display:flex;justify-content:center;margin:1rem 0 1.5rem 0;}
.yt-btn{display:inline-block;padding:.55rem .9rem;border-radius:.6rem;text-decoration:none;border:1px solid rgba(127,127,127,.35);}
.yt-btn:hover{opacity:.9}

/* Video cards */
.yt-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:1rem;}
.yt-card{border:1px solid rgba(127,127,127,.25);border-radius:.9rem;overflow:hidden;}
.yt-embed{position:relative;padding-bottom:56.25%;height:0;}
.yt-embed iframe{position:absolute;top:0;left:0;width:100%;height:100%;}
.yt-meta{padding:.75rem .9rem;}
.yt-title{font-weight:700;line-height:1.25;}
.yt-sub{opacity:.8;font-size:.9rem;margin-top:.2rem;}
.yt-desc{margin-top:.55rem;opacity:.9;font-size:.95rem;line-height:1.4;}

.yt-status{padding:.2rem 0 .8rem 0;opacity:.85;font-size:.95rem;}
</style>

{% raw %}
<script>
(() => {
  const PLAYLIST_ID = "PL6-MIz5lpF6KsSKMpXc7QyQd1qxA7VCd5";
  const FEED_URL = `https://www.youtube.com/feeds/videos.xml?playlist_id=${PLAYLIST_ID}`;

  const statusEl = document.getElementById("playlistStatus");
  const gridEl = document.getElementById("playlistGrid");

  function escapeHtml(s) {
    return (s || "").replace(/[&<>"']/g, (c) => ({
      "&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"
    }[c]));
  }

  function parseFeed(xmlText) {
    const doc = new DOMParser().parseFromString(xmlText, "text/xml");
    const entries = Array.from(doc.getElementsByTagName("entry"));

    return entries.map(e => {
      const title = e.getElementsByTagName("title")[0]?.textContent?.trim() || "Untitled";
      const publishedRaw = e.getElementsByTagName("published")[0]?.textContent || "";
      const published = publishedRaw ? new Date(publishedRaw).toLocaleDateString() : "";
      const videoId =
        e.getElementsByTagNameNS("http://www.youtube.com/xml/schemas/2015", "videoId")[0]?.textContent ||
        e.getElementsByTagName("yt:videoId")[0]?.textContent ||
        "";

      return { title, published, videoId };
    }).filter(x => x.videoId);
  }

  function render(videos) {
    gridEl.innerHTML = "";
    if (!videos.length) {
      statusEl.textContent = "No videos found in this playlist.";
      return;
    }

    statusEl.textContent = ""; // hide status
    const frag = document.createDocumentFragment();

    for (const v of videos) {
      const card = document.createElement("div");
      card.className = "yt-card";
      card.innerHTML = `
        <div class="yt-embed">
          <iframe
            loading="lazy"
            src="https://www.youtube.com/embed/${v.videoId}"
            title="${escapeHtml(v.title)}"
            frameborder="0"
            allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
            allowfullscreen>
          </iframe>
        </div>
        <div class="yt-meta">
          <div class="yt-title">${escapeHtml(v.title)}</div>
          ${v.published ? `<div class="yt-sub">${escapeHtml(v.published)}</div>` : ``}
        </div>
      `;
      frag.appendChild(card);
    }

    gridEl.appendChild(frag);
  }

  async function load() {
    try {
      statusEl.textContent = "Loading playlist…";
      const res = await fetch(FEED_URL);
      if (!res.ok) throw new Error(`HTTP ${res.status}`);
      const xmlText = await res.text();
      const videos = parseFeed(xmlText);
      render(videos);
    } catch (err) {
      // Still give them something usable if fetch is blocked
      statusEl.innerHTML =
        `Could not load the playlist feed in this browser. You can still view it on YouTube: ` +
        `<a href="https://www.youtube.com/playlist?list=${PLAYLIST_ID}" target="_blank" rel="noopener">open playlist</a>.`;
    }
  }

  load();
})();
</script>
{% endraw %}
