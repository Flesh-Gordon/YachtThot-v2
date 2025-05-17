# YachtThot Reddit Bot (Snark Engine Edition)

YachtThot is a Reddit bot that listens for comments requesting songs and replies with a YouTube link, Spotify/Last.fm genre metadata, and a snarky response.

---

## Features

- YouTube video search (via `youtube-search-python`)
- Spotify and Last.fm genre detection
- Genre-specific and fallback snark
- Song rating tracking via Firestore
- GitHub webhook-based deployment
- Systemd management with log rotation

---

## 1. Deployment (Manual)

### A. Clone and set up the repo

```bash
cd ~
git clone https://github.com/Flesh-Gordon/YachtThot-v2.git
cd YachtThot-v2
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt