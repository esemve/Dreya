import datetime
from Messenger.Messenger import Messenger
from Terminal import Terminal

class EventNotificator:
    def __init__(self):
        try:
            from Config import Config
            now = datetime.datetime.now()
            today = int(now.strftime('%j'))

            for event in Config.events:
                eventDate = datetime.datetime(now.year, int(event.month), int(event.day), 0, 0, 0)

                eventDay = int(eventDate.strftime('%j'))

                if today == eventDay :
                    Messenger.sendMessage("", "Ma van "+event.content)
                    continue
                elif today+1 == eventDay:
                    Messenger.sendMessage("", "Holnap lesz " + event.content)
                    continue
                elif today + 2 == eventDay:
                    Messenger.sendMessage("", "Holnapután lesz " + event.content)
                    continue
                elif today + 7 == eventDay:
                    Messenger.sendMessage("", "Egy hét múlva lesz " + event.content)
                    continue
                elif today + 14 == eventDay:
                    Messenger.sendMessage("", "Két hét múlva lesz " + event.content)
                    continue
                elif today + 30 == eventDay:
                    Messenger.sendMessage("", "30 nap múlva lesz " + event.content)
                    continue
                elif today+1 == eventDay+365:
                    Messenger.sendMessage("", "Holnap lesz " + event.content)
                    continue
                elif today + 2 == eventDay+365:
                    Messenger.sendMessage("", "Holnapután lesz " + event.content)
                    continue
                elif today + 7 == eventDay+365:
                    Messenger.sendMessage("", "Egy hét múlva " + event.content)
                    continue
                elif today + 14 == eventDay+365:
                    Messenger.sendMessage("", "Két hét múlva lesz " + event.content)
                    continue
                elif today + 30 == eventDay+365:
                    Messenger.sendMessage("", "30 nap múlva lesz " + event.content)
                    continue

        except Exception as ex:
            Terminal.error("", "eventNotificator.error", ex)
