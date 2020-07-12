import asyncio

import quickspy
from spiders import Spider
from quickspy import SpiderAgent

import settings

qs = quickspy.start_qsp(settings)
spider_agent_group= [SpiderAgent(Spider(qs)), SpiderAgent(Spider(qs)), SpiderAgent(Spider(qs))]


async def main():
    await asyncio.gather(
        spider_agent_group[0].run(),
        spider_agent_group[1].run()
    )
    pass


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