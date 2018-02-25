# -*- coding: utf-8 -*-

from Questions.Question import Question
import os
import datetime

class Sleep(Question):

    def getAnswer(self):

        try:
            os.unlink("nosleep")
        except:
            pass

        now = datetime.datetime.now()
        if now.hour < 24 and now.hour > 5:
            return self.randomAnswer([
                "Rendben, este megyek aludni",
                "Megyek alszom, amint éjfélt üt az óra!",
                "Rendben, elalszom amint kell",
            ])

        return self.randomAnswer([
            "Szép álmokat!",
            "Jóéjt",
            "Megyek aludni",
            "Rendben, jóéjt",
        ])
