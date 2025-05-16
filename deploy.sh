#!/bin/bash
cd /home/thefleshgordon/reddit_bot
git pull origin main
systemctl restart yachtthot-bot.service
