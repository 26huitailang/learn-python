# coding: utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
import random
import datetime
import pymysql
import re

conn = pymysql.connect(host='127.0.0.1', user='root', passwd='root', db='scraping', charset='utf8')
cur = conn.cursor()
cur.execute('USE scraping')

# 改变随机数生成器的种子，利用现在的时间
random.seed(datetime.datetime.now())


def store(title, content):
    """
    将title,content插入数据库
    :param title: 抓取的标题
    :param content: 抓取的内容
    :return: 
    """
    cur.execute("INSERT INTO pages (title, content) VALUES (%s, %s)", (title, content))
    cur.connection.commit()


def getLinks(articleUrl):
    """得到词条内部链接
    :param articleUrl: 文章的链接后面部分
    :return: 符合正则的词条内部链接，以<a>标签的形式
    """
    # 获得页面内容
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    # 利用BS解析
    bsObj = BeautifulSoup(html, 'lxml')
    # 获取存取的title和content
    title = bsObj.find('h1').get_text()
    content = bsObj.find('div', {'id': 'mw-content-text'}).find('p').get_text()
    # 调用store函数存入数据库
    store(title, content)
    # 根据BS解析结果获得内链
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a",
                                                            href=re.compile(
                                                                "^(/wiki/)((?!:).)*$"))  # 正则，开头为/wiki/且整个字符串不包含:

links = getLinks('/wiki/Kevin_Bacon')
try:
    while len(links) > 0:
        newArticle = links[random.randint(0, len(links) - 1)].attrs['href']
        print(newArticle)
        links = getLinks(newArticle)
finally:
    cur.close()
    conn.close()
