# coding: utf-8

import gevent
from gevent.event import Event, AsyncResult
# evt = Event()
evt = AsyncResult()
is_ok = False

def setter():
    print('T: 好好听课')
    gevent.sleep(5)  # 持续时间为5
    print('T: 好的,下课')
    evt.set('hello world')


def waiter(sid=0):
    # 等待下课
    print('S{}: 听课'.format(sid))
    data = evt.get()
    print(data)
    print('S{}: 哈哈,终于下课了'.format(sid))


def main() :
    gevent.joinall([
        gevent.spawn(setter),
        gevent.spawn(waiter, 1),
        gevent.spawn(waiter, 2),
    ])

if __name__ == '__main__' :
    main()
