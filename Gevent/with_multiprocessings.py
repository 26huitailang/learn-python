"""
以进程为单位启动协程任务组，主进程处理SIGTERM信号，关闭所有子进程
"""
import os
import gevent
import gevent.monkey
import time
import datetime
import requests
from multiprocessing import Process
import multiprocessing
import signal
import random

gevent.monkey.patch_all()


urls = [
        'https://www.baidu.com',
        'https://www.facebook.com',
        'https://www.google.com',
        'https://www.qq.com',
        'https://www.github.com',
        'http://127.0.0.1:8000/api/v1/mzitu/tags/'
    ]
processes = []

def _process_one(sleep_time=0):
    while True:
        for url in urls:
            try:
                resp = requests.get(url)
                print("{} - {}".format(os.getpid(), resp.status_code))
            except requests.ConnectionError as e:
                print("wahaha: {}".format(e))
            print("{} {}".format(datetime.datetime.now(), url))
            sleep_time = random.random() * 10
            print("sleep {}".format(sleep_time))
            time.sleep(sleep_time)


def process_start(task_list):
    spawn_list = [gevent.spawn(x) for x in task_list]
    gevent.joinall(spawn_list)


def term_func():
    for process in processes:
        process.terminate()


def gevent_main():
    signal.signal(signal.SIGTERM, term_func)  # 注册信号，当主进程收到信号时，执行这个函数
    task_list = [_process_one, _process_one, _process_one]
    # p_count = multiprocessing.cpu_count()
    p_count = 1
    for t in range(p_count):
        p = Process(target=process_start, args=(task_list,))
        p.daemon = True  # 子进程完毕关闭主进程
        p.start()
        processes.append(p)
    for p in processes:
        p.join()


if __name__ == '__main__':
    gevent_main()
