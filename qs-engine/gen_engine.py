import asyncio


import quickspy
from quickspy import SpiderAgent
from quickspy.coro import CoroManager,EventManager


from spiders.spiders import Spider
import settings as root_settings
from quickspy import EAgent

#检查文件???????????
#读取根设置
#开启qs
qs = quickspy.Quickspy(root_settings)
#读取spider设置

#实例spider

spider1 = Spider()
spider2 = Spider()
spider3 = Spider()

#注册spider

_, spider1.qsparts = qs.reg_spider(spider1)
_, spider2.qsparts = qs.reg_spider(spider2)
_, spider3.qsparts = qs.reg_spider(spider3)

#用spideragent包装spider
agt1 = SpiderAgent(spider1)
agt3 = SpiderAgent(spider2)
agt2 = SpiderAgent(spider3)

#spider_agent_group= [SpiderAgent(Spider(qs)), SpiderAgent(Spider(qs))]


#初始化循环
em = EventManager()
cm = CoroManager()

qsa = EAgent(qs, cm)

cm.wake()
cm.wake()
cm.wake()
cm.add_event(agt1.run())
cm.add_event(agt2.run())
cm.add_event(agt3.run())

async def main():
    #进入消息循环
    await asyncio.gather(
        qsa.run(),
        cm.coros[0].run(),
        cm.coros[1].run(),
        cm.coros[2].run(),
        cm.coros[4].run(),
        cm.coros[5].run(),
        cm.coros[6].run(),
        cm.coros[7].run(),
        cm.coros[8].run(),
    )
    #关闭消息循环
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