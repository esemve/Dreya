# -*- coding: utf-8 -*-

import xml.etree.ElementTree as ET
from Series.Series import Series
from Notifications.Event import Event as NotificationEvent
from Terminal import Terminal


class Config:

    cameraIp = ""
    cameraUserPass = ""
    messengerSenderGateway = ""
    ezRss = ""
    showsFolder = ""
    showsTorrentFolder = ""
    bkkFutarLine = ""
    bkkFutarStopId = ""


    series = []
    events = []
    bkkLines = []

    @staticmethod
    def init():
        Terminal.info("Config xml feldolgozas...")
        tree = ET.parse('config.xml')
        root = tree.getroot()
        Config.cameraIp = root.find("cameraIp").text
        Config.cameraUserPass = root.find("cameraUserPass").text
        Config.messengerSenderGateway = root.find("messengerSenderGateway").text
        Config.ezRss = root.find("ezRss").text
        Config.showsFolder = root.find("showsFolder").text
        Config.showsTorrentFolder = root.find("showsTorrentFolder").text
        Config.bkkFutarLine = root.find("bkkfutar").text
        Config.bkkFutarStopId = root.find("bkkfutar").get('stop')

        for bkkline in root.find("bkk").findall("line"):
            Config.bkkLines.append(bkkline.text)

        for fevent in root.find("events").findall("event"):
            month = int(fevent.get("month"))
            day = int(fevent.get("day"))
            event = fevent.text

            eventObject = NotificationEvent(month,day,event)
            Config.events.append(eventObject)

        for fseries in root.find("shows").findall("series"):
            name = fseries.find("name").text
            torrentTitle = fseries.find("torrentTitle").text
            subtitleText = fseries.find("subtitleText").text
            notIn = fseries.find("notIn").text

            seriesObject = Series(name, torrentTitle, subtitleText, notIn)
            Config.series.append(seriesObject)

        Terminal.info("Config betöltve!")

