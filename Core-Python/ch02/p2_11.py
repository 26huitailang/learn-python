# coding: utf-8
"""
菜单选项
"""
from p2_9 import avg
a = [1, 2, 3]
print(a)
while 1:
    print('(1) 取五个数的和')
    print('(2) 取五个数的平均值')
    print('(X) 退出')
    opt = input('选择：')
    if opt == '1':
        sum = 0
        for num in a:
            sum += num
        print(sum)
    elif opt == '2':
        avg(a)
    elif opt == 'X' or opt == 'x':
        break
    else:
        print('没有这个选项')
print('已退出')
