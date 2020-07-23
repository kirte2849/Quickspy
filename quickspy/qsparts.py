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
        self.pool = {}

    def reg(self, info):
        if info.uuid not in self.pool:
            temp = RegedNE(info.uuid, NetEngine())
            self.pool[info.uuid] = temp
            return temp
        else:
            return self.pool[info.uuid]

    def status(self):
        return self.pool


class UPMannager:
    def __init__(self):
        self.pool = {}  #{uuid: urlpool}

    def reg(self, info):
        if info.uuid not in self.pool:
            temp = RegedUP(info.uuid, UrlManager())
            self.pool[info.uuid] = temp
            return temp
        else:
            return self.pool[info.uuid]

    def status(self):
        return self.pool


class MMannager:
    def __init__(self):
        self.pool = {}

    def reg(self, info):
        if info.uuid not in self.pool:
            temp = RegedM(info.uuid, MMannager())
            self.pool[info.uuid] = temp
            return temp
        else:
            return self.pool[info.uuid]

    def status(self):
        return self.pool


class LMannager:
    def __init__(self):
        self.pool = {}

    def reg(self, info):
        if info.uuid not in self.pool:
            temp = RegedL(info.uuid, LMannager())
            self.pool[info.uuid] = temp
            return temp
        else:
            return self.pool[info.uuid]

    def status(self):
        return self.pool