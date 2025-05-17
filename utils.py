import isodate
import math

def parse_duration(duration_iso):
    duration = isodate.parse_duration(duration_iso)
    total_minutes = duration.seconds // 60
    seconds = duration.seconds % 60
    return f"{total_minutes}:{seconds:02d}"

def build_media_bar(duration_str):
    total_blocks = 20
    scrubber = "🔘"
    fill = "▬"

    # Parse "3:32" format to seconds
    minutes, seconds = map(int, duration_str.split(":"))
    total_seconds = minutes * 60 + seconds

    # Set scrubber at ~15% (or pick random position between 10–25%)
    progress_ratio = 0.15
    scrubber_index = math.floor(progress_ratio * total_blocks)

    bar = fill * scrubber_index + scrubber + fill * (total_blocks - scrubber_index - 1)

    # Calculate matching timestamp
    scrubber_seconds = math.floor(progress_ratio * total_seconds)
    scrubber_minutes = scrubber_seconds // 60
    scrubber_secs = scrubber_seconds % 60
    scrubber_time = f"{scrubber_minutes}:{scrubber_secs:02d}"

    return f"▶️ ⏸ ⏹ {bar}  {scrubber_time} / {duration_str} 🔊"