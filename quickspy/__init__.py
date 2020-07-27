from collections import namedtuple
import socket


from quickspy.engine_agent import EAgent
from quickspy.color import *
from quickspy.msgengine import QssClient
from quickspy.net.netengine import NetEngine
from quickspy.spider_agent import SpiderAgent
from quickspy.qsparts import *
from quickspy.jsonmsg import JsonMsgManager,jsmsg

Qsparts = namedtuple('Qsparts', ['UrlPool', 'NetEngine', 'Messager', 'Logger'])



class Quickspy:
    def __init__(self, root_settings):
        # self.url_pool_pool = []
        # self.netengine_pool = []
        self.spider_pool = [] #[(spider,qsparts)]
        # self.logger_pool = []
        ##self.coros = None
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect(('localhost', 2546))
        except socket.error as msg:
            print(RED(f'at Quickspy.init :{msg}'))

    def reg_spider(self, spider):
        spiderinfo = spider.get_spiderinfo()
        qsparts = Qsparts(
            UrlManager(self.s),
            NetEngine(self.s),
            Messenger(spiderinfo.uuid),
            Logger()

        )
        self.spider_pool.append((spider, qsparts))
        return (spider, qsparts)


#need add some exception to solve **kwargs
#@arise Database_argument_Error
# def start_qs(root_settings):
#     '''start_qsp()'''
#     url_pool = Qssclient().get_url_pool()
#     netengine = Netengine()
#     qsp = Quickspy(netengine, url_pool)
#     return qsp
