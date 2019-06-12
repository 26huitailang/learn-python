"""
队列Block模式
"""
import gevent
import gevent.monkey
import time
import datetime
import requests
from gevent import queue
gevent.monkey.patch_all()

data_queue = queue.Queue()


def push_data():
    data_list = []

    while True:
        item = data_queue.get()
        data_list.append(item)

        while len(data_list) < 30:
            try:
                item = data_queue.get(block=False)
                data_list.append(item)
                time.sleep(0.31)
                continue
            except queue.Empty:
                break
        print("pushed: {}".format(data_list))
        data_list = []
        time.sleep(1)


def create_data():
    count = 0
    while True:
        count += 1
        if count % 100 == 0:
            time.sleep(0.2)
        data_queue.put(count)
        print("created: {}".format(count))
        time.sleep(0.3)


def gevent_main():
    spawns = []
    spawns = [gevent.spawn(create_data), gevent.spawn(push_data)]

    gevent.joinall(spawns)


if __name__ == '__main__':
    gevent_main()
