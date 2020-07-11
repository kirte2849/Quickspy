"""   each parts conmunicate """

import os

from quickspy.color import *
import requests


URL_POLL = ['http;//www.baidu.com/', 'https;//www.bilibili.com/']


class Man:
    def __init__(self, ip, port):
        pass


class Qssclient:
    def __init__(self, ip, port):
        pass

    def get_urls(self, num = 1):
        requests.post(ip + int(num))

    def get_text(self):
        return URL_POLL.pop()
