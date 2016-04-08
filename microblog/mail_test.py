#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask.ext.mail import Message
from app import app, mail
from config import ADMINS
msg = Message('test subject', sender = ADMINS[0], recipients = ADMINS)
msg.body = 'text body'
msg.html = '<b>HTML</b> body'
# try:
#     with app.app_context():
#         mail.send(msg)
# except:
#     print "fail"
with app.app_context():
    mail.send(msg)
