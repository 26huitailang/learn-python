import gevent
import gevent.monkey
import time
import datetime
gevent.monkey.patch_all()


def _thread_one():
    while True:
        print(1)
        start = time.time()
        gevent.sleep(3)
        # print("{} {}".format('one', time.time() - start))
        print("{} {}".format('one', datetime.datetime.now()))


def _thread_two():
    while True:
        print(2)
        start = time.time()
        gevent.sleep(4)
        # print("{} {}".format('two', time.time() - start))
        print("{} {}".format('two', datetime.datetime.now()))


def _thread_three():
    while True:
        print(3)
        start = time.time()
        gevent.sleep(5)
        # print("{} {}".format('three', time.time() - start))
        print("{} {}".format('three', datetime.datetime.now()))


def main():
    # 三个协程
    thread_list = [_thread_one, _thread_two, _thread_three]
    spawns = []
    for t in thread_list:
        spawns += [gevent.spawn(t)]

    gevent.joinall(spawns)


def all_in_one():
    # 一个协程
    while True:
        _thread_one()
        _thread_three()
        _thread_three()
        gevent.sleep(3)


def main_all_in_one():
    gevent.joinall([gevent.spawn(all_in_one)])


if __name__ == '__main__':
    main()
#     main_all_in_one()
