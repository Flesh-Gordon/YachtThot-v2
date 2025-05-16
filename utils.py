import isodate

def parse_duration(duration_iso):
    duration = isodate.parse_duration(duration_iso)
    total_minutes = duration.seconds // 60
    seconds = duration.seconds % 60
    return f"{total_minutes}:{seconds:02d}"

def build_media_bar(duration_str):
    return "▮▮▮▯▯▯▯▯▯▯"
