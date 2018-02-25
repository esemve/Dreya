# -*- coding: utf-8 -*-

from Terminal import Terminal

class Normalizer:

    normalized = []

    def __init__(self, text):

        try:
            text = text.lower()
            replaceArray = {"á": "a", "é": "e", "í": "i", "ó": "o", "ö": "o", "ő": "o", "ú": "u", "ü": "u",
                            "ű": "u", ":": " ", "-": " ", "!": " ", "?": " "}
            text = self.replace_all(text, replaceArray)

            validchars = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r",
                          "s", "t", "u", "v", "w", "x", "y", "z", " ", "0","1","2","3","4","5","6","7","8","9"]

            result = ""
            i = 0
            for c in text:
                i = i + 1

                if c in validchars:
                    if len(text) > i and (c != text[i] or c in ["0","1","2","3","4","5","6","7","8","9"]):
                        result = result + c
                    elif len(text) <= i:
                        result = result + c

            text = result

            normalized = text.split(" ")

            self.normalized = normalized

        except Exception as ex:
            Terminal.error("", "textParser.error", ex)

    def replace_all(self, text, dic):
        for i, j in dic.items():
            text = text.replace(i, j)
        return text

    def getNormalized(self):
        return self.normalized
