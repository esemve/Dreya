import urllib
import requests


class Http:

    @staticmethod
    def download(url, path):
        headers = {'User-Agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0'}
        req = urllib.request.Request(url, None, headers)
        file = urllib.request.urlopen(req)
        with open(path, 'wb') as output:
            output.write(file.read())
        output.close()

    @staticmethod
    def get(url):
        headers = {'User-Agent': 'Mozilla/5.0 (Android 4.4; Mobile; rv:41.0) Gecko/41.0 Firefox/41.0'}
        req = urllib.request.Request(url, None, headers)
        return urllib.request.urlopen(req).read()

    @staticmethod
    def post(url, data):
        r = requests.post(url, data=data)
        return r.text