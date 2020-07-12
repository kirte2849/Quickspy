from lxml import etree


class Spider:
    def __init__(self, qs):
        self.netengine = qs.netengine
        self.url_pool = qs.url_pool
        pass

    async def parse(self, response):
        return(await response.gettitle())

    def get_url(self):
        return self.url_pool.get_text()

    def push(self, urls):
        self.url_pool.