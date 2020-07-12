from quickspy.color import *
from quickspy.msgengine import Qssclient
from quickspy.net.netengine import Netengine
from quickspy.net import netengine

from quickspy.spider_agent import SpiderAgent


class Quickspy:
    def __init__(self, netengine, url_pool):
        self.netengine = netengine
        self.url_pool = url_pool
        pass


#need add some exception to solve **kwargs
#@arise Database_argument_Error
def start_qsp(settings):
    '''start_qsp()'''
    url_pool = Qssclient()
    netengine = Netengine()
    qsp = Quickspy(netengine, url_pool)
    return qsp
