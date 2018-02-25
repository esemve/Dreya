# -*- coding: utf-8 -*-

from Questions.Question import Question

class Thx(Question):

    def getAnswer(self):
        return self.randomAnswer([
            "Szívesen :)",
            "<3",
            "Ezért vagyok :)",
            "Szóra sem érdemes",
        ])
