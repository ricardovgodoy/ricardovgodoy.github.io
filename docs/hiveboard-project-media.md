# HiveBoard project preview

The homepage Research projects section and the Research page use the same
10-second preview: printing parts, an assembled board with a ball valve,
and the Macao hand operating the valve.

- Project: https://hiveboard-bench.github.io/
- Code and hardware: https://github.com/EESC-LabRoM/HiveBoard
- Files: `images/projects/hiveboard-print-to-use.mp4`, `.webm`, and `.webp`.

## Sources and edit

1. **Printing, 0–3 seconds.** Source: https://hiveboard-bench.github.io/assets/videos/video_1.mp4
   Source interval 6–126 seconds, played at 40×. Crop 960 × 540 at (240, 180)
   in the 1280 × 720 source, then resize to 800 × 450.
2. **Assembled board, 3–5 seconds.** Source: https://github.com/hiveboard-bench/hiveboard-bench.github.io/releases/download/v1.0-v1.0-videos/macao_torque_valve.mp4
   Source interval 20–22 seconds at original speed. Crop 800 × 450 at
   (220, 1120) in the 1080 × 1920 source. The board and installed valve are
   stationary during this interval.
3. **Manipulation, 5–10 seconds.** Same Macao source, interval 26.5–31.5 seconds
   at original speed. Crop 960 × 540 at (120, 1020), then resize to 800 × 450.

The printing and manipulation shots are separate recordings, not a continuous
trial. Straight cuts separate the three shots; footage is not reversed.
The poster is taken at 3.5 seconds in the edited video and shows the board
with the valve installed.

Both video formats are 800 × 450 at 24 fps, with audio and source metadata
removed. MP4 uses H.264, yuv420p, CRF 26, and fast-start metadata. WebM uses
VP9, yuv420p, CRF 34, and zero target bitrate. The still uses WebP quality 85.

## Validation

Both outputs decode completely. Duration, dimensions, frame rate, absence
of audio, and project media paths were checked. Frames across all three shots
were inspected to check the board and the hand remain visible within the crop.
The existing video elements provide autoplay, muted looping, MP4 fallback,
and reduced-motion handling on both pages.

The former `hiveboard-benchmark-board.*` assets remain available for existing
links but are no longer selected by the project data. Full source downloads
are not included in the website repository.
