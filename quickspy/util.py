import uuid
import time
import random

from quickspy.color import *



def get_uuid():
    uid = str(uuid.uuid4())
    suid = ''.join(uid.split('-'))
    return suid


def better_print(style='line', sep=0.06):
    if style == 'line':
        def bprint(msg):
            for each in msg.split('\n'):
                print(each)
                time.sleep(sep)
    elif style == 'char':
        def bprint(msg):
            for char in msg:
                print(char, end='')
                time.sleep(sep)
            print()
    elif style == 'colorchar':
        def bprint(msg):
            for char in msg:
                print(COLOR(random.choice(['red', 'yellow', 'white', 'purplish_red', 'turquoise', 'green']), char), end='')
                time.sleep(sep)
            print()
    return bprint
