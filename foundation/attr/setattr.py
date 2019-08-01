import time


# 错误示范
class Base:
    def get(self, item, default=None):
        return self.__getattribute__(item) or default


class ClassWrong(Base):
    def __init__(self, *args, **kwargs):
        # 触发__setattr__
        self.count = 0

    def __setattr__(self, name, value):
        # 还没有设置count，报错
        super().__setattr__(name, value)
        func = {"count": self.set_count}.get(name)
        func and func()

    def set_count(self):
        print(99)


class ClassRight:
    def __init__(self, *args, **kwargs):
        self.count = 0
        return super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        print(name)
        func = {"count": self.set_count}.get(name)
        func and func()
        return super().__setattr__(name, value)

    def set_count(self):
        print("hello")


if __name__ == "__main__":
    # b = ClassWrong()
    # print(b.count)

    r = ClassRight()
    while 1:
        time.sleep(1)
        # 每次对item属性设值时，都触发__setattr__方法
        r.count = 1
