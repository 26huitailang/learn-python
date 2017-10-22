#!/usr/bin/python
# coding: utf-8
from functools import wraps
from datetime import datetime


# 直接使用wrapper
def log(func):  # 被装饰的函数作为参数传入装饰器函数
    def wrapper(*args, **kw):  # 装饰器接受被装饰函数的所有参数
        print('call %s()' % func.__name__)  # 装饰器的操作
        return func(*args, **kw)  # 返回被装饰函数并传入参数
    return wrapper  # 返回装饰器


'''
如果decorator本身需要传入参数，那就需要编写一个返回decorator的高阶函数，
写出来会更复杂。比如，要自定义log的文本：
'''
def log1(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator


"""
因为返回的那个wrapper()函数名字就是'wrapper'，所以，需要把原始函数的__name__等属性
复制到wrapper()函数中，否则，有些依赖函数签名的代码执行就会出错。

不需要编写wrapper.__name__ = func.__name__这样的代码，
Python内置的functools.wraps就是干这个事的，
所以，一个完整的decorator的写法如下：
"""
def log2(func):
    @wraps(func)
    def wrapper(*args, **kw):
        print('call %s()' % func.__name__)
        return func(*args, **kw)
    return wrapper


'''
由于log()是一个decorator，返回一个函数，
所以，原来的now()函数仍然存在，只是现在同名的now变量指向了新的函数，
于是调用now()将执行新函数，即在log()函数中返回的wrapper()函数。
'''
# 此处修改装饰器，体验不同装饰器的区别
# @log
# @log1('excute')
@log2
def now():
    print(datetime.now())

"""同等操作
2层嵌套 now = log(now)
3层嵌套 now = log1('excute')(now)
"""

# 经过装饰后，原有的__name__属性由'now'变为'wrapper'
# 因为返回的那个wrapper()函数名字就是'wrapper'
print(now.__name__)


if __name__ == '__main__':
    now()
