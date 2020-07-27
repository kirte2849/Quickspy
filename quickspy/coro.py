import asyncio

from quickspy.exceptions import FinishedError


SLEEPING = 0
WAITING = 1
WORKING = 2
DISTRIBUTED = 3

class EventManager:
    def __init__(self):
        pass

 
class CoroManager:
    def __init__(self):
        self.coros = [Coro(id) for id in range(50)]
        self.running_events = []
        self.waiting_events = []
        self.finished_events = []

    def add_event(self, event):
        '''event is a coroutine'''
        for coro in self.coros:
            if coro.status is WAITING:
                coro.event = event
                coro.status = DISTRIBUTED
                break

    def wake(self):
        '''wake coro'''
        for coro in self.coros:
            if coro.status is SLEEPING:
                coro.status = WAITING
                break


class Coro:
    def __init__(self, id):
        self.id = id
        self.sign = True
        self.status = SLEEPING
        self.event = None

    def kill(self):
        '''don't call this function'''
        self.sign = False

    async def run(self):
        while self.sign:
            if self.event is not None:
                try:
                    await self.event
                except FinishedError:
                    print('finished!')
                except Exception as e:
                    self.event = None
                    print(repr(e))
                finally:
                    self.event = None
                self.status = WAITING
            await asyncio.sleep(1)



