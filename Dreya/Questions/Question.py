# -*- coding: utf-8 -*-

import random

class Question:
    normalized = []
    original = ""
    sender = ""

    def __init__(self, sender, normalized, original):
        self.normalized = normalized
        self.original = original
        self.sender = sender

    def randomAnswer(self, answers):
        return random.choice(answers)