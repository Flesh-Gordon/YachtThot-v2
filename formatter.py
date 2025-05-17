import random

def format_reply(title, url, duration):
    # Convert duration from string format (e.g., "3:45") to seconds
    def parse_duration(duration_str):
        parts = duration_str.split(':')
        try:
            if len(parts) == 2:
                minutes, seconds = map(int, parts)
                return minutes * 60 + seconds
            elif len(parts) == 3:
                hours, minutes, seconds = map(int, parts)
                return hours * 3600 + minutes * 60 + seconds
        except ValueError:
            pass
        return 0  # fallback if malformed

    total_seconds = parse_duration(duration)
    if total_seconds <= 1:
        bar = "▶️ ⏸ ⏹ 🔘▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬ 0:01 / 0:01 🔊"
    else:
        # Random scrubber position
        current_seconds = random.randint(1, total_seconds - 1)
        filled = round((current_seconds / total_seconds) * 20)
        bar = f"▶️ ⏸ ⏹ {'▬' * (filled - 1)}🔘{'▬' * (20 - filled)} {format_time(current_seconds)} / {format_time(total_seconds)} 🔊"

    return f"""**NOW PLAYING:**

[{title}]({url})
{bar}"""

def format_time(seconds):
    minutes = seconds // 60
    remaining = seconds % 60
    return f"{minutes}:{remaining:02}"