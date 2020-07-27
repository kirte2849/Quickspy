import asyncio
import json

class Msg:
    def __init__(self, msg, messenger):
        self.jsmsg = None
        self.msger = messenger
        self.msg = msg

    def get_msg(self):
        return self.get_jsmsg()['body']['msg']

    def loadjs(self):
        print(f'will load data :{self.msg}')
        self.jsmsg = json.loads(self.msg, strict=False) if self.jsmsg is None else self.jsmsg

    def text(self):
        return self.msg

    def get_jsmsg(self):
        if self.jsmsg:
            return self.jsmsg
        else:
            self.loadjs()
            return self.jsmsg

    async def sendback(self, textmsg):
        await self.msger.send(self.get_jsmsg()['header']['fromname'], textmsg)
        #判断是否发送成功
        await self.msger.read()




class Messenger:
    def __init__(self, clientname = 'DefaultClientName'):
        self.clientname = clientname
        self.reader = None
        self.writer = None

    async def send(self, toname, msg):
        await self.write(f'send {toname} "{msg}"')

    async def connect(self, host='localhost', port=2546):
        self.reader, self.writer = await asyncio.open_connection(host, port)
        await self.register()
        await self.read() #will recive 'register successfully'

    async def heartbeat(self):
        await self.write('heartbeat')
        recv = await self.read()
        print(f'at messenger.heartbeat; recv:{recv}')
        recv = json.loads(recv)
        commands = []
        for each in recv:
            commands.append(Msg(each, self))
        return commands

    async def register(self):
        await self.write(f'register {self.clientname}')

    async def write(self, msg, encoding='utf-8'):
        if encoding is None:
            self.writer.write(msg)
            await self.writer.drain()
        else:
            self.writer.write(msg.encode(encoding))
            await self.writer.drain()

    async def read(self, encoding='utf-8', size=2048):
        if encoding is None:
            data = await self.reader.read(size)
            return data
        else:
            data = await self.reader.read(size)
            data = data.decode(encoding)
            return data

    def isconnected(self):
        return bool(self.reader and self.writer)

    async def close(self):
        self.writer.close()



    # async def tcp_echo_client(message):
    #     print(f'Send: {message!r}')
    #     self.writer.write(message.encode())
    #
    #     data = await reader.read(100)
    #     print(f'Received: {data.decode()!r}')
    #
    #     print('Close the connection')
    #     await writer.close()