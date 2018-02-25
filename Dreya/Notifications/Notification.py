import sqlite3

import datetime
import calendar
from Messenger.Messenger import Messenger

class Notification:

    def check(self):

        current = int(calendar.timegm(datetime.datetime.utcnow().utctimetuple()))
        current = current+30

        connection = sqlite3.connect('database.db')

        c = connection.cursor()
        c.execute('SELECT * FROM main.notifications WHERE thetime<?', (current,))
        row = c.fetchall()

        c.execute("DELETE FROM main.notifications WHERE thetime<?",(current,))
        connection.commit()
        connection.close()

        if row:
            for arow in row:
                Messenger.sendMessage(arow[0],"Megkértél rá: "+arow[2])
