# -*- coding: utf-8 -*-

from Questions.Question import Question

class WhatsUp(Question):

    def getAnswer(self):
        return self.randomAnswer([
            "Semmi különös",
            "Jól vagyok köszönöm",
            "Remekül vagyok, köszönöm kérdésed",
        ])
