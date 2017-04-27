# coding: utf-8
# !/usr/local/bin/python
"""
###########################################################################
use the Python SMTP mail interface module to send email messages; this
is just a simple one-shot send script--see pymail, PyMailGUI, and
PyMailCGI for clients with more user interaction features; also see
popmail.py for a script that retrieves mail, and the mailtools pkg
for attachments and formatting with the standard library email package;
###########################################################################
"""

import smtplib, sys, email.utils
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import time
from urllib.request import urlopen

mailserver = 'smtp.gmail.com'  # ex: smtp.rmi.net


def sendMail(subject, body):
    From = '26huitailang@gmail.com'  # or import from mailconfig
    To = '50590960@qq.com'  # input('To?   ').strip()                 # ex: python-list@python.org
    Tos = To.split(';')  # allow a list of recipients
    Subj = subject
    Date = email.utils.formatdate()  # curr datetime, rfc2822
    user = '26huitailang@gmail.com'
    passwd = ''
    if passwd == '':
        passwd = str(input("passwd:"))

    # standard headers, followed by blank line, followed by text
    text = ('From: %s\nTo: %s\nDate: %s\nSubject: %s\n\n' % (From, To, Date, Subj))

    # print('Type message text, end with line=[Ctrl+d (Unix), Ctrl+z (Windows)]')
    text += body

    print('Connecting...')
    server = smtplib.SMTP(mailserver, 587)  # connect, no log-in step
    server.starttls()
    server.login(user, passwd)
    failed = server.sendmail(From, Tos, text)
    server.quit()
    if failed:  # smtplib may raise exceptions
        print('Failed recipients:', failed)  # too, but let them pass here
    else:
        print('No errors.')
    print('Bye.')

bsObj = BeautifulSoup(urlopen('https://isitchristmas.com/'), 'lxml')
print(bsObj.find('a', {'id': 'answer'}).get_text())
while bsObj.find('a', {'id': 'answer'}).get_text() == '不是':
    print('It is not Christmas yet.')
    time.sleep(5)
# bsObj = BeautifulSoup(urlopen('https://isitchristmas.com/'), 'lxml')
sendMail("It's Christmas!",
         "According to https://isitchristmas.com, it is Christmas!")