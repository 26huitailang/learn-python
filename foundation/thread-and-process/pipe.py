"""
让进程通过管道通信，管道在创建的时候都r,w都指向parent
然后fork一个child，此时管道也会被fork，parent和child分别关闭r/w，
这样就形成了，parent写，child读的一个管道基本通信。
"""
import os
import time


def parent(rfd, wfd):
    """写，关闭读"""
    print('This is parent')
    os.close(rfd)
    w = os.fdopen(wfd, 'w')
    count = 0
    while True:
        time.sleep(1)
        w.write('Number {}\n'.format(count))
        w.flush()  # 不然读不到
        count += 1


def child(rfd, wfd):
    """读，写关闭"""
    print('This is child')
    os.close(wfd)
    r = os.fdopen(rfd)
    while True:
        line = r.readline()[:-1]  # 去掉\n不然print会换行
        print('Child {} got {} at {}'.format(os.getpid(), line, time.time()))


rfd, wfd = os.pipe()
pid = os.fork()
print(pid)
if pid != 0:
    child(rfd, wfd)
else:
    parent(rfd, wfd)
