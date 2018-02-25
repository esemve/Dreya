#!/bin/bash

result=`ps aux | grep -i "11:USER:" | grep -v "grep" | wc -l`

if [ $result -ge 1 ]
   then
	find /mnt/ramdisk -maxdepth 1 -mmin +20 -type f -delete
   else
        echo "Starting ffmpeg..."
	ffmpeg -i rtmp://XXX.XXX.XXX.XXX:1935/flash/11:USER:PASSWORD  -vf fps=1 -strftime 1 "/mnt/ramdisk/webc_%Y-%m-%d_%H-%M-%S.png"
fi

