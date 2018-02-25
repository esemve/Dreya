import os

from time import time
from time import sleep

import subprocess


class PhoneDetect:

    key1 = False
    key2 = False

    tmpKey1 = False
    tmpKey2 = False

    ip1 = b"192.168.0.xxx"
    ip2 = b"192.168.0.xxx"

    checktime = 0

    def check(self):

        while True:

            timestamp = int(time())
            if (timestamp > self.checktime):

                self.tmpKey1 = False
                self.tmpKey2 = False

                self.checkArp()
                self.checkArp()
                self.checkArp()

                PhoneDetect.key1 = self.tmpKey1
                PhoneDetect.key2 = self.tmpKey2

                if PhoneDetect.key1 == True or PhoneDetect.key2 == True:
                    self.checktime = timestamp + 300

            sleep(3)


    def checkArp(self):
        p = subprocess.Popen("arp-scan --localnet", stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()
        p_status = p.wait()

        if output.find(self.ip1)>0:
            self.tmpKey1 = True

        if output.find(self.ip2)>0:
            self.tmpKey2 = True