from collections import namedtuple


from quickspy.net import NetEngine
from quickspy.net import UrlManager
from quickspy.messenger import Logger
from quickspy.messenger import Messenger

RegedNE = namedtuple('RegedNE', ['info', 'NE'])
RegedUP = namedtuple('RegedUP', ['info', 'UP'])
RegedM = namedtuple('RegedM', ['info', 'M'])
RegedL = namedtuple('RegedL', ['info', 'L'])

class NEMannager:
    def __init__(self):
        self.pool = []

    def reg(self, info):
        temp = RegedNE(info, NetEngine())
        self.pool.append(temp)
        return temp


class UPMannager:
    def __init__(self):
        self.pool = []

    def reg(self, info):
        temp = RegedUP(info, UrlManager())
        self.pool.append(temp)
        return temp


class MMannager:
    def __init__(self):
        self.pool = []

    def reg(self, info):
        temp = RegedM(info, Messenger())
        self.pool.append(temp)
        return temp


class LMannager:
    def __init__(self):
        self.pool = []

    def reg(self, info):
        temp = RegedL(info, Logger())
        self.pool.append(temp)
        return temp