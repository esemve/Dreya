# -*- coding: utf-8 -*-

from pyquery import PyQuery as pq
from Messenger.Messenger import Messenger

class Weather:

    last = ""

    def check(self):
        d = pq(url="http://www.met.hu/idojaras/veszelyjelzes/riasztas/index.php?kt=101")

        print(p.text)
        print("JEP");
        from Database import Database
        self.last = Database.get("weatherAlert","")

        try:
            p = d.find(".w-tbl td")
            msg = p.text()

            if self.last != msg:
                self.last = msg

                Database.set("weatherAlert",msg)

                if self.last!="":
                    Messenger.sendMessage(msg)

        except Exception as ex:
            pass

