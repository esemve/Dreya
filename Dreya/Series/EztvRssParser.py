import xml.etree.ElementTree as ET
from Terminal import Terminal
import time
import urllib

class EztvRssParser:
    def check(self):

        headers = {'User-Agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0'}

        from Config import Config
        try:

            req = urllib.request.Request(Config.ezRss, None, headers)
            rssContent = urllib.request.urlopen(req).read()
            root = ET.fromstring(rssContent).find("channel")

            for item in reversed(root.findall("item")):

                print(item.find("title").text);
                for series in Config.series:
                    series.checkDownload(item.find("title").text, item.find("enclosure").get("url"))

        except Exception as ex:
            Terminal.error("RSS feldolgozasi hiba", "EztvRssParser.error",ex)
