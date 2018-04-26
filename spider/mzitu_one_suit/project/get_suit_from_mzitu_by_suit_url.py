#!/usr/bin/python
# coding: utf-8
import requests
import re
import sys
import time
import os
import random
import json
import threading

from .get_proxies import GetProxies
from .runtimes import DB_PATH
from .redis_queue import RedisQueue


PROXY_SOURCE_URL = 'http://www.xicidaili.com/nn/'

USER_AGENT_LIST = [
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
    "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
]

get_proxies = GetProxies(PROXY_SOURCE_URL, random.choice(USER_AGENT_LIST))
queue = RedisQueue('mzitu')


def get_max_page_num(html):
    pattern = re.compile(r'<span>(\d+)</span>')
    page_num = pattern.findall(html)
    print(html)
    print(page_num)
    return int(page_num[-1])


def header(referer):
    headers = {
        'Host': 'i.meizitu.net',
        'Pragma': 'no-cache',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'User-Agent': random.choice(USER_AGENT_LIST),
        'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer': '{}'.format(referer),
    }
    return headers


def get_proxy_url(ip, port):
    proxy_url = "http://{}:{}".format(ip, port)
    return proxy_url


def proxy_request(url):
    flag = True
    page = None
    while flag:
        ip, port = get_proxies.get_random_ip()
        try:
            time.sleep(0.5)
            proxy_url = get_proxy_url(ip, port)
            proxies = {"https": proxy_url}
            # proxies = {"http": proxy_url, "https": proxy_url}
            response = requests.get(url, proxies=proxies)
        except requests.exceptions.ProxyError as e:
            print(e)
            get_proxies.mark_invalid_proxy_ip(ip, port)
        else:
            flag = False
            page = response.content.decode('utf-8')
            response.connection.close()

    return page


def get_image_urls(suit_url):
    page = proxy_request(suit_url)

    max_page_num = get_max_page_num(page)
    title = re.search(r'class=\"main-title\">(.+?)</', page)
    title = title.group(1).strip()
    title = re.sub(r'[/\\:*?"<>|]', '-', title)  # windows 非法文件夹名字符
    folder = DB_PATH
    folder = os.path.join(folder, title)
    if not os.path.isdir(folder):
        os.makedirs(folder, exist_ok=True)

    print(title)
    for i in range(1, max_page_num + 1):
        filename = os.path.join(folder, "{:0>2d}.jpg".format(i))

        # urllib.request.urlretrieve(img_url, filename, check_rate)
        if os.path.isfile(filename):
            print("已存在：{}".format(filename))
            continue

        time.sleep(0.5)
        url = suit_url + '/{}'.format(i)
        print(url)
        page = proxy_request(url)
        # print(page)
        img_url = re.search(r'class=\"main-image(.+?)src=\"(.+?)\"', page)
        img_url = img_url.groups()[1]
        print(img_url)

        queue.put(json.dumps({'filename': filename, 'url': img_url, 'header_url': url}))

    return


def requests_get(url, headers=None):
    ip, port = get_proxies.get_random_ip()
    proxy_url = get_proxy_url(ip, port)
    proxies = {"https": proxy_url}

    return requests.get(url, headers=headers, proxies=proxies)


def download_images_to_local():
    while queue.qsize() < 8:
        pass

    while not queue.empty():
        item = queue.get()
        item = json.loads(item)

        if os.path.isfile(item['filename']):
            print("已存在：{}".format(item['filename']))
            continue

        img_bytes = requests_get(item['url'], headers=header(item['header_url']))
        with open(item['filename'], 'wb') as f:
            f.write(img_bytes.content)
        print("Downloaded {}".format(item['url']))
        time.sleep(1)

    return


def main():
    ip_list = get_proxies.get_ip_list()
    get_proxies.store_to_sqlite(ip_list)

    suit_url = sys.argv[1]
    print(suit_url)

    # 线程
    t1_get_image_urls = threading.Thread(target=get_image_urls, args=(suit_url,))
    t2_download_images = threading.Thread(target=download_images_to_local)
    t1_get_image_urls.start()
    time.sleep(4)
    t2_download_images.start()
    t1_get_image_urls.join()
    t2_download_images.join()
