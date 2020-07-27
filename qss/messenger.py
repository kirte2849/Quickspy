import asyncio
import json
import time
from collections import namedtuple

from quickspy.color import *
from quickspy.util import get_uuid
from quickspy import jsmsg

from qss.urlmanager import UrlManager

CONN_TIMEOUT = 60000

Temp = namedtuple('Temp', ['comefrom', 'msg'])




class NoAPIError(Exception):
    def __init__(self, api):
        self.api = api
        super()

    def repr(self):
        return f'None API could parse this api:{self.api}'

class Client:
    def __init__(self, name, addr):
        self.name = name
        self.addr = addr
        self.temp = []


class Avarage:
    def __init__(self, _range=5):
        self._range = _range
        self.histoty = []

    def add(self):
        self.histoty.append(time.time())

    def refresh(self):
        self.histoty = [each for each in self.histoty if each >= time.time() - self._range]

    def speed(self):
        now = time.time()
        useful_time = 0
        #print(f'history: {self.histoty}')
        for each in self.histoty:
            if each >= now - self._range:
                useful_time += 1
            else:
                continue
        #print(f'useful_time: {useful_time}')
        self.refresh()
        return useful_time/self._range

class NetEngine:
    def __init__(self):
        self.ava = Avarage(1)

    def add(self):
        self.ava.add()

    def speed(self):
        return self.ava.speed()

RegedNE = namedtuple('RegedNE', ['uuid', 'NE'])
RegedUP = namedtuple('RegedUP', ['uuid', 'UP'])
RegedM = namedtuple('RegedM', ['uuid', 'M'])
RegedL = namedtuple('RegedL', ['uuid', 'L'])

class NEMannager:
    def __init__(self):
        self.pool = {}

    def reg(self, uuid):
        if uuid not in self.pool:
            temp = RegedNE(uuid, NetEngine())
            self.pool[uuid] = temp
            return temp.NE
        else:
            return self.pool[uuid].NE

class UPMannager:
    def __init__(self):
        self.pool = {}

    def reg(self, uuid):
        if uuid not in self.pool:
            temp = RegedUP(uuid, UrlManager())
            self.pool[uuid] = temp
            return temp.UP
        else:
            return self.pool[uuid].UP

