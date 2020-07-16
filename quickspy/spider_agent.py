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

            backurl = None
            result = None

            try:
                response = await self.spider.qsparts.NetEngine.NE.get(url)
                result, backurl = self.spider.parse(response)
            except TimeoutError:
                print(f'time out at spider {self.spider.spiderinfo.name : On download url {url}}')
                self.qsparts.UrlPool.UP.add_new_url(url)
            except Exception as e:
                print(repr(e))

            #回调url
            if backurl:
                self.qsparts.UrlPool.UP.add_new_url(backurl)
            print(result)
        raise FinishedError

