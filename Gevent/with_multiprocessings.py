import gevent
import gevent.monkey
import time
import datetime
import requests
from multiprocessing import Process

gevent.monkey.patch_all()


urls = [
        'https://www.baidu.com',
        'https://www.facebook.com',
        'https://www.google.com',
        'https://www.qq.com',
        'https://www.github.com',
        'http://127.0.0.1:8000/api/v1/mzitu/tags/'
    ]


def _process_one(url, sleep_time=0):
    try:
        resp = requests.get(url)
        print(resp.status_code)
    except requests.ConnectionError as e:
        print("wahaha: {}".format(e))
    print("{} {}".format(datetime.datetime.now(), url))
    time.sleep(sleep_time)


def process_start(task_list):
    gevent.joinall(task_list)


def sync_main():
    start = time.time()
    for url in urls:
        resp = requests.get(url)
        print(resp.status_code)
        print("{} {}".format(datetime.datetime.now(), url))
    end = time.time()
    print(end - start)


def gevent_main():
    start = time.time()
    task_list = [gevent.spawn(_process_one, url, 1) for url in urls]
    for t in range(4):
        p = Process(target=process_start, args=(task_list,))
        p.start()

    end = time.time()
    print(end - start)

if __name__ == '__main__':
    gevent_main()
    sync_main()
