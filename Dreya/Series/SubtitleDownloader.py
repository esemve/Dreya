# -*- coding: utf-8 -*-


from pyquery import PyQuery as pq
import glob
from Series.MkvFile import MkvFile


class SubtitleDownloader:

    mkvFiles = []


    def check(self):

        self.mkvFiles = []
        self.loadFiles()

        d = pq(url="http://feliratok.info")
        #d = pq(filename="temp.html")
        p = d.find(".result")

        for row in d("table").find("tr"):
            if d(row).find("td").find("small").text()=="Magyar":
                link = d(row).find("a").eq(1).attr("href")
                content = d(row).find("td").text()
                for mkvFile in self.mkvFiles:
                    mkvFile.subtitle(content, link)

        for mkvFile in self.mkvFiles:
            mkvFile.downloadMaxScore()


#        for row in p:
#            rowEl = pq(row.html())
#            print rowEl.find(".lang")


    def loadFiles(self):
        from Config import Config
        for file in glob.glob(Config.showsFolder+"*.mkv"):
            mkvfile = MkvFile(file)
            if mkvfile.isSearcheable():
                self.mkvFiles.append(mkvfile)
