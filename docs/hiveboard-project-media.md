# HiveBoard project preview

HiveBoard is featured as the fourth selected project on the homepage and as a research project under **Manipulation benchmarks**. The existing three homepage projects are retained. No publication entry or placeholder paper link is added.

- Project page: https://hiveboard-bench.github.io/
- Code and hardware assets: https://github.com/EESC-LabRoM/HiveBoard
- Description: A modular, 3D-printed benchmark board for evaluating robot grippers, hands, and prostheses on industrial mechanisms, with reusable simulation assets.
- The project page reports 13 interchangeable attachments, four manipulation platforms, and articulated URDF/USD simulation models.

## Genuine preview footage

- Source: [Spot operating the large gate valve, linked by the HiveBoard project page](https://github.com/hiveboard-bench/hiveboard-bench.github.io/releases/download/v1.0-v1.0-videos/spot_big_valve.mp4).
- Selected interval: 38.5–44.5 seconds; six seconds of physical gate-valve manipulation, selected after inspecting the full clip and the candidate interval.
- Poster: source frame at 41.5 seconds.
- Outputs: `images/projects/hiveboard-benchmark-board.webm`, `.mp4`, and `.webp`.
- Original 1280 × 720 framing retained without cropping or stretching. Audio and ancillary metadata streams removed. WebM uses VP9; MP4 uses H.264 with yuv420p and fast-start metadata.
- The natural loop has a small wrist-position reset at its seam; footage is not reversed or altered to imply an unrecorded result.

The full downloaded video remains outside the website repository.

## Validation

- Complete Jekyll build passed with only the existing legacy/Sass warnings.
- YAML and all three new media paths validated; both videos decode fully and have no audio streams.
- Desktop (1440 × 1000) and mobile (390 × 844) checks passed for both pages: WebM playback, MP4 fallback, poster loading, original aspect ratio, source links, wording, and no horizontal overflow.
- The homepage retains the original three projects and adds HiveBoard fourth. Research now contains six projects. Both pages have eight looping previews overall.
- Publication records, workflows, navigation, and the YouTube updater are unchanged.
