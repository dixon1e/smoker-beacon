#!/bin/bash
# Desc: Deploy the smoker-beacon system from a PCDuino
#       Copy all assets to their proper locations
#       Prepare all logging locations
#
# Set up logging and PID locations
mkdir -p -- "/var/log/smoker-beacon"
chown -R linaro:linaro /var/log/smoker-beacon

mkdir -p -- "/var/run/smoker-beacon"
chown -R linaro:linaro /var/run/smoker-beacon

mkdir -p -- "/home/linaro/logs"

# make sure to set up the root cron job using the 'crontab -e' command!
# then add this line at the end:
# @reboot su linaro -c "DISPLAY=:0.0 sh /home/linaro/smoker-beacon/startall.sh >/home/linaro/logs/cronlog 2>&1"
