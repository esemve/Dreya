#!/bin/sh
DEFAULTPASS="DEFAULTPASS"

FILENAME=$(ls -t /mnt/ramdisk/ | head -1)
FILENAME="/mnt/ramdisk/$FILENAME"

gpg --passphrase $DEFAULTPASS -c $FILENAME

FILENAME="$FILENAME.gpg"

sshpass -p "xxxxxxxxxxxx" scp -P 5510 $FILENAME ipcamuser@remote.host:/home/ipcam/images/
unlink $FILENAME