# !/usr/bin/env python
# -*- coding: utf8 -*-
# client

import socket

s = socket.socket()

host = socket.gethostname()  # 本地运行，否则改用对应的主机地址
port = 1234

s.connect((host, port))
print s.recv(1024)
