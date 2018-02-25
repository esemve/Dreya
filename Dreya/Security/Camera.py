import urllib

class Camera:

    def open(self):
        self.speakWithCamera(0)
        pass

    def close(self):
        self.speakWithCamera(7)
        pass

    def speakWithCamera(self, position):
        from Config import Config
        request = urllib.request.Request("http://"+Config.cameraIp+":81/web/cgi-bin/hi3510/param.cgi?cmd=preset&-act=goto&-number="+str(position))
        request.add_header("Authorization", "Basic %s" % Config.cameraUserPass)
        result = urllib.request.urlopen(request)
        print(result)

