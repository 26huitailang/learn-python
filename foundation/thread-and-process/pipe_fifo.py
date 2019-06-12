"""
命名管道，通过os.mkfifo创建一个管道文件

FIFOs are pipes that can be accessed like regular files. FIFOs exist until they are deleted (for example with os.unlink()). Generally, FIFOs are used as rendezvous between “client” and “server” type processes: the server opens the FIFO for reading, and the client opens it for writing. Note that mkfifo() doesn’t open the FIFO — it just creates the rendezvous point.
"""
import os
import time

pipe_name = 'pipe_test'


def parent():
    pipeout = os.open(pipe_name, os.O_WRONLY)
    count = 0
    while True:
        os.write(pipeout, 'Number {}\n'.format(count).encode())
        count += 1
        time.sleep(1)


def child():
    pipein = os.open(pipe_name, os.O_RDONLY)
    while True:
        line = os.read(pipein, 1024)
        print('Child {} got {} at {}'.format(os.getpid(), line, time.time()))


if not os.path.exists(pipe_name):
    os.mkfifo(pipe_name)

pid = os.fork()
print(pid)
if pid != 0:
    child()
else:
    parent()
