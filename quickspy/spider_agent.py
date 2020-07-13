'''Mananage spider'''

class SpiderAgent:
    def __init__(self, spider):
        self.spider = spider

    async def run(self):
        self.netengine = qs.netengine
        self.url_pool = qs.url_pool

        while True:
            url = self.spider.url_pool.get_text()
            if not url:
                break
            byte = await self.spider.netengine.get(url)
            result, backurl =self.spider.parse(byte)
            self.spider.push(backurl)
            print(result)