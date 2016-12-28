#!/usr/bin/python
# coding: utf-8
import urllib
import re


def getHtml(url):
    # 获取html文本
    page = urllib.urlopen(url)
    html = page.read().decode("utf8")
    return html


def getImg(html):
    # 筛选html页面中需要的图片链接
    reg = r'src="(.+?\.jpg)" alt="(.+?)"'
    imgre = re.compile(reg)
    imglist = re.findall(imgre, html)
    # 下载
    x = 0
    for imgurl, imgname in imglist:
        urllib.urlretrieve(imgurl, 'c:\users\peter\desktop\\test\%s.jpg' % imgname)
        x += 1
    return imglist

html = getHtml("https://movie.douban.com/nowplaying/chengdu/")

print getImg(html)
