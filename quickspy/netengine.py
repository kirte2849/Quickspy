import aiohttp


class Netengine:
    def __init__(self):
        pass

    async def get(self, url):
        async with aiohttp.ClientSession() as session:
            return await session.get(url)