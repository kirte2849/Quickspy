import asyncio
import uuid
from collections import namedtuple

from quickspy.color import *


Temp = namedtuple('Temp', ['comefrom', 'msg'])


def get_uuid():
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    return suid

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


class QSS:
    def __init__(self):
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

        #发送欢迎消息
        writer.write(BLUE(f'{this_addr} Welcome to use QuickSpy!\n\r').encode())
        await writer.drain()

        while True:
            #引导
            writer.write('>'.encode())
            await writer.drain()

            #接收命令
            recived = await reader.read(1024)
            print(RED(f'Reciving data: {recived}'))

            #解析命令
            decoded = recived.decode(errors='ignore').strip()
            print(RED(f'Decoded data: {decoded}'))

            #参数分离
            if decoded.find(' '):
                command = decoded.split(' ')[0]
                args = decoded.split(' ')[1:]
            else:
                command, args = decoded, []
            print(BLUE(f'Command: {command}\nargs: {args}'))

            #@@@@解释命令返回行为@@@@#
            #@@@@每个命令解释都要添加异常处理??

            # 欢迎
            if command == 'Hello,QuickSpy!' and this_client:
                writer.write('Hello, my master! Welcome to QuickSpy.')

            # 认证？ recv register [name]
            elif command == 'register':
                try:
                    user = args[0]
                except:
                    user = None
                if not user:
                    user = get_uuid()
                if not user in self.clients:
                    this_client = Client(user, this_addr)
                    self.clients[user] = this_client
                    writer.write('Register successifully!\n\r'.encode())
                else:
                    writer.write(f'Name \'{user}\' has already been registered!\n\r'.encode())

            # 转发send name msg
            elif command == 'send' and this_client:
                if len(args) == 2:
                    self.clients[args[0]].temp.append(args[1])
                    writer.write('Send successfully!\n\r'.encode())
                else:
                    writer.write('Wrong command!\n\r'.encode())

            elif command == 'whoami' and this_client:
                writer.write(f'Name: {this_client.name}\n\rAddr: {this_client.addr}\n\rTemp: {this_client.temp}\n\r'.encode())

            #heartbeat >> return ['', '', '']
            elif command == 'heartbeat' and this_client:
                for msg in self.clients[this_client.name].temp:
                    writer.write((msg + '\n\r').encode())
                self.clients[this_client.name].temp = []

            #展示clients
            elif command == 'status' and this_client:
                for name, client in self.clients.items():
                    writer.write(f'Client({name}) >> Addr: {client.addr} , Temp:{client.temp}\n\r'.encode())

            # 保险
            else:
                writer.write('No command find!\n\r'.encode())


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
