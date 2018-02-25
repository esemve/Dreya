# -*- coding: utf-8 -*-

from Questions.Question import Question

class Life(Question):

    def getAnswer(self):
        return self.randomAnswer([
            "42",
            "Természetesen 42",
            "A válasz: 42",
        ])
