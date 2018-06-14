def solution(x):
    try:
        r = str(x)[::-1]  # 翻转字符串
        if int(r) == x:  # 取整型
            return True
        else:
            return False
    except ValueError as e:  # 如果负数会到这儿
        return False
