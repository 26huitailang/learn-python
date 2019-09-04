import requests
import sys
from bs4 import BeautifulSoup


class LazyProperty:
    """ 用描述符实现延迟加载的属性 """

    def __init__(self, method):
        self.method = method
        self.method_name = method.__name__

    def __get__(self, obj, cls):
        """实例化后，调用该属性时，获得方法的value，然后通过setattr覆盖掉该方法，第二次该实例访问的就是method_name属性的值，而不包含里面的方法"""
        if not obj:
            return None
        value = self.method(obj)
        print("value {}".format(value))
        setattr(obj, self.method_name, value)
        return value


class Test:
    def __init__(self):
        self.x = "foo"
        self.y = "bar"
        self._suites = None

    @property
    def a(self):
        return "a"

    @LazyProperty
    def suites(self):  # 构造函数里没有初始化，第一次访问才会被调用
        print("initializing self._suites which is: {}".format(self._suites))
        html = requests.get(sys.argv[1])
        init_page = BeautifulSoup(html.content, "lxml")
        init_ul_img = init_page.find("ul", class_="img")

        self._suites = []
        for li in init_ul_img.find_all("li"):
            a_tags = li.find_all("a")
            name = a_tags[1].text
            href = a_tags[0].attrs["href"]
            self._suites.append((name, href))
        return self._suites


def main():
    t = Test()
    print(t.x)
    print(t.y)
    # 访问LazyProperty, resource里的print语句只执行一次，实现了延迟加载和一次执行
    print(t.suites)
    print(t.suites)
    print(t.suites)


if __name__ == "__main__":
    main()
