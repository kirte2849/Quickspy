import socket
import sys
import json

from quickspy.color import *



class Main():
    def __init__(self):
        self.s = None

        self.connect()
        self.login()
        self.loop()

    def connect(self, host = 'localhost', port = 2546):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((host, port))
            print('Welcome to Quickspy console!')
        except socket.error as msg:
            print(RED(f'at Main.connect :{msg}'))

    def getmsg(self, jsmsg): #retrun [something]
        jstext = json.loads(jsmsg, strict=False)
        return jstext['body']['msg']

    def heartbeart(self):
        # heartbeat
        s.send('heartbeat'.encode())
        recved = self.s.recv(1024)
        jsrecved = json.loads(recved, strict=False)
        for each in jsrecved:
            msg = each['body']['msg']
            print(msg)

    def send(self, toname, msg):
        self.s.send(f'send {toname} "{msg}"'.encode())
        recved = s.recv(1024).decode()

    def login(self):
        # login
        self.s.send('register admin'.encode())
        self.s.recv(1024)

    def loop(self):
        while True:
            #main
            ipt = input(GREEN('>')) #test

            if ipt == '':
                continue

            if ipt == 'exit' or ipt == 'close' or ipt == 'quit':
                self.s.send('close'.encode())
                recved = self.s.recv(1024).decode()
                break

            elif 'send' in ipt:
                self.s.send(ipt.encode())
                self.s.recv(1024)


            else:
                self.s.send(ipt.encode())
                recved = self.s.recv(1024).decode()
                print(recved)

        self.s.close()


if __name__ == '__main__':
    m = Main()