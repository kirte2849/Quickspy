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

                #show coros|urlpool
                elif command == 'show':

                    #coros
                    if args[0] == 'coros':
                        _msg = ''
                        for coro in self.cm.coros:
                            _msg += f'Coro({coro.id}): Status: {coro.status}\n'
                        await msg.sendback(_msg.strip())

                    #show urlpool [spideruuid|name]
                    elif args[0] == 'urlpool':
                        for spider, qsparts in self.qs.spider_pool:
                            if spider.spiderinfo.uuid == args[1] or spider.spiderinfo.name == args[1]:
                                _spider, _qsparts = spider, qsparts
                                url_pool = qsparts.UrlPool.UP
                                _msg = f'new_url: {url_pool.new_urls}\nold_url: {url_pool.old_urls}'
                                break
                        await msg.sendback(_msg)

                    #show spiders info
                    elif args[0] == 'spiders' and args[1] == 'info':
                        _msg = ''
                        for spider, qsparts in self.qs.spider_pool:
                            _msg += f'({spider.spiderinfo.name}, {spider.spiderinfo.uuid})\n'
                        await msg.sendback(_msg.strip())

                elif command == 'exec':
                    result = exec(args[0])
                    return result

                elif command == 'wake':
                    self.cm.wake()

                else:
                    await msg.sendback('QuickSpy: No command find!')



            #sleep
            await asyncio.sleep(2)

