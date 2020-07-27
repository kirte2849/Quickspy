import socket
import time

from quickspy.color import *

class UrlManager:
    def __init__(self, s):
        self.s = s

    def get_url(self):
        self.s.send("eval self.upmanager.reg('default').get_url()".encode())
        url = self.s.recv(2048).decode()
        print(RED('at get_url: ' + url))
        time.sleep(0.1)
        return url

    def add_new_url(self, url):
        self.s.send(f"eval self.upmanager.reg('default').add_new_url('{url}')".encode())
        self.s.recv(2048)
        time.sleep(0.1)

