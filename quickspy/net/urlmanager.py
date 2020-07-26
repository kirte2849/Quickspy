import socket

from quickspy.color import *

class UrlManager:
    def __init__(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect(('localhost', 2546))
        except socket.error as msg:
            print(RED(f'at Main.connect :{msg}'))

    async def get_url(self):
        self.s.send('urlpool get_url'.encode())
        url = self.s.recv(1024).decode()
        print(RED('at get_url: ' + url))
        return url

    async def add_new_url(self, url):
        self.s.send(f'urlpool add_new_url {url}'.encode())
        self.s.recv(1024)

