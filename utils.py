import isodate

def parse_duration(duration_str):
    if isinstance(duration_str, str) and ":" in duration_str:
        return duration_str
    try:
        duration = isodate.parse_duration(duration_str)
        total_minutes = duration.seconds // 60
        seconds = duration.seconds % 60
        return f"{total_minutes}:{seconds:02d}"
    except Exception:
        return "0:00"

def build_media_bar(duration_str):
    total_blocks = 20
    scrubber = "🔘"
    fill = "▬"

    try:
        minutes, seconds = map(int, duration_str.split(":"))
        total_seconds = minutes * 60 + seconds
    except:
        total_seconds = 0

    progress_ratio = 0.15
    scrubber_index = int(progress_ratio * total_blocks)

    bar = fill * scrubber_index + scrubber + fill * (total_blocks - scrubber_index - 1)

    scrubber_time = f"{(int(progress_ratio * total_seconds)) // 60}:{(int(progress_ratio * total_seconds)) % 60:02d}"
    return f"▶️ ⏸ ⏹ {bar}  {scrubber_time} / {duration_str} 🔊"