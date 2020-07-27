import time

class Avarage:
    def __init__(self, _range=5):
        self._range = _range
        self.histoty = []

    def add(self):
        self.histoty.append(time.time())

    def refresh(self):
        self.histoty = [each for each in self.histoty if each >= time.time() - self._range]

    def speed(self):
        now = time.time()
        useful_time = 0
        #print(f'history: {self.histoty}')
        for each in self.histoty:
            if each >= now - self._range:
                useful_time += 1
            else:
                continue
        #print(f'useful_time: {useful_time}')
        self.refresh()
        return useful_time/self._range


a = Avarage(1)
for i in range(1020):
    a.add()
    print(a.speed())
    time.sleep(0.01)

print('finished')

for i in range(2000):
    print(a.speed())
    time.sleep(0.1)

