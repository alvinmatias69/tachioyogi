from Presenter import Presenter
import urllib.request
import time

class Downloader:
    def __init__(self, location, timeOut):
        self.location = location
        self.timeOut = timeOut
    def download(self, links):
        presenter = Presenter(len(links))
        for index in range(len(links)):
            title, link = links[index][0], links[index][1]
            urllib.request.urlretrieve(link, self.location + title + '.torrent')
            presenter.present()
            time.sleep(self.timeOut)
        print("Download has been finish successfully")