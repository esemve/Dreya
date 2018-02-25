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
from Questions.Weather import Weather

def wolThread():
    while True:
        time.sleep(10)
        WakeOnLan()
        time.sleep(randint(1, 5))

def phoneDetectThread():
    while True:
        phoneDetect = PhoneDetect()
        phoneDetect.check()
        time.sleep(randint(1, 5))


class Test:

    def __init__(self):

        Terminal.info("Test...")
        Database.init()
        Config.init()

        weather = Weather('a',['szerda'],"Milyen ido lesz hetfon")
        print(weather.getAnswer())



Test()
