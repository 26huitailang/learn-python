import gevent
import gevent.monkey

gevent.monkey.patch_all()

def _thread_one():
    while True:
        print(1)
        gevent.sleep(3)


def _thread_two():
    while True:
        print(2)
        gevent.sleep(4)


def _thread_three():
    while True:
        print(3)
        gevent.sleep(5)


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
    # main()
    main_all_in_one()
