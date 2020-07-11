import aiohttp


class Netengine:
    def __init__(self):
        pass

    async def fetch(self, url):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                return await response.text()