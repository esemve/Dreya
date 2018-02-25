# -*- coding: utf-8 -*-

import os.path
import re
from Messenger.Messenger import Messenger
from Http import Http
from Terminal import Terminal

class MkvFile:
    file = ""
    parts = ""
    series = ""
    maxurl = ""
    maxscore = 0
    serep = ""

    def __init__(self, file):
        self.file = file
        self.parts = self.normalizer(file)


    def normalizer(self, text):
        text = text.lower()
        text = text.replace("."," ")
        text = text.replace("-", " ")
        text = text.replace("]", " ")
        text = text.replace("[", " ")
        text = text.replace(")", " ")
        text = text.replace("(", " ")
        text = text.replace(":", " ")
        text = text.replace("!", " ")
        text = text.replace("_", " ")
        text = text.replace("/", " ")
        text = text.replace(",", " ")
        text = text.replace("  ", " ")
        text = text.replace("  ", " ")
        text = text.replace("  ", " ")

        return text

    def isSearcheable(self):
        from Config import Config

        for series in Config.series:
            if series.checkSubtitle(self.parts):
                if not os.path.isfile(self.file.replace(".mkv", ".srt")):
                    self.series = series
                    return True

        return False

    def downloadMaxScore(self):
        if self.maxscore > 0:
            try:
                Http.download("http://feliratok.info"+self.maxurl, self.file.replace(".mkv", ".srt"))
                Messenger.sendMessage("",self.series.name + self.serep + " magyar felirat letoltve!")
                Terminal.info(self.series.name + self.serep + " magyar felirat letoltve!", "info")
            except Exception as ex:
                print(ex)
                return 0

    def subtitle(self, text,  url):
        check = self.normalizer(text)

        try:
            output = re.search('s[0-9].e[0-9].', check, flags=re.IGNORECASE)
            if output:
                output = output.group(0)
                ep = output.split("e")
            else:
                output = re.search('[0-9]*x[0-9]*', check, flags=re.IGNORECASE)
                if output:
                    output = output.group(0)
                    ep = output.split("x")
                else:
                    return 0

            if len(ep) > 1:
                season = int(ep[0])
                origseason = str(int(ep[0]))
                episode = int(ep[1])

                if episode < 10:
                    episode = "0" + str(episode)

                episode = str(episode)

                if season < 10:
                    season = "0" + str(season)

                season = str(season)

                find1 = "s" + season + "e" + episode
                find2 = season + "x" + episode
                find3 = "s" + origseason + "e" + episode
                find4 = origseason + "x" + episode

                if find1 in self.parts or find2 in self.parts or find3 in self.parts or find4 in self.parts:
                    if self.series.checkSubtitle(check):
                        self.serep = find1.upper()
                        subtitleparts = check.split(" ")

                        score = 0
                        for part in subtitleparts:
                            if part in self.file:
                                score = score + 1

                        if score > self.maxscore:
                            self.maxscore = score
                            self.maxurl = url

        except Exception as ex:
            return 0
