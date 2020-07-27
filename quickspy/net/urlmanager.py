import socket
import time

from quickspy.color import *

class UrlManager:
    def __init__(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect(('localhost', 2546))
        except socket.error as msg:
            print(RED(f'at Quickspy.init :{msg}'))

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

