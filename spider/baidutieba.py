#!/urs/bin/python
# coding: utf-8
'python2环境'

import urllib2
import re


class TagHandler:
    """
    用于清理内容中影响打印的标记
    """
    # 清理图片链接
    removeImg = re.compile('<img.*?>')
    # 清理超链接
    removeAddr = re.compile('<a.*?>|</a>')
    # replaceLine = re.compile('<tr>|<div>|</div>|</p>')
    # replaceTD = re.compile('<td>')
    # 根据观察，12个空格为换行标志，所以替换为换行符\n
    replacePara = re.compile(' {12}')
    # 替换为换行符\n
    replaceBR = re.compile('<br><br>|<br>')
    # 移除所有其他的标记
    removeExtraTag = re.compile('<.*?>')
    # 移除6-8次空格，改方法有问题，结果输出不对
    removeSpaces = re.compile(' {6,8}?')

    def replace(self, x):
        """
        替换方法用sub执行，最后调用该方法即可
        """
        x = re.sub(self.removeImg, "", x)
        x = re.sub(self.removeAddr, "", x)
        # x = re.sub(self.replaceLine, "\n", x)
        # x = re.sub(self.replaceTD, "\t", x)
        x = re.sub(self.replacePara, "\n  ", x)
        x = re.sub(self.replaceBR, "\n", x)
        x = re.sub(self.removeExtraTag, "", x)
        x = re.sub(self.removeSpaces, "\n", x)
        # 清理首尾的空白
        return x.strip()


class BDTB:
    """
    BDTB类，爬取百度贴吧的类
    """

    def __init__(self, baseUrl, seeLZ):
        """
        初始化，传入baseUrl基地址，seeLZ是否只看楼主
        """
        self.baseUrl = baseUrl
        self.seeLZ = '?see_lz=' + str(seeLZ)
        # 标签清除工具类的对象
        self.taghandler = TagHandler()
        # 默认输出文档标题，如果没有获取到标题的话
        self.defaultTitle = "baidutieba"
        # 输出的楼层号，默认为1
        self.floor = 1

    def getPage(self, pageNum):
        """
        传入页码，获取该页帖子的代码
        """
        try:
            # 构建URL
            url = self.baseUrl + self.seeLZ + '&pn=' + str(pageNum)
            request = urllib2.Request(url)
            response = urllib2.urlopen(request)
            # print response.read()
            # 返回utf8格式
            return response.read().decode("utf8")
        # 捕捉错误原因
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print u"连接百度贴吧失败，错误原因", e.reason
                return None

    def getTitle(self, indexPage):
        """
        获取帖子的标题
        """
        pattern = re.compile('<h3 class="core_title_txt.*?>(.*?)</h3>', re.S)
        # search匹配，返回Match对象，否则返回None
        result = re.search(pattern, indexPage)
        # 如果存在标题，返回标题，否则返回None
        if result:
            # print result.group(1)  # 测试输出
            return result.group(1).strip()
        else:
            return None

    def getPageNum(self, indexPage):
        """
        传入一页代码，获取帖子总页数
        """
        pattern = re.compile(
            '<li class="l_reply_num.*?</span>.*?<span.*?>(.*?)</span>', re.S)
        # 返回Match对象，否则返回None
        result = re.search(pattern, indexPage)
        # 存在返回总页数，否则返回None
        if result:
            # print result.group(1)  # 测试输出
            return result.group(1).strip()
        else:
            return None

    def getContent(self, page):
        """
        获取帖子每层的内容
        """
        pattern = re.compile('<div id="post_content_.*?>(.*?)</div>', re.S)
        # 获取所有的内容
        items = re.findall(pattern, page)
        # 内容列表
        contents = []
        # 去除标签处理，并添加到内容列表中
        for item in items:
            content = "\n" + self.taghandler.replace(item) + "\n"
            contents.append(content.encode("utf8"))
        return contents

    def setFileTitle(self, title):
        """
        如果文档标题不为None，设置标题，否则使用默认标题
        """
        if title is not None:
            self.file = open(title + ".txt", "w+")
        else:
            self.file = open(self.defaultTitle + ".txt", "w+")

    def writeFile(self, contents):
        """
        将内容写入文档，并添加楼层的分隔线
        """
        for content in contents:
            floorLine = "\n" + str(self.floor) + "-" * 30 + "\n"
            self.file.write(floorLine)
            self.file.write(content)
            self.floor += 1

    def start(self):
        """
        开始方法，如果不能返回pageNum则链接失效
        """
        indexPage = self.getPage(1)
        pageNum = self.getPageNum(indexPage)
        title = self.getTitle(indexPage)
        self.setFileTitle(title)
        if pageNum is None:
            print u"URL已失效，请重试"
            return
        try:
            print u"该贴共" + str(pageNum) + u"页"
            for i in range(1, int(pageNum) + 1):
                print u"正在写入第" + str(i) + u"页数据"
                page = self.getPage(i)
                contents = self.getContent(page)
                self.writeFile(contents)
        except IOError, e:
            print u"写入异常，原因" + e.message
        finally:
            self.file.close()
            print "Done!"


if __name__ == '__main__':
    baseUrl = "http://tieba.baidu.com/p/3138733512"  # 3138733512
    seeLZ = raw_input('是否只获取楼主发言，是输入1，否输入0:'.decode("utf8").encode('gbk'))
    bdtb = BDTB(baseUrl, seeLZ)
    bdtb.start()
