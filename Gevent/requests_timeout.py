import gevent
import gevent.monkey
import time
import datetime
import requests

gevent.monkey.patch_all()


urls = [
        # 'https://www.baidu.com',
        # 'https://www.facebook.com',
        # 'https://www.google.com',
        # 'https://www.qq.com',
        # 'https://www.github.com',
        'http://127.0.0.1:8000/api/v1/mzitu/tags/'
    ]


def _thread_one(url, id):
    count = 0
    while True:
        count += 1
        try:
            print("=" * 20)
            start = time.time()
            if count % 100 == 0:
                raise requests.ConnectionError
            resp = requests.get(url)
            print(resp.status_code)
            print("{} {} {}".format(id, datetime.datetime.now(), url))
        except requests.ConnectionError as e:
            print("Error: {}".format(e))
        finally:
            time.sleep(0)
            print("time gap: {}".format(time.time() - start))


def sync_main():
    for url in urls:
        resp = requests.get(url)
        print(resp.status_code)
        print("{} {}".format(datetime.datetime.now(), url))


def gevent_main():
    spawns = [gevent.spawn(_thread_one, urls[-1], id) for id in range(5)]
    gevent.joinall(spawns)

if __name__ == '__main__':
    start = time.time()
    gevent_main()
    end = time.time()
    print(end - start)
    # sync_main()
    # print(time.time() - end)