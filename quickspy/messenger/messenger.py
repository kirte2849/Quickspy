import asyncio

class Messenger:
    def __init__(self):
        self.reader = None
        self.writer = None

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection('127.0.0.1', 2546)

    def write(self, msg, encoding='utf-8'):
        if encoding is None:
           self.writer.write(msg)
        else:
            self.writer.write(msg.encode(encoding))

    async def read(self, encoding='utf-8', size=None):
        if encoding is None:
            self.data = await self.reader.read(size)
            self.data = self.data.decode()
        else:
            self.data = await self.reader.read(size)
            self.data = self.data.decode(encoding)

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