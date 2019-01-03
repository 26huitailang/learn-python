# coding:utf8
import gevent
from gevent.event import Event

evt = Event()


def setter():
    print('Wait for me')
    gevent.sleep(3)  # 3秒后唤醒所有在evt上等待的协程
    print("Ok, I'm done")
    evt.set()  # 唤醒


def waiter():
    print("I'll wait for you")
    evt.wait()  # 等待
    print('Finish waiting')


gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter)
])
