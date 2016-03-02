#!/usr/bin/python
# -*- coding: utf-8 -*- 

# stuff = raw_input('> ')
# stuff = "go north east"
# print stuff
# words = stuff.split()
directions = ('direction', 'north', 'south', 'east', 'west', 'down', 'up', 'left', 'right', 'back')
verbs = ('verb', 'go', 'stop', 'kill', 'eat')
stops = ('the', 'in', 'of', 'from', 'at', 'it')
nouns = ('door', 'bear', 'princess', 'cabinet')
# numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')


def scan(stuff):
    # 扫描用户输入的内容，判断词语，返回相应的类型
    words = stuff.split()
    val = []
    for word in words:
        if word in directions:
            val.append(('direction', word))
        elif word in verbs:
            val.append(('verb', word))
        elif word in stops:
            val.append(('stop', word))
        elif word in nouns:
            val.append(('noun', word))
        else:
            try:
                num = int(word)
                val.append(('number', num))
            except ValueError:
                val.append(('error', word))
    return val