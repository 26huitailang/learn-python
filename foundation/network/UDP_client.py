#coding: utf-8
__author__ = 'peter'

import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in ['www.baidu.com\r\n3001',
             'www.google.com\r\n3002', 
             'www.facebook.com\r\n3003',]:
    # 发送数据:
    s.sendto(data.encode('utf-8'), ('127.0.0.1', 9000))
    # 接收数据:
    print(s.recv(1024))
s.close()
