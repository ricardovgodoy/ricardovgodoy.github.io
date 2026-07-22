#!/usr/bin/env python3
"""Build the website video list from YouTube uploads, playlists, and collaborations."""

from __future__ import annotations

import html
import json
import os
import re
import sys
import unicodedata
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Iterator
from urllib.request import Request, urlopen


CHANNEL_URL = os.environ.get("YOUTUBE_CHANNEL_URL", "https://www.youtube.com/@RicardoVGodoy").rstrip("/")
CHANNEL_ID = os.environ.get("YOUTUBE_CHANNEL_ID", "UC1qeevKED2n7lqWOmtbZxYg")
PLAYLIST_IDS = [
    value.strip()
    for value in os.environ.get(
        "YOUTUBE_PLAYLIST_IDS", "PL6-MIz5lpF6KsSKMpXc7QyQd1qxA7VCd5"
    ).split(",")
    if value.strip()
]
OUT_PATH = Path(__file__).resolve().parents[1] / "_data" / "videos.yml"

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124 Safari/537.36"
)
VIDEO_ID_RE = re.compile(r"^[A-Za-z0-9_-]{11}$")
NS = {
    "atom": "http://www.w3.org/2005/Atom",
    "yt": "http://www.youtube.com/xml/schemas/2015",
}


def fetch_text(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Language": "en-US,en;q=0.9",
        },
    )
    with urlopen(request, timeout=30) as response:
        return response.read().decode("utf-8", errors="replace")


def parse_initial_data(page: str) -> Any:
    decoder = json.JSONDecoder()
    markers = (
        "var ytInitialData = ",
        "window[\"ytInitialData\"] = ",
        "ytInitialData = ",
    )
    for marker in markers:
        start = page.find(marker)
        if start == -1:
            continue
        start += len(marker)
        try:
            data, _ = decoder.raw_decode(page[start:])
            return data
        except json.JSONDecodeError:
            continue
    raise ValueError("Could not find YouTube initial page data")


