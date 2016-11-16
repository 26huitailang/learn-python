#!/usr/bin/env python

print 'Content-type: text/html\n\n'

import cgitb; cgitb.enable()

from psycopg2 import psycopg1 as psycopg
conn = psycopg.connect('dbname=foo user=bar password=123456')
curs = conn.cursor()

print """
<html>
    <head>
        <title>The FooBar Bulletin Board</title>
    </head>
    <body>
        <h1>The FooBar Bulletin Board</h1>
        """

curs.execute('SELECT * FROM messages')
rows = curs.dictfetchall()
toplevel = []
children = {}

for row in rows:
    parent_id = row['reply_to']
    if parent_id is None:
        toplevel.append(row)
    else:
        # dict{parent_id: row}
        children.setdefault(parent_id, []).append(row)


def format(row):
    print row['subject']
    try:
        # kids[row, row, ...]
        kids = children[row['id']]
    except KeyError:
        pass
    else:
        print '<blockquote>'
        # kid is a row with parent_id
        for kid in kids:
            format(kid)
        print '</blockquote>'

print '<p>'

for row in toplevel:
    format(row)

print """
        </p>
    </body>
</html>
"""
