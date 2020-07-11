class Spider:
    def __init__(self, qs):
        self.netengine = qs.netengine
        self.url_poll = qs.urlpoll
        pass

    def parse(self):
        pass

    def get_url(self):
        return self.url_poll.get_text()
        pass