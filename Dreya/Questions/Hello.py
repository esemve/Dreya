# -*- coding: utf-8 -*-

from Questions.Question import Question

class Hello(Question):

    def getAnswer(self):
        return self.randomAnswer([
            "Szia!",
            "Hello!",
        ])
