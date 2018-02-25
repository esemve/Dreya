import serial
import time
import subprocess

class SerialReader:

    key1 = ""
    key2 = ""

    motion = False
    temp = ""

    @staticmethod
    def read():
        while (True):
            i = 0
            try:
                proc = subprocess.Popen(['bash','serialreader.sh'],stdout=subprocess.PIPE)
                while True:
                    line = proc.stdout.readline()
                    if line != '':
                        line = line.strip().decode("UTF-8")
                        if line.strip() == "nomotion":
                            SerialReader.motion = False
                        if line.strip() == "motion":
                            SerialReader.motion = True


            except Exception as ex:
                print('EXCEPTION', ex)
