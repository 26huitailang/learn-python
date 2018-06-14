def solution(s):
    # filter返回判断函数结果为True的结果，过滤字符和数字
    # map小写所有字符
    s = list(map(lambda x: x.lower(), filter(lambda x: x.isalpha() or x.isdigit(), s)))
    return s == s[::-1]


if __name__ == '__main__':
    r = solution("A man, a plan, a canal: Panama")
    print(r)
