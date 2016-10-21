#!/usr/bin/env python
# -*- coding: utf-8 -*-
from nntplib import NNTP
from time import strftime, time, localtime

day = 24 * 60 * 60  # 一天的秒数

yesterday = localtime(time() - day)
date = strftime('%y%m%d', yesterday)
hour = strftime('%H%M%S', yesterday)

servername = 'news2.neva.ru'
group = 'comp.lang.python.announce'
server = NNTP(servername)

ids = server.newnews(group, date, hour)[1]  # 获取文章的id列表

for id in ids:
    head = server.head(id)[3]
    for line in head:
        if line.lower().startswith('subject:'):
            subject = line[9:]
            break  # 找到subject后没有必要继续

    body = server.body(id)[3]

    print subject
    print '-'*len(subject)
    print '\n'.join(body)

server.quit()