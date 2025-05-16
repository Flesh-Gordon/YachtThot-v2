#!/bin/bash
cd /home/thefleshgordon/YachtThot-v2
git fetch origin snark-engine
git checkout snark-engine
git reset --hard
git pull origin snark-engine --rebase
sudo systemctl restart yachtthot-bot.service