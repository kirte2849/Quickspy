import aiohttp
import asyncio

from quickspy.netengine import Netengine
from quickspy.msgengine import Qssclient
from quickspy.color import *

nengine=Netengine()


async def main():
    html = await nengine.get('http://bilibili.com')
    print(html)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())