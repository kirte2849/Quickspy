class Spider:
    def __init__(self):
        self.name = None
        self.uuid = None
        self.spiderinfo = None
        self.spider_settings = None
        self.qsparts = None


    def get_spiderinfo(self):
        if self.spiderinfo is None:
            spiderinfo = SpiderInfo()
            spiderinfo.name = self.name
            spiderinfo.uuid = self.uuid
            self.spiderinfo = spiderinfo
        return self.spiderinfo

    def parse(self, response):
        title = response.gettitle()
        next_page = response.xpath('//body//a[7]/@href')
        if next_page:
            next_page = next_page[0]
        else:
            next_page = None
        return (title,next_page)

    def get_url(self):
        return self.url_pool.get_text()


class SpiderInfo:
    def __init__(self):
        self.name = None
        self.uuid = None


class Example(Spider):
    def parse(self):
        pass

    def get_url(self):
        pass