#!/usr/bin/python
# coding: utf-8
"""
运行scrapy的文件，python entrypoint.py命令运行
dingdian为spider中Myspider类的name属性
"""
from scrapy.cmdline import execute
execute(['scrapy', 'crawl', 'dingdian'])