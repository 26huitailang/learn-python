#!/usr/bin/python
# coding: utf-8
import os
import time
import threading
import multiprocessing
from mongodb_queue import MongoQueue
from download import request
from bs4 import BeautifulSoup
import re

SLEEP_TIME = 1


def mzitu_crawler(max_threads=2):
    crawl_queue = MongoQueue('meinvxiezhenji', 'crawl_queue')

    def pageurl_crawler():
        while True:
            try:
                url = crawl_queue.pop()
                print(url)
            except KeyError:
                print('队列没有数据')
                break
            # 如果没有exception
            else:
                # img_urls = []
                req = request.get(url, 3).text
                title = crawl_queue.pop_title(url)
                mkdir(title)
                os.chdir('d:\mzitu\\' + title)
                max_span = BeautifulSoup(req, 'lxml').find('div', class_='pagenavi').find_all('span')[-2].get_text()
                for page in range(1, int(max_span) + 1):
                    page_url = url + '/' + str(page)
                    # 解析并获得图片URL
                    img_dict = BeautifulSoup(request.get(page_url, 3).text, 'lxml').find('div', class_='main-image').find('img')
                    if img_dict is not None:
                        img_url = img_dict['src']
                    else:
                        print(u'没有获取到img_url*********************')
                    img_url_reg = re.compile('http://.*?\.jpg', re.S)
                    if re.match(img_url_reg, img_url):
                        # 套图所有的图片地址添加到img_urls
                        # img_urls.append(img_url)
                        save(img_url)
                crawl_queue.complete(url)

    def save(img_url):
        """
        保存图片
        """
        # 图片URL的倒数9位到5位为图片名称
        name = img_url[-9:-4]
        # 如果名字出现像12/01.jpg的话windows会no such file directory
        name = re.sub(r'/', '-', name)
        # 请求，获取图片URL的Response
        img = request.get(img_url, 3)
        # 打开文件文件，ab 为追加二进制模式，因为要写入图片
        f = open(name + '.jpg', 'ab')
        # img.content才是图片的内容
        f.write(img.content)
        # 关闭文件
        f.close()

    def mkdir(path):
        """
        创建文件夹，每个套图的
        """
        # 清除首尾空白
        path = path.strip()
        # 构建绝对路径，注意os.path和传入的path不是同一个
        is_exists = os.path.exists(os.path.join("D:\mzitu", path))
        # 如不存在，就新建一个，否则打印已经存在
        if not is_exists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\mzitu", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

    threads = []
    while threads or crawl_queue:
        for thread in threads:
            if not thread.is_alive():  # is_alive判断是否为空
                threads.remove(thread)
        while (len(threads) < max_threads) and crawl_queue.peek():
            thread = threading.Thread(target=pageurl_crawler)
            thread.setDaemon(True)  # 主进程killed的时候，子线程也会killed
            thread.start()
            threads.append(thread)
        time.sleep(SLEEP_TIME)

def process_crawler():
    process = []
    num_cpus = multiprocessing.cpu_count()
    print('将会启动进程数为：', num_cpus)
    for i in range(num_cpus):
        p = multiprocessing.Process(target=mzitu_crawler)
        p.start()
        process.append(p)
    for p in process:
        p.join()


if __name__ == '__main__':
    process_crawler()
