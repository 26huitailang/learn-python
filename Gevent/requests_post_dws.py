"""
HTTP POST效率很高
"""
import gevent
import gevent.monkey
import time
import datetime
import requests
import logging
from requests.auth import AuthBase
from http import HTTPStatus
import json

gevent.monkey.patch_all()


urls = [
        # 'https://www.baidu.com',
        # 'https://www.facebook.com',
        # 'https://www.google.com',
        # 'https://www.qq.com',
        # 'https://www.github.com',
        'http://127.0.0.1:8000/api/v1/mzitu/tags/'
    ]
class TokenAuthDWS(AuthBase):
    def __init__(self, token):
        self.token = token

    def __call__(self, r):
        r.headers['Authorization'] = 'Token {}'.format(self.token)
        return r


def send_api_post_request(url, token, payload):
    try:
        r = requests.post(url, auth=TokenAuthDWS(token), json=payload)
    except requests.ConnectionError:
        logging.warning('API server connect failed, method:POST, url:{}'.format(url))
        return False, None

    if r.status_code != HTTPStatus.CREATED:
        logging.warning('API request failed, method:POST, url:{}, status_code:{}'.format(url, r.status_code))
        return False, None

    try:
        data = r.json()
    except (ValueError, json.JSONDecodeError):
        logging.error('API response data parse error, method:POST, url:{}, response:{}'.format(url, r.text))
        return False, None

    return True, data


def _thread_one(url, id):
    while True:
        host = 'http://127.0.0.1:8001'
        url = '{host}/api/ss_agent/ss_agents/{pk}/port_access_log/batch_post/'.format(host=host, pk='2dd2107d-f9b3-4d4c-a7d4-160b83201a28')
        ip = '1.1.1.1'
        log = [
            {"host": "wallpap", "path": "/api/a1/lock/23","port": 2009,"datetime":"2018-01-03"},
            {"host": "234dfs", "path": "/api/a1/lock/23","port": 2009,"datetime":"2018-02-03"},
            {"host": "ssss", "path": "/api/a1/lock/23","port": 5012,"datetime":"2018-01-03"},
            {"host": "waddddllpap", "path": "/api/a1/lock/23","port": 2321,"datetime":"2018-01-03"},
            {"host": "aaaa", "path": "/api/a1/lock/23","port": 4009,"datetime":"2018-01-03"},
        ] * 20

        r = send_api_post_request(url, '', payload={'ip_address': ip, 'log_list': log})
        print (r)


def gevent_main():
    spawns = [gevent.spawn(_thread_one, urls[-1], id) for id in range(5)]
    gevent.joinall(spawns)

if __name__ == '__main__':
    gevent_main()