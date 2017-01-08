#!/usr/bin/python
# coding: utf-8

import requests
import re
import random
import time


class Download():

    def __init__(self):
        self.iplist = []
        haoip_html = requests.get("http://haoip.cc/tiqu.htm")
        iplistn = re.findall(r'r/>(.*?)<b', haoip_html.text, re.S)
        for ip in iplistn:
            i = re.sub('\n', '', ip)
            self.iplist.append(i.strip())
            # print(i.strip())
        # print(self.iplist)
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
        print(u'开始获取：', url)
        user_agent = random.choice(self.user_agent_list)
        headers = {'User-Agent': user_agent}
        # 代理为空
        if proxy is None:
            try:
                return requests.get(url, headers=headers)
            except:
                if num_retries > 0:
                    time.sleep(8)
                    print(u'获取网页出错，8S后将尝试获取倒数第：', num_retries, u'次')
                    return self.get(url, timeout, num_retries-1)
                else:
                    print(u'开始使用代理')
                    time.sleep(8)
                    ip_proxy = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': ip_proxy}
                    return self.get(url, timeout, proxy,)
        # 代理不为空
        else:
            try:
                ip_proxy = ''.join(str(random.choice(self.iplist)).strip())
                # print(IP)
                proxy = {'http': ip_proxy}
                return requests.get(url, headers=headers, proxies=proxy, timeout=timeout)
            except:
                if num_retries > 0:
                    time.sleep(8)
                    ip_proxy = ''.join(str(random.choice(self.iplist)).strip())
                    proxy = {'http': ip_proxy}
                    print(u'当前代理：', ip_proxy)
                    return self.get(url, timeout, proxy, num_retries-1)
                else:
                    print(u'代理也失效了！取消使用代理，切换本机地址')
                    return self.get(url, 3)

request = Download()

# if __name__ == '__main__':
#     download = Download()
#     print(download.get('http://www.mzitu.com', 3))


