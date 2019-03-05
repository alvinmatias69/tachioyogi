from WebPage import WebPage
from Crawler import Crawler
from Downloader import Downloader

def main(baseUrl, title, encoder, location, timeOut):
    webPage = WebPage(baseUrl, title)
    crawler = Crawler(webPage.generate(), baseUrl, encoder)
    downloader = Downloader(location, timeOut)
    downloader.download(crawler.generateDownloadLinks())

baseUrl = 'https://nyaa.si'
title = ''
encoder = ''
location = './Downloads/'
timeOut = 0.5
main(baseUrl, title, encoder, location, timeOut)