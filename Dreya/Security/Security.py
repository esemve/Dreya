from time import sleep
from time import time
import threading
import pygame
import random
import subprocess
import hashlib
import datetime

from Security.SerialReader import SerialReader
from Security.PhoneDetect import PhoneDetect
from Security.Camera import Camera
from Messenger.Messenger import Messenger

class Security:

    armed = False
    alert = False

    key1 = False
    key2 = False

    statusModify = 0
    camera = ""

    firstMotion = 0
    lastAlert = 0
    armedTime = 0
    lastMessageSent = 0


    def __init__(self):
        self.camera = Camera()

        self.key1 = PhoneDetect.key1
        self.key2 = PhoneDetect.key2

        if self.key1==False and self.key2==False:
            self.armed = True
            self.camera.open()
        else:
            self.camera.close()

        while True:
            timestamp = int(time())

            if PhoneDetect.key1!=self.key1:
                self.statusModify = timestamp
                self.key1 = PhoneDetect.key1

            if PhoneDetect.key2!=self.key2:
                self.statusModify = timestamp
                self.key2 = PhoneDetect.key2

            if self.statusModify == timestamp:
                if self.key1==False and self.key2==False:
                    self.armed = True
                    self.armedTime = timestamp
                    self.camera.open()
                else:
                    if self.armed:
                        if self.armedTime < timestamp - 600:
                            Messenger.sendMessage("", "Riasztó kikapcsolva")
                    self.armed = False
                    self.armedTime = 0
                    self.camera.close()

            if self.armed and SerialReader.motion:
                if self.armedTime == timestamp-600:
                    Messenger.sendMessage("","Riasztó aktív!")

                if self.armedTime < timestamp-600:
                    if self.lastAlert < timestamp-10:
                        self.lastAlert = timestamp
                        self.mp3(["mp3/alert.mp3"])

                        delta = datetime.datetime.now() + datetime.timedelta(0, 1)
                        img = "webc_" + delta.strftime("%Y-%m-%d_%H-%M-%S") + ".png"

                        md5text = "showDreyaImage" + img
                        md5 = hashlib.md5(md5text.encode()).hexdigest()

                        Messenger.sendMessage("", "Mozgás a lakásban! http://remote.host.com/watchtheimage.php?id=" + md5)

                    self.upload()

            sleep(1)

    def mp3(self, mp3s):
        mp3 = random.choice(mp3s)

#        pygame.init()
#        pygame.mixer.init()
#        pygame.mixer.music.load(mp3)
#        pygame.mixer.music.play()

    def upload(self):
        threading.Thread(target = upload).start()

def upload():
    bashCommand = "/Dreya/upload.sh"
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()