#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
14-1的SocketServer实现
"""

from SocketServer import TCPServer, StreamRequestHandler


class Handler(StreamRequestHandler):

    def handle(self):
        addr = self.request.getpeername()
        print 'Got connection from', addr
        self.wfile.write('Thank you for connecting')

server = TCPServer(('', 1234), Handler)
server.serve_forever()