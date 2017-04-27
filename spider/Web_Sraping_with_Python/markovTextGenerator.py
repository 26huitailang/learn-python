# coding: utf-8
from urllib.request import urlopen
from random import randint


def wordListSum(wordList):
    """
    计算某词后出现的所有词的总次数，目的是计算randIndex所在区间
    :param wordList: word_a为key的value，{word_a :{word_e: 2, word_f: 8, ...}}
    :return: value中所有词的总次数
    """
    sum = 0
    for word, value in wordList.items():
        sum += value
    return sum


def retrieveRandomWord(wordList):
    """
    检索一个词后面出现的单词中的一个随机
    :param wordList: {word_a :{word_e: 2, word_f: 8, ...}}中word_a为key的value
    :return: 随机检索到的word
    """
    # 当前词典值的总和，产生一个随机数
    randIndex = randint(1, wordListSum(wordList))
    # 遍历字典所有值，逐个相减，为负表示落在该区间
    for word, value in wordList.items():
        # 逐级相减
        randIndex -= value
        # 如果值为负时，表示索引值落在该区间内，返回属于这个值的word
        if randIndex <= 0:
            return word


def buildWordDict(text):
    # 剔除换行符号和引号
    text = text.replace("\n", " ")
    text = text.replace("\"", "")

    # 保证每个标点符号和前面的单词在一起
    # 这样不会被剔除，保留在马尔科夫链中
    punctuation = [',', '.', ';', ':']
    for symbol in punctuation:
        text = text.replace(symbol, " "+symbol+" ")
    words = text.split(" ")
    # 过滤空单词
    words = [word for word in words if word != ""]

    wordDict = dict()
    for i in range(1, len(words)):
        if words[i-1] not in wordDict:
            # 为单词新建一个词典
            wordDict[words[i-1]] = {}
        if words[i] not in wordDict[words[i-1]]:
            # {words[i-1]: {words[i]: 0}}
            wordDict[words[i-1]][words[i]] = 0
        wordDict[words[i-1]][words[i]] = wordDict[words[i-1]][words[i]] + 1
    return wordDict


def run():
    text = str(urlopen("http://pythonscraping.com/files/inaugurationSpeech.txt").read(), 'utf-8')
    wordDict = buildWordDict(text)
    for w in wordDict:
        print(w)
    # 生成链长为n的马尔科夫链
    length = 100
    chain = ""
    currentWord = "I"
    for i in range(0, length):
        chain += currentWord + " "
        currentWord = retrieveRandomWord(wordDict[currentWord])

    print(chain)


if __name__ == '__main__':
    run()