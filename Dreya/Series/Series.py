# -*- coding: utf-8 -*-

from Messenger.Messenger import Messenger
from Http import Http
from Terminal import Terminal
import re

class Series():

    season = 0
    episode = 0

    name = ""
    torrent = ""
    subtitle = ""
    notIn = ""

    cacheKey = ""

    def __init__(self, name, torrent, subtitle, notIn):
        self.name = name
        self.cacheKey = "series."+name

        if name:
            self.torrent = torrent.lower()
        if subtitle:
            self.subtitle = subtitle.lower()
        if notIn:
            self.notIn = notIn.lower()

        from Database import Database

        self.episode = int(Database.get(self.cacheKey+".episode", "0"))
        self.season = int(Database.get(self.cacheKey + ".season", "0"))


    def checkSubtitle(self, text):
        text = text.lower()
        if self.subtitle in text:
            return True

        return False


    def checkDownload(self, text, url):
        text = text.lower()

        from Config import Config
        from Database import Database


        if self.torrent in text and "720p" in text and ((self.notIn and self.notIn not in text) or self.notIn==""):

            output = re.search('s[0-9].e[0-9].', text, flags=re.IGNORECASE).group(0)
            ep = re.findall('[0-9].', output, flags=re.IGNORECASE)
            season = int(ep[0])
            episode = int(ep[1])


            if (season>self.season | (season==self.season & episode>self.episode)):

                filename = url.split("/")
                filename = filename[-1]

                try:
                    Http.download(url, Config.showsTorrentFolder+filename)

                    self.season = season
                    self.episode = episode


                    Database.set(self.cacheKey + ".episode", episode)
                    Database.set(self.cacheKey + ".season", season)

                    Messenger.sendMessage("", self.name + " S" + ep[0] + "E" + ep[1] + " torrent letöltve!")
                    Terminal.info(self.name + " S" + ep[0] + "E" + ep[1] + " torrent letöltve!", "info")

                except IOError as e:
                    Terminal.error("", "series.error", e)