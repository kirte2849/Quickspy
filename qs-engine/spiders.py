from lxml import etree


class Spider:
    def __init__(self, qs):
        pass

    def parse(self, response):
        title = response.gettitle()
        next_page = response.xpath('//body//a[7]/@href')
        next_page= next_page[0]
        return (title,next_page)

    def get_url(self):
        return self.url_pool.get_text()

    def push(self, urls):
        self.url_pool.push(urls)