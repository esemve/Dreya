import sys

sys.path.append('./Vendor/cssselect/')
sys.path.append('./Vendor/pyquery/')
sys.path.append('./Messenger/')
sys.path.append('./Questions/')
sys.path.append('./Notifications/')
sys.path.append('./Series/')
sys.path.append('./Security/')
sys.path.append('./Features/')

import time
import Series
import datetime
import threading
from subprocess import call
from Config import Config
from random import randint
from Terminal import Terminal
from Database import Database
from Notifications.Bkk import Bkk
from Messenger.WebServer import WebServer
from Notifications.Weather import Weather
from Security.SerialReader import SerialReader
from Notifications.EventNotificator import EventNotificator
from Notifications.Notification import Notification
from Security.Security import Security
from Security.PhoneDetect import PhoneDetect
from Features.WakeOnLan import WakeOnLan

def timer():
    while True:
        now = datetime.datetime.now()

        if now.hour == 10 and now.minute == 1 and now.second == 1:
            EventNotificator()

        time.sleep(1)

def ezRssParserThread():
    while True:
        #time.sleep(20)
        eztvRssReader = Series.EztvRssParser()
        eztvRssReader.check()
        time.sleep(randint(400, 600))

def subtitleDownloaderThread():
    while True:
        time.sleep(2)
        subtitleDownloader = Series.SubtitleDownloader()
        subtitleDownloader.check()
        time.sleep(randint(400, 600))

def wolThread():
    while True:
        time.sleep(10)
        WakeOnLan()
        time.sleep(randint(1, 5))

def bkkThread():
    while True:
        time.sleep(10)
        bkk = Bkk()
        bkk.check()
        time.sleep(randint(150, 350))

def webserverThread():
    WebServer()

def securityThread():
    while True:
        time.sleep(20)
        try:
            Security()
        except Exception as ex:
            print("[exception.security] ", ex)

def weatherThread():
    while True:
        time.sleep(100)
        weather = Weather()
        weather.check()
        time.sleep(randint(400, 600))

def serialReaderThread():
    while True:
        time.sleep(5)
        SerialReader.read()
        time.sleep(randint(5, 10))

def phoneDetectThread():
    while True:
        phoneDetect = PhoneDetect()
        phoneDetect.check()
        time.sleep(randint(1, 5))


def notificationThread():
    while True:
        time.sleep(30)

        try:
            noti = Notification()
            noti.check()
        except Exception as ex:
            pass

        time.sleep(30)

class Dreya:

    def __init__(self):

        call(["/Dreya/usbreset.sh"])


        Terminal.info("Dreya indul...")
        Database.init()
        Config.init()

        EztvRssParserThread = threading.Thread(target=ezRssParserThread)
        EztvRssParserThread.start()

        SubtitleDownloaderThread = threading.Thread(target=subtitleDownloaderThread)
        SubtitleDownloaderThread.start()

        BkkThread = threading.Thread(target=bkkThread)
        BkkThread.start()

        NotificationThread = threading.Thread(target=notificationThread)
        NotificationThread.start()

        WebServerThread = threading.Thread(target=webserverThread)
        WebServerThread.start()

        SerialReaderThread = threading.Thread(target=serialReaderThread)
        SerialReaderThread.start()

        PhoneDetectThread = threading.Thread(target=phoneDetectThread)
        PhoneDetectThread.start()

        SecurityThread = threading.Thread(target=securityThread)
        SecurityThread.start()

        WeatherThread = threading.Thread(target=weatherThread)
        WeatherThread.start()

        WolThread = threading.Thread(target=wolThread)
        WolThread.start()

        timerThread = threading.Thread(target=timer)
        timerThread.start()

Dreya()
