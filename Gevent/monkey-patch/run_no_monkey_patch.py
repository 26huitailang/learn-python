"""
验证monkey_patch影响的范围，两个程序在不同的venv执行，看看patch的函数对象是否属于Gevent？

- 同一个环境不同进程
    - 先启动 python run_with_monkey_patch.py，再启动不带补丁的
    - 发现在同一个环境两个进程下，monkey_patch不影响，动态替换的
- 同一个环境同一个进程
    - 修改下代码run_with_monkey_patch, 引入no_patch，运行发现被替换
- 同一个环境fork进程
    - process_fork.py, 从程序中用进程启动另外一个不带布丁的代码
    - 子进程的也是patch后的环境

monkey_patch实现原理: http://xiaorui.cc/2016/04/27/%E6%BA%90%E7%A0%81%E5%88%86%E6%9E%90%E4%B9%8Bgevent-monkey-patch_all%E5%AE%9E%E7%8E%B0%E5%8E%9F%E7%90%86/
"""
import gevent
from gevent import monkey
import socket
import time

# monkey.patch_all()

def no_patch():
    while True:
        print("no patch: {}".format(socket.socket))
        time.sleep(3)


if __name__ == "__main__":
    no_patch()
