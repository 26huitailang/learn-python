#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nntplib import NNTP
from time import strftime, time, localtime
from email import message_from_string
from urllib import urlopen
import textwrap
import re

day = 24 * 60 * 60 # number of seconds in one day


def wrap(string, max=70):
    """
    将字符串调整为最大行宽。
    """
    return '\n'.join(textwrap.wrap(string)) + '\n'


class NewsAgent:
    """
    从新闻来源获取新闻项目并发布到新闻目标的对象
    """
    def __init__(self):
        self.sources = []
        self.destinations = []

    def addSource(self, source):
        self.sources.append(source)

    def addDestination(self, dest):
        self.destinations.append(dest)

    def distribute(self):
        """
        从所有来源获取所有新闻项目并发布到所有目标
        """
        items = []
        for source in self.sources:
            items.extend(source.getItems())
        for dest in self.destinations:
            dest.receiveItems(items)


class NewsItem:
    """
    包括标题和主体文本的简单新闻项目。
    """
    def __init__(self, title, body):
        self.title = title
        self.body = body


class NNTPSource:
    """
    从NNTP组中获取新闻项目的新闻来源
    """
    def __init__(self, servername, group, window):
        self.servername = servername
        self.group = group
        self.window = window

    def getItems(self):
        start = localtime(time() - self.window*day)  # window=1,表示一天前
        date = strftime('%y%m%d', start)
        hour = strftime('%H%M%S', start)

        server = NNTP(self.servername)

        ids = server.newnews(self.group, date, hour)[1]
        # print ids

        for id in ids:
            lines = server.article(id)[3]
            message = message_from_string('\n'.join(lines))

            title = message['subject']
            body = message.get_payload()
            if message.is_multipart():
                body = body[0]

            yield NewsItem(title, body)

        server.quit()


class SimpleWebSource:
    """
    使用正则表达式从网页中提取新闻项目的新闻来源
    """
    def __init__(self, url, titlePattern, bodyPattern):
        self.url = url
        self.titlePattern = re.compile(titlePattern)
        self.bodyPattern = re.compile(bodyPattern)

    def getItems(self):
        text = urlopen(self.url).read()
        titles = self.titlePattern.findall(text)
        bodies = self.bodyPattern.findall(text)
        for title, body in zip(titles, bodies):
            yield NewsItem(title, wrap(body))


class PlainDestination:
    """
    将所有新闻项目格式化为纯文本的新闻目标类
    """
    def receiveItems(self, items):
        for item in items:
            print item.title
            print '-'*len(item.title)
            print item.body


class HTMLDestination:
    """
    将所有新闻项目格式化为HTML的目标类。
    """
    def __init__(self, filename):
        self.filename = filename

    def receiveItems(self, items):
        out = open(self.filename, 'w')
        print >> out, """
        <html>
            <head>
                <title>Today's News</title>
            </head>
            <body>
            <h1>Today's News</h1>
        """

        print >> out, '<ul>'
        id = 0
        for item in items:
            id += 1
            print >> out, '    <li><a href="#%i">%s</a></li>' % (id, item.title)
        print >> out, '</ul>'

        id = 0
        for item in items:
            id += 1
            print >> out, '<h2><a name="%i">%s</a></h2>' % (id, item.title)
            print >> out, '<pre>%s</pre>' % item.body

        print >> out, """
            </body>
        </html>
        """


def runDefaultSetup():
    """
    来源和目标的默认位置。可以自己修改。
    """
    agent = NewsAgent()

    # 从BBC新闻站获取新闻的SimpleWebSource:
    # bbc_url = 'http://news.bbc.co.uk/text_only.stm'  # wiki，15年BBC取消了text only页面，改用响应式页面
    # bbc_title = r'(?s)a href="[^"]*">\s*<b>\s*(.*?)\s*</b>'
    # bbc_body = r'(?s)</a>\s*<br />\s*(.*?)\s*<'
    # bbc = SimpleWebSource(bbc_url, bbc_title, bbc_body)
    #
    # agent.addSource(bbc)

    # 从comp.lang.python.announce获取新闻的NNTPSource
    clpa_server = 'news2.neva.ru'  # Insert real server name
    clpa_group = 'comp.lang.python.announce'
    clpa_window = 8  # 可能当天没有新闻
    clpa = NNTPSource(clpa_server, clpa_group, clpa_window)

    agent.addSource(clpa)

    # 增加纯文本目标和HTML目标：
    agent.addDestination(PlainDestination())
    agent.addDestination(HTMLDestination('news.html'))

    # 发布新闻项目：
    agent.distribute()

if __name__ == '__main__':
    runDefaultSetup()