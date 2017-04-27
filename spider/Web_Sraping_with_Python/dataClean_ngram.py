# coding: utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup
from collections import OrderedDict
import re
import string
import operator


def isCommon(ngram):
    commonWords = ["the", "be", "and", "of", "a", "in", "to", "have", "it",
                   "i", "that", "for", "you", "he", "with", "on", "do", "say", "this",
                   "they", "is", "an", "at", "but", "we", "his", "from", "that", "not",
                   "by", "she", "or", "as", "what", "go", "their", "can", "who", "get",
                   "if", "would", "her", "all", "my", "make", "about", "know", "will",
                   "as", "up", "one", "time", "has", "been", "there", "year", "so",
                   "think", "when", "which", "them", "some", "me", "people", "take",
                   "out", "into", "just", "see", "him", "your", "come", "could", "now",
                   "than", "like", "other", "how", "then", "its", "our", "two", "more",
                   "these", "want", "way", "look", "first", "also", "new", "because",
                   "day", "more", "use", "no", "man", "find", "here", "thing", "give",
                   "many", "well"]
    for word in ngram:
        if word in commonWords:
            return True
    return False


def cleanInput(input):
    # 避免大小写误认为是两个不同的词组
    input = input.lower()
    # 去掉一个或多个\n
    content = re.sub('\n+', " ", input)
    # 连续多余的空格替换为一个
    content = re.sub(' +', " ", content)
    # 去除方括号包裹的数字，如[1]
    content = re.sub('\[[0-9]*\]', "", content)
    # str to bytes object, utf-8
    content = bytes(content, 'UTF-8')
    # bytes to str, 按ascii解码为unicode
    content = content.decode('ascii', 'ignore')
    cleanInput = []
    content = content.split(' ')
    for item in content:
        # print(string.punctuation)
        # !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
        item = item.strip(string.punctuation)
        # 删除单个字符，除了a、i
        if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
            cleanInput.append(item)
    return cleanInput


def getNgrams(input, n):
    input = cleanInput(input)
    output = dict()
    for i in range(len(input) - n + 1):
        newNGram = " ".join(input[i: i + n])
        # 检查是否含有常用单词
        if not isCommon(newNGram.split(' ')):
            if newNGram in output:
                output[newNGram] += 1
            else:
                output[newNGram] = 1
    return output


def parseWiki():
    html = urlopen("http://en.wikipedia.org/wiki/Python_(programming_language)")
    bsObj = BeautifulSoup(html, 'lxml')
    content = bsObj.find("div", {"id": "mw-content-text"}).get_text()
    ngrams = getNgrams(content, 2)
    # 排序列表是词组和数量的元组，根据数量倒序排列
    ngrams_freq = OrderedDict(sorted(ngrams.items(), key=lambda t: t[1], reverse=True))
    for k, v in ngrams_freq.items():
        if v > 8:
            print(k, v)
    print("2-grams count is: " + str(len(ngrams)))


def parseInaugurationSpeech():
    content = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
    ngrams = getNgrams(content, 2)
    ngrams_freq = sorted(ngrams.items(), key=operator.itemgetter(1), reverse=True)
    # print(ngrams_freq)
    for k, v in ngrams_freq:
        if v > 1:
            print(k, v)
    print("2-grams count is: " + str(len(ngrams)))


if __name__ == '__main__':
    parseInaugurationSpeech()
