# coding: utf-8
"""
带循环和条件判断的用户输入。使用 raw_input()函数来提示用户输入一个 1 和 100 之间的数，如果用户输入的数满足这个条件，显示成功并退出。否则显示一个错误信息然后再次提示用户输入数值，直到满足条件为止。
"""
def noloop():
    "返回函数本身，直到成功"
    user_input = raw_input('Enter a num 1-100: ')
    try:
        num = int(user_input)
        if num >= 1 and num <= 100:
            print "right!"
        else:
            print "out of range"
            return noloop()
    except Exception, e:
        print e
        return noloop()


def withloop():
    user_input = raw_input()
    try:
        num = int(user_input)
    except Exception, e:
        print e
        return withloop()
    while not(num >= 1 and num <= 100):
        print "out of range"
        return withloop()
    print 'right'

withloop()
