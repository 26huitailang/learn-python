#!/usr/bin/python
import re 
import urllib
def getHtml(url):
    page=urllib.urlopen(url)
    html=page.read()
    return html
def getjpg(html):
    r=r'src="(http://.*\.jpg)"'
    re_jpg=re.compile(r)
    jpgList=re.findall(re_jpg,html)
    filename=1
    for jpgurl in jpgList:
        urllib.urlretrieve(jpgurl,"%s.jpg" %filename)
        print  'file "%s.jpg" done' %filename
        filename+=1
url=raw_input("please input the source url:")
html=getHtml(url)
getjpg(html)