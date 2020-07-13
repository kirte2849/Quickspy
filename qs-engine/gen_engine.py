import asyncio

import quickspy
from spiders import Spider
from quickspy import SpiderAgent

import settings

qs = quickspy.start_qsp(settings) #开启流
spider_agent_group= [SpiderAgent(Spider(qs)), SpiderAgent(Spider(qs)), SpiderAgent(Spider(qs))]


async def main():
    await asyncio.gather(
        coro[0].run(),
        coro[1].run()
    )
    await qs.netengine.close() #close streem


#init
def init():
    pass


if __name__ == '__main__':
    doc = r'''
                  o8888888o
                  88" . "88
                  (| -_- |)
                  O\  =  /O
               ____/`---'\____
             .'  \\|     |//  `.
            /  \\|||  :  |||//  \
           /  _||||| -:- |||||-  \
           |   | \\\  -  /// |   |
           | \_|  ''\---/''  |   |
           \  .-\__  `-`  ___/-. /
         ___`. .'  /--.--\  `. . __
      ."" '<  `.___\_<|>_/___.'  >'"".
     | | :  `- \`.;`\ _ /`;.`/ - ` : | |
     \  \ `-.   \_ __\ /__ _/   .-` /  /
======`-.____`-.___\_____/___.-`____.-'======
                   `=---='
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
         佛祖保佑       永无BUG
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''
    print(doc)
    init()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())