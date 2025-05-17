import random

def format_reply(video_info, snark=None, dedication=None, snark_override=None):
    title = video_info.get("title", "Unknown Title")
    url = video_info.get("url", "")
    duration = video_info.get("duration", "0:00")

    # Calculate random timestamp and media bar
    try:
        total_seconds = sum(int(x) * 60 ** i for i, x in enumerate(reversed(duration.split(":"))))
        if total_seconds > 0:
            current_seconds = random.randint(1, total_seconds)
        else:
            current_seconds = 1
    except:
        total_seconds = 0
        current_seconds = 1

    def format_time(seconds):
        minutes = seconds // 60
        secs = seconds % 60
        return f"{minutes}:{secs:02d}"

    timestamp = format_time(current_seconds)
    duration_str = format_time(total_seconds)

    media_bar = f"▶️ ⏸ ⏹ 🔘{'▬' * 22} {timestamp} / {duration_str} 🔊"

    reply = f"**NOW PLAYING:**\n\n[{title}]({url})\n\n{media_bar}"

    # Dedication message
    if dedication:
        reply += f"\n\n**DEDICATED TO:** {dedication}"

    # Snark logic
    final_snark = snark_override if snark_override else snark
    if final_snark:
        reply += f"\n\n> {final_snark}"

    return reply