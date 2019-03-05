from bs4 import BeautifulSoup

def createHtmlIterable(webPage):
    return BeautifulSoup(webPage.text, 'html.parser')

class Crawler:
    def __init__(self, webPage, baseUrl, encoder):
        self.baseUrl = baseUrl
        self.encoder = encoder
        self.webPage = createHtmlIterable(webPage)
    
    def generateDownloadLinks(self):
        animeList = self.webPage.find_all('tr', 'success')
        downloadLinks = []
        for anime in animeList:
            a_list = anime.find('td', attrs={"colspan": "2"}).find_all('a')
            animeTitle = a_list[len(a_list)-1].contents[0]
            if self.encoder in animeTitle:
                downloadUrl = self.baseUrl + anime.find('td', 'text-center').a['href']
                downloadLinks.append((animeTitle, downloadUrl))
        return downloadLinks