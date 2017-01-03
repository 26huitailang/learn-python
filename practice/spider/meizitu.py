#coding:utf-8
import requests
from bs4 import BeautifulSoup
import re

DownPath = "/pic"
import urllib
head = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'}
TimeOut = 100
PhotoName = 0
c = '.jpeg'
PWD="/pic"
for x in range(1, 4):
    site = "http://www.meizitu.com/a/5462.html"
    Page = requests.session().get(site, headers=head, timeout=TimeOut)
    Coding = (Page.encoding)
    Content = Page.content  # decode(Coding).encode('utf-8')
    ContentSoup = BeautifulSoup(Content, "lxml")
    jpg = ContentSoup.find_all('div', {'class':'postContent'})
    for photo in jpg:
        PhotoAdd = photo.get('data-original')
        PhotoName += 1
        Name = (str(PhotoName)+c)
        r = requests.get(PhotoAdd, stream=True)
        with open(PWD+Name, 'wb') as fd:
            for chunk in r.iter_content():
                fd.write(chunk)
print ("You have down %d photos" %PhotoName)