from time import sleep
from time import time
import datetime
from wakeonlan import wol

from Security.PhoneDetect import PhoneDetect

class WakeOnLan:

    anyAtHome = False
    changedDate = 0

    def __init__(self):

        self.changedDate = int(time())

        if PhoneDetect.key1 == True or PhoneDetect.key2 == True:
            self.anyAtHome = True

        while True:
            timestamp = int(time())

            if PhoneDetect.key1 == True or PhoneDetect.key2 == True:
                if self.anyAtHome == False:
                    self.anyAtHome = True

                    if self.changedDate < timestamp-900:
                        wol.send_magic_packet('11.2B.34.88.C9.55', ip_address='xxx.xxx.xxx.xxx', port=9)
                        wol.send_magic_packet('11.2B.34.88.C9.55', ip_address='xxx.xxx.xxx.xxx', port=7)

                    self.changedDate = timestamp

            if PhoneDetect.key1 == False and PhoneDetect.key2 == False:
                if self.anyAtHome == True:
                    self.anyAtHome = False
                    self.changedDate = timestamp

            sleep(2)
