class Database:
    def __init__(self, host='localhost', ip='29017'):
        self.ip = int(ip)
        self.host = host
        self.db = db