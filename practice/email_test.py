# -*- coding: utf-8 -*-

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
# import socket

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr(( \
        Header(name, 'utf-8').encode(), \
        addr.encode('utf-8') if isinstance(addr, unicode) else addr))

# from_addr = raw_input('From: ')
# password = raw_input('Password: ')
# to_addr = raw_input('To: ')
# smtp_server = raw_input('SMTP server: ')
from_addr = 'chensijian199182@163.com'
password = '123456...'
to_addr = '50590960@qq.com'
smtp_server = 'smtp.163.com'

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr(u'Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr(u'管理员 <%s>' % to_addr)
msg['Subject'] = Header(u'来自SMTP的问候……', 'utf-8').encode()

try:
    server = smtplib.SMTP(smtp_server, 25)
    # server = socket.getaddrinfo(smtp_server, 25)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    print 'success to mail!'
except:
    print 'failed to mail!'
server.quit()