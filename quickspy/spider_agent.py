'''Mananage spider'''

class SpiderAgent:
    def __init__(self, spider):
        self.spider = spider

    async def run(self):
        while True:
            url = self.spider.url_pool.get_text()
            if not url:
                break
            response = await self.spider.netengine.get(url)
            result =await self.spider.parse(response)
            print(result)