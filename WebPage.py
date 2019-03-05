import requests

def encodeTitleUrl(title):
    symbol = "+"
    titleList = title.split(" ")
    return symbol.join(titleList)

class WebPage:
    def __init__(self, baseUrl, title):
        self.baseUrl = baseUrl
        self.title = encodeTitleUrl(title)
        self.page = 1
    def generate(self):
        url = self.baseUrl + "/?f=2&c=1_2&q=" + self.title + "&p=" + str(self.page)
        return requests.get(url)
    def next(self):
        self.page = self.page + 1