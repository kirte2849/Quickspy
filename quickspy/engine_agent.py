import asyncio
import json

from quickspy.jsonmsg import JsonMsgManager

from .messenger import Messenger




class EAgent:
    def __init__(self, qs, cm):
        self.cm = cm
        self.qs = qs
        self.m = Messenger('quickspy')

    async def run(self):

        #conn and register
        await self.m.connect()

        while True:
            #heaartbeat
            commands = await self.m.heartbeat()

            #say hello
            for msg in commands:

                #解释参数
                if msg.get_msg().find(' '):
                    command = msg.get_msg().split(' ')[0]
                    if (msg.get_msg().find('\"') == -1):
                        args = msg.get_msg().split(' ')[1:]
                    else:
                        first = msg.get_msg().find('\"')
                        last = msg.get_msg().rfind('\"')
                        lstring = msg.get_msg()[msg.get_msg().find(' ') + 1:first].strip()
                        rstring = msg.get_msg()[first + 1: last]
                        if lstring.find(' ') != -1:
                            args = lstring.split(' ')
                            args.append(lstring)
                        else:
                            args = [lstring, rstring]
                else:
                    command, args = msg.get_msg(), []

                print(command, args)

                if command == 'hello':
                    await msg.sendback('Hello, I am the agent of this quickspy engine : gen_engine')

                #show command
                elif command == 'show':
                    if args[0] == 'coros':
                        for coro in self.cm.coros:
                            await msg.sendback(f'Coro({coro.id}): Status: {coro.status}')
                else:
                    await msg.sendback('QuickSpy: No command find!')



            #sleep
            await asyncio.sleep(2)

