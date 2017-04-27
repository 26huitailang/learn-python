# coding: utf-8
"""
将网上获取的CSV文件直接读取为文件，不用保存到本地
"""
from urllib.request import urlopen
from io import StringIO
import csv

data = urlopen('http://pythonscraping.com/files/MontyPythonAlbums.csv').read().decode('ascii', 'ignore')
# 装换为文件对象
dataFile = StringIO(data)
# csvReader = csv.reader(dataFile)
dictReader = csv.DictReader(dataFile)

print(dictReader.fieldnames)

for row in dictReader:
    print(row)
    # print("The album \""+row[0]+"\" was released in "+str(row[1]))
