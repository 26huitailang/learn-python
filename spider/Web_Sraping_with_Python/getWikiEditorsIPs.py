# coding: utf-8
"""循环遍历词条内链中词条的编辑历史，通过IP地址获取国家代码

每次遍历完一个词条后，随机从内链中选取一个词条继续访问，直到某个词条的内链为0
"""
from urllib.request import urlopen, HTTPError
from bs4 import BeautifulSoup
import datetime
import random
import re
import json

# 改变随机数生成器的种子，利用现在的时间
random.seed(datetime.datetime.now())


def getLinks(articleUrl):
    """得到词条内部链接
    
    :param articleUrl: 文章的链接后面部分
    :return: 符合正则的词条内部链接，以<a>标签的形式
    """
    # 获得页面内容
    html = urlopen("http://en.wikipedia.org" + articleUrl)
    # 利用BS解析
    bsObj = BeautifulSoup(html, 'lxml')
    # 根据BS解析结果获得内链
    return bsObj.find("div", {"id": "bodyContent"}).findAll("a",
                                                            href=re.compile(
                                                                "^(/wiki/)((?!:).)*$"))  # 正则，开头为/wiki/且整个字符串不包含:


def getHistoryIPs(pageUrl):
    """获取编辑历史的IP地址
    没有登录的用户编辑之后，会留下IP地址
    
    :param pageUrl: 内链的后面部分
    :return: IP地址的列表
    """
    # 编辑历史页面URL链接格式是：
    # http://en.wikipedia.org/w/index.php?title=Title_in_URL&action=history
    # 相比词条基础地址没有/wiki/
    pageUrl = pageUrl.replace("/wiki/", "")
    # 构建编辑历史的URL
    historyUrl = "http://en.wikipedia.org/w/index.php?title=" + pageUrl + "&action=history"
    print("history url is: " + historyUrl)
    html = urlopen(historyUrl)
    bsObj = BeautifulSoup(html, 'lxml')
    # 找出class属性是"mw-userlink mw-anonuserlink"的链接
    # 没有登录的用户用IP地址代替用户名
    ipAddresses = bsObj.findAll("a", {"class": "mw-userlink mw-anonuserlink"})
    # 用set存放去重
    addressList = set()
    for ipAddress in ipAddresses:
        addressList.add(ipAddress.get_text())
    return addressList


def getCountry(ipAddress):
    """获得国家缩写字母
    
    :param ipAddress: 传入一个IP地址 
    :return: 国家缩写字母
    """
    # 因为freegeoip.net无法查询IPv6地址，可能引起404，所以用try保证稳定
    try:
        response = urlopen("http://freegeoip.net/json/" + ipAddress).read().decode('utf-8')
    except HTTPError:
        return None
    # 转换获取的JSON数据为字典
    responseJson = json.loads(response)
    # 获取country_code关键字的值
    return responseJson.get("country_code")

# 获取该词条下的内链
links = getLinks("/wiki/Python_(programming_language)")

# 随机访问不同词条下的内链，直到某个页面内链为0
while len(links) > 0:
    for link in links:
        print("-------------------------")
        # 获取某个内链的编辑历史IP地址列表
        historyIPs = getHistoryIPs(link.attrs["href"])
        for historyIP in historyIPs:
            # 查询IP地址的国家代码
            country = getCountry(historyIP)
            # 如果发生错误，getCountry返回None
            if country is not None:
                print(historyIP + " is from " + country)
        # 随机抽取一个内链作为词条，遍历该词条下的所有内链
        newLink = links[random.randint(0, len(links) - 1)].attrs["href"]
        # 获取新的词条的所有内链
        links = getLinks(newLink)
