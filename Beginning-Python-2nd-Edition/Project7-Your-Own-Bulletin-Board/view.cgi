#!/usr/bin/env python

print 'Content-type: text/html\n\n'

import cgitb; cgitb.enable()

from psycopg2 import psycopg1 as psycopg
conn = psycopg.connect('dbname=foo user=bar password=123456')
curs = conn.cursor()

import cgi, sys
form = cgi.FieldStorage()
id = form.getvalue('id')

print """
<html>
    <head>
        <title>View Message</title>
    </head>
    <body>
        <h1>View Message</h1>
        """

# check id int
try:
    id = int(id)
except:
    print 'Invalid message ID'
    sys.exit()

curs.execute('SELECT * FROM messages WHERE id = %i' % id)
rows = curs.dictfetchall()

if not rows:
    print 'Unknown message ID'
    sys.exit()

row = rows[0]

print """
        <p><b>Subject:</b> %(subject)s<br />
        <b>Sender:</b> %(sender)s<br />
        <pre>%(text)s</pre>
        </p>
        <hr />
        <a href="main.cgi">Back to the mian page</a>
        | <a href="edit.cgi?reply_to=%(id)s">Reply</a>
    </body>
</html>
""" % row
