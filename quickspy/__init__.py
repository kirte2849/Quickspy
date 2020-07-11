from quickspy.color import *
from quickspy.msgengine import Qssclient
from quickspy.util import Database

class Quickspy:
    def __init__(self, netengine, url_poll):
        self.netengine = netengine
        self.url_poll = url_poll
        pass


#need add some exception to solve **kwargs
#@arise Database_argument_Error
def start_qsp(*args, **kwargs):
    '''start_qsp(Database | [host='localhost', port = 29727])'''
    if not type(*args[0]) is Database:
        db = Database(kwargs[0], kwargs[1])
    else;
        db = arq[0]
    qsp = Quickspy()
    return qsp