def walk_dicts(value: Any) -> Iterator[dict[str, Any]]:
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_dicts(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_dicts(child)


def contains_key(value: Any, wanted: str) -> bool:
    return any(wanted in item for item in walk_dicts(value))


def text_value(value: Any) -> str:
    if not isinstance(value, dict):
        return ""
    if isinstance(value.get("simpleText"), str):
        return value["simpleText"].strip()
    if isinstance(value.get("content"), str):
        return value["content"].strip()
    runs = value.get("runs")
    if isinstance(runs, list):
        return "".join(
            run.get("text", "") for run in runs if isinstance(run, dict)
        ).strip()
    return ""


def relative_date(value: Any) -> str:
    texts: list[str] = []
    for item in walk_dicts(value):
        for key in ("content", "simpleText", "accessibilityLabel"):
            if isinstance(item.get(key), str):
                texts.append(item[key])

    now = datetime.now(timezone.utc)
    for original in texts:
        normalized = unicodedata.normalize("NFKD", original.casefold())
        normalized = "".join(
            char for char in normalized if not unicodedata.combining(char)
        )
        if normalized.strip() in {"today", "hoy", "hoje"}:
            return now.date().isoformat()

        match = re.search(
            r"(\d+)\s+(seconds?|minutes?|hours?|days?|weeks?|months?|years?)\s+ago",
            normalized,
        )
        if not match:
            match = re.search(
                r"(?:hace|ha)\s+(\d+)\s+"
                r"(segundos?|minutos?|horas?|dias?|semanas?|mes(?:es)?|anos?)",
                normalized,
            )
        if not match:
            continue

        amount = int(match.group(1))
        unit = match.group(2)
        if unit.startswith(("second", "segundo")):
            delta = timedelta(seconds=amount)
        elif unit.startswith(("minute", "minuto")):
            delta = timedelta(minutes=amount)
        elif unit.startswith(("hour", "hora")):
            delta = timedelta(hours=amount)
        elif unit.startswith(("day", "dia")):
            delta = timedelta(days=amount)
        elif unit.startswith(("week", "semana")):
            delta = timedelta(weeks=amount)
        elif unit.startswith(("month", "mes")):
            delta = timedelta(days=30 * amount)
        else:
            delta = timedelta(days=365 * amount)
        return (now - delta).date().isoformat()
    return ""


def extract_page_videos(data: Any, collaborations_only: bool = False) -> list[dict[str, str]]:
    videos: list[dict[str, str]] = []
    seen: set[str] = set()

    for node in walk_dicts(data):
        view = node.get("lockupViewModel")
        if not isinstance(view, dict):
            continue
        if view.get("contentType") != "LOCKUP_CONTENT_TYPE_VIDEO":
            continue
        if collaborations_only and not contains_key(view, "avatarStackViewModel"):
            continue

        video_id = view.get("contentId", "")
        if not isinstance(video_id, str) or not VIDEO_ID_RE.fullmatch(video_id):
            continue
        if video_id in seen:
            continue

        metadata = view.get("metadata", {}).get("lockupMetadataViewModel", {})
        title = text_value(metadata.get("title", {}))
        videos.append(
            {
                "youtube_id": video_id,
                "title": title,
                "date": relative_date(metadata),
            }
        )
        seen.add(video_id)

    if collaborations_only:
        return videos

    # Older YouTube layouts use renderer objects instead of lockupViewModel.
    for node in walk_dicts(data):
        for renderer_name in ("playlistVideoRenderer", "gridVideoRenderer"):
            renderer = node.get(renderer_name)
            if not isinstance(renderer, dict):
                continue
            video_id = renderer.get("videoId", "")
            if (
                not isinstance(video_id, str)
                or not VIDEO_ID_RE.fullmatch(video_id)
                or video_id in seen
            ):
                continue
            videos.append(
                {
                    "youtube_id": video_id,
                    "title": text_value(renderer.get("title", {})),
                    "date": relative_date(renderer),
                }
            )
            seen.add(video_id)

    return videos


def parse_upload_feed(xml_text: str) -> list[dict[str, str]]:
    root = ET.fromstring(xml_text)
    videos: list[dict[str, str]] = []
    for entry in root.findall("atom:entry", NS):
        video_id = entry.findtext("yt:videoId", default="", namespaces=NS).strip()
        title = entry.findtext("atom:title", default="", namespaces=NS).strip()
        published = entry.findtext("atom:published", default="", namespaces=NS).strip()
        if not VIDEO_ID_RE.fullmatch(video_id) or not title or not published:
            continue
        videos.append(
            {
                "youtube_id": video_id,
                "title": title,
                "date": published[:10],
            }
        )
    return videos


def meta_attributes(tag: str) -> dict[str, str]:
    attributes: dict[str, str] = {}
    for match in re.finditer(r"([:\w-]+)\s*=\s*([\"'])(.*?)\2", tag, re.DOTALL):
        attributes[match.group(1).lower()] = html.unescape(match.group(3)).strip()
    return attributes


def utc_date(value: str) -> str:
    if not value:
        return ""
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return value[:10] if re.fullmatch(r"\d{4}-\d{2}-\d{2}.*", value) else ""
    if parsed.tzinfo is None:
        return parsed.date().isoformat()
    return parsed.astimezone(timezone.utc).date().isoformat()


def parse_video_page(page: str) -> dict[str, str]:
    title = ""
    date = ""
    for tag in re.findall(r"<meta\b[^>]*>", page, flags=re.IGNORECASE):
        attributes = meta_attributes(tag)
        if not title and (
            attributes.get("name", "").lower() == "title"
            or attributes.get("property", "").lower() == "og:title"
        ):
            title = attributes.get("content", "")
        if not date and attributes.get("itemprop", "").lower() in {
            "datepublished",
            "uploaddate",
        }:
            date = utc_date(attributes.get("content", ""))

    if not date:
        match = re.search(r'"publishDate"\s*:\s*"(\d{4}-\d{2}-\d{2})', page)
        if match:
            date = match.group(1)

    return {"title": title, "date": date}


def hydrate_video(video: dict[str, str]) -> dict[str, str]:
    page = fetch_text(f"https://www.youtube.com/watch?v={video['youtube_id']}")
    metadata = parse_video_page(page)
    return {
        "youtube_id": video["youtube_id"],
        "title": metadata["title"] or video["title"],
        "date": metadata["date"] or video["date"],
    }


def read_existing_videos() -> list[dict[str, str]]:
    if not OUT_PATH.exists():
        return []

    videos: list[dict[str, str]] = []
    current: dict[str, str] = {}
    fields = {
        "- title: ": "title",
        "  youtube_id: ": "youtube_id",
        "  date: ": "date",
    }
    for line in OUT_PATH.read_text(encoding="utf-8").splitlines():
        if line.startswith("- title: ") and current:
            if current.get("youtube_id"):
                videos.append(current)
            current = {}
        for prefix, field in fields.items():
            if not line.startswith(prefix):
                continue
            raw_value = line[len(prefix) :]
            try:
                current[field] = str(json.loads(raw_value))
            except json.JSONDecodeError:
                current[field] = raw_value.strip().strip('"')
            break
    if current.get("youtube_id"):
        videos.append(current)
    return videos


def merge_videos(*groups: list[dict[str, str]]) -> list[dict[str, str]]:
    merged: dict[str, dict[str, str]] = {}
    for group in groups:
        for video in group:
            video_id = video["youtube_id"]
            current = merged.get(video_id)
            if current is None:
                merged[video_id] = video.copy()
                continue
            if not current.get("title") and video.get("title"):
                current["title"] = video["title"]
            if not current.get("date") and video.get("date"):
                current["date"] = video["date"]

    return sorted(
        merged.values(),
        key=lambda video: (video.get("date", ""), video.get("title", "")),
        reverse=True,
    )


def write_yaml(videos: list[dict[str, str]]) -> None:
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with OUT_PATH.open("w", encoding="utf-8") as output:
        for video in videos:
            video_id = video["youtube_id"]
            output.write(f"- title: {json.dumps(video['title'], ensure_ascii=False)}\n")
            output.write(f"  youtube_id: {json.dumps(video_id)}\n")
            output.write(f"  date: {json.dumps(video['date'])}\n")
            output.write(
                f'  thumbnail: "https://i.ytimg.com/vi/{video_id}/hqdefault.jpg"\n'
            )


def main() -> int:
    existing_by_id = {
        video["youtube_id"]: video for video in read_existing_videos()
    }

    upload_feed = fetch_text(
        f"https://www.youtube.com/feeds/videos.xml?channel_id={CHANNEL_ID}"
    )
    uploads = parse_upload_feed(upload_feed)
    if not uploads:
        raise RuntimeError("The YouTube uploads feed returned no videos")

    playlist_videos: list[dict[str, str]] = []
    for playlist_id in PLAYLIST_IDS:
        page = fetch_text(f"https://www.youtube.com/playlist?list={playlist_id}")
        videos = extract_page_videos(parse_initial_data(page))
        if not videos:
            raise RuntimeError(f"Playlist {playlist_id} returned no videos")
        try:
            playlist_feed = fetch_text(
                f"https://www.youtube.com/feeds/videos.xml?playlist_id={playlist_id}"
            )
            feed_videos = parse_upload_feed(playlist_feed)
        except Exception as error:
            print(f"Warning: playlist feed unavailable: {error}", file=sys.stderr)
            feed_videos = []
        playlist_videos.extend(merge_videos(videos, feed_videos))

    channel_page = fetch_text(CHANNEL_URL)
    collaborations = extract_page_videos(
        parse_initial_data(channel_page), collaborations_only=True
    )
    if not collaborations:
        raise RuntimeError("The YouTube Collaborations section returned no videos")

    candidates = merge_videos(uploads, playlist_videos, collaborations)
    complete: list[dict[str, str]] = []
    unresolved: list[dict[str, str]] = []
    for video in candidates:
        previous = existing_by_id.get(video["youtube_id"], {})
        if not video.get("title") and previous.get("title"):
            video["title"] = previous["title"]
        if previous.get("date"):
            video["date"] = previous["date"]
        if video.get("title") and video.get("date"):
            complete.append(video)
        else:
            unresolved.append(video)

    print(
        f"Resolved {len(complete)} videos from feeds, channel pages, or stored data; "
        f"{len(unresolved)} require watch-page metadata"
    )

    hydrated: list[dict[str, str]] = []
    with ThreadPoolExecutor(max_workers=4) as executor:
        pending = {
            executor.submit(hydrate_video, video): video["youtube_id"]
            for video in unresolved
        }
        for future in as_completed(pending):
            video_id = pending[future]
            try:
                hydrated.append(future.result())
            except Exception as error:
                print(
                    f"Warning: watch-page metadata unavailable for {video_id}: {error}",
                    file=sys.stderr,
                )

    incomplete = [
        video["youtube_id"]
        for video in hydrated
        if not video.get("title") or not video.get("date")
    ]
    if incomplete:
        print(
            "Warning: skipped videos without a title or publication date: "
            + ", ".join(incomplete),
            file=sys.stderr,
        )

    videos = merge_videos(
        complete,
        [
            video
            for video in hydrated
            if video.get("title") and video.get("date")
        ],
    )
    if not videos:
        raise RuntimeError("No complete video entries were available")
    write_yaml(videos)
    print(
        f"Wrote {len(videos)} videos to {OUT_PATH} "
        f"({len(uploads)} uploads, {len(playlist_videos)} playlist entries, "
        f"{len(collaborations)} collaborations before deduplication)"
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception as error:
        print(f"Video update failed: {error}", file=sys.stderr)
        sys.exit(1)
