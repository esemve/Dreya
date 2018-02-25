# -*- coding: utf-8 -*-

from Questions.Question import Question
from Security.SerialReader import SerialReader

class Temp(Question):

    def getAnswer(self):
        temp = SerialReader.temp

        return self.randomAnswer([
            "Jelenleg itthon "+temp+" fok van",
            "Itthon "+temp+" °C a hőmérséklet",
            temp + " °C van itthon",
            "A benti hőmérséklet "+temp+" fok"
        ])
