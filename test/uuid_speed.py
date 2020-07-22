from quickspy.util import get_uuid
import time

def run():
    start = time.time()

    for i in range(100000):
        get_uuid()

    end = time.time()

    all_time = end - start

    speed = 100000/all_time
    print(speed)
    return speed

speed = 0
for i in range(20):
    speed += run()

print(f'speed: {speed/20} per second')
