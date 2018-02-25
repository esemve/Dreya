# -*- coding: utf-8 -*-

from Questions.Question import Question

import sqlite3
import time
import datetime

class Money(Question):

    hasMoney = False
    minus = False

    def getAnswer(self):

        if "kerestem" in self.normalized or "bevetel" in self.normalized or "talaltam" in self.normalized or "kaptam" in self.normalized or "kerestunk" in self.normalized:
            self.minus = True

        for word in self.normalized:
            if word.isdigit():
                if int(word) > 50:
                    self.save(word)


        if self.hasMoney:
            if self.minus:
                return self.randomAnswer([
                    "Ez mindig jó hír :)",
                    "Remek! :)",
                    "Ez jó hír",
                    "Köszönöm, hogy szóltál, felírtam",
                    "Felírva, megjegyezve! :)",
                    "Jee! Felírtam",
                    "Grat! Elmentettem",
                    "Done! :)"
                ])
            return self.randomAnswer([
                "Felírtam",
                "Rendben, megjegyeztem",
                "Köszi, hogy szóltál",
                "Köszönöm, hogy jelezted",
                "Köszönöm, hogy szóltál, felírtam",
                "Felírva, megjegyezve!",
                "Ok",
                "Köszi, elmentettem",
                "Done!"
            ])

            return self.randomAnswer([
                "Sajnos nem értettem, hogy mennyi pénzről van szó",
                "Mennyit?",
                "Nem értettem az összeget"
            ])


    def save(self, money):
        self.hasMoney = True

        if self.minus:
            money = 0-int(money)

        connection = sqlite3.connect('database.db')
        c = connection.cursor()

        key = int(time.time())
        now = datetime.datetime.now()
        week = datetime.datetime.now().isocalendar()[1]

        c.execute("INSERT INTO main.money VALUES (?,?,?,?,?,?,?,?)",(key, self.sender,money, now.year, now.month, now.day, week, self.original))
        connection.commit()
        connection.close()

