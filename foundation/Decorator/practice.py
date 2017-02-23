#!/usr/bin/python
# coding: utf-8
"""
请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。

再思考一下能否写出一个@log的decorator，使它既支持：

@log
def f():
    pass

又支持：

@log('execute')
def f():
    pass
"""

from functools import wraps


def log(text):
    if callable(text):  # 如果text有__call__属性，则传入是函数或类
        @wraps(text)
        def wrapper(*args, **kw):
            print('begin call')
            text(*args, **kw)
            print('end call')
        return wrapper
    # 否则text是字符串或数字
    else:
        def decorator(func):
            @wraps(func)
            def wrapper(*args, **kw):
                print('begin call')
                print('%s %s()' % (text, func.__name__))
                func(*args, **kw)
                print('end call')
            return wrapper
        return decorator


@log
def f1():
    print('2层嵌套装饰器')
@log('excute')
def f2():
    print('3层嵌套装饰器')


if __name__ == '__main__':
    f1()
    f2()
