# -*- coding: utf-8 -*-

from Questions.Question import Question

import sqlite3
import time
import datetime

class MoneyStatus(Question):

    now = ""
    week = ""
    conenction = ""
    c = ""

    def getAnswer(self):

        try:
            self.connection = sqlite3.connect('database.db')
            self.c = self.connection.cursor()

            self.now = datetime.datetime.now()
            self.week = datetime.datetime.now().isocalendar()[1];

            if "honapban" in self.normalized or "honap" in self.normalized:
                answer = self.getMonth()
            if "ma" in self.normalized or "mai" in self.normalized:
                answer = self.getDay()
            elif "iden" in self.normalized or "evben" in self.normalized:
                answer = self.getYear()
            else:
                answer = self.getWeek()

            self.connection.close()

            return self.randomAnswer(answer)

        except Exception as ex:

            return "Valami hiba történt az adatbázis piszkálásakor :("

    def getMonth(self):
        self.c.execute('SELECT SUM(price) FROM main.money WHERE month = ? AND year = ?', (self.now.month,self.now.year))
        row = self.c.fetchone()

        if (row):
            money = str(row[0])
            return [
                "A hónapban összesen "+money+" Ft lett elköltve",
                "Összesen " + money + " Ft kiadás keletkezett a hónapban",
                "Ebben a hónapban " + money + " Ft kiadás keletkezett",
            ]

        return [
            "Sajnos nem tudok segíteni",
            "Nem tudom",
            "Nincsenek adataim a kérdés megválaszolására"
        ]

    def getDay(self):
        self.c.execute('SELECT SUM(price) FROM main.money WHERE month = ? AND year = ? AND day = ?', (self.now.month,self.now.year, self.now.day))
        row = self.c.fetchone()

        if (row):
            money = str(row[0])
            return [
                "Ma összesen "+money+" Ft lett elköltve",
                "Összesen " + money + " Ft kiadás keletkezett ma",
                "A mai nap " + money + " Ft kiadás keletkezett",
            ]

        return [
            "Sajnos nem tudok segíteni",
            "Nem tudom",
            "Nincsenek adataim a kérdés megválaszolására"
        ]


    def getYear(self):
        self.c.execute('SELECT SUM(price) FROM main.money WHERE year = ?', (self.now.year,))
        row = self.c.fetchone()

        if (row):
            money = str(row[0])
            return [
                "Idén " + money + " Ft lett elköltve",
                "Összesen " + money + " Ft kiadás keletkezett idén",
                "Ebben az évben " + money + " Ft kiadás keletkezett",
            ]

        return [
            "Sajnos nem tudok segíteni",
            "Nem tudom",
            "Nincsenek adataim a kérdés megválaszolására"
        ]

    def getWeek(self):
        self.c.execute('SELECT SUM(price) FROM main.money WHERE week=? AND year = ?', (self.week,self.now.year))
        row = self.c.fetchone()

        if (row):
            money = str(row[0])
            return [
                "A héten " + money + " Ft lett elköltve",
                "Elköltöttetek " + money + " Ft -ot a héten",
                "Ezen a héten " + money + " Ft kiadás keletkezett",
            ]

        return [
            "Sajnos nem tudok segíteni",
            "Nem tudom",
            "Nincsenek adataim a kérdés megválaszolására"
        ]


