import aiohttp


from quickspy.net import Response

class Netengine:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def close(self):
        await self.session.close()

    async def get(self, url):
         async with self.session.get(url) as response:
             temp = await response.read()

             _response = Response(temp)
             _response.url = response.url
             _response.status = response.status

             return _response