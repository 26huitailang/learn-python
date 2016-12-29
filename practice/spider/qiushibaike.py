#!/usr/bin/python
# coding: utf-8

import urllib
import urllib2
import re

page = 1
url = 'http://www.qiushibaike.com/hot/page/' + str(page)
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
headers = {'User-Agent': user_agent}
try:
    request = urllib2.Request(url, headers = headers)
    response = urllib2.urlopen(request)
    content = response.read().decode("utf8")
    # 0 name, 1 content, 2 img, 3 votes
    pattern = re.compile('<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?content".*?<span>(.*?)</span>.*?</a>(.*?)<div class="stats".*?number">(.*?)</i>', re.S)
    items = re.findall(pattern, content)
    for item in items:
        havaImg = re.search('img', item[2])
        if not havaImg:
            print item[0]
            print item[1]
            print '\3' + item[3]
            print "-" * 10
except urllib2.URLError, e:
    if hasattr(e, "code"):
        print e.code
    if hasattr(e, "reason"):
        print e.reason

