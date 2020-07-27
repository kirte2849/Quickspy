'''Mananage spider'''
from asyncio import TimeoutError

from quickspy.exceptions import FinishedError
from quickspy.color import *


class SpiderAgent:
    def __init__(self, spider):
        self.spider = spider

    async def run(self):
        self.qsparts = self.spider.qsparts
        self.qsparts.UrlPool.add_new_url('http://www.tujigu.com/s/40/')
        while True:
            url = self.qsparts.UrlPool.get_url()
            print(f'at spider_agent get_url from qss: {url}')
            if url == 'None':
                break

            backurl = None
            result = None

            try:
                response = await self.spider.qsparts.NetEngine.get(url)
                result, backurl = self.spider.parse(response)
                print(f'backurl : {backurl}')
            except TimeoutError:
                print(f'time out at spider {self.spider.spiderinfo.name : On download url {url}}')
                self.qsparts.UrlPool.add_new_url(url)
            except Exception as e:
                print(repr(e))

            #回调url
            if backurl:
                self.qsparts.UrlPool.add_new_url(backurl)
            print(BLUE(f'at spideragent: result: {result}'))
        raise FinishedError

