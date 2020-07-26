import os
import sys
import time
import random
from collections import namedtuple


ALIVE = '*'
EMPTY = ' '


Query = namedtuple('Query', ('y', 'x'))

def count_neighbors(y, x):
    n_ = yield Query(y + 1, x + 0)  # North
    ne = yield Query(y + 1, x + 1)  # Northeast
    e_ = yield Query(y + 0, x + 1)  # East
    se = yield Query(y - 1, x + 1)  # Southeast
    s_ = yield Query(y - 1, x + 0)  # South
    sw = yield Query(y - 1, x - 1)  # Southwest
    w_ = yield Query(y + 0, x - 1)  # West
    nw = yield Query(y + 1, x - 1)  # Northwest
    neighbor_states = [n_, ne, e_, se, s_, sw, w_, nw]
    count = 0
    for state in neighbor_states:
        if state == ALIVE:
            count += 1
    return count

Transition = namedtuple('Transition', ('y', 'x', 'state'))

def step_cell(y, x):
    state = yield Query(y, x)
    neighbors = yield from count_neighbors(y, x)
    next_state = game_logic(state, neighbors)
    yield Transition(y, x, next_state)


def game_logic(state, neighbors):
    if state == ALIVE:
        if neighbors < 2:
            return EMPTY     # Die: Too few
        elif neighbors > 3:
            return EMPTY     # Die: Too many
    else:
        if neighbors == 3:
            return ALIVE     # Regenerate
    return state


TICK = object()

def simulate(height, width):
    while True:
        for y in range(height):
            for x in range(width):
                yield from step_cell(y, x)
        yield TICK


class Grid(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.rows = []
        for _ in range(self.height):
            self.rows.append([EMPTY] * self.width)

    def query(self, y, x):
        return self.rows[y % self.height][x % self.width]

    def assign(self, y, x, state):
        self.rows[y % self.height][x % self.width] = state

    def random_alive(self, live_count):
        xy = [(i,j) for i in range(self.width) for j in range(self.height)]
        for i,j in random.sample(xy, live_count):
            self.assign(i, j, ALIVE)

    def live_a_generation(self,grid, sim):
        # self.change_state(EMPTY)
        progeny = Grid(grid.height, grid.width)
        item = next(sim)
        while item is not TICK:
            if isinstance(item, Query):
                state = grid.query(item.y, item.x)
                item = sim.send(state)
            else:  # Must be a Transition
                progeny.assign(item.y, item.x, item.state)
                item = next(sim)
        return progeny

    def __str__(self):
        output = ''
        for row in self.rows:
            for cell in row:
                output += cell
            output += '\n'
        return output.strip()


def main(x,y,k):
    os.system('cls') # linux 为 clear
    grid = Grid(x, y)
    grid.random_alive(k)
    clear = '\x1b[{}A\x1b[{}D'.format(x,y)
    print(grid, end='')
    sim = simulate(grid.height, grid.width)
    while 1:
        time.sleep(.1)
        grid = grid.live_a_generation(grid, sim)
        print(clear)
        print(grid, end='')
        time.sleep(.1)
        print(clear)

if __name__ == '__main__':
    main(30,40,205)