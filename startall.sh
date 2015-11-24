#!/bin/bash
echo "Starting sensor.py..."
/home/linaro/scale/startsensor.sh 2>&1 >/home/linaro/logs/sensor.log &
echo "Starting dispatcher.py..."
/home/linaro/scale/startdispatcher.sh 2>&1 >/home/linaro/logs/dispatcher.log &
