"""   each parts conmunicate """

import os

from quickspy.color import *
import requests


URL_POOL = ['http://www.baidu.com/', 'https://www.bilibili.com/']


class Man:
    def __init__(self, ip, port):
        pass


class Qssclient:
    def __init__(self, host='localhost', port=123):
        pass

    def get_urls(self, num = 1):
        requests.post(ip + int(num))

    def get_text(self):
        if URL_POOL:
            return URL_POOL.pop()
        else:
            return None

    def get_url_pool(self):
        pass