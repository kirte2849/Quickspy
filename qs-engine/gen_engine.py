import aiohttp
import asyncio

from quickspy.netengine import Netengine

nengine=Netengine()


async def main():
    async with aiohttp.ClientSession() as session:
        html = await nengine.get('http://www.baidu.com')
        print(html.text())

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())