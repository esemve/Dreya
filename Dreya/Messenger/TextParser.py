# -*- coding: utf-8 -*-

from Messenger.Classify import Classify
from Questions.Hello import Hello
from Questions.Life import Life
from Questions.Sleep import Sleep
from Questions.NoSleep import NoSleep
from Questions.WhatsUp import WhatsUp
from Questions.Time import Time
from Questions.Joke import Joke
from Questions.Weather import Weather
from Questions.Cities import Cities
from Questions.Temp import Temp
from Questions.Load import Load
from Questions.Money import Money
from Questions.MoneyStatus import MoneyStatus
from Questions.Thx import Thx
from Questions.Notification import Notification
from Messenger.Normalizer import Normalizer

class TextParser:

    questionClasses = {
        Hello,
        Time,
        Life,
        WhatsUp,
        NoSleep,
        Sleep,
        Joke,
        Weather,
        Money,
        MoneyStatus,
        Cities,
        Temp,
        Load,
        Thx,
        Notification
    }

    originalMessage = ""
    sender = ""
    normalized = []
    answer = ""

    def __init__(self, sender, message):
        self.originalMessage = message
        self.sender = sender


        normalizer = Normalizer(message)
        self.normalized = normalizer.getNormalized()

        classify = Classify()
        ai_answer = classify.check(" ".join(self.normalized))

        for className in self.questionClasses:

            if className.__name__ == ai_answer:
                question = className( self.sender, self.normalized, self.originalMessage )

                #if question.hasAnswer() == True:
                self.answer = question.getAnswer()
                break

        if not self.answer:
            self.answer = "Sajnos nem tudok segíteni"

    def getAnswer(self):
        return self.answer