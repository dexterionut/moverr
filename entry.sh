#!/bin/sh

# start cron
crond -f -l 8 && tail -f /var/log/cron.log