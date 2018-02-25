# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq
from Messenger.Messenger import Messenger

class Bkk:

    def check(self):
        try:
            d = pq(url="https://twitter.com/bkkbudapest")

            for tweet in reversed(d("#timeline").find(".tweet")):
                timestamp = d(tweet).find("._timestamp").attr("data-time")
                text = d(tweet).find(".tweet-text").text()

                from Database import Database
                from Config import Config

                lastSent = int(Database.get("bkkLastAlert", "0"))
                timestamp = int(timestamp)

                if (timestamp > lastSent):
                    for line in Config.bkkLines:
                        if line in text:
                            Database.set("bkkLastAlert", str(timestamp))
                            Messenger.sendMessage("", "Bkk Info - " + text)
                            break

        except Exception as ex:
            print("[bkk.error] ", ex)