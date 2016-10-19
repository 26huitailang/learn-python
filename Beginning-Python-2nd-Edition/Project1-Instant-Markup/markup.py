#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, re
from handlers import *
from util import *
from rules import *

class Parser:
    """
    语法分析器读取文本文件、应用规则并且控制处理程序、
    """
    def __init__(self, handler):
        self.handler = handler
        self.rules = []
        self.filters = []

    def addRule(self, rule):
        self.rules.append(rule)

    def addFilter(self, pattern, name):
        def filter(block, handler):
            return re.sub(pattern, handler.sub(name), block)
        self.filters.append(filter)

    def parse(self, file):
        self.handler.start('document')
        for block in blocks(file):
            for filter in self.filters:
                block = filter(block, self.handler)
            for rule in self.rules:
                if rule.condition(block):
                    last = rule.action(block, self.handler)
                    if last: break
        self.handler.end('document')


class BasicTextParser(Parser):
    """
    在构造函数中增加规则和过滤器的具体语法分析器。
    """
    def __init__(self, handler):
        Parser.__init__(self, handler)
        self.addRule(ListRule())
        self.addRule(ListItemRule())
        self.addRule(TitleRule())
        self.addRule(HeadingRule())
        self.addRule(ParagraphRule())

        self.addFilter(r'\*(.+?)\*', 'emphasis')
        self.addFilter(r'(http://[\.a-zA-Z/]+)', 'url')
        self.addFilter(r'([\.a-zA-Z]+@[\.a-zA-Z]+[a-zA-Z]+)', 'mail')

handler = HTMLRenderer()
parser = BasicTextParser(handler)

# parser.parse(sys.stdin)
# 执行： python markup.py < test_input.txt > test_output2.html


# 自动转换
def main():
    try:
        file = open('test_input.txt', 'r')
        f = open('test_output.html', 'w')
        oldStdout = sys.stdout
        sys.stdout = f # 把文件对象赋给sys.stdout，输出的对象为文件对象的write方法
        parser.parse(file)
    finally:
        if file:
            file.close()
        if f:
            f.close()
        if oldStdout:
            sys.stdout = oldStdout
    print "Markup finished!"

if __name__ == '__main__':
    main()

