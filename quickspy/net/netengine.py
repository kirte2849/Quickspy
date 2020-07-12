import aiohttp


from quickspy.net import Response

class Netengine:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def close(self):
        await self.session.close()

    async def get(self, url):
         response = await self.session.get(url)
         return Response(response)