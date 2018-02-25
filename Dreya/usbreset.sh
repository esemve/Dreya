#!/bin/bash

set -euo pipefail
IFS=$'\n\t'

VENDOR="2341"
PRODUCT="0043"

for DIR in $(find /sys/bus/usb/devices/ -maxdepth 1 -type l); do
  if [[ -f $DIR/idVendor && -f $DIR/idProduct &&
        $(cat $DIR/idVendor) == $VENDOR && $(cat $DIR/idProduct) == $PRODUCT ]]; then
    echo 0 > $DIR/authorized
    echo $DIR/authorized
    sleep 0.5
    echo "USB RESET DONE"
    echo 1 > $DIR/authorized
    echo $DIR/authorized
  fi
done