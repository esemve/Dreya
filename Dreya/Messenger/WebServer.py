# -*- coding: utf-8 -*-

from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
import json
from TextParser import TextParser
from Terminal import Terminal

# This class will handles any incoming request from
# the browser
class myHandler(BaseHTTPRequestHandler):
    # Handler for the GET requests
    def do_GET(self):
        payload =  self.path.replace("/messenger/?payload=","")

        if payload!= self.path:
            try:
                payload = urllib.parse.unquote(payload)
                payload = json.loads(payload)

                if len(payload) > 0 and payload["message"] and payload["sender"]:

                    parser = TextParser(payload["sender"], payload["message"])
                    self.send_response(200)
                    self.send_header('Content-type', 'text/html')
                    self.end_headers()
                    self.wfile.write(parser.getAnswer().encode())
                return

            except Exception as ex:
                print("[EXCEPTION]", ex)
                raise(ex)
                self.sendError()
                return

        self.sendError()
        return

    def sendError(self):
        self.send_response(403)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write("Forbidden".encode())

class WebServer:

    def __init__(self):
        try:
            PORT_NUMBER = 12080
            # Create a web server and define the handler to manage the
            # incoming request
            server = HTTPServer(('', PORT_NUMBER), myHandler)
            Terminal.info("Webserver elindítva: " + str(PORT_NUMBER))
            # Wait forever for incoming htto requests
            server.serve_forever()
        except KeyboardInterrupt:
            Terminal.info("^C received, shutting down the web server")
            server.socket.close()
        except Exception as ex:
            Terminal.info("", "webserver.error", ex)
