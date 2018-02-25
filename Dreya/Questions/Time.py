# -*- coding: utf-8 -*-

from Questions.Question import Question

import datetime

class Time(Question):

    def getAnswer(self):
        now = datetime.datetime.now()

        return self.randomAnswer([
            "A pontos idő "+str(now.hour)+" óra "+str(now.minute)+" perc",
            str(now.hour) + " óra " + str(now.minute) + " perc",
        ])
