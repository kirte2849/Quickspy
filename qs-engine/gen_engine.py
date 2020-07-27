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

spiders = [Spider() for _ in range(50)]

#注册spider
agts = []
for spider in spiders:
    _, spider.qsparts = qs.reg_spider(spider)
    agts.append(SpiderAgent(spider))

#用spideragent包装spider

#spider_agent_group= [SpiderAgent(Spider(qs)), SpiderAgent(Spider(qs))]


#初始化循环
em = EventManager()
cm = CoroManager()

qsa = EAgent(qs, cm)

for each in range(1):
    cm.wake()

cm.add_event(agts[0 ].run())
cm.add_event(agts[1 ].run())
cm.add_event(agts[2 ].run())
cm.add_event(agts[3 ].run())
cm.add_event(agts[4 ].run())
cm.add_event(agts[5 ].run())
cm.add_event(agts[6 ].run())
cm.add_event(agts[7 ].run())
cm.add_event(agts[8 ].run())
cm.add_event(agts[9 ].run())
cm.add_event(agts[10].run())
cm.add_event(agts[11].run())
cm.add_event(agts[12].run())
cm.add_event(agts[13].run())
cm.add_event(agts[14].run())
cm.add_event(agts[15].run())
cm.add_event(agts[16].run())
cm.add_event(agts[17].run())
cm.add_event(agts[18].run())
cm.add_event(agts[19].run())
cm.add_event(agts[20].run())
cm.add_event(agts[21].run())
cm.add_event(agts[22].run())
cm.add_event(agts[23].run())
cm.add_event(agts[24].run())
cm.add_event(agts[25].run())
cm.add_event(agts[26].run())
cm.add_event(agts[27].run())
cm.add_event(agts[28].run())
cm.add_event(agts[29].run())
cm.add_event(agts[30].run())
cm.add_event(agts[31].run())
cm.add_event(agts[32].run())
cm.add_event(agts[33].run())
cm.add_event(agts[34].run())
cm.add_event(agts[35].run())
cm.add_event(agts[36].run())
cm.add_event(agts[37].run())
cm.add_event(agts[38].run())
cm.add_event(agts[39].run())
cm.add_event(agts[40].run())
cm.add_event(agts[41].run())
cm.add_event(agts[42].run())
cm.add_event(agts[43].run())
cm.add_event(agts[44].run())
cm.add_event(agts[45].run())
cm.add_event(agts[46].run())
cm.add_event(agts[47].run())
cm.add_event(agts[48].run())
cm.add_event(agts[49].run())


async def main():
    #进入消息循环
    await asyncio.gather(
        qsa.run(),
        cm.coros[0].run(),
        cm.coros[1].run(),
        cm.coros[2].run(),
        cm.coros[3].run(),
        cm.coros[4].run(),
        cm.coros[5].run(),
        cm.coros[6].run(),
        cm.coros[7].run(),
        cm.coros[8].run(),
        cm.coros[9].run(),
        cm.coros[10].run(),
        cm.coros[11].run(),
        cm.coros[12].run(),
        cm.coros[13].run(),
        cm.coros[14].run(),
        cm.coros[15].run(),
        cm.coros[16].run(),
        cm.coros[17].run(),
        cm.coros[18].run(),
        cm.coros[19].run(),
        cm.coros[20].run(),
        cm.coros[21].run(),
        cm.coros[22].run(),
        cm.coros[23].run(),
        cm.coros[24].run(),
        cm.coros[25].run(),
        cm.coros[26].run(),
        cm.coros[27].run(),
        cm.coros[28].run(),
        cm.coros[29].run(),
        cm.coros[30].run(),
        cm.coros[31].run(),
        cm.coros[32].run(),
        cm.coros[33].run(),
        cm.coros[34].run(),
        cm.coros[35].run(),
        cm.coros[36].run(),
        cm.coros[37].run(),
        cm.coros[38].run(),
        cm.coros[39].run(),
        cm.coros[40].run(),
        cm.coros[41].run(),
        cm.coros[42].run(),
        cm.coros[43].run(),
        cm.coros[44].run(),
        cm.coros[45].run(),
        cm.coros[46].run(),
        cm.coros[47].run(),
        cm.coros[48].run(),
        cm.coros[49].run()

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