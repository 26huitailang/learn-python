# coding: utf-8
from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("http://www.pythonscraping.com")
bsObj = BeautifulSoup(html, 'lxml')
imageLocation = bsObj.find("a", {"id": "logo"}).find("img")["src"]
print(imageLocation)
urlretrieve(imageLocation, "logo.jpg")
