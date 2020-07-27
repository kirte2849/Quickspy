from quickspy.util import get_uuid
from quickspy.item import Url, Res, Item

class Spider:
    def __init__(self):
        self.name = 'main'
        self.uuid = '11111'
        self.spiderinfo = None
        self.spider_settings = None
        self.qsparts = None


    def get_spiderinfo(self):
        self.spiderinfo = SpiderInfo(self.uuid, self.name)
        return self.spiderinfo

    def parse(self, response):
        title = response.gettitle()
        next_page = 'https://www.tujigu.com' + response.xpath("//a[@class='next']//@href")[-1]
        if next_page:
            next_page = next_page
        else:
            next_page = None

        res = Res()
        res.text_res = title

        backurls = []
        backurls.append(Url(next_page, response.url, 'main_page'))

        return (res, backurls) #return (res,[url,url])

    def get_url(self):
        return self.url_pool.get_text()


class SpiderInfo:
    def __init__(self, uuid, name='DefaultSpiderName'):
        self.name = name
        self.uuid = uuid


class Example(Spider):
    def parse(self, response):
        pass

    def get_url(self):
        pass