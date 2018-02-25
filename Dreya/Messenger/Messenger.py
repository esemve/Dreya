# -*- coding: utf-8 -*-

from Http import Http
import urllib

class Messenger:


    def sendMessage(recipient = "", content = ""):

        if content:
            import json
            from Config import Config
            json = urllib.parse.quote(str(json.dumps({"recipient": recipient, "message": content})))
            payload = {"payload": json}
            Http.post(Config.messengerSenderGateway, payload)
