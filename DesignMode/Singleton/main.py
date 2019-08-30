"""
__init__是一个class的初始化方法，而构造方法其实是内部的__new__方法，可以用该方法实现singleton

输出：
    Sun: <__main__.Sun object at 0x1006a9668>
    already have <__main__.Sun object at 0x1006a9668>
    Sun: <__main__.Sun object at 0x1006a9668>
    Moon: <__main__.Moon object at 0x1006a96a0>
    already have <__main__.Moon object at 0x1006a96a0>
    Moon: <__main__.Moon object at 0x1006a96a0>

初始化得到的是同一个对象，都是在__new__方法中创建的
"""


class Singleton(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls, *args, **kwargs)
        else:
            print("already have {}".format(cls._instance))
        return cls._instance


class Sun(Singleton):
    def __init__(self):
        print("Sun: {}".format(self))


class Moon(Singleton):
    def __init__(self, *args, **kwargs):
        print("Moon: {}".format(self))


if __name__ == "__main__":
    Sun()
    Sun()
    Moon()
    Moon()
