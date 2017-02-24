# coding: utf-8
"""
带循环和条件判断的用户输入。使用 raw_input()函数来提示用户输入一个 1 和 100 之间的数，如果用户输入的数满足这个条件，显示成功并退出。否则显示一个错误信息然后再次提示用户输入数值，直到满足条件为止。
"""
a = [n for n in range(3, 17)]
def avg(numlist):
    "求平均值"
    sum = 0
    for num in numlist:
        sum += num
    print(float(sum) / len(numlist))


avg(a)