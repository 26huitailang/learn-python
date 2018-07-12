# Copyright (c) 2012 Denis Bilenko. See LICENSE for details.
"""A simple UDP server.
For every message received, it sends a reply back.
You can use udp_client.py to send a message.
"""
from __future__ import print_function
from gevent.server import DatagramServer
import arrow

class EchoServer(DatagramServer):

    def handle(self, data, address): # pylint:disable=method-hidden
        data = parse_access_log_https(data.decode())
        print('%s: got %r' % (address[0], data))
        self.socket.sendto(('Received %s bytes' % len(data)).encode('utf-8'), address)


def parse_access_log_https(raw_data):
    """解析ss发送过来的https数据"""
    try:
        host, port = raw_data.split('\r\n')
        obj = {
            'host': host,
            'port': port,
            'datetime': str(arrow.utcnow().datetime),
            'protocol': 'https',
        }
    except AttributeError:
        obj = None
        # sentry_client.captureException()

    return obj


if __name__ == '__main__':
    print('Receiving datagrams on :9000')
EchoServer(':9000').serve_forever()
