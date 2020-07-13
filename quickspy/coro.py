STOPING = 0
WAITING = 1
import asyncio


class EventManager:
    def __init__(self):
        pass

 
class CoreManager:
    def __init__(self):
        self.cores = {id: Coro(id) for id in range(10)}
        self.coros_status = {id: STOPING for id in range(len(self.cores))}
        self.running_events = []
        self.waiting_events = []
        self.finished_events = []

    def add_event(self, event):
        for id, status in self.coros_status.items():
            if status is WAITING:
                self.cores[id].event = event

    def exam(self):
        self.coros_status = {id: status for id, status in self.cores.items()}


class Coro:
    def __init__(self, id = None):
        self.id = None
        self.sign = None
        self.status = STOPING
        self.event = None
        pass

    async def run(self):
        if self.status is WAITING:
            if self.event is not None:
                await self.event()
        await asyncio.sleep(5)

