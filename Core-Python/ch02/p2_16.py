# coding: utf-8
path = input("路径：")

file = open(path, 'r', encoding='utf-8')
for line in file:
    print(line, end='')
file.close()