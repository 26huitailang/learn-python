#!/usr/bin/python
# -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode
 
#----------------------------------
# 电影票房调用示例代码 － 聚合数据
# 在线接口文档：http://www.juhe.cn/docs/44
#----------------------------------
 
def main():
 
    #配置您申请的APPKey
    appkey = "*********************"
 
    #1.最新票房榜
    request1(appkey,"GET")
 
    #2.网票票房
    request2(appkey,"GET")
 
 
 
#最新票房榜
def request1(appkey, m="GET"):
    url = "http://v.juhe.cn/boxoffice/rank"
    params = {
        "area" : "", #票房榜的区域,CN-内地，US-北美，HK-香港
        "key" : appkey, #应用APPKEY(应用详细页查询)
        "dtype" : "", #返回数据的格式,xml/json，默认json
 
    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)
 
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"
 
#网票票房
def request2(appkey, m="GET"):
    url = "http://v.juhe.cn/boxoffice/wp"
    params = {
        "key" : appkey, #应用APPKEY
        "dtype" : "", #返回数据的格式,xml或json，默认json
 
    }
    params = urlencode(params)
    if m =="GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)
 
    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            #成功请求
            print res["result"]
        else:
            print "%s:%s" % (res["error_code"],res["reason"])
    else:
        print "request api error"
 
 
 
if __name__ == '__main__':
    main()