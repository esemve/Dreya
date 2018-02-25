#!/bin/bash

if [ ! -f /Dreya/nosleep ]; then
    killall python3
    killall ffmpeg
    echo '3-1' > /sys/bus/usb/drivers/usb/unbind
    /Dreya/suspend_until.sh 8:00
fi

