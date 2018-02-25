# -*- coding: utf-8 -*-

from Questions.Question import Question

import time
import datetime
import calendar
import sqlite3

class Notification(Question):

    def getAnswer(self):
        try:

            detectText = []

            for word in self.normalized:
                if word!="hogy" and word!="h":
                    detectText.append(word)
                else:
                    break

            hour = 9
            min = 0
            settedTime = False
            numbers = ("1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","01","02","03","04","05","06","07","08","09")
            date = datetime.date.today()

            if "holnap" in detectText:
                date = datetime.date.today() + datetime.timedelta(days=1)
            elif "holnaputan" in detectText:
                date = datetime.date.today() + datetime.timedelta(days=2)
            elif "hetfon" in detectText:
                date = self.getNextDay(0)
            elif "keden" in detectText or "ked" in detectText:
                date = self.getNextDay(1)
            elif "szerdan" in detectText or "szerda" in detectText:
                date = self.getNextDay(2)
            elif "csutortokon" in detectText or "csutortok" in detectText:
                date = self.getNextDay(3)
            elif "penteken" in detectText or "pentek" in detectText :
                date = self.getNextDay(4)
            elif "szombaton" in detectText or "szombat" in detectText:
                date = self.getNextDay(5)
            elif "vasarnap" in detectText or "vasarnap" in detectText:
                date = self.getNextDay(6)

            if "delben" in detectText:
                hour = 12
            elif "delelott" in detectText:
                hour = 10
            elif "reggel" in detectText:
                hour = 8
            elif "delutan" in detectText:
                hour = 16
            elif "este" in detectText:
                hour = 18
            elif "ejszaka" in detectText:
                hour = 21

            i = 0
            for word in detectText:
                check = i+1
                if int(len(detectText)) > int(check):

                    checkNext = detectText[i + 1].replace("kor", "")

                    if checkNext.isdigit() == False:
                        i += 1
                        continue

                    if word == "fel" and checkNext in numbers:

                        hour = int(checkNext)-1
                        if hour<8:
                            hour += 12
                        min = 30
                        settedTime = True
                        break

                    if word == "negyed" and checkNext in numbers:
                        hour = int(checkNext)-1
                        if hour<8:
                            hour += 12
                        min = 15
                        settedTime = True
                        break

                    if word == "haromnegyed" and checkNext in numbers:
                        hour = int(checkNext)-1
                        if hour<8:
                            hour += 12
                        min = 45
                        settedTime = True
                        break
                i += 1


            if settedTime == False:
                i = 0
                for word in detectText:
                    word = word.replace("kor", "")
                    if word.isdigit():
                        if word in numbers:
                            hour = word
                            detectText[i] = ""
                            break
                    i += 1

                i = 0
                for word in detectText:
                    word = word.replace("kor","")
                    if word.isdigit():
                        if word in numbers:
                            min = word
                            detectText[i] = ""
                            break
                    i += 1

            theDate = datetime.datetime(int(date.year),int(date.month),int(date.day), int(hour), int(min))
            current = int(calendar.timegm(datetime.datetime.utcnow().utctimetuple()))
            timestamp = int(calendar.timegm(theDate.utctimetuple()))

            if current > timestamp:
                return self.randomAnswer([
                    "Valamit félreérthettem szerintem, a múlba nem tudok emlékeztetőt állítani",
                    "Ajjaj, kérlek fogalmazd át a kérdésed, mert a múltba nem tudok emlékeztetőt állítani"
                ])

            self.save(timestamp)

            return self.randomAnswer([
                "Állítottam egy emlékeztetőt ekkorra: "+theDate.strftime("%Y-%m-%d %H:%M"),
                "Emlékeztető beállítva: "+theDate.strftime("%Y-%m-%d %H:%M"),
                "Szólni fogok ekkor: "+theDate.strftime("%Y-%m-%d %H:%M")
            ])

        except Exception as ex:
            return "Valami nagy galiba történt, átfogalmaznád a kérdést?"

    def getNextDay(self, dayNumber):
        dt = datetime.date.today()
        return dt + datetime.timedelta(days=(7 - dt.weekday() + dayNumber))

    def save(self, when):
        connection = sqlite3.connect('database.db')
        c = connection.cursor()

        c.execute("INSERT INTO main.notifications VALUES (?,?,?)",(self.sender, when, self.original))
        connection.commit()
        connection.close()
