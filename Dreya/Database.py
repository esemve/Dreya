import shelve
import hashlib
import sqlite3

class Database:

    @staticmethod
    def init():
        pass

    @staticmethod
    def set(key, value):
        connection = sqlite3.connect('database.db')
        c = connection.cursor()
        key = hashlib.md5(key.encode('utf-8')).hexdigest()
        c.execute("DELETE FROM main.settings WHERE key=?",(key,))
        c.execute("INSERT INTO main.settings VALUES (?,?)",(key,value))
        connection.commit()
        connection.close()

    @staticmethod
    def get(key, default):
        connection = sqlite3.connect('database.db')
        key = hashlib.md5(key.encode('utf-8')).hexdigest()
        c = connection.cursor()
        c.execute('SELECT * FROM main.settings WHERE key=?', (key,))
        row = c.fetchone()
        connection.commit()
        connection.close()
        if (row):
            return row[1]
        return default


    @staticmethod
    def close():
        pass
