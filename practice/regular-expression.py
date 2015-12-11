import re
# someone@gmail.com
# bill.gates@microsoft.com

test = raw_input('Email: ')
re_email = re.compile(r'^(\w+|(\w+.\w+))\@(\w+?).(com|net|org|gov|cn)$')

if re_email.match(test):
	print 'it is a right email address.'
else:
	print 'wrong email address.'