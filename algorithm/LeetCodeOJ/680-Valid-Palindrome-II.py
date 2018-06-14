def solution(s):
    l = len(s)
    for i in range(len(s) // 2):
        if s[i] != s[-1-i]:
            # 左边或右边拿掉一个字符成立
            return s[i: l-i-1] == s[i: l-i-1][::-1] or s[i+1: l-i] == s[i+1: l-i][::-1]
    return True
