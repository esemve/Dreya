class Event:
    content = ""
    day = 1
    month = 1

    def __init__(self, month, day, content):
        self.content = content
        self.day = day
        self.month = month
