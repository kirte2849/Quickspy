from collections import namedtuple


from quickspy.net import NetEngine
from quickspy.net import UrlManager
from quickspy.messenger import Logger
from quickspy.messenger import Messenger

RegedNE = namedtuple('RegedNE', ['uuid', 'NE'])
RegedUP = namedtuple('RegedUP', ['uuid', 'UP'])
RegedM = namedtuple('RegedM', ['uuid', 'M'])
RegedL = namedtuple('RegedL', ['uuid', 'L'])

class NEMannager:
    def __init__(self):
        self.pool = {}

    def reg(self, uuid):
        if uuid not in self.pool:
            temp = RegedNE(uuid, NetEngine())
            self.pool[uuid] = temp
            return temp.NE
        else:
            return self.pool[uuid].NE


class UPMannager:
    def __init__(self):
        self.pool = {}  #{uuid: urlpool}

    def reg(self, uuid):
        if uuid not in self.pool:
            temp = RegedUP(uuid, UrlManager())
            self.pool[uuid] = temp
            return temp.UP
        else:
            return self.pool[uuid].UP


class MMannager:
    def __init__(self):
        self.pool = {}

    def reg(self, uuid):
        if uuid not in self.pool:
            temp = RegedM(uuid, Messenger())
            self.pool[uuid] = temp
            return temp.M
        else:
            return self.pool[uuid].M

class LMannager:
    def __init__(self):
        self.pool = {}

    def reg(self, uuid):
        if uuid not in self.pool:
            temp = RegedL(uuid, Logger())
            self.pool[uuid] = temp
            return temp.L
        else:
            return self.pool[uuid].L
