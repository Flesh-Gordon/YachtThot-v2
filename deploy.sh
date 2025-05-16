#!/bin/bash
cd /home/thefleshgordon/YachtThot-v2
git pull origin main
systemctl restart yachtthot-bot.service