class QSS:
    def __init__(self):

        self.nemanager = NEMannager()
        self.upmanager = UPMannager()
        #self.mmannager = MMannager()
        #self.lmanager = LMannager()

        self.conns = {}   #{addr:time,addr:time, ....}
        self.clients = {}  #{name: <class Client>}

    #认证
    async def run(self, reader, writer):

        # data = await reader.read(100)
        # message = data.decode()
        # addr = writer.get_extra_info('peername')
        # print(f"Received {message!r} from {addr!r}"
        # print(f"Send: {message!r}")
        # writer.write(data)
        # await writer.drain()
        # print("Close the connection")
        # writer.close()

        #get peer info

        this_client = None
        this_addr = writer.get_extra_info('peername')

        #添加时间
        self.conns[this_addr] = time.time()

        print(f'Get a new connection from addr : {this_addr}')

        #发送欢迎消息
        # writer.write('Welcome to use QuickSpy!'.encode())
        # await writer.drain()

        while True:

            #timeout
            if int(time.time() - self.conns[this_addr]) >= CONN_TIMEOUT:
                del self.conns[this_addr]
                if this_client:
                    del self.clients[this_client.name]
                writer.write('Connections timeout!'.encode())
                await writer.drain()
                break

            #接收命令
            recived = await reader.read(2048)
            print(RED(f'Reciving data: {recived}'))

            #解析命令
            decoded = recived.decode(errors='ignore').strip()
            print(RED(f'Decoded data: {decoded}'))

            #参数分离
            if decoded.find(' '):
                command = decoded.split(' ')[0]
                if (decoded.find('\"') == -1):
                    args = decoded.split(' ')[1:]
                else:
                    first = decoded.find('\"')
                    last = decoded.rfind('\"')
                    lstring = decoded[decoded.find(' ') + 1: first - 1]
                    rstring = decoded[first + 1: last]
                    if lstring.find(' ') != -1:
                        args = lstring.split(' ')
                        args.append(rstring)
                    else:
                        args = [lstring, rstring]
            else:
                command, args = decoded, []
            print(BLUE(f'Command: {command}\nargs: {args}'))

            #@@@@解释命令返回行为@@@@#
            #@@@@每个命令解释都要添加异常处理??

            # 欢迎
            if command == 'Hello,QuickSpy!' and this_client:
                writer.write('Hello, my master! Welcome to QuickSpy.'.encode())

            # 认证？ recv register [name]
            elif command == 'register':
                try:
                    user = args[0]
                except:
                    user = None
                if not user:
                    user = get_uuid()

                #test
                this_client = Client(user, this_addr)
                self.clients[user] = this_client
                writer.write('Register successifully!'.encode())

                # if not user in self.clients:
                #     this_client = Client(user, this_addr)
                #     self.clients[user] = this_client
                #     writer.write('Register successifully!'.encode())
                # else:
                #     writer.write(f'Name \'{user}\' has already been registered!'.encode())

            elif command == 'reg':
                pass

            elif command == 'eval':
                try:
                    result = eval(args[0])
                    writer.write(str(result).encode())
                except Exception as e:
                    writer.write(''.encode())
                    print(RED(f'at qss eval: {str(e)}'.encode()))

            elif command == 'exec':
                try:
                    result = exec(args[0])
                    writer.write(result.encode())
                except Exception as e:
                    writer.write(str(e).encode())

            # 转发send name msg
            elif command == 'send' and this_client:
                if len(args) == 2:
                    self.clients[args[0]].temp.append(jsmsg(this_client.name, args[0], args[1]))
                    writer.write(jsmsg('QSS', this_client.name, 'Send successfully!').encode())
                else:
                    writer.write('Wrong command!'.encode())

            elif command == 'whoami' and this_client:
                writer.write(f'Name: {this_client.name}\nAddr: {this_client.addr}\nTemp: {this_client.temp}'.encode())

            #heartbeat >> return ['', '', '']
            elif command == 'heartbeat' and this_client:
                msgs = []
                for msg in self.clients[this_client.name].temp:
                    msgs.append(msg)
                writer.write(json.dumps(msgs).encode())
                self.clients[this_client.name].temp = []
                self.conns[this_client.addr] = time.time()

            #show
            elif command == 'show' and this_client:
                #展示链接tcp
                if args[0] == 'conns':
                    for addr, _time in self.conns.items():
                        writer.write(f'Addr:{addr}, Time{int(_time)}'.encode())

            #clear [conns|clients]
            elif command == 'clear':
                _this_client = this_client
                if args == []:
                    args[0] = 'conns|clients'
                if args[0] == 'conns':
                    self.conns = {_this_client.addr: time.time()}
                if args[0] == 'clients':
                    self.clients = {_this_client.name: _this_client}
                if args[0] == 'conns|clients' or args[0] == 'client|conns':
                    self.conns = {_this_client.addr: time.time()}
                    self.clients = {_this_client.name: _this_client}
                writer.write('Clear succesifully!'.encode())

            #get name
            elif command == 'get':
                for msg in self.clients[args[0]].temp:
                    writer.write(msg.encode())
                self.clients[args[0]].temp = []

            #close conn
            elif command == 'close' and this_client:
                del self.clients[this_client.name]
                del self.conns[this_client.addr]
                writer.write('Close connection'.encode())
                await writer.drain()
                break

            #展示clients
            elif command == 'status' and this_client:
                _msg = ''
                for name, client in self.clients.items():
                    _msg += f'Client({name}) >> Addr: {client.addr} , Temp:{client.temp}\n'
                writer.write(_msg.strip().encode())

            # 保险
            else:
                writer.write('No command find!'.encode())


            #刷新缓冲
            await writer.drain()



async def main():

    qss = QSS()

    server = await asyncio.start_server(qss.run, '127.0.0.1', 2546)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    await server.serve_forever()
    server.close()

asyncio.run(main())
