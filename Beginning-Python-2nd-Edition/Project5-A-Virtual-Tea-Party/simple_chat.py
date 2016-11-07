#!/usr/bin/env python
# -*- coding: utf-8 -*-
from asyncore import dispatcher
from asynchat import async_chat
import socket
import asyncore

PORT = 5005
NAME = 'TestChat'


class ChatSession(async_chat):
    """
    处理服务器和一个用户之间连接的类。
    """
    def __init__(self, server, sock):
        # 标准设置任务：
        async_chat.__init__(self, sock)
        self.server = server
        self.set_terminator('\r\n')
        self.data = []
        # 问候用户：
        self.push('Welcome to %s\r\n' % self.server.name)

    def collect_incoming_data(self, data):
        self.data.append(data)

    def found_terminator(self):
        """
        如果发现了一个终止对象，也就意味着读入了一个完整的行，将其广播给每个人。
        """
        line = ''.join(self.data)
        self.data = []
        self.server.broadcast(line)

    def handle_close(self):
        async_chat.handle_close(self)
        self.server.disconnect(self)


class ChatServer(dispatcher):
    """
    接受连接并且产生单个会话的类。它还会处理到其他会话的广播。
    """
    def __init__(self, port, name):
        # Standard setup tasks
        dispatcher.__init__(self)
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()  # 没有正确关闭端口时，可以短时间重用同一个端口，否则会等待一段时间
        self.bind(('', port))  # ''表示本机或所有接口
        self.listen(5)
        self.name = name
        self.sessions = []

    def disconnect(self, session):
        self.sessions.remove(session)

    def broadcast(self, line):
        for session in self.sessions:
            session.push(line + '\r\n')

    def handle_accept(self):
        conn, addr = self.accept()
        # print 'Connection attempt from', addr[0]
        self.sessions.append(ChatSession(self, conn))

if __name__ == '__main__':
    s = ChatServer(PORT, NAME)
    try:
        asyncore.loop()
    except KeyboardInterrupt:
        print
