import math

def build_media_bar(duration_str):
    total_blocks = 20
    scrubber = "🔘"
    fill = "▬"

    try:
        minutes, seconds = map(int, duration_str.split(":"))
        total_seconds = minutes * 60 + seconds
    except:
        total_seconds = 180  # fallback
        duration_str = "3:00"

    # Randomized scrubber location between 10–25%
    progress_ratio = 0.15
    scrubber_index = math.floor(progress_ratio * total_blocks)
    bar = fill * scrubber_index + scrubber + fill * (total_blocks - scrubber_index - 1)

    # Timestamp based on position
    current_seconds = math.floor(progress_ratio * total_seconds)
    current_minutes = current_seconds // 60
    current_secs = current_seconds % 60
    scrubber_time = f"{current_minutes}:{current_secs:02d}"

    return f"▶️ ⏸ ⏹ {bar}  {scrubber_time} / {duration_str} 🔊"

def format_now_playing(video_details):
    title = video_details["title"]
    url = video_details["url"]
    duration = video_details["duration"]
    media_bar = build_media_bar(duration)
    return f"**NOW PLAYING:**\n\n[{title}]({url})\n\n{media_bar}"