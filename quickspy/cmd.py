import os

from quickspy.color import *


def size():
    width = os.get_terminal_size().columns
    height = os.get_terminal_size().lines
    return (width, height)

def chsize(width, height):
    os.system(f"mode con cols={width} lines={height}")

def clear():
    _ = os.system('cls')

def umove(counts):
    print(f'\x1b[{counts}A', end='')

def dmove(counts):
    print(f'\x1b[{counts}B', end='')

def lmove(counts):
    print(f'\x1b[{counts}D', end='')

def rmove(counts):
    print(f'\x1b[{counts}C', end='')


#wait
class ConsolePainter:
    def init(self):
        self.width, self.height = size()
        self.index = (0, 0)
        clear()

    def moveto(self, x, y):
        pass