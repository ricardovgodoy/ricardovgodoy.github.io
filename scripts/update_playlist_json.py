#!/usr/bin/env python3
import json
import os
import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from urllib.request import Request, urlopen

PLAYLIST_ID = "PL6-MIz5lpF6KsSKMpXc7QyQd1qxA7VCd5"
FEED_URL = f"https://www.youtube.com/feeds/videos.xml?playlist_id={PLAYLIST_ID}"

# Output file in Jekyll _data
OUT_PATH = os.path.join(os.path.dirname(__file__), "..", "_data", "playlist_videos.json")

# Namespaces in the feed
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
}

def fetch_xml(url: str) -> str:
    req = Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urlopen(req, timeout=30) as r:
        return r.read().decode("utf-8", errors="replace")

def main() -> int:
    xml_text = fetch_xml(FEED_URL)
    root = ET.fromstring(xml_text)

    videos = []
    for entry in root.findall("atom:entry", NS):
        title_el = entry.find("atom:title", NS)
        pub_el = entry.find("atom:published", NS)
        vid_el = entry.find("yt:videoId", NS)

        if vid_el is None or vid_el.text is None:
            continue

        title = (title_el.text or "").strip() if title_el is not None else ""
        published = (pub_el.text or "").strip() if pub_el is not None else ""

        # Keep date compact (YYYY-MM-DD) for display
        date_out = ""
        if published:
            try:
                date_out = datetime.fromisoformat(published.replace("Z", "+00:00")).date().isoformat()
            except Exception:
                date_out = ""

        videos.append({
            "id": vid_el.text.strip(),
            "title": title,
            "date": date_out
        })

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        json.dump(videos, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(videos)} videos to {OUT_PATH}")
    return 0

if __name__ == "__main__":
    sys.exit(main())
