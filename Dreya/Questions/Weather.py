# -*- coding: utf-8 -*-

from Questions.Question import Question
from pyquery import PyQuery as pq

class Weather(Question):

    days = []
    dayNames = []

    def getAnswer(self):

        self.getWeather()

        if "holnap utan" in self.normalized or "utan" in self.normalized or "holnaputan" in self.normalized:
            return "Holnapután "+self.days[2]
        if "holnap" in self.normalized:
            return "Holnap "+self.days[1]

        if "hetfo" in self.normalized or "hetfon" in self.normalized or "hetfore" in self.normalized:
            return "Hétfőn "+self.getByDayName("hétfő")

        if "ked" in self.normalized or "keden" in self.normalized or "kedre" in self.normalized:
            return "Kedden "+self.getByDayName("kedd")

        if "szerda" in self.normalized or "szerdan" in self.normalized or "szerdara" in self.normalized:
            return "Szerdán "+self.getByDayName("szerda")

        if "csutortok" in self.normalized or "csutortokon" in self.normalized or "csutortokre" in self.normalized:
            return "Csütörtökön "+self.getByDayName("csütörtök")

        if "pentek" in self.normalized or "penteken" in self.normalized or "pentekre" in self.normalized:
            return "Pénteken "+self.getByDayName("péntek")

        if "szombat" in self.normalized or "szombaton" in self.normalized or "szombatra" in self.normalized:
            return "Szombaton "+self.getByDayName("szombat")

        if "vasarnap" in self.normalized or "vasarnapon" in self.normalized or "vasarnapra" in self.normalized:
            return "Vasárnap "+self.getByDayName("vasárnap")


        return "Ma "+self.days[0]


    def getByDayName(self,dayName):
        i = 0
        for day in self.dayNames:
            if i>0:
                if day == dayName:
                    return self.days[i]

            i = i + 1

    def getWeather(self):
        d = pq(url="https://www.idokep.hu/elorejelzes/Budapest")

        dayArray = ["hétfő","kedd","szerda","csütörtök","péntek","szombat","vasárnap"]

        i = 0


        card = d('.huszonegy')

        for row in d(card).find(".oszlop"):

                i = i+1

                if i == 8:
                    return


                fulltext = d(row).text()
                fulltext = fulltext.replace('\n'," ").strip()
                test = fulltext.split(" ")

                for dayName in dayArray:
                    if fulltext.lower().find(dayName) >= 0:
                        day = dayName
                        break

                self.days.append(fulltext)
                self.dayNames.append(day)