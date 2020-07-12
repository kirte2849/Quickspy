import aiohttp


from quickspy.net import Response

class Netengine:
    def __init__(self):
        pass

    async def get(self, url):
        session = async aiohttp.ClientSession()
            async with session.get(url) as response:
                return Response(response)
