from lxml import etree
import re

import aiohttp


class Response:
    def __init__(self, byte, encoding = 'utf-8'):
        global ENCODING
        ENCODING = encoding

        self.url = None
        self.html = None
        self.byte = byte
        self.HTML = None
        self.status = None

    def get_html(self):
        if self.html is None:
            self.html = self.get_byte().decode(ENCODING)
        return self.html

    def get_byte(self):
        return self.byte

    def xpath(self, exp):
        temp = self.get_HTML()
        return temp.xpath(exp)

    def findall(self, exp):
        return re.findall(self.get_html(), exp)

    def get_HTML(self):
        if self.HTML is None:
            self.HTML = etree.HTML(self.get_html())
        return self.HTML

    def get_url(self):
        return self.url

    def gettitle(self):
        temp = self.get_HTML()
        return temp.xpath('//title/text()')[0]


class NetEngine:
    def __init__(self):
        self.session = aiohttp.ClientSession()

    async def close(self):
        await self.session.close()

    async def get(self, url, timeout=10):
         async with self.session.get(url, timeout=timeout) as response:
             print(f'netengine:timeot = {timeout}')
             temp = await response.read()

             _response = Response(temp)
             _response.url = response.url
             _response.status = response.status

             return _response