#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
分叉技术的服务器，放到linux虚拟机上，将客户端的连接地址改为对应服务器地址
"""

from SocketServer import TCPServer, ForkingMixIn, StreamRequestHandler


class Server(ForkingMixIn, TCPServer):
    pass


class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank you for connecting')

server = Server(('', 1234), Handler)
server.serve_forever()
