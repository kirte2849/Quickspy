from lxml import etree
import re

class Response:
    def __init__(self, response, encoding = 'utf-8'):
        global ENCODING
        ENCODING = encoding

        self.response = response
        self.url = response.url
        self.html = None
        self.byte = None
        self.HTML = None

    async def get_html(self):
        self.html = await self.get_byte()
        return self.html.encode(ENCODING)

    async def get_byte(self):
        if not self.byte:
          self.byte = await self.response.text()
        return self.byte

    async def xpath(selfj, exp):
        temp = await self.get_HTML()
        return temp.xpath(exp)

    async def findall(self, exp):
        return re.findall(await self.get_html(), exp)

    async def get_HTML(self):
        if not self.HTML:
            self.HTML = etree.HTML(await self.get_html())
        return self.HTML

    async def get_url(self):
        return self.url

    async def gettitle(self):
        temp = await self.get_HTML()
        return temp.xpath('//title/text()')[0]