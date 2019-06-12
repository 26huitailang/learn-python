import gevent
import gevent.monkey
import time
import datetime
import requests

gevent.monkey.patch_all()


urls = [
        'https://www.baidu.com',
        'https://www.facebook.com',
        'https://www.google.com',
        'https://www.qq.com',
        'https://www.github.com',
        'http://127.0.0.1:8000/api/v1/mzitu/tags/'
    ]


def _thread_one(url):
    resp = requests.get(url)
    print(resp.status_code)
    print("{} {}".format(datetime.datetime.now(), url))


def sync_main():
    for url in urls:
        resp = requests.get(url)
        print(resp.status_code)
        print("{} {}".format(datetime.datetime.now(), url))


def gevent_main():
    spawns = []
    for t in urls * 3:
        spawns += [gevent.spawn(_thread_one, t)]

    gevent.joinall(spawns)

if __name__ == '__main__':
    start = time.time()
    gevent_main()
    end = time.time()
    print(end - start)
    # sync_main()
    # print(time.time() - end)