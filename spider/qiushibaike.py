#!/usr/bin/python
# coding: utf-8

import urllib
import re


class Qiubai:

    # 初始化，定义一些变量
    def __init__(self):
        # 初始页面为1
        self.pageIndex = 1
        # 定义UA
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
        # 定义headers
        self.headers = {'User-Agent': self.user_agent}
        # 存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        # 程序是否继续运行
        self.enable = False

    def getPage(self, pageIndex):
        """
        传入某一页面的索引后的页面代码
        """
        try:
            url = 'http://www.qiushibaike.com/hot/page/' + str(pageIndex)
            # 构建request
            request = urllib.request.Request(url, headers=self.headers)
            # 利用urlopen获取页面代码
            response = urllib.request.urlopen(request)
            # 页面转为utf-8编码
            pageCode = response.read().decode("utf8")
            return pageCode
        # 捕获错误原因
        except urllib.error.URLError as e:
            if hasattr(e, "reason"):
                print(u"连接糗事百科失败，错误原因", e.reason)
                return None

    def getPageItems(self, pageIndex):
        """
        传入某一页代码，返回本页不带图的段子列表
        """
        # 获取页面代码
        pageCode = self.getPage(pageIndex)
        # 如果获取失败，返回None
        if not pageCode:
            print("页面加载失败...")
            return None
        # 匹配模式
        pattern = re.compile(
            '<div.*?author clearfix">.*?<h2>(.*?)</h2>.*?<div.*?content".*?<span>(.*?)</span>.*?</a>(.*?)<div class="stats".*?number">(.*?)</i>', re.S)
        # findall匹配整个页面内容,items匹配结果
        items = re.findall(pattern, pageCode)
        # 存储整页的段子们
        pageStories = []
        # 遍历正则表达式匹配的结果, 0name, 1content, 2img, 3votes
        for item in items:
            # 是否含有图片
            haveImg = re.search("img", item[2])
            # 不含，加入pageStories
            if not haveImg:
                # 替换content中的<br/>标签为\n
                replaceBR = re.compile('<br/>')
                text = re.sub(replaceBR, "\n", item[1])
                # 在pageStories中存储：名字、内容、赞数
                pageStories.append(
                    [item[0].strip(), text.strip(), item[3].strip()])
        return pageStories

    def loadPage(self):
        """
        加载并提取页面的内容，加入到列表中
        """
        # 如未看页数少于2，则加载并抓取新一页补充
        if self.enable is True:
            if len(self.stories) < 2:
                pageStories = self.getPageItems(self.pageIndex)
                if pageStories:
                    # 添加到self.stories列表中
                    self.stories.append(pageStories)
                    # 实际访问的页码+1
                    self.pageIndex += 1

    def getOneStory(self, pageStories, page):
        """
        调用该方法，回车输出一个段子，q结束程序
        """
        # 循环访问一页的段子
        for story in pageStories:
            # 等待用户输入，回车输出段子，q退出
            input = input()
            self.loadPage()
            # 如果用户输入q退出
            if input == "q":
                # 停止程序运行，start()中while判定
                self.enable = False
                return
            # 打印story:0 name, 1 content, 2 votes
            print(u"第%d页\t发布人:%s\t\3:%s\n%s" % (page, story[0], story[2], story[1]))

    def start(self):
        """
        开始方法
        """
        print(u"正在读取糗事百科，回车查看新段子，q退出")
        # 程序运行变量True
        self.enable = True
        # 加载一页内容
        self.loadPage()
        # 局部变量，控制当前读到了第几页
        nowPage = 0
        # 直到用户输入q，self.enable为False
        while self.enable:
            if len(self.stories) > 0:
                # 吐出一页段子
                pageStories = self.stories.pop(0)
                # 用于打印当前页面，当前页数+1
                nowPage += 1
                # 输出这一页段子
                self.getOneStory(pageStories, nowPage)


if __name__ == '__main__':
    qiubaiSpider = Qiubai()
    qiubaiSpider.start()
