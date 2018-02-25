# -*- coding: utf-8 -*-

from Questions.Question import Question
import os

class Load(Question):

    def getAnswer(self):

        load = os.getloadavg()

        return self.randomAnswer([
            str(load[0])+" / "+str(load[1])+" / "+str(load[2]),
            "Aktuális: "+str(load[0])+" / átlag: "+str(load[1])+" / "+str(load[2])
        ])
