#-*- encoding: utf-8 -*-
import os, sys
import smtplib
from smtplib import SMTP_SSL
from email.header import Header
from email.mime.text import MIMEText
from config import mailInfo

# mailInfo = {
#     "from": "50590960@qq.com",
#     "to": "50590960@qq.com",
#     "hostname": "smtp.qq.com",
#     "username": "50590960@qq.com",
#     "password": "gsuzrbmkxhvybiac",
#     "mailsubject": "this is test",
#     "mailtext": "hello, <h1>this is send mail test.</h1>",
#     "mailencoding": "utf-8"
# }

if __name__ == '__main__':
    smtp = SMTP_SSL(mailInfo["hostname"])
    smtp.set_debuglevel(1)
    smtp.ehlo(mailInfo["hostname"])
    smtp.login(mailInfo["username"],mailInfo["password"])

    msg = MIMEText(mailInfo["mailtext"],_subtype="html",_charset=mailInfo["mailencoding"])
    msg["Subject"] = Header(mailInfo["mailsubject"],mailInfo["mailencoding"])
    msg["from"] = mailInfo["from"]
    msg["to"] = mailInfo["to"]
    smtp.sendmail(mailInfo["from"], mailInfo["to"], msg.as_string())

    smtp.quit()