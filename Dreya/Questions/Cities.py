# -*- coding: utf-8 -*-

from Questions.Question import Question
from pyquery import PyQuery as pq
from Messenger.Normalizer import Normalizer

class Cities(Question):


    def getAnswer(self):

        city = self.checkHungarianCities()
        if city != "":
            return city
        city = self.checkUSACities()
        if city != "":
            return city


        return self.randomAnswer([
            "Sajnos nem tudom melyik városra gondolsz",
            "Kérlek fogalmazd újra a kérdésed",
            "Sajnos nem tudom melyik városra vagy kíváncsi"
        ])

    def checkHungarianCities(self):
        d = pq(url="https://hu.wikipedia.org/wiki/Magyarorsz%C3%A1g_v%C3%A1rosai")

        for table in d(".wikitable"):
            for trs in d(table).find("tr"):
                i = 0

                thisCity = ""
                live = ""
                size = ""
                megye = ""

                for td in d(trs).find("td"):
                    i += 1
                    content = d(td).text()

                    if i == 1:
                        normalizer = Normalizer(content)
                        city = normalizer.getNormalized()
                        city = city[0]

                        for text in self.normalized:
                            if city == text or city+"on" == text or city+"con" == text or city+"i" == text or city+"ban" == text or city+"et" == text or city+"n" == text or city+"en" == text or city+"nak" == text or city+"nek" == text or city+"nok" == text or city+"ek" == text:
                                thisCity = content

                        if thisCity == "":
                            break

                    elif i == 7:
                        size = content
                    elif i == 6:
                        live = content
                    elif i == 3:
                        megye = content

                if thisCity != "":
                    return self.randomAnswer([
                        thisCity+" "+megye+" megyei város "+live+" lakossal "+size+" km2 területtel",
                        "A "+megye+" megyében található "+thisCity + " város " + live + " lakossal " + size + " km2 területtel rendelkezik",
                    ])

        return ""

    def checkUSACities(self):
        d = pq(url="https://hu.wikipedia.org/wiki/Az_Amerikai_Egyes%C3%BClt_%C3%81llamok_v%C3%A1rosainak_list%C3%A1ja_n%C3%A9pess%C3%A9g_szerint")

        for table in d(".wikitable"):
            for trs in d(table).find("tr"):
                i = 0

                thisCity = ""
                live = ""
                size = ""
                megye = ""

                for td in d(trs).find("td"):
                    i += 1
                    content = d(td).text()

                    if i == 2:
                        normalizer = Normalizer(content)
                        city = normalizer.getNormalized()

                        city = " ".join(city).split("[")
                        city = city[0]

                        if city in " ".join(self.normalized):
                            thisCity = content.split("[")[0]

                    elif i == 7:
                        size = content
                        size = size.split("mi")
                        size = size[1]
                    elif i == 4:
                        live = content
                        live = live.split(" ")
                        del live[0]
                        live = ".".join(live)
                    elif i == 3:
                        state = content

                if thisCity != "":
                    return self.randomAnswer([
                        thisCity+" az USA "+state+" államban találhtó városa "+live+" lakossal "+size+" területen",
                        thisCity + " az USA egy városa " + state + " államban. Lakosainak száma " + live + ", területe " + size,
                        "Az USA -ban " + state + " államban található "+ thisCity + " " + live + " lakossal és " + size+" területtel rendelkezik",
                    ])

        return ""