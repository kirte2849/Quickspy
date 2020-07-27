'''Mananage spider'''
from asyncio import TimeoutError

from quickspy.exceptions import FinishedError
from quickspy.color import *
from quickspy.item import Item, Res, Url


class SpiderAgent:
    def __init__(self, spider):
        self.spider = spider

    async def run(self):
        print(f'at spiderengent({self.spider.spiderinfo.name}: start)')
        self.qsparts = self.spider.qsparts
        self.qsparts.UrlPool.add_new_url('http://www.tujigu.com/s/40/')
        while True:
            url = self.qsparts.UrlPool.get_url()
            print(f'at spider_agent get_url from qss: {url}')
            if url == 'None':
                break

            backurls = None
            try:
                response = await self.spider.qsparts.NetEngine.get(url)
                res, backurls = self.spider.parse(response)
                print(f'at spideragent res: {res}')
                print(f'at spideragent backurl : {backurl.url}')
            except TimeoutError:
                print(f'time out at spider {self.spider.spiderinfo.name : On download url {url}}')
                self.qsparts.UrlPool.add_new_url(url)
            except Exception as e:
                print(repr(e))

            #回调url
            for backurl in backurls:
                if backurl.url:
                    self.qsparts.UrlPool.add_new_url(backurl.url)
        raise FinishedError

