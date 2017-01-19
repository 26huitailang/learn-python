#!/usr/bin/python
# coding: utf-8
import requests
from bs4 import BeautifulSoup
import os


class Mzitu():
    """
    抓取妹子图的类
    all_url，获得mzitu.com/all上面需要的内容
    html，分析套图地址，获得套图每张图片的页面代码
    img，根据图片页面代码获得图片的URL
    save，保存图片
    mkdir，创建相应的文件夹
    request，复用requests.get()
    """
    def all_url(self, url):
        """
        传入mzitu.com/all汇总信息页面，获取套图的地址
        """
        # 调用request函数把地址传进去会返回给我们一个response
        html = self.request(url)
        # BS用lxml解析器分析html.text网页代码，找到div class='all'标签下所有的<a>标签信息
        all_a = BeautifulSoup(html.text, 'lxml').find(
            'div', class_='all').find_all('a')
        # 遍历所有<a>
        for a in all_a:
            # 获取<a>内容作为标题
            title = a.get_text()
            # 加点提示
            print(u'开始保存：', title)
            # 有个标题带有 ？ 这个符号Windows系统是不能创建文件夹的所以要替换掉
            path = str(title).replace("?", '_')
            # 调用mkdir函数创建文件夹！这儿path代表的是标题title哦！不要糊涂了哦！
            self.mkdir(path)
            # 切换到目录，原文只有path，运行有问题
            mzitu_path = "d:\mzitu\\" + path
            os.chdir(mzitu_path)
            # 获取<a>中的href链接，套图地址
            href = a['href']
            # 调用html函数把href参数传递过去，获取每页图片的地址
            self.html(href)

    def html(self, href):
        """
        这个函数是处理套图地址获得每页图片的页面地址
        """
        # 请求套图地址，获得Response
        html = self.request(href)
        # 获得最大页码，根据观察是div class='pagenavi'标签中，所有span的倒数第二个
        max_span = BeautifulSoup(html.text, 'lxml').find(
            'div', class_='pagenavi').find_all('span')[-2].get_text()
        # 构建每页图片地址并调用img函数获得图片URL
        for page in range(1, int(max_span) + 1):
            # 构建图片页面地址
            page_url = href + '/' + str(page)
            # 调用img函数
            self.img(page_url)

    def img(self, page_url):
        """
        这个函数处理图片页面地址获得图片URL
        """
        # 请求，获取图片页面的Response
        img_html = self.request(page_url)
        # 解析并获得图片URL
        img_url = BeautifulSoup(img_html.text, 'lxml').find(
            'div', class_='main-image').find('img')['src']
        # 调用save函数保存图片
        self.save(img_url)

    def save(self, img_url):
        """
        保存图片
        """
        # 图片URL的倒数9位到5位为图片名称
        name = img_url[-9:-4]
        # 请求，获取图片URL的Response
        img = self.request(img_url)
        # 打开文件文件，ab 为追加二进制模式，因为要写入图片
        f = open(name + '.jpg', 'ab')
        # img.content才是图片的内容
        f.write(img.content)
        # 关闭文件
        f.close()

    def mkdir(self, path):
        """
        创建文件夹，每个套图的
        """
        # 清除首尾空白
        path = path.strip()
        # 构建绝对路径，注意os.path和传入的path不是同一个
        is_exists = os.path.exists(os.path.join("D:\mzitu", path))
        # 如不存在，就新建一个，否则打印已经存在
        if not is_exists:
            print(u'建了一个名字叫做', path, u'的文件夹！')
            os.makedirs(os.path.join("D:\mzitu", path))
            return True
        else:
            print(u'名字叫做', path, u'的文件夹已经存在了！')
            return False

    def request(self, url):
        """
        获取网页的response 然后返回
        """
        headers = {
            'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}
        content = requests.get(url, headers=headers)
        return content


if __name__ == '__main__':
    # 实例化
    mzitu = Mzitu()
    # 给函数all_url传入参数，你可以当作启动爬虫（就是入口）
    mzitu.all_url('http://www.mzitu.com/all')
