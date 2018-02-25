# -*- coding: utf-8 -*-

from Questions.Question import Question
from pyquery import PyQuery as pq

class Joke(Question):

    def getAnswer(self):

        try:
            d = pq(url="http://vicc.eu/index.php?veletlen")
            p = d.find(".vicc:first")

            return p.text()
        except Exception:
            return "Sajnos most nem tudok egy jó viccet sem."

