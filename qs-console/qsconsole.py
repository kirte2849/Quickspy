import socket
import sys
import json
from threading import Thread
import time

from quickspy.color import *
import quickspy.cmd as cmd
import console_ui as ui
from quickspy.util import better_print

bprint = better_print('line')

# class QSChat:
#     def init(self, key, value):
#         key = str(key)
#         value = str(value)
#         line13 = '+------------------+'
#         text = key + ': ' + value
#         if len(text) > 18:
#             text = text[:15] + '...'
#         else:
#             text = text.ljust(18, '')
#         line2 = '|' + text + '|'
#         return line13 + '\n' + line2 + '\n' + line13

class Sign:
    def __init__(self):
        self.sign = 1

    def stop(self):
        self.sign = 0
        cmd.clear()


def run_md(f, main):
    sign = Sign()
    t = Thread(target=f, args=(sign, main))
    t.start()
    if input() == 'q':
        sign.stop()


def myhelp():
    return ui.HELP


def show_md_all(sign, main):
    while sign.sign:
        cmd.clear()
        speed = main.s.send("self.nemanager.reg('default').speed()".encode())
        print(speed)
        time.sleep(1)
        cmd.clear()


class Main:
    def __init__(self):
        self.s = None

        self.connect()
        self.login()
        self.loop()

    def connect(self, host='localhost', port=2546):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((host, port))
        except socket.error as msg:
            print(RED(f'at Main.connect :{msg}'))

    def recvjslist(self):#retrun [{jamsg},{jsmsg}]
        return json.loads(self.recvtext(), strict=False)

    def recvtext(self):
        return self.s.recv(1024).decode()

    def getmsg(self, jsmsg): #retrun [[],[],[]]
        return jsmsg['body']['msg']

    def heartbeart(self):#retrun list
        # heartbeat
        self.s.send('heartbeat'.encode())
        jsmsglist = self.recvjslist()
        _msg = []
        for each in jsmsglist:
            _msg.append(self.getmsg(json.loads(each, strict=False)))
        return _msg

    def login(self):
        # login
        self.s.send('register admin'.encode())
        self.s.recv(1024)

    def loop(self):
        while True:
            #main
            print(GREEN('>'), end='')
            ipt = input() #test
            
            #参数分离
            if ipt.find(' '):
                command = ipt.split(' ')[0]
                if (ipt.find('\"') == -1):
                    args = ipt.split(' ')[1:]
                else:
                    first = ipt.find('\"')
                    last = ipt.rfind('\"')
                    lstring = ipt[ipt.find(' ') + 1: first - 1]
                    rstring = ipt[first + 1: last]
                    if lstring.find(' ') != -1:
                        args = lstring.split(' ')
                        args.append(rstring)
                    else:
                        args = [lstring, rstring]
            else:
                command, args = ipt, []

            if command == '':
                continue

            if command == 'exit' or ipt == 'close' or ipt == 'quit':
                self.s.send('close'.encode())
                recved = self.s.recv(1024).decode()
                break

            elif command == 'go':
                pass

            elif command == 'help':
                print(myhelp())

            elif command == 'cls':
                cmd.clear()

            elif command == 'bannel':
                cmd.clear()
                bprint(ui.colorful_bannel())
                #print(ui.random_color_bannel())
                bprint(ui.FIRST_HELP)

            elif command == 'monitor':
                if (args[0] == '' or args[0] == 'all') if len(args) >= 1 else True:
                    run_md(show_md_all, self)

            elif command == 'debug':
                if args[0] == 'recv':
                    self.s.recv(1024)

            else:
                self.s.send(ipt.encode())
                recved = self.s.recv(1024).decode()
                print(recved)

        self.s.close()


if __name__ == '__main__':
    bprint(ui.colorful_bannel())
    #bprint(ui.random_color_bannel())
    bprint(ui.FIRST_HELP)
    m = Main()
