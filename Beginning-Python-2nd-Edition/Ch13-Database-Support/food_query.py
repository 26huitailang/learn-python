#!/usr/bin/env python
# coding: utf-8

import sqlite3, sys

conn = sqlite3.connect('food.db')
curs = conn.cursor()

query = 'SELECT * FROM food WHERE %s' % sys.argv[1]
print query
curs.execute(query)
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print '%s: %s' % pair
    print

# 运行
# python food_query.py "kcal <= 100 AND fiber >= 2 ORDER BY sugar"
# 这组数据fiber没有>=10的