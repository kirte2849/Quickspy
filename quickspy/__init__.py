from collections import namedtuple


from quickspy.color import *
from quickspy.msgengine import QssClient
from quickspy.net.netengine import NetEngine
from quickspy.spider_agent import SpiderAgent
from quickspy.qsparts import *

Qsparts = namedtuple('Qsparts', ['UrlPool', 'NetEngine', 'Messager', 'Logger'])



class Quickspy:
    def __init__(self, root_settings):
        # self.url_pool_pool = []
        # self.netengine_pool = []
        self.spider_pool = [] #[(spider,qsparts)]
        # self.logger_pool = []

        #parse root settings
        self.nemanager = NEMannager()
        self.upmanager = UPMannager()
        self.mmannager = MMannager()
        self.lmanager = LMannager()

        ##self.coros = None

    def get_url_pool(self, spiderinfo):
        return self.upmanager.reg(spiderinfo)

    def get_netengine(self, spiderinfo):
        return self.nemanager.reg(spiderinfo)

    def reg_spider(self, spider):
        spiderinfo = spider.get_spiderinfo()
        qsparts = Qsparts(
            self.get_url_pool(spiderinfo),
            self.get_netengine(spiderinfo),
            self.get_messenger(spiderinfo),
            self.get_logger(spiderinfo)
        )
        self.spider_pool.append((spider, qsparts))
        return (spider, qsparts)

    def get_messenger(self, spiderinfo):
        return self.mmannager.reg(spiderinfo)

    def get_logger(self, spiderinfo):
        return self.lmanager.reg(spiderinfo)


#need add some exception to solve **kwargs
#@arise Database_argument_Error
# def start_qs(root_settings):
#     '''start_qsp()'''
#     url_pool = Qssclient().get_url_pool()
#     netengine = Netengine()
#     qsp = Quickspy(netengine, url_pool)
#     return qsp
