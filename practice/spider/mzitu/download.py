#!/usr/bin/python
# coding: utf-8

import requests
import re
import random
import time


class Download():
    """
    发起request的类，在爬取过程中不断更换User-Agent和ip proxy
    让服务器认为是不同的浏览器和用户在访问，避免被拒绝访问
    """

    def __init__(self):
        # 初始化一个iplist，存储代理ip地址
        self.iplist = []
        # 获取haoip网站的response
        haoip_html = requests.get("http://haoip.cc/tiqu.htm")
        # 匹配网页内容的代理ip地址，得到一个iplistn的列表
        iplistn = re.findall(r'r/>(.*?)<b', haoip_html.text, re.S)
        # 处理ip地址列表，并添加到self.iplist
        for ip in iplistn:
            # 替换\n为''
            i = re.sub('\n', '', ip)
            # 去掉首尾空白，添加到self.iplist中
            self.iplist.append(i.strip())
            # print(i.strip())
        # print(self.iplist)
        # User-Agent的列表，用于随机选择并更换UA
        self.user_agent_list = [
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
            "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 (KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
            "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 (KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
            "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
        ]

    def get(self, url, timeout, proxy=None, num_retries=6):
        """
        获取url的response
        timeout：传入requests.get判定超时
        proxy：传入代理ip，默认为None时，使用本机IP
        num_retries：判断获取的最大次数，超过后更换IP，默认为6
        """
        # 提示信息
        print(u'开始获取：', url)
        # 随机从self.user_agent_list中选取一个UA
        user_agent = random.choice(self.user_agent_list)
        # 构建headers
        headers = {'User-Agent': user_agent}
        # 代理为空
        if proxy is None:
            # 尝试获取url的response并返回
            try:
                return requests.get(url, headers=headers)
            # 出错，运行以下代码
            except:
                # 如果num_retries大于0，继续尝试
                if num_retries > 0:
                    # 等待8秒
                    time.sleep(8)
                    # 提示信息
                    print(u'获取网页出错，8S后将尝试获取倒数第：', num_retries, u'次')
                    # 调用函数本身，继续判定
                    return self.get(url, timeout, num_retries - 1)
                # 尝试了规定的次数后
                else:
                    # 提示信息
                    print(u'开始使用代理')
                    # 等待8秒
                    time.sleep(8)
                    # 从self.iplist中随机选择一个IP地址，类型str，去掉首尾空白
                    ip_proxy = ''.join(str(random.choice(self.iplist)).strip())
                    # 构建proxy，最终会传入requests.get
                    proxy = {'http': ip_proxy}
                    # 调用函数本身，继续判定
                    return self.get(url, timeout, proxy,)
        # 代理不为空
        else:
            # 尝试使用代理IP地址
            try:
                # 随机选取IP地址，去掉中间的空白，str类型，去掉首尾空白
                ip_proxy = ''.join(str(random.choice(self.iplist)).strip())
                # print(IP)
                # 构建proxy，最终传入requests.get
                proxy = {'http': ip_proxy}
                # 发起requests.get请求response
                return requests.get(url, headers=headers, proxies=proxy, timeout=timeout)
            # 出错，尝试多次
            except:
                # 尝试多次
                if num_retries > 0:
                    time.sleep(8)
                    ip_proxy = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': ip_proxy}
                    print(u'当前代理：', ip_proxy)
                    # 调用自身，num_retries - 1
                    return self.get(url, timeout, proxy, num_retries - 1)
                # 达到最大次数，代理失效，切换本机IP
                else:
                    print(u'代理也失效了！取消使用代理，切换本机地址')
                    # 不传入proxy，默认为空
                    return self.get(url, 3)


# 构建一个实例，在down_mzitu.py中导入
request = Download()

# if __name__ == '__main__':
#     download = Download()
#     print(download.get('http://www.mzitu.com', 3))
