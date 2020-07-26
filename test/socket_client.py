import asyncio
from messenger import Messenger

m = Messenger()


async def hello():
    await m.connect()
    while True:
        data = await m.read()
        print(f'data : {data}')
        m.write(input())


asyncio.run(hello())