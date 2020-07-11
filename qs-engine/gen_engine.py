import aiohttp
import asyncio

from quickspy.netengine import Netengine

nengine=Netengine()


async def main():
    html = await nengine.fetch('http://bilibili.com')
    print(html)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())