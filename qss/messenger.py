import asyncio

from quickspy.color import *

from orders import CommandParser



class NoAPIError(Exception):
    def __init__(self, api):
        self.api = api
        super()

    def repr(self):
        return f'None API could parse this api:{self.api}'



class QSS:
    def __init__(self):
        self.peer = set()
        self.cp = CommandParser()

    async def run(self, reader, writer):
        # data = await reader.read(100)
        # message = data.decode()
        # addr = writer.get_extra_info('peername')
        #
        # print(f"Received {message!r} from {addr!r}")
        #
        # print(f"Send: {message!r}")
        # writer.write(data)
        # await writer.drain()
        #
        # print("Close the connection")
        # writer.close()

        #get peer info
        addr = writer.get_extra_info('peername')
        self.peer.add(addr)

        #认证？

        #发送欢迎消息
        writer.write(BLUE(f'{addr} Welcome to use QuickSpy!\n\r').encode())
        await writer.drain()

        #main
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

            #处理命令
            ods = self.cp.parse_command(command, args)


            #防止ods为od
            if type(ods) is not type([]):
                ods = [ods]

            #解释命令返回行为
            for od in ods:

                #
                if od.api == 'sendback':
                    # sendback
                    writer.write((od.text + '\n\r').encode())

                #
                elif od.api == 'sendto':
                    # sendto host:port msg
                    pass

                #
                else:
                    raise NoAPIError(od.api)


            #发送结果


            #刷新缓冲
            await writer.drain()

            print(od.text)



async def main():

    qss= QSS()

    server = await asyncio.start_server(qss.run, '127.0.0.1', 2546)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    await server.serve_forever()
    server.close()

asyncio.run(main())
