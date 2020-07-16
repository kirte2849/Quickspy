

class Order:
    def __init__(self, text=None, api='sendback', res=None):
        self.api = api
        self.text = text
        self.res = res

class CommandParser:
    def __init__(self):
        pass

    def parse_command(self, command, args):

        #欢迎
        if command == 'Hello,QuickSpy!':
            return Order('Hello, my master! Welcome to QuickSpy.')

        #转发
        if command == 'send':
            try:
                host, port = args[0].split(':')
                return Order('send: Still not suports send ')
            except:
                return Order('send: ERROR input!')

        #保险
        else:
            return Order('No command find!')

