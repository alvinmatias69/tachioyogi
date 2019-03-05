# Tachioyogi
A simple nyaa torrent batch downloader written in python

## Usage

How to use this software

### Requirements

Please make sure your system has the followings
- [python 3](https://www.python.org/)
- [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)

### Configurations

Open `index.py` and find the followings.

```python
baseUrl = 'https://nyaa.si' # Nyaa base url, change this with nyaa latest url 
title = ''                  # Anime title
encoder = ''                # Encoder of the anime
location = './Downloads/'    # Download locations
timeOut = 0.5               # Interval between each torrent download
```

Modify those based on your needs.

### Batch Download

Run `index.py` using python 3

```sh
$ python3 index.py
```

## TODO
* [ ] Implement resolution selection
* [ ] Implement crawl on multiple page

---
**Matias Alvin 2019**
