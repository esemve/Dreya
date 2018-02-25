# -*- coding: utf-8 -*-

from Questions.Question import Question

class NoSleep(Question):

    def getAnswer(self):

        try:
            open("nosleep", 'w').close()
        except:
            pass

        return self.randomAnswer([
            "Rendben, nem megyek aludni amíg nem szólsz",
            "Ébren maradok",
            "Nem alszok, amíg ti sem",
            "Szólj, ha mehetek aludni!",
        ])
