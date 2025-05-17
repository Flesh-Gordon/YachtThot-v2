# YachtThot Bot

## Log Rotation Setup (Systemd + Logrotate)

To prevent log bloat, add the following configuration to:
```conf
/var/log/yachtthot-bot.log /var/log/yachtthot-bot.err {
    weekly
    rotate 4
    compress
    missingok
    notifempty
    create 644 thefleshgordon thefleshgordon
    sharedscripts
    postrotate
        systemctl kill -s SIGUSR1 yachtthot-bot.service >/dev/null 2>&1 || true
    endscript
}