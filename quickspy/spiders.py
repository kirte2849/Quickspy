class Spider:
    def __init__(self, qs):
        self.netengine = qs.netengine
        self.url_pool = qs.url_pool
        pass

    def parse(self, response):
        return(response)
        pass

    def get_url(self):
        return self.url_pool.get_text()
        pass