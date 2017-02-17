#!/bin/bash

if [ ! -f /Dreya/nosleep ]; then
    killall java
    ./suspend_until.sh 8:00
fi
