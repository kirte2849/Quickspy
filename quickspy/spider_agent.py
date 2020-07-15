'''Mananage spider'''
from asyncio import TimeoutError

from quickspy.exceptions import FinishedError


class SpiderAgent:
    def __init__(self, spider):
        self.spider = spider

    async def run(self):
        self.qsparts = self.spider.qsparts
        self.qsparts.UrlPool.UP.add_new_url('http://www.bilibilli.com')
        while True:
            url = self.qsparts.UrlPool.UP.get_url()
            if not url:
                break
            try:
                byte = await self.spider.qsparts.NetEngine.NE.get(url)
            except TimeoutError:
                byte = b''
                print(f'time out at spider {self.spider.spiderinfo.name}')
            result, backurl =self.spider.parse(byte)
            if backurl:
                self.qsparts.UrlPool.UP.add_new_url(backurl)
            print(result)
        raise FinishedError

